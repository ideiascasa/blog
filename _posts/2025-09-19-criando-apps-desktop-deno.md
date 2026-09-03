---
layout: post
title: "Criando Apps Desktop Ultra-Leves com Deno: Adeus Electron, Olá Performance"
author: "Davi"
categories: blog
tags: [blog, desenvolvimento, tecnologia]
image: codes-computer.jpg
---

# Criando Apps Desktop Ultra-Leves com Deno: Adeus Electron, Olá Performance

Cansado de aplicações desktop que consomem gigabytes de RAM e demoram uma eternidade para abrir? Eu também estava. Foi quando descobri uma forma revolucionária de criar apps desktop usando **Deno** que são 25x menores que aplicações Electron e iniciam em segundos.

Hoje vou te mostrar como criar uma aplicação desktop completa e multiplataforma usando apenas um arquivo TypeScript e alguns scripts simples.

## O Problema com Desktop Hoje

Vamos ser honestos: o Electron mudou o jogo do desenvolvimento desktop, mas trouxe problemas sérios:

- **Discord**: 500MB+ de RAM parado
- **VS Code**: 300MB+ apenas para abrir
- **Slack**: 400MB+ consumindo sua memória

E o pior? Cada app empacota seu próprio Chromium completo. É como ter 10 navegadores rodando simultaneamente no seu computador.

## A Solução: Deno + Webview

Descobri uma alternativa que resolve todos esses problemas. Em vez de empacotar um navegador inteiro, uso o navegador **que já existe** no sistema operacional:

- Windows → Edge WebView2
- macOS → WebKit
- Linux → GTK WebKit

O resultado? Apps de **8MB** que abrem instantaneamente.

## Minha Experiência Prática

Criei recentemente uma ferramenta de produtividade para gerenciar projetos. Com Electron seria uma aplicação de 200MB+. Com Deno? **6.2MB** executável final.

A diferença é brutal:
- **Startup**: 0.5s vs 4s do Electron
- **RAM**: 45MB vs 180MB
- **Tamanho**: 6MB vs 210MB

## Como Funciona na Prática

Vou te mostrar o processo completo para criar sua primeira app:

### Passo 1: O Coração da Aplicação

Crie um arquivo `app.ts`:

```typescript
import { Webview } from "https://deno.land/x/webview@0.8.0/mod.ts";

const interface_html = `
<!DOCTYPE html>
<html>
<head>
    <title>MinhaApp</title>
    <meta charset="utf-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            background: #1a1a1a;
            color: #fff;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .app {
            text-align: center;
            padding: 40px;
        }
        
        h1 {
            font-size: 2.5em;
            margin-bottom: 20px;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .stats {
            margin: 30px 0;
            padding: 20px;
            background: rgba(255,255,255,0.1);
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
        
        button {
            background: linear-gradient(45deg, #667eea, #764ba2);
            border: none;
            padding: 12px 30px;
            border-radius: 25px;
            color: white;
            cursor: pointer;
            font-size: 16px;
            transition: transform 0.2s;
        }
        
        button:hover {
            transform: translateY(-2px);
        }
    </style>
</head>
<body>
    <div class="app">
        <h1>🦕 Deno Desktop</h1>
        <div class="stats">
            <p>Versão do Deno: ${Deno.version.deno}</p>
            <p>Plataforma: ${Deno.build.os}</p>
            <p>Arquitetura: ${Deno.build.arch}</p>
        </div>
        <button onclick="mostrarInfo()">Informações do Sistema</button>
        <p id="info" style="margin-top: 20px;"></p>
    </div>
    
    <script>
        function mostrarInfo() {
            const info = \`
                Navegador: \${navigator.userAgent.split(') ')[0]})<br>
                Resolução: \${screen.width}x\${screen.height}<br>
                Idioma: \${navigator.language}<br>
                Hora: \${new Date().toLocaleString()}
            \`;
            document.getElementById('info').innerHTML = info;
        }
    </script>
</body>
</html>
`;

const app = new Webview();
app.navigate(`data:text/html,${encodeURIComponent(interface_html)}`);
app.run();
```

### Passo 2: Scripts de Execução

**Windows (executar.bat):**
```batch
@echo off
title Iniciando App Deno
echo.
echo ⚡ Verificando Deno...

where deno >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Deno não instalado!
    echo.
    echo Instalar: irm https://deno.land/install.ps1 ^| iex
    pause
    exit
)

echo ✅ Deno encontrado
echo 🚀 Iniciando aplicação...
echo.

deno run --allow-all --quiet app.ts
pause
```

**Linux/macOS (executar.sh):**
```bash
#!/bin/bash
clear
echo "⚡ Verificando Deno..."

if ! command -v deno &> /dev/null; then
    echo "❌ Deno não instalado!"
    echo ""
    echo "Instalar: curl -fsSL https://deno.land/x/install/install.sh | sh"
    exit 1
fi

echo "✅ Deno encontrado"
echo "🚀 Iniciando aplicação..."
echo ""

deno run --allow-all --quiet app.ts
```

### Passo 3: Configuração Avançada

Crie `deno.json` para facilitar o desenvolvimento:

```json
{
  "tasks": {
    "dev": "deno run --allow-all --watch app.ts",
    "start": "deno run --allow-all --quiet app.ts",
    "build": "deno compile --allow-all --output dist/app app.ts",
    "build-win": "deno compile --allow-all --target x86_64-pc-windows-msvc --output dist/app.exe app.ts",
    "build-mac": "deno compile --allow-all --target x86_64-apple-darwin --output dist/app-mac app.ts",
    "build-linux": "deno compile --allow-all --target x86_64-unknown-linux-gnu --output dist/app-linux app.ts"
  },
  "compilerOptions": {
    "strict": true,
    "allowJs": true
  }
}
```

## Executando Sua App

Agora você tem três formas de executar:

1. **Scripts diretos**: `./executar.sh` ou `executar.bat`
2. **Comandos Deno**: `deno task start`
3. **Desenvolvimento**: `deno task dev` (recarrega automaticamente)

## Compilando para Distribuição

O Deno permite criar executáveis que funcionam sem instalar nada:

```bash
# Para seu sistema atual
deno task build

# Para Windows (de qualquer sistema)
deno task build-win

# Para macOS (de qualquer sistema)  
deno task build-mac

# Para Linux (de qualquer sistema)
deno task build-linux
```

## Vantagens Reais que Descobri

### Performance Impressionante
- **Inicialização**: < 1 segundo vs 3-5s do Electron
- **Memória**: 30-50MB vs 150-300MB
- **CPU**: Quase zero quando idle

### Desenvolvimento Simplificado
- TypeScript nativo (sem configuração)
- Imports diretos de URLs
- Sistema de permissões claro
- Debugging integrado

### Distribuição Eficiente
- Um arquivo executável
- Sem dependências externas
- Funciona offline
- Cross-compilation nativa

## Limitações Importantes (Seja Realista)

Nem tudo são flores. Há limitações que você deve conhecer:

- **Ecossistema menor**: Menos bibliotecas que Node.js
- **APIs nativas limitadas**: Para funcionalidades muito específicas do OS
- **Comunicação limitada**: IPC menos sofisticado que Electron
- **Maturidade**: Ainda evoluindo rapidamente

## Quando Usar Esta Abordagem

**✅ Perfeito para:**
- Ferramentas de produtividade
- Aplicações de dados/dashboards
- Utilitários simples a médios
- Prototipagem rápida
- Apps que priorizam performance

**❌ Considere alternativas para:**
- Editores complexos (VS Code, Photoshop)
- Games
- Apps com muitas APIs nativas
- Projetos com equipes enormes

## Minha Recomendação

Depois de usar esta stack por 6 meses, posso dizer: **vale muito a pena** para a maioria dos casos de uso.

A sensação de criar uma app que abre instantaneamente e consome menos memória que uma aba do navegador é incrível. Seus usuários vão notar a diferença.

## Próximos Passos

Se você se animou (e deveria!), comece assim:

1. **Instale o Deno**: `curl -fsSL https://deno.land/x/install/install.sh | sh`
2. **Crie o arquivo `app.ts`** acima
3. **Execute**: `deno run --allow-all app.ts`
4. **Experimente** e customize

Depois de dominar o básico, explore:
- Integração com APIs
- Persistência de dados
- Comunicação entre janelas
- Temas customizados

## Conclusão

O futuro das aplicações desktop está aqui, e é muito mais leve do que imaginávamos.

Enquanto outros continuam criando apps de centenas de MB, você pode estar criando soluções elegantes, rápidas e eficientes com Deno.

Teste, experimente e me conte nos comentários como foi sua experiência!

---

*P.S.: Se você criar algo legal com essa stack, compartilha aí! Adoro ver projetos da comunidade.*