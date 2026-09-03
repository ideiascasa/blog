---
layout: post
title: "Jules + Render - Fluxo Completo Automatizado"
author: "Davi"
categories: blog
tags: [blog,automacao,devops,github-actions]
image: codes-computer.jpg
---

# Jules + Render: Integração Completa Explicada

## 🎯 A Verdade Sobre a Integração Jules → Render

**Pergunta original:** "Jules tem integração com Render.com?"

**Resposta:** Jules **NÃO tem integração direta** com Render, mas você pode criar um fluxo **completamente automático** que liga Jules → GitHub → Render em sequência usando GitHub Actions.

---

## 🔗 Como Funciona a "Integração" Indireta

```
┌─────────────────────────────────────────────────────┐
│ GITHUB ISSUE                                        │
│ "Implementar login com Google"                      │
│ Comentário: @julius                                │
└─────────────────────────────────────────────────────┘
         ↓ (GitHub Actions Webhook)
┌─────────────────────────────────────────────────────┐
│ GITHUB ACTIONS WORKFLOW                             │
│ Detecta menção @julius                              │
│ Dispara curl para Jules API                         │
└─────────────────────────────────────────────────────┘
         ↓ (curl HTTP POST)
┌─────────────────────────────────────────────────────┐
│ JULES API (Google Cloud)                            │
│ 1. Clona seu repositório                            │
│ 2. Analisa código (2M token context)                │
│ 3. Gera plano e aguarda aprovação                   │
│ 4. Executa desenvolvimento                          │
│ 5. Roda testes                                      │
│ 6. Cria Pull Request                                │
└─────────────────────────────────────────────────────┘
         ↓ (GitHub API)
┌─────────────────────────────────────────────────────┐
│ GITHUB PULL REQUEST                                 │
│ PR criada automaticamente por Jules                 │
│ Com testes e commits estruturados                   │
└─────────────────────────────────────────────────────┘
         ↓ (GitHub Actions - nova trigger)
┌─────────────────────────────────────────────────────┐
│ GITHUB ACTIONS - CI/CD PIPELINE                     │
│ - Roda tests adicionais                             │
│ - Valida build                                      │
│ - Faz merge automático se OK                        │
└─────────────────────────────────────────────────────┘
         ↓ (Merge para main)
┌─────────────────────────────────────────────────────┐
│ RENDER WEBHOOK                                      │
│ Detecta novo commit em main                         │
│ Dispara deploy automático                           │
└─────────────────────────────────────────────────────┘
         ↓ (Build + Deploy)
┌─────────────────────────────────────────────────────┐
│ RENDER PRODUCTION                                   │
│ App running e live para usuários                    │
│ Logs disponíveis no dashboard                       │
└─────────────────────────────────────────────────────┘
```

---

## 📝 Passo 1: Como Jules Pega Issues do GitHub

Jules **não lê automaticamente** issues. Você precisa:

### Opção A: Mencioná-lo em comentário (Recomendado)

```
# Issue já existe no GitHub

Comentário do Product Owner:
@julius Implemente conforme descrito no body da issue

↓ GitHub Actions detecta @julius mention
↓ Extrai o número da issue e body
↓ Chama Jules API com o texto como prompt
```

### Opção B: Disparar via Workflow Manual

```bash
# Abrir Issue
gh issue create --title "Feature: Cancelamento" \
  --body "Permitir clientes cancelarem..."

# Depois disparar workflow manualmente
gh workflow run auto-deploy.yml \
  -f task_description="Implementar cancelamento de agendamentos" \
  -f issue_number=42
```

---

## 🔑 Passo 2: A Chave - Jules API Key

Para Jules **fazer algo**, você precisa da API key:

### Obter a Chave

```bash
# 1. Ir em https://jules.google
# 2. Fazer login com GitHub
# 3. Clicar em Account Settings (ícone de usuário)
# 4. Selecionar "API Keys"
# 5. Copiar a chave (começa com "goog_")
```

### Armazenar Seguramente

```bash
# NO repositório GitHub:
# Settings → Secrets and variables → Actions
# Criar novo secret:
Name: JULES_API_KEY
Value: goog_seu_valor_aqui

# Usar no código:
env:
  JULES_API_KEY: ${{ secrets.JULES_API_KEY }}
```

---

## 📡 Passo 3: Chamar Jules via API

### Opção A: Via GitHub Actions (Automático)

```yaml
# .github/workflows/auto-deploy.yml

jobs:
  call-julius:
    runs-on: ubuntu-latest
    steps:
      - name: List connected repositories
        env:
          JULES_API_KEY: ${{ secrets.JULIUS_API_KEY }}
        run: |
          curl -s 'https://jules.googleapis.com/v1alpha/sources' \
            -H "X-Goog-Api-Key: $JULIUS_API_KEY" | jq
```

### Opção B: Via CLI/Terminal (Manual)

```bash
export JULIUS_API_KEY='goog_seu_valor'

# Listar repositórios conectados
curl 'https://jules.googleapis.com/v1alpha/sources' \
  -H "X-Goog-Api-Key: $JULIUS_API_KEY" | jq

# Resposta esperada:
{
  "sources": [
    {
      "name": "sources/github/seu-usuario/seu-repo",
      "id": "github/seu-usuario/seu-repo",
      "githubRepo": {
        "owner": "seu-usuario",
        "repo": "seu-repo"
      }
    }
  ]
}
```

---

## 🚀 Passo 4: Criar Sessão Jules (A Mágica Acontece)

```bash
curl -X POST 'https://jules.googleapis.com/v1alpha/sessions' \
  -H "Content-Type: application/json" \
  -H "X-Goog-Api-Key: $JULIUS_API_KEY" \
  -d '{
    "prompt": "Implementar sistema de cancelamento de agendamentos",
    "sourceContext": {
      "source": "sources/github/seu-usuario/seu-repo",
      "githubRepoContext": {
        "startingBranch": "main"
      }
    },
    "automationMode": "AUTO_CREATE_PR",
    "title": "Feature: Cancelamento de Agendamentos"
  }'

# ✅ Resposta:
{
  "name": "sessions/31415926535897932384",
  "id": "31415926535897932384",
  "state": "PLANNING",
  "prompt": "Implementar sistema de cancelamento...",
  "progress": 15
}
```

### O Que Acontece Internamente

```
Jules recebe o prompt
    ↓
1. Clona TODO seu repositório em uma VM segura no Google Cloud
2. Analisa estrutura (package.json, tsconfig.json, etc)
3. Entende o padrão de código (arquitetura, dependências)
4. Gera um PLANO detalhado com:
   - Quais arquivos serão modificados
   - Qual código será adicionado
   - Quais testes serão criados
5. **AGUARDA APROVAÇÃO** (se não estiver em AUTO_CREATE_PR)
6. Executa o código (dentro da VM)
7. Roda testes automaticamente
8. Cria commits estruturados
9. Abre Pull Request no seu GitHub
```

---

## 🔍 Passo 5: Monitorar Progresso

```bash
SESSION_ID="31415926535897932384"

# Verificar estado (a cada 30 segundos)
curl "https://jules.googleapis.com/v1alpha/sessions/$SESSION_ID" \
  -H "X-Goog-Api-Key: $JULIUS_API_KEY" | jq

# Estados possíveis:
# - PLANNING     (analisando código)
# - EXECUTING    (criando código)
# - COMPLETED    (sucesso)
# - FAILED       (erro)
```

---

## ✅ Passo 6: Resultado - Pull Request Automática

Quando Jules termina, você terá:

```
┌─────────────────────────────────────────────────────┐
│ PULL REQUEST (Criada automaticamente)               │
├─────────────────────────────────────────────────────┤
│ Title: "Feature: Cancel appointments"               │
│ Branch: feature/cancel-appointments-xyz123         │
│                                                     │
│ Commits:                                            │
│ ✅ feat: Add CancelModal component                  │
│ ✅ feat: Add DELETE /api/appointments/:id           │
│ ✅ test: Add comprehensive test suite               │
│                                                     │
│ Files Changed:                                      │
│ + components/appointments/CancelModal.tsx           │
│ + pages/api/appointments/[id].DELETE.ts             │
│ + tests/appointments.cancel.test.ts                 │
│                                                     │
│ Checks:                                             │
│ ✅ 42 tests passed                                  │
│ ✅ 85% coverage                                     │
│ ✅ Lint passed                                      │
│ ✅ Build success                                    │
│                                                     │
│ [Approve] [Request Changes] [Merge]                │
└─────────────────────────────────────────────────────┘
```

---

## 🤖 Passo 7: GitHub Actions Detects PR e Roda Testes

```yaml
# Seu workflow dispara automaticamente quando PR é criada

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      
      - name: Install & Test
        run: |
          npm install
          npm test      # ✅ 42 passed
          npm run lint  # ✅ 0 issues
          npm run build # ✅ Success
```

---

## 🔀 Passo 8: Merge Automático (Condicional)

Se **todos os testes passarem**, GitHub Actions pode fazer merge automático:

```yaml
jobs:
  merge:
    needs: [ci]
    if: success()  # Só roda se CI passou
    runs-on: ubuntu-latest
    steps:
      - name: Merge PR
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          gh pr merge ${{ github.event.number }} \
            --auto \
            --squash \
            --delete-branch
```

---

## 🚢 Passo 9: Render Deploy (AQUI É A INTEGRAÇÃO!)

Quando PR é **mergeada para main**, Render é disparado:

### Setup no Render

```
1. Conectar repositório GitHub ao Render
   - Dashboard → New → Web Service
   - Conectar com seu repositório GitHub
   
2. Desabilitar Auto-Deploy (importante!)
   - Settings → Build and Deploy → Auto-Deploy → OFF
   
3. GitHub Actions vai controlar quando fazer deploy
```

### Webhook Automático

```
Quando commit é feito em main:
  ↓
GitHub Actions detecta (via workflow)
  ↓
Chama Render Deploy Action
  ↓
Render recebe comando de deploy
  ↓
Render faz:
   - npm install
   - npm run build
   - npm start
  ↓
Health checks validam (GET /health → 200)
  ↓
App live em https://seu-app.render.com
```

---

## 💡 Passo 10: Integração com Antigravity (Tarefas Complexas)

Para tarefas **muito grandes**, use Antigravity **antes** de Jules:

```
┌──────────────────────────────────┐
│ ANTIGRAVITY IDE                  │
│ (Planejamento + Design)          │
│                                  │
│ Descrever arquitetura complexa:  │
│ - Refatoração de auth            │
│ - Migração de DB                 │
│ - API redesign                   │
└──────────────────────────────────┘
        ↓ (Gera plano aprovado)
┌──────────────────────────────────┐
│ DIVIDIR EM MICRO-TASKS           │
│ - Task 1: Setup Auth             │
│ - Task 2: Update Routes          │
│ - Task 3: Create Tests           │
│ - Task 4: Documentation          │
└──────────────────────────────────┘
        ↓ (Disparar para cada task)
┌──────────────────────────────────┐
│ JULIUS                           │
│ Executa cada task em sequência   │
│ ou paralela (se independentes)   │
└──────────────────────────────────┘
```

---

## 📊 Timeline Completa: Issue → Production

```
Tempo      | Evento
-----------|─────────────────────────────────────────────
T+0min     | Issue criada e comentário @julius
T+0:30min  | GitHub Actions dispara
T+1min     | Jules API session criada
T+2min     | Jules começa a clonar repositório
T+5min     | Jules termina análise, gera plano
T+5:30min  | ⏳ Aguardando aprovação (se necessário)
T+6min     | ✅ Plano aprovado
T+7min     | Jules começa implementação
T+12min    | Jules roda testes
T+15min    | ✅ Testes passam
T+16min    | Jules cria Pull Request
T+16:30min | GitHub Actions detecta PR
T+17min    | GitHub Actions roda CI/CD pipeline
T+19min    | ✅ Todos os testes passaram
T+19:30min | GitHub Actions faz merge automático
T+20min    | Webhook dispara Render
T+20:30min | Render começa build (Docker)
T+24min    | Render build completo
T+25min    | Deploy iniciado
T+26min    | Health check passa ✅
T+27min    | 🚀 APP LIVE EM PRODUÇÃO

TOTAL: ~27 MINUTOS (sem intervenção manual!)
Tradicional: 3-5 DIAS com várias pessoas
```

---

## 🔐 Configuração Segura (Secrets)

Você precisa desses segredos no GitHub:

| Secret | Valor | Onde Obter |
|--------|-------|-----------|
| `JULIUS_API_KEY` | goog_... | https://jules.google → Account Settings |
| `RENDER_SERVICE_ID` | srv-... | Render Dashboard → Service → URL (copy ID) |
| `RENDER_API_KEY` | ... | https://dashboard.render.com → Account |
| `GITHUB_TOKEN` | Automático | Já existe no GitHub |

### Como Adicionar Secrets

```bash
# Via CLI GitHub
gh secret set JULIUS_API_KEY --body "goog_seu_valor"
gh secret set RENDER_SERVICE_ID --body "srv-seu-id"
gh secret set RENDER_API_KEY --body "sua-api-key"

# Ou via web:
# Repositório → Settings → Secrets and variables → Actions → New
```

---

## ⚡ Exemplo Real: Salão de Beleza

### Issue no GitHub:

```markdown
# Feature: Cancelamento de Agendamentos

Clientes devem conseguir cancelar agendamentos até 24h antes.

Detalhes técnicos:
- Modal de confirmação
- SMS via Twilio
- Auditoria
- Testes com 80%+ cobertura
```

### Comentário:

```
@julius Implemente conforme descrito
```

### O que acontece (automático):

```
1️⃣ GitHub Actions dispara
2️⃣ Chama Julius API com issue body
3️⃣ Julius analisa seu código Next.js + Supabase
4️⃣ Julius gera plano (vê que precisa:
     - CancelModal.tsx (React)
     - DELETE /api/appointments/:id (API)
     - Integration com Twilio (SMS)
     - Tests com Jest)
5️⃣ Julius executa tudo
6️⃣ Julius roda npm test → 42 passed ✅
7️⃣ Julius cria PR
8️⃣ GitHub Actions rodam testes novamente
9️⃣ Tudo OK → Merge automático
🔟 Render detecta novo commit
1️⃣1️⃣ Render faz build e deploy
1️⃣2️⃣ Health checks passam
1️⃣3️⃣ Feature live em produção

TOTAL: ~25 MINUTOS
```

---

## 🎯 Resumo da Integração

**Jules NÃO faz deploy direto**, mas você cria um pipeline onde:

1. **GitHub Issues** = tarefas
2. **@julius mention** = trigger
3. **Jules API** = implementação
4. **GitHub Actions** = orquestração
5. **Render** = deploy final

O resultado é um **fluxo completamente automático** de Issue → Production sem intervenção manual.

---

## 🚀 Próximos Passos

1. Obter Jules API Key
2. Adicionar secrets no GitHub
3. Criar `.github/workflows/auto-deploy.yml` (usar exemplo do documento anterior)
4. Criar primeira Issue de teste
5. Comentar @julius
6. Acompanhar a mágica acontecer ✨

**Tempo total de setup: 30 minutos**
**Economia de tempo por deploy: ~3-5 horas**


[^1]: https://ieeexplore.ieee.org/document/10205946/

[^2]: https://ieeexplore.ieee.org/document/10101113/

[^3]: https://arxiv.org/abs/2508.06495

[^4]: https://arxiv.org/abs/2506.07278

[^5]: http://biorxiv.org/lookup/doi/10.1101/2021.10.18.464256

[^6]: https://www.semanticscholar.org/paper/14c7f1f104875ba7fdefaa8f7c391e5f9e5627d8

[^7]: https://storage.googleapis.com/jnl-up-j-jors-files/journals/1/articles/64/submission/proof/64-1-788-1-10-20151120.pdf

[^8]: https://arxiv.org/pdf/2312.17294.pdf

[^9]: https://arxiv.org/pdf/2311.10516.pdf

[^10]: http://arxiv.org/pdf/2305.18150.pdf

[^11]: https://arxiv.org/pdf/2206.06401.pdf

[^12]: https://www.mdpi.com/2073-431X/13/2/33/pdf?version=1706174086

[^13]: http://arxiv.org/pdf/2408.00921.pdf

[^14]: http://arxiv.org/pdf/2503.04921.pdf

[^15]: https://developers.google.com/jules/api

[^16]: https://jules.google

[^17]: https://developers.googleblog.com/en/level-up-your-dev-game-the-jules-api-is-here/

[^18]: https://github.com/google-labs-code/jules-action

[^19]: https://atalupadhyay.wordpress.com/2025/08/12/googles-jules-ai-coding-agent-from-concept-to-production/

[^20]: https://www.reddit.com/r/google_antigravity/comments/1pk3d7p/just_wanted_to_share_my_own_experience_with/

[^21]: https://github.com/marketplace/actions/deploy-to-render-current-commit-only

[^22]: https://jangwook.net/en/blog/en/jules-autocoding/

[^23]: https://ainativedev.io/news/gemini-3-meets-antigravity-googles-next-step-in-agentic-development

[^24]: https://github.com/marketplace/actions/deploy-to-render

[^25]: https://jules.google/docs/api/reference/

[^26]: https://slashdot.org/software/comparison/Google-Antigravity-vs-Jules/

[^27]: https://github.com/JorgeLNJunior/render-deploy

[^28]: https://www.linkedin.com/pulse/jules-googles-ai-writes-pull-requests-why-full-stack-should-gaddam-4xkhe

[^29]: https://wellstsai.com/en/post/using-google-antigravity/

[^30]: https://github.com/marketplace/actions/deploy-to-render-com

[^31]: https://github.com/SamyRai/Juleson

[^32]: https://lobehub.com/mcp/scarmonit-antigravity-jules-orchestration

[^33]: https://github.com/marketplace/actions/render-deploy-action

[^34]: https://jules.google/docs

[^35]: https://antigravity.codes/workflows

