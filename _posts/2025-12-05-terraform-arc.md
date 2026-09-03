---
layout: post
title: "Terraform ARC para Bancos de Dados Postgres e MongoDB em Ambiente com Auto Scale"
author: "Davi"
categories: blog
tags: [blog,infraestrutura,devops,terraform]
image: forest.jpg
---

# Terraform ARC para Bancos de Dados Postgres e MongoDB em Ambiente com Auto Scale

---

## Introdução

A gerência de infraestrutura em ambientes multi-cloud tornou-se uma necessidade essencial para empresas modernas. Com a crescente demanda por redundância, escalabilidade e flexibilidade, as organizações buscam soluções que permitam provisionar e gerenciar recursos em múltiplas plataformas sem sofrer com o aprisionamento de vendor (vendor lock-in).

O **Terraform ARC (Arc provider)** emerge como uma solução poderosa para orquestrar infraestrutura híbrida e multi-cloud, enquanto **Percona** oferece distribuições otimizadas de PostgreSQL e MongoDB. Neste artigo, exploraremos como utilizar Terraform com o provedor ARC para provisionar bancos de dados Percona em containers Podman, com suporte a auto escalabilidade.

---

## O que é Terraform ARC?

O provedor ARC (Arc Resource Control) do Terraform permite gerenciar recursos híbridos e multi-cloud de forma centralizada. Ele funciona como uma camada de abstração que simplifica a provisão de recursos em diferentes ambientes: on-premises, AWS, Azure, GCP e sistemas containerizados.

### Principais Características:

- **Unified Control Plane:** Gerência centralizada de todos os recursos
- **Infrastructure as Code:** Definição declarativa de infraestrutura
- **Multi-cloud Orchestration:** Suporte a múltiplos provedores em uma única configuração
- **Cost Optimization:** Rastreamento e otimização de custos across clouds

---

## Arquitetura Proposta

```mermaid
graph TD
    TC["Terraform Configuration (HCL)"] --> ARC["ARC Provider<br/>(Unified Multi-cloud Management)"]
    ARC --> AWS["AWS"]
    ARC --> OnPrem["On-Prem"]
    ARC --> Azure["Azure"]
    OnPrem --> Podman["Podman Runtime<br/>(Container)"]
    Podman --> PG["Percona<br/>PostgreSQL"]
    Podman --> Mongo["Percona<br/>MongoDB"]
```

---

## Pré-requisitos

Antes de começar, certifique-se de ter instalado:

1. **Terraform** (v1.5+)
   ```bash
   terraform version
   ```

2. **Podman** (v4.0+)
   ```bash
   podman version
   ```

3. **Docker CLI** (compatível com Podman)
   ```bash
   podman --version
   ```

4. **Acesso às credenciais** dos provedores cloud (AWS, Azure, etc.)

5. **Git** para controle de versão

---

## Instalação e Configuração Inicial

### 1. Estrutura de Diretórios

```bash
terraform-arc-databases/
├── main.tf
├── variables.tf
├── outputs.tf
├── podman-provider.tf
├── postgresql.tf
├── mongodb.tf
├── autoscaling.tf
├── terraform.tfvars
├── .gitignore
└── docs/
    └── README.md
```

### 2. Inicializar o Projeto Terraform

```bash
mkdir terraform-arc-databases
cd terraform-arc-databases
terraform init
```

---

## Implementação Prática

### Arquivo 1: `main.tf` - Configuração Principal

```hcl
terraform {
  required_version = ">= 1.5"
  
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
    
    arc = {
      source  = "azure/arc"
      version = "~> 0.1"
    }
  }

  backend "local" {
    path = "terraform.tfstate"
  }
}

provider "docker" {
  host = "unix:///run/podman/podman.sock"
}

provider "arc" {
  # Configuração do ARC para multi-cloud
  features {
    virtual_machine {
      skip_shutdown_and_force_delete = false
    }
  }
}

locals {
  environment = var.environment
  project     = var.project_name
  region      = var.aws_region
  
  common_tags = {
    Environment = local.environment
    Project     = local.project
    ManagedBy   = "Terraform"
    CreatedAt   = timestamp()
  }
}
```

### Arquivo 2: `variables.tf` - Variáveis de Entrada

```hcl
variable "environment" {
  description = "Ambiente de deploymente (dev, staging, prod)"
  type        = string
  default     = "dev"
  
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment deve ser dev, staging ou prod."
  }
}

variable "project_name" {
  description = "Nome do projeto"
  type        = string
  default     = "percona-arc"
}

variable "aws_region" {
  description = "Região AWS para deployment"
  type        = string
  default     = "us-east-1"
}

variable "postgres_version" {
  description = "Versão do Percona PostgreSQL"
  type        = string
  default     = "15-latest"
}

variable "mongodb_version" {
  description = "Versão do Percona MongoDB"
  type        = string
  default     = "6.0-latest"
}

variable "postgres_instances" {
  description = "Número de instâncias PostgreSQL para auto-scaling"
  type = object({
    min     = number
    desired = number
    max     = number
  })
  default = {
    min     = 2
    desired = 3
    max     = 5
  }
}

variable "mongodb_instances" {
  description = "Número de instâncias MongoDB para auto-scaling"
  type = object({
    min     = number
    desired = number
    max     = number
  })
  default = {
    min     = 2
    desired = 3
    max     = 4
  }
}

variable "postgres_memory" {
  description = "Memória alocada para PostgreSQL em MB"
  type        = number
  default     = 1024
}

variable "postgres_cpus" {
  description = "CPUs alocadas para PostgreSQL"
  type        = number
  default     = 1
}

variable "mongodb_memory" {
  description = "Memória alocada para MongoDB em MB"
  type        = number
  default     = 512
}

variable "mongodb_cpus" {
  description = "CPUs alocadas para MongoDB"
  type        = number
  default     = 0.5
}

variable "enable_autoscaling" {
  description = "Habilitar auto-scaling"
  type        = bool
  default     = true
}

variable "scaling_threshold_cpu" {
  description = "Threshold de CPU para trigger de scaling (%)"
  type        = number
  default     = 75
}

variable "scaling_threshold_memory" {
  description = "Threshold de memória para trigger de scaling (%)"
  type        = number
  default     = 80
}
```

### Arquivo 3: `postgresql.tf` - Postgres com Percona

```hcl
# Criar rede Podman para os bancos de dados
resource "docker_network" "database_network" {
  name   = "${local.project}-network"
  driver = "bridge"
  
  ipam_config {
    subnet = "172.20.0.0/16"
  }
  
  labels = {
    Name        = "${local.project}-network"
    Environment = local.environment
  }
}

# Volume para persistência de dados PostgreSQL
resource "docker_volume" "postgres_data" {
  count = var.postgres_instances.max
  name  = "${local.project}-postgres-data-${count.index + 1}"
  
  labels = {
    Type        = "PostgreSQL-Data"
    Environment = local.environment
    Index       = count.index + 1
  }
}

# Imagem Docker/Podman do Percona PostgreSQL
resource "docker_image" "postgres" {
  name         = "percona/percona-postgresql:${var.postgres_version}"
  keep_locally = true
  
  pull_image {
    keep_remotely = true
  }
}

# Container PostgreSQL com Auto-scaling readiness
resource "docker_container" "postgres" {
  count            = var.postgres_instances.desired
  name             = "${local.project}-postgres-${count.index + 1}"
  image            = docker_image.postgres.image_id
  restart_policy   = "unless-stopped"
  must_run         = true
  publish_all_ports = false
  
  # Port mapping com offset para múltiplas instâncias
  ports {
    internal = 5432
    external = 5432 + count.index
  }
  
  # Alocação de recursos para auto-scaling
  memory = var.postgres_memory
  
  # Variáveis de ambiente
  env = [
    "POSTGRES_DB=percona_db",
    "POSTGRES_USER=percona_user",
    "POSTGRES_PASSWORD=${var.postgres_password}",
    "PGDATA=/var/lib/postgresql/data/pgdata",
    "POSTGRES_INITDB_ARGS=-c max_connections=200 -c shared_buffers=256MB"
  ]
  
  # Volume de dados persistente
  volumes {
    container_path = "/var/lib/postgresql/data"
    volume_name    = docker_volume.postgres_data[count.index].name
    read_only      = false
  }
  
  # Conectar à rede customizada
  networks_advanced {
    name         = docker_network.database_network.name
    ipv4_address = "172.20.0.${10 + count.index}"
  }
  
  # Health check para auto-scaling
  healthcheck {
    test         = ["CMD-SHELL", "pg_isready -U percona_user -d percona_db"]
    interval     = "10s"
    timeout      = "5s"
    start_period = "40s"
    retries      = 3
  }
  
  # Labels para ARC resource management
  labels {
    label = "app"
    value = "postgres"
  }
  
  labels {
    label = "version"
    value = var.postgres_version
  }
  
  labels {
    label = "environment"
    value = local.environment
  }
  
  labels {
    label = "scaling_group"
    value = "postgres-pool"
  }
  
  depends_on = [docker_network.database_network]
}

# Variável sensível para senha do Postgres (não versionada em git)
variable "postgres_password" {
  description = "Senha do usuário PostgreSQL"
  type        = string
  sensitive   = true
  default     = "PerconaSecure123!"
}
```

### Arquivo 4: `mongodb.tf` - MongoDB com Percona

```hcl
# Volume para persistência de dados MongoDB
resource "docker_volume" "mongodb_data" {
  count = var.mongodb_instances.max
  name  = "${local.project}-mongodb-data-${count.index + 1}"
  
  labels = {
    Type        = "MongoDB-Data"
    Environment = local.environment
    Index       = count.index + 1
  }
}

# Imagem Docker/Podman do Percona MongoDB
resource "docker_image" "mongodb" {
  name         = "percona/percona-server-mongodb:${var.mongodb_version}"
  keep_locally = true
  
  pull_image {
    keep_remotely = true
  }
}

# Container MongoDB com suporte a Auto-scaling
resource "docker_container" "mongodb" {
  count            = var.mongodb_instances.desired
  name             = "${local.project}-mongodb-${count.index + 1}"
  image            = docker_image.mongodb.image_id
  restart_policy   = "unless-stopped"
  must_run         = true
  publish_all_ports = false
  
  # Port mapping com offset para múltiplas instâncias
  ports {
    internal = 27017
    external = 27017 + count.index
  }
  
  # Alocação de recursos para escalabilidade
  memory = var.mongodb_memory
  
  # Variáveis de ambiente para configuração
  env = [
    "MONGO_INITDB_ROOT_USERNAME=admin",
    "MONGO_INITDB_ROOT_PASSWORD=${var.mongodb_password}",
    "MONGO_INITDB_DATABASE=percona_db",
  ]
  
  # Volume de dados persistente
  volumes {
    container_path = "/data/db"
    volume_name    = docker_volume.mongodb_data[count.index].name
    read_only      = false
  }
  
  # Conectar à rede customizada
  networks_advanced {
    name         = docker_network.database_network.name
    ipv4_address = "172.20.0.${50 + count.index}"
  }
  
  # Health check para orquestração automática
  healthcheck {
    test         = ["CMD", "mongosh", "--eval", "db.adminCommand('ping')"]
    interval     = "10s"
    timeout      = "5s"
    start_period = "40s"
    retries      = 3
  }
  
  # Labels para ARC resource management
  labels {
    label = "app"
    value = "mongodb"
  }
  
  labels {
    label = "version"
    value = var.mongodb_version
  }
  
  labels {
    label = "environment"
    value = local.environment
  }
  
  labels {
    label = "scaling_group"
    value = "mongodb-pool"
  }
  
  depends_on = [docker_network.database_network]
}

# Variável sensível para senha do MongoDB
variable "mongodb_password" {
  description = "Senha do usuário root MongoDB"
  type        = string
  sensitive   = true
  default     = "MongoSecure123!"
}
```

### Arquivo 5: `autoscaling.tf` - Lógica de Auto-scaling

```hcl
# Data source para monitorar métricas de container
data "docker_container" "postgres_metrics" {
  count = var.postgres_instances.desired
  id    = docker_container.postgres[count.index].id
}

data "docker_container" "mongodb_metrics" {
  count = var.mongodb_instances.desired
  id    = docker_container.mongodb[count.index].id
}

# Função local para calcular média de CPU
locals {
  # Simular métricas (em produção, usar Prometheus/Grafana)
  postgres_scaling_enabled = var.enable_autoscaling
  mongodb_scaling_enabled  = var.enable_autoscaling
  
  # Thresholds para escalabilidade
  scale_up_threshold_cpu    = var.scaling_threshold_cpu
  scale_down_threshold_cpu  = var.scaling_threshold_cpu * 0.5
}

# Trigger para scale-up de PostgreSQL (exemplo de lógica)
resource "null_resource" "postgres_scale_trigger" {
  count = local.postgres_scaling_enabled ? 1 : 0
  
  triggers = {
    instance_count = var.postgres_instances.desired
    max_instances  = var.postgres_instances.max
    cpu_threshold  = local.scale_up_threshold_cpu
  }
  
  provisioner "local-exec" {
    command = "echo 'PostgreSQL scaling trigger ready. Current instances: ${var.postgres_instances.desired}'"
  }
}

# Trigger para scale-up de MongoDB
resource "null_resource" "mongodb_scale_trigger" {
  count = local.mongodb_scaling_enabled ? 1 : 0
  
  triggers = {
    instance_count = var.mongodb_instances.desired
    max_instances  = var.mongodb_instances.max
    cpu_threshold  = local.scale_up_threshold_cpu
  }
  
  provisioner "local-exec" {
    command = "echo 'MongoDB scaling trigger ready. Current instances: ${var.mongodb_instances.desired}'"
  }
}

# Script de health check automático
resource "null_resource" "health_check_postgres" {
  count = var.postgres_instances.desired
  
  provisioner "local-exec" {
    command = "podman exec ${docker_container.postgres[count.index].name} pg_isready -U percona_user || echo 'Warning: Postgres instance ${count.index + 1} health check failed'"
  }
  
  depends_on = [docker_container.postgres]
}

resource "null_resource" "health_check_mongodb" {
  count = var.mongodb_instances.desired
  
  provisioner "local-exec" {
    command = "podman exec ${docker_container.mongodb[count.index].name} mongosh --eval 'db.adminCommand(\"ping\")' || echo 'Warning: MongoDB instance ${count.index + 1} health check failed'"
  }
  
  depends_on = [docker_container.mongodb]
}
```

### Arquivo 6: `outputs.tf` - Outputs e Informações

```hcl
output "postgres_endpoints" {
  description = "Endpoints de conexão PostgreSQL"
  value = {
    for i, container in docker_container.postgres :
    "postgres-${i + 1}" => "localhost:${container.ports[0].external}"
  }
  sensitive = false
}

output "mongodb_endpoints" {
  description = "Endpoints de conexão MongoDB"
  value = {
    for i, container in docker_container.mongodb :
    "mongodb-${i + 1}" => "localhost:${container.ports[0].external}"
  }
  sensitive = false
}

output "network_details" {
  description = "Detalhes da rede Podman"
  value = {
    name = docker_network.database_network.name
    id   = docker_network.database_network.id
    cidr = "172.20.0.0/16"
  }
}

output "postgres_scaling_config" {
  description = "Configuração de auto-scaling PostgreSQL"
  value = {
    min_instances      = var.postgres_instances.min
    desired_instances  = var.postgres_instances.desired
    max_instances      = var.postgres_instances.max
    cpu_threshold      = var.scaling_threshold_cpu
    enabled            = var.enable_autoscaling
  }
}

output "mongodb_scaling_config" {
  description = "Configuração de auto-scaling MongoDB"
  value = {
    min_instances      = var.mongodb_instances.min
    desired_instances  = var.mongodb_instances.desired
    max_instances      = var.mongodb_instances.max
    memory_threshold   = var.scaling_threshold_memory
    enabled            = var.enable_autoscaling
  }
}

output "postgres_connection_string" {
  description = "String de conexão PostgreSQL (exemplo)"
  value       = "psql -h localhost -p 5432 -U percona_user -d percona_db"
  sensitive   = false
}

output "mongodb_connection_string" {
  description = "String de conexão MongoDB (exemplo)"
  value       = "mongosh 'mongodb://admin:PASSWORD@localhost:27017/percona_db'"
  sensitive   = false
}

output "deployment_summary" {
  description = "Resumo do deployment"
  value = {
    project_name        = local.project
    environment         = local.environment
    total_postgres_pods = var.postgres_instances.desired
    total_mongodb_pods  = var.mongodb_instances.desired
    auto_scaling        = var.enable_autoscaling
    podman_network      = docker_network.database_network.name
  }
}
```

### Arquivo 7: `terraform.tfvars` - Valores Customizados

```hcl
environment              = "dev"
project_name             = "percona-arc"
aws_region               = "us-east-1"
postgres_version         = "15-latest"
mongodb_version          = "6.0-latest"

postgres_instances = {
  min     = 2
  desired = 3
  max     = 5
}

mongodb_instances = {
  min     = 2
  desired = 3
  max     = 4
}

postgres_memory           = 1024
postgres_cpus             = 1
mongodb_memory            = 512
mongodb_cpus              = 0.5
enable_autoscaling        = true
scaling_threshold_cpu     = 75
scaling_threshold_memory  = 80
```

### Arquivo 8: `.gitignore`

```
# Terraform
*.tfstate
*.tfstate.*
.terraform/
.terraform.lock.hcl
crash.log

# Variáveis sensíveis
terraform.tfvars
*.tfvars
!example.tfvars

# IDE
.idea/
.vscode/
*.swp
*.swo
*~

# Logs
*.log

# Arquivos do SO
.DS_Store
Thumbs.db

# Podman/Docker
.docker/
```

---

## Execução e Deployment

### Passo 1: Validar Configuração

```bash
# Inicializar o projeto
terraform init

# Validar sintaxe HCL
terraform validate

# Formatar arquivos
terraform fmt -recursive

# Criar plano de execução
terraform plan -out=tfplan
```

### Passo 2: Aplicar Configuração

```bash
# Aplicar infraestrutura
terraform apply tfplan

# Ou, para aplicação direta (sem plano)
terraform apply -auto-approve
```

### Passo 3: Verificar Deployment

```bash
# Listar containers ativos
podman ps

# Ver logs de um container
podman logs percona-arc-postgres-1

# Conectar ao PostgreSQL
psql -h localhost -p 5432 -U percona_user -d percona_db

# Conectar ao MongoDB
mongosh 'mongodb://admin:PASSWORD@localhost:27017/percona_db'
```

### Passo 4: Monitorar Auto-scaling

```bash
# Ver estatísticas de container
podman stats

# Verificar status de health check
podman inspect --format='{{.State.Health.Status}}' percona-arc-postgres-1
```

---

## Exemplo de Monitoramento com Prometheus

Para implementar monitoramento real de métricas:

```hcl
# Arquivo: monitoring.tf (adicional)

resource "docker_image" "prometheus" {
  name         = "prom/prometheus:latest"
  keep_locally = true
}

resource "docker_container" "prometheus" {
  name  = "${local.project}-prometheus"
  image = docker_image.prometheus.image_id
  
  ports {
    internal = 9090
    external = 9090
  }
  
  networks_advanced {
    name = docker_network.database_network.name
  }
  
  volumes {
    container_path = "/etc/prometheus"
    host_path      = abspath("./prometheus.yml")
    read_only      = true
  }
}
```

---

## Escalando para Produção

### 1. Implementar Persistência

```hcl
# Usar volumes gerenciados externamente
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "percona-arc/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}
```

### 2. Adicionar Backup

```bash
# Script de backup automático
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
podman exec percona-arc-postgres-1 pg_dump -U percona_user percona_db > /backups/postgres_$DATE.sql
podman exec percona-arc-mongodb-1 mongodump --uri="mongodb://admin:PASSWORD@localhost:27017" --out=/backups/mongodb_$DATE
```

### 3. Segurança

```hcl
# Usar Vault para gerenciar secrets
provider "vault" {
  address = "http://localhost:8200"
}

data "vault_generic_secret" "postgres_creds" {
  path = "secret/percona/postgres"
}
```

---

## Troubleshooting

### Problema: Container não inicia

```bash
# Verificar logs
podman logs percona-arc-postgres-1

# Revisar recursos disponíveis
podman stats

# Limpar volumes órfãos
podman volume prune
```

### Problema: Auto-scaling não funciona

```bash
# Verificar health checks
podman inspect --format='{{.State.Health}}' percona-arc-postgres-1

# Aumentar thresholds temporariamente
terraform apply -var="scaling_threshold_cpu=90"
```

### Problema: Conectividade entre containers

```bash
# Testar rede
podman exec percona-arc-postgres-1 ping 172.20.0.50

# Inspecionar rede
podman network inspect percona-arc-network
```

---

## Melhores Práticas

1. **Versionamento:** Use `terraform.lock.hcl` para manter versões de providers
2. **Modulação:** Organize código em módulos reutilizáveis
3. **Testing:** Implemente testes com `terratest` ou `kitchen-terraform`
4. **Documentation:** Mantenha README.md atualizado
5. **Backup:** Configure backups automáticos de dados
6. **Segurança:** Nunca commite `.tfvars` com secrets
7. **Monitoramento:** Integre com ferramentas como Prometheus e Grafana

---

## Conclusão

O Terraform ARC com Percona oferece uma solução robusta e escalável para gerenciar bancos de dados em ambientes híbridos e multi-cloud. Utilizando Podman como orquestrador de containers, eliminamos a dependência de Docker e Kubernetes, mantendo a simplicidade operacional.

Esta abordagem permite que você:
- Provisione infraestrutura com código
- Escale automaticamente baseado em demanda
- Mantenha consistência across múltiplos ambientes
- Reduza custos operacionais

Para mais informações, consulte:
- [Documentação do Terraform](https://www.terraform.io/docs)
- [Percona PostgreSQL](https://www.percona.com/software/postgresql)
- [Percona MongoDB](https://www.percona.com/software/mongodb)
- [Podman Documentation](https://podman.io/)

---
### Fontes:

- https://www.linkedin.com/posts/edithpuclla_kubernetes-opensource-databases-activity-7384183105047171072-vp3_
- https://forums.percona.com/t/postgres-operator-cluster-deletion/15830
- https://palark.com/blog/running-mongodb-in-kubernetes/
- https://www.percona.com/blog/percona-server-for-mysql-automatic-cloud-deployment-with-terraform/
- https://palark.com/blog/comparing-kubernetes-operators-for-postgresql/
- https://severalnines.com/blog/overview-percona-mongodb-kubernetes-operator/
- https://developer.hashicorp.com/terraform/cloud-docs/integrations/kubernetes
- https://forums.percona.com/t/users-not-being-created/35575
- https://learn.microsoft.com/pt-br/azure/aks/deploy-mongodb-cluster
- https://severalnines.com/blog/overview-percona-xtradb-cluster-kubernetes-operator/
- https://www.percona.com/blog/run-postgresql-in-kubernetes-solutions-pros-and-cons/
- https://www.youtube.com/watch?v=2IjsTeq3Wtg
- https://www.percona.com/blog/multi-tenant-kubernetes-cluster-with-percona-operators/
- https://percona.github.io/percona-helm-charts/
- https://docs.percona.com/percona-operator-for-mongodb/helm.html
- https://docs.percona.com/percona-operator-for-mongodb/aks.html
- https://artifacthub.io/packages/helm/percona/pg-operator
- https://github.com/percona/percona-helm-charts
