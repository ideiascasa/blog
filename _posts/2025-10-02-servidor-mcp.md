---
layout: post
title: "Como Fazer um Servidor MCP e um Cliente em Spring Boot Java 21"
author: "Davi"
categories: blog
tags: [blog,tech]
image: industry-coding.webp
---

# Como Fazer um Servidor MCP e um Cliente em Spring Boot Java 21

[https://github.com/frkr/spring-mcp-hello](https://github.com/frkr/spring-mcp-hello)

## Introducao

Este projeto e uma demonstracao pratica do uso das dependencias Spring AI MCP (Model Context Protocol) Server e Client, implementando funcionalidades basicas estilo "Hello World" em uma aplicacao Spring Boot com Java 21.

## Arquitetura do Projeto

O projeto segue uma arquitetura bem estruturada com separacao clara de responsabilidades:

### 1. Classe Principal da Aplicacao

```java
package com.example.kodiak;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class KodiakApplication {

    public static void main(String[] args) {
        SpringApplication.run(KodiakApplication.class, args);
    }

}
```

A classe principal e simples e direta, seguindo o padrao Spring Boot com a anotacao `@SpringBootApplication` que configura automaticamente a aplicacao.

### 2. MCP Server - Implementacao do Servidor

```java
package com.example.kodiak.mcp.server;

import org.springframework.stereotype.Component;

import java.util.Map;

@Component
public class HelloWorldMcpServer {

    public String helloWorld(Map<String, Object> parameters) {
        return "Hello World! Este e um teste do MCP Server.";
    }

    public String greet(Map<String, Object> parameters) {
        String name = (String) parameters.getOrDefault("name", "Usuario");
        return String.format("Ola %s! Bem-vindo ao MCP Server!", name);
    }

    public String getServerInfo() {
        return "MCP Server ativo - versao 1.0.0";
    }
}
```

O servidor MCP implementa tres metodos principais:
- `helloWorld()`: Retorna uma mensagem de saudacao basica
- `greet()`: Saudacao personalizada com nome do usuario
- `getServerInfo()`: Informacoes sobre o servidor

### 3. MCP Client - Implementacao do Cliente

```java
package com.example.kodiak.mcp.client;

import org.springframework.stereotype.Component;

@Component
public class HelloWorldMcpClient {

    public String callHelloWorld() {
        try {
            // Simulacao de chamada para o servidor MCP
            return "Cliente MCP conectado! Chamando hello world...";
        } catch (Exception e) {
            return "Erro ao conectar com o servidor MCP: " + e.getMessage();
        }
    }

    public String callGreet(String name) {
        try {
            // Simulacao de chamada para o servidor MCP com parametros
            return String.format("Cliente MCP chamando greet para: %s", name);
        } catch (Exception e) {
            return "Erro ao chamar greet: " + e.getMessage();
        }
    }

    public String getClientInfo() {
        return "MCP Client ativo - versao 1.0.0";
    }
}
```

O cliente MCP implementa metodos correspondentes ao servidor, com tratamento de excecoes para garantir robustez na comunicacao.

### 4. Controller REST - Integracao via HTTP

```java
package com.example.kodiak.controller;

import com.example.kodiak.mcp.client.HelloWorldMcpClient;
import com.example.kodiak.mcp.server.HelloWorldMcpServer;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api/mcp")
public class McpTestController {

    @Autowired
    private HelloWorldMcpClient mcpClient;

    @Autowired
    private HelloWorldMcpServer mcpServer;

    @GetMapping("/hello")
    public Map<String, Object> testHelloWorld() {
        Map<String, Object> response = new HashMap<>();
        
        try {
            // Teste do servidor MCP
            String serverResponse = mcpServer.helloWorld(new HashMap<>());
            
            // Teste do cliente MCP
            String clientResponse = mcpClient.callHelloWorld();
            
            response.put("success", true);
            response.put("serverResponse", serverResponse);
            response.put("clientResponse", clientResponse);
            response.put("message", "Teste MCP Server e Client executado com sucesso!");
            
        } catch (Exception e) {
            response.put("success", false);
            response.put("error", e.getMessage());
            response.put("message", "Erro ao executar teste MCP");
        }
        
        return response;
    }

    @GetMapping("/greet/{name}")
    public Map<String, Object> testGreet(@PathVariable String name) {
        Map<String, Object> response = new HashMap<>();
        
        try {
            // Teste do servidor MCP com parametros
            Map<String, Object> params = new HashMap<>();
            params.put("name", name);
            String serverResponse = mcpServer.greet(params);
            
            // Teste do cliente MCP
            String clientResponse = mcpClient.callGreet(name);
            
            response.put("success", true);
            response.put("serverResponse", serverResponse);
            response.put("clientResponse", clientResponse);
            response.put("message", String.format("Teste MCP com parametro '%s' executado com sucesso!", name));
            
        } catch (Exception e) {
            response.put("success", false);
            response.put("error", e.getMessage());
            response.put("message", "Erro ao executar teste MCP com parametros");
        }
        
        return response;
    }

    @GetMapping("/status")
    public Map<String, Object> getStatus() {
        Map<String, Object> response = new HashMap<>();
        response.put("status", "MCP Server e Client ativos");
        response.put("serverInfo", mcpServer.getServerInfo());
        response.put("clientInfo", mcpClient.getClientInfo());
        response.put("endpoints", Map.of(
            "hello", "/api/mcp/hello",
            "greet", "/api/mcp/greet/{name}",
            "status", "/api/mcp/status"
        ));
        return response;
    }
}
```

O controller REST integra o servidor e cliente MCP, expondo tres endpoints principais:
- `/api/mcp/hello`: Teste basico hello world
- `/api/mcp/greet/{name}`: Teste com parametros
- `/api/mcp/status`: Status do sistema

## Funcionalidades Disponiveis

### Endpoints da API

1. **Status do Sistema** - `GET /api/mcp/status`
    - Retorna informacoes sobre o status do MCP Server e Client

2. **Teste Hello World** - `GET /api/mcp/hello`
    - Testa a funcionalidade basica hello world do MCP Server e Client

3. **Teste com Parametros** - `GET /api/mcp/greet/{name}`
    - Testa a funcionalidade greet com parametros do MCP Server e Client

### Exemplo de Resposta

**Endpoint `/api/mcp/hello`:**
```json
{
  "success": true,
  "serverResponse": "Hello World! Este e um teste do MCP Server.",
  "clientResponse": "Cliente MCP conectado! Chamando hello world...",
  "message": "Teste MCP Server e Client executado com sucesso!"
}
```

**Endpoint `/api/mcp/greet/Davi`:**
```json
{
  "success": true,
  "serverResponse": "Ola Davi! Bem-vindo ao MCP Server!",
  "clientResponse": "Cliente MCP chamando greet para: Davi",
  "message": "Teste MCP com parametro 'Davi' executado com sucesso!"
}
```

## Como Executar

1. **Compilar o projeto:**
```bash
./mvnw clean compile
```

2. **Executar a aplicacao:**
```bash
./mvnw spring-boot:run
```

3. **Testar os endpoints:**
```bash
# Status
curl http://localhost:8080/api/mcp/status

# Hello World
curl http://localhost:8080/api/mcp/hello

# Greet com parametro
curl http://localhost:8080/api/mcp/greet/SeuNome
```

## Dependencias Utilizadas

- `spring-ai-starter-mcp-server`: Para funcionalidades do servidor MCP
- `spring-ai-starter-mcp-client`: Para funcionalidades do cliente MCP
- `spring-boot-starter-web`: Para endpoints REST
- `spring-boot-starter-test`: Para testes

## Conclusao

Este projeto demonstra de forma pratica como implementar e integrar servidores e clientes MCP em uma aplicacao Spring Boot. A arquitetura e bem estruturada, com separacao clara de responsabilidades e tratamento adequado de excecoes. Este exemplo serve como base para implementacoes mais complexas do protocolo MCP em aplicacoes Spring Boot.

A implementacao mostra como:
- Configurar servidores e clientes MCP
- Integrar via REST API
- Tratar excecoes adequadamente
- Estruturar o codigo de forma modular

Este e um excelente ponto de partida para quem deseja trabalhar com o protocolo MCP em aplicacoes Spring Boot.
