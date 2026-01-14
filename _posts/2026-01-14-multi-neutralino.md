---
layout: post
title: "Construindo uma Aplicação Multiplataforma com Neutralino, React e TypeScript"
author: "Davi"
categories: blog
tags: [blog,tech]
image: neutra.png
---

Olá! Neste post vamos criar uma aplicação portable e multifuncional usando **Neutralino** como base. A ideia é simples, mas poderosa: um único executável que funciona tanto como **GUI desktop (Windows, macOS, Linux)** quanto como **CLI (especialmente no Linux com cron)**.

## 🎯 O Conceito

Imagine você tendo: 

- Um `app.exe` (ou `app-linux`) que pode ser executado na máquina local e abre uma interface React bonita
- O mesmo executável copiado para um servidor Linux, rodando via cron com parâmetro `--run` para execução headless

Tudo isso com **zero dependências externas**, 100% TypeScript, e portable para qualquer lugar. Vamos lá!

## 📋 Arquitetura da Solução

```
my-portable-app/
├── src/
│   ├── cli/
│   │   └── index.ts          # Lógica CLI (--run flag)
│   ├── desktop/
│   │   ├── App.tsx           # Componente React principal
│   │   └── main.ts           # Entry point desktop
│   ├── shared/
│   │   └── utils.ts          # Funções compartilhadas
│   └── index.ts              # Router: detecta ambiente
├── resources/
│   ├── css/
│   ├── html/
│   └── js/
├── neutralino.conf.json      # Configuração Neutralino
├── package.json
└── tsconfig.json
```


## 🚀 Setup Inicial

### 1. Criar o projeto Neutralino com TypeScript

```bash
# Instale o CLI do Neutralino globalmente
npm install -g @neutralinojs/neu

# Crie um novo projeto
neu create my-portable-app

cd my-portable-app

# Instale as dependências
npm install
npm install --save-dev typescript tsx @types/node react react-dom
npm install --save-dev -D @types/react @types/react-dom
```


### 2. Configure o `tsconfig.json`

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "jsx": "react-jsx",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "outDir": "./dist",
    "rootDir": "./src"
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
```


### 3. Configure o `neutralino.conf.json`

```json
{
  "cli": {
    "binaryName": "my-portable-app",
    "resourcesPath": "/resources/",
    "extensionsPath": "/extensions/",
    "documentRoot": "/resources/",
    "url": "/index.html"
  },
  "documentRoot": "/resources/",
  "url": "/index.html",
  "enableServer": true,
  "enableNativeAPI": true,
  "enableExtensions": true,
  "nativeBlockList": [],
  "documentRoot": "/resources/",
  "url": "/index.html",
  "defaultOpen": true,
  "url": "/",
  "logging": {
    "enabled": true,
    "writeToLogFile": false
  },
  "documentRoot": "/resources/",
  "url": "/index.html"
}
```


## 💻 Implementação

### Arquivo: `src/shared/utils.ts`

Funções compartilhadas entre CLI e GUI:

```typescript
export interface AppConfig {
  mode: 'cli' | 'gui';
  verbose: boolean;
}

export function getHelloWorld(): string {
  return 'Hello World';
}

export async function executeTask(taskName: string): Promise<void> {
  console.log(`[Task] Executando: ${taskName}`);
  console.log(`[Result] ${getHelloWorld()}`);
  
  // Simule uma operação assíncrona
  await new Promise(resolve => setTimeout(resolve, 100));
  
  console.log('[Task] Concluído com sucesso!');
}

export function parseArguments(args: string[]): { 
  mode: 'cli' | 'gui'; 
  flags: Record<string, string | boolean> 
} {
  const flags: Record<string, string | boolean> = {};
  let mode: 'cli' | 'gui' = 'gui';

  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    
    if (arg === '--run') {
      mode = 'cli';
      flags.run = true;
    } else if (arg === '--verbose') {
      flags.verbose = true;
    } else if (arg.startsWith('--')) {
      const [key, value] = arg.substring(2).split('=');
      flags[key] = value || true;
    }
  }

  return { mode, flags };
}
```


### Arquivo: `src/cli/index.ts`

Modo CLI para execução headless:

```typescript
import { executeTask, getHelloWorld } from '../shared/utils';

/**
 * Modo CLI - Executado quando --run é passado
 * Ideal para cron jobs no Linux
 */
export async function runCLI(): Promise<void> {
  console.log('╔════════════════════════════════════╗');
  console.log('║   My Portable App - CLI Mode       ║');
  console.log('╚════════════════════════════════════╝');
  console.log('');

  try {
    // Exiba a mensagem Hello World
    console.log(`✓ ${getHelloWorld()}`);
    console.log('');

    // Execute alguma tarefa
    console.log('▶ Iniciando execução de tarefas...');
    console.log('');
    
    await executeTask('task-1');
    
    console.log('');
    console.log('✓ Execução concluída com êxito!');
    console.log('');

    // Retorne status de sucesso
    process.exit(0);
  } catch (error) {
    console.error('✗ Erro durante execução:', error);
    process.exit(1);
  }
}
```


### Arquivo: `src/desktop/App.tsx`

Componente React para GUI:

```typescript
import React, { useEffect, useState } from 'react';
import { getHelloWorld, executeTask } from '../shared/utils';

interface LogEntry {
  timestamp: string;
  message: string;
  type: 'info' | 'success' | 'error';
}

export function App(): JSX.Element {
  const [logs, setLogs] = useState<LogEntry[]>([]);
  const [loading, setLoading] = useState(false);

  const addLog = (message: string, type: 'info' | 'success' | 'error' = 'info'): void => {
    const timestamp = new Date().toLocaleTimeString('pt-BR');
    setLogs(prev => [...prev, { timestamp, message, type }]);
  };

  useEffect(() => {
    addLog(getHelloWorld(), 'success');
  }, []);

  const handleExecuteTask = async (): Promise<void> => {
    setLoading(true);
    addLog('▶ Iniciando tarefa...', 'info');

    try {
      await executeTask('gui-task');
      addLog('✓ Tarefa concluída com sucesso!', 'success');
    } catch (error) {
      addLog(`✗ Erro: ${error}`, 'error');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <header style={styles.header}>
        <h1>📦 My Portable App</h1>
        <p>GUI + CLI Multiplataforma</p>
      </header>

      <main style={styles.main}>
        <section style={styles.section}>
          <h2>Console de Execução</h2>
          <div style={styles.console}>
            {logs.map((log, idx) => (
              <div
                key={idx}
                style={{
                  ...styles.logEntry,
                  borderLeft: `4px solid ${
                    log.type === 'success'
                      ? '#10b981'
                      : log.type === 'error'
                        ? '#ef4444'
                        : '#3b82f6'
                  }`,
                  color: 
                    log.type === 'success'
                      ? '#10b981'
                      : log.type === 'error'
                        ? '#ef4444'
                        : '#111827',
                }}
              >
                <span style={styles.timestamp}>[{log.timestamp}]</span>
                <span>{log.message}</span>
              </div>
            ))}
          </div>
        </section>

        <section style={styles.section}>
          <h2>Ações</h2>
          <button
            onClick={handleExecuteTask}
            disabled={loading}
            style={{
              ...styles.button,
              opacity: loading ? 0.6 : 1,
              cursor: loading ? 'not-allowed' : 'pointer',
            }}
          >
            {loading ? '⏳ Executando...' : '▶ Executar Tarefa'}
          </button>
        </section>
      </main>

      <footer style={styles.footer}>
        <small>v1.0.0 | TypeScript + React + Neutralino</small>
      </footer>
    </div>
  );
}

const styles: Record<string, React.CSSProperties> = {
  container: {
    minHeight: '100vh',
    backgroundColor: '#f3f4f6',
    display: 'flex',
    flexDirection: 'column',
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif',
  },
  header: {
    backgroundColor: '#1f2937',
    color: 'white',
    padding: '2rem',
    textAlign: 'center',
    borderBottom: '4px solid #3b82f6',
  },
  main: {
    flex: 1,
    padding: '2rem',
    maxWidth: '800px',
    margin: '0 auto',
    width: '100%',
  },
  section: {
    backgroundColor: 'white',
    borderRadius: '0.5rem',
    padding: '1.5rem',
    marginBottom: '1.5rem',
    boxShadow: '0 1px 3px rgba(0,0,0,0.1)',
  },
  console: {
    backgroundColor: '#111827',
    color: '#ecf0f1',
    padding: '1rem',
    borderRadius: '0.375rem',
    fontFamily: 'Courier New, monospace',
    fontSize: '0.875rem',
    maxHeight: '300px',
    overflowY: 'auto',
    marginBottom: '1rem',
  },
  logEntry: {
    padding: '0.5rem',
    marginBottom: '0.25rem',
    borderRadius: '0.25rem',
  },
  timestamp: {
    color: '#9ca3af',
    marginRight: '0.5rem',
    fontWeight: 'bold',
  },
  button: {
    backgroundColor: '#3b82f6',
    color: 'white',
    border: 'none',
    padding: '0.75rem 1.5rem',
    borderRadius: '0.375rem',
    fontSize: '1rem',
    fontWeight: '600',
    boxShadow: '0 1px 3px rgba(0,0,0,0.1)',
  },
  footer: {
    backgroundColor: '#f9fafb',
    borderTop: '1px solid #e5e7eb',
    padding: '1rem',
    textAlign: 'center',
    color: '#6b7280',
  },
};
```


### Arquivo: `src/desktop/main.ts`

Entry point para o modo desktop:

```typescript
import { App } from './App';
import React from 'react';
import { createRoot } from 'react-dom/client';

/**
 * Modo Desktop - Renderiza a aplicação React
 */
export function initializeDesktopApp(): void {
  const rootElement = document.getElementById('root');
  
  if (!rootElement) {
    console.error('Elemento #root não encontrado!');
    return;
  }

  const root = createRoot(rootElement);
  root.render(React.createElement(App));
}

// Inicialize quando o documento estiver pronto
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeDesktopApp);
} else {
  initializeDesktopApp();
}
```


### Arquivo: `src/index.ts`

Router principal - detecta ambiente:

```typescript
import { parseArguments } from './shared/utils';
import { runCLI } from './cli';

/**
 * Ponto de entrada da aplicação
 * Detecta se está em modo CLI ou Desktop
 */
async function main(): Promise<void> {
  // Em Neutralino, Neutralino.events.onWindowOpen dispara quando GUI abre
  // Em Node.js direto, process.argv tem os argumentos da CLI

  // Verifique se está rodando em Node.js
  if (typeof process !== 'undefined' && process.versions && process.versions.node) {
    // Modo Node.js CLI
    const args = process.argv.slice(2);
    const { mode } = parseArguments(args);

    if (mode === 'cli') {
      await runCLI();
      return;
    }
  }

  // Modo Desktop (GUI)
  if (typeof window !== 'undefined') {
    const { initializeDesktopApp } = await import('./desktop/main');
    initializeDesktopApp();
  }
}

main().catch(error => {
  console.error('Erro crítico:', error);
  process.exit(1);
});
```


### Arquivo: `resources/index.html`

HTML principal:

```html
<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My Portable App</title>
    <style>
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }
      
      body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      }

      #root {
        width: 100%;
        min-height: 100vh;
      }
    </style>
  </head>
  <body>
    <div id="root"></div>
    
    <!-- Carregue o Neutralino API (se disponível) -->
    <script src="js/neutralino.js"></script>
    
    <!-- Seu código compilado -->
    <script type="module" src="js/app.js"></script>
  </body>
</html>
```


## 📦 Build e Deploy

### Script de build no `package.json`:

```json
{
  "scripts": {
    "dev": "neu run",
    "build": "tsc && neu build",
    "build:linux": "tsc && neu build --release linux-x64",
    "build:windows": "tsc && neu build --release windows-x64",
    "build:macos": "tsc && neu build --release macos-x64",
    "cli": "tsx src/index.ts --run",
    "gui": "neu run"
  }
}
```


### Build para cada plataforma:

```bash
# Build para Linux (64-bit)
npm run build:linux

# Build para Windows (64-bit)
npm run build:windows

# Build para macOS (Universal)
npm run build:macos
```


## 🐧 Usando no Linux com Cron

Copie o executável para seu servidor e configure no crontab:

```bash
# Copie o executável
scp dist/my-portable-app-linux_x64 user@server:/opt/apps/

# No servidor, edite o crontab
crontab -e

# Adicione esta linha para executar diariamente às 2 da manhã
0 2 * * * /opt/apps/my-portable-app-linux_x64 --run

# Ou a cada 30 minutos
*/30 * * * * /opt/apps/my-portable-app-linux_x64 --run --verbose
```


## ✨ Características Principais

✅ **100% Portable** - Nenhuma dependência externa necessária
✅ **Multiplataforma** - Windows, macOS, Linux com o mesmo código
✅ **Dual Mode** - GUI moderna (React) + CLI para servidores
✅ **TypeScript** - Type-safe em toda a aplicação
✅ **Leve** - Arquivo final com ~50-100MB (comprimido ~20MB)
✅ **Zero Config** - Basta copiar e executar
✅ **Cron Ready** - Perfeito para job scheduling no Linux

## 🎓 Conclusão

Com essa arquitetura, você consegue:

1. **Desenvolver localmente** com React hot-reload
2. **Distribuir para usuários** como GUI desktop portable
3. **Rodar no servidor** como CLI headless via cron
4. **Manter código único** compartilhado entre os dois modos
5. **Zero dependências** em qualquer máquina que execute

Seja criativo! Você pode expandir isso com:

- Sincronização de dados entre GUI e CLI
- Armazenamento local com SQLite
- APIs HTTP para integração
- Plugins via extensões Neutralino
- Logging persistente
- Auto-updates

Happy coding! 🚀

***

**Gostou deste tutorial?** Deixe um comentário ou abra uma issue se tiver dúvidas sobre implementação!
<span style="display:none">[^1_1][^1_10][^1_11][^1_12][^1_13][^1_14][^1_15][^1_16][^1_17][^1_18][^1_19][^1_2][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_3][^1_30][^1_31][^1_32][^1_33][^1_4][^1_5][^1_6][^1_7][^1_8][^1_9]</span>

<div align="center">⁂</div>

[^1_1]: https://arxiv.org/abs/2411.09607

[^1_2]: https://www.semanticscholar.org/paper/5bb1bf39cc8b20edbcf141fe1d81c9e21e5f80d5

[^1_3]: https://ieeexplore.ieee.org/document/10756687/

[^1_4]: https://arxiv.org/abs/2408.15729

[^1_5]: https://aclanthology.org/2024.semeval-1.60

[^1_6]: https://ijsir.org/index.php/IJSIR/article/view/14

[^1_7]: https://link.springer.com/10.1007/978-3-031-70359-1

[^1_8]: https://link.aps.org/doi/10.1103/PhysRevD.110.043528

[^1_9]: https://doi.apa.org/doi/10.1037/tra0001724

[^1_10]: https://www.semanticscholar.org/paper/1d63c032d905ec3632a0d61588bd0cf24a2daff1

[^1_11]: http://link.aps.org/pdf/10.1103/PhysRevD.109.103037

[^1_12]: https://www.epj-conferences.org/articles/epjconf/pdf/2024/05/epjconf_chep2024_05015.pdf

[^1_13]: https://arxiv.org/pdf/0909.1492.pdf

[^1_14]: http://arxiv.org/pdf/1211.4873.pdf

[^1_15]: http://arxiv.org/abs/2410.05380

[^1_16]: http://arxiv.org/pdf/2501.04309.pdf

[^1_17]: https://escholarship.org/content/qt20v0155k/qt20v0155k.pdf?t=r6fjkq

[^1_18]: https://arxiv.org/abs/0708.3342

[^1_19]: https://www.typescriptlang.org/pt/play/javascript/javascript-essentials/hello-world.ts.html

[^1_20]: https://www.youtube.com/watch?v=VDgihqrZUQg

[^1_21]: https://franciscochaves.com.br/blog/hello-world-em-typescript/

[^1_22]: https://www.youtube.com/watch?v=akze3iCZa2U

[^1_23]: https://www.youtube.com/watch?v=TyqaIE_g1x4

[^1_24]: https://neutralino.js.org

[^1_25]: https://stackoverflow.com/questions/71705998/is-there-a-way-to-create-a-neutralinojs-project-based-on-svelte-and-typescript

[^1_26]: https://www.reddit.com/r/programming/comments/xrxb23/build_lightweight_crossplatform_desktop_apps_with/

[^1_27]: https://learn.microsoft.com/pt-pt/dotnet/csharp/tour-of-csharp/tutorials/hello-world

[^1_28]: https://github.com/neutralinojs/neutralinojs/releases

[^1_29]: https://neutralino.js.org/docs/release-notes/cli/

[^1_30]: https://dev.to/ajeebkp23/neutralinojs-for-lightweight-crossplatform-applications-2odn

[^1_31]: https://www.youtube.com/watch?v=GuDUgnitWEA

[^1_32]: https://codezri.org/blog/neutralinojs-2024-roadmap/

[^1_33]: https://neutralino.js.org/docs/cli/neu-cli/


---

# é possivel compilar as versoes windows e linux usando meu mac ?

Sim, é totalmente possível compilar para Windows e Linux usando seu Mac! Neutralino suporta **cross-compilation** nativamente. Vou detalhar as opções:

## ✅ Cross-Compilation no Mac

### Opção 1: Usando Neutralino CLI (Recomendado)

O Neutralino CLI permite compilar para qualquer plataforma a partir do seu Mac:

```bash
# Build para Linux (64-bit) no Mac
neu build --release linux-x64

# Build para Windows (64-bit) no Mac
neu build --release windows-x64

# Build para macOS (Universal binary)
neu build --release macos-x64

# Build para todas as plataformas de uma vez
neu build --release
```

Isso gera os executáveis na pasta `dist/`:

```
dist/
├── my-portable-app-linux_x64/
├── my-portable-app-windows_x64/
└── my-portable-app-macos_x64/
```


### Opção 2: Usando Docker para Isolamento (Avançado)

Se quiser ambiente totalmente isolado:

```bash
# Instale Docker Desktop no Mac (se não tiver)
brew install docker

# Crie um Dockerfile para compilação cruzada
cat > Dockerfile << 'EOF'
FROM ubuntu:22.04

# Instale dependências
RUN apt-get update && apt-get install -y \
    curl \
    npm \
    git \
    build-essential

# Instale Node.js
RUN npm install -g npm@latest

# Instale Neutralino CLI
RUN npm install -g @neutralinojs/neu

WORKDIR /app

# Copie seu projeto
COPY . .

# Instale dependências do projeto
RUN npm install

# Build
CMD ["neu", "build", "--release"]
EOF

# Execute o build dentro do container
docker build -t my-app-builder .
docker run -v $(pwd)/dist:/app/dist my-app-builder

# Os arquivos compilados estarão em ./dist/
```


## 📋 Verificação de Dependências no Mac

Antes de compilar, certifique-se que você tem:

```bash
# Verifique Node.js
node --version  # v18+ recomendado
npm --version   # v9+

# Verifique Neutralino
neu --version

# Se não tiver, instale:
npm install -g @neutralinojs/neu

# Verifique ferramentas de build (opcional)
xcode-select --install  # Isso vai pedir permissão para instalar
```


## 🔧 Configuração do `neutralino.conf.json` para Cross-Compilation

```json
{
  "cli": {
    "resourcesPath": "/resources/",
    "extensionsPath": "/extensions/",
    "documentRoot": "/resources/",
    "url": "/index.html",
    "binaryName": "my-portable-app"
  },
  "url": "/index.html",
  "documentRoot": "/resources/",
  "defaultOpen": true,
  "enableServer": true,
  "enableNativeAPI": true,
  "enableExtensions": false,
  "nativeBlockList": [],
  "logging": {
    "enabled": true,
    "writeToLogFile": false
  },
  "windowIcon": "/resources/icons/icon-256x256.png",
  "documentRoot": "/resources/",
  "url": "/index.html"
}
```


## 📦 Script de Build Completo no `package.json`

```json
{
  "name": "my-portable-app",
  "version": "1.0.0",
  "description": "App multiplataforma GUI + CLI",
  "scripts": {
    "dev": "neu run",
    "build": "npm run compile && neu build",
    "build:all": "npm run compile && neu build --release",
    "build:mac": "npm run compile && neu build --release macos-x64",
    "build:windows": "npm run compile && neu build --release windows-x64",
    "build:linux": "npm run compile && neu build --release linux-x64",
    "compile": "tsc",
    "compile:watch": "tsc --watch",
    "cli": "tsx src/index.ts --run",
    "gui": "neu run"
  },
  "devDependencies": {
    "@neutralinojs/neu": "^latest",
    "@types/node": "^20",
    "@types/react": "^18",
    "@types/react-dom": "^18",
    "react": "^18",
    "react-dom": "^18",
    "tsx": "^4",
    "typescript": "^5"
  }
}
```


## 🚀 Workflow Completo no Mac

```bash
# 1. Clone/setup seu projeto
git clone seu-repo
cd seu-repo
npm install

# 2. Compile TypeScript
npm run compile

# 3. Build para TODAS as plataformas
npm run build:all

# OU compile individual:
npm run build:mac
npm run build:windows
npm run build:linux

# 4. Teste os binários
# No Mac, teste o macOS
dist/my-portable-app-macos_x64/my-portable-app

# 5. Distribua (exemplo com GitHub Releases)
gh release create v1.0.0 \
  dist/my-portable-app-macos_x64/my-portable-app \
  dist/my-portable-app-windows_x64/my-portable-app.exe \
  dist/my-portable-app-linux_x64/my-portable-app
```


## 📊 Comparação de Abordagens

| Aspecto | Neutralino CLI | Docker |
| :-- | :-- | :-- |
| **Velocidade** | ⚡ Mais rápido | 🐢 Mais lento (overhead) |
| **Dependências** | Precisa das ferramentas | Tudo no container |
| **Espaço em disco** | ~500MB | ~2-3GB (imagem) |
| **Facilidade** | ✅ Mais simples | ❌ Mais complexo |
| **Reprodutibilidade** | ⚠️ Depende do Mac | ✅ Garantida |

**Recomendação:** Use o Neutralino CLI direto no Mac (Opção 1) para desenvolvimento. Use Docker apenas se precisar de builds garantidamente idênticas em CI/CD.

## 🔐 Assinatura de Código (Opcional)

Se for distribuir para produção, considere assinar os binários:

### macOS

```bash
codesign -s - dist/my-portable-app-macos_x64/my-portable-app
```


### Windows (do Mac, você não consegue assinar nativamente)

Você precisará de uma máquina Windows ou usar um serviço de CI/CD como GitHub Actions.

## 💡 Dica Pro: GitHub Actions para Builds Automáticas

```yaml
# .github/workflows/build.yml
name: Build Multi-Platform

on:
  push:
    tags:
      - 'v*'

jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [macos-latest, ubuntu-latest, windows-latest]
        include:
          - os: macos-latest
            target: macos-x64
          - os: ubuntu-latest
            target: linux-x64
          - os: windows-latest
            target: windows-x64

    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '20'

      - run: npm install
      - run: npm run compile
      - run: npm run build:${{ matrix.target }}

      - uses: softprops/action-gh-release@v1
        with:
          files: dist/**/*
```

Assim você constrói para todas as plataformas automaticamente!

## ✨ Resumo

**TL;DR:**

```bash
# No seu Mac, simplesmente rode:
npm install -g @neutralinojs/neu
npm install
npm run compile
neu build --release  # Compila para Mac, Windows e Linux

# Pronto! Os binários estarão em ./dist/
```

É literalmente isso! 🎉 Você consegue fazer tudo desde seu Mac sem precisar de uma máquina Windows ou Linux.

Tem mais alguma dúvida sobre a compilação cruzada?

---

# Construindo uma Aplicação Multiplataforma com Neutralino, React e TypeScript - Guia Completo

Olá! Neste post vamos criar uma aplicação **portable, multiplataforma e dual-mode** usando **Neutralino** como base. A ideia é poderosa: um único executável que funciona tanto como **GUI desktop (Windows, macOS, Linux)** quanto como **CLI headless (perfeito para cron jobs)**.

Tudo isso com **zero dependências externas**, 100% TypeScript, e compilável de qualquer lugar - inclusive direto do seu Mac para todas as plataformas.

***

## 🎯 O Conceito Geral

Imagine você tendo:

- Um `app.exe` / `app-macos` / `app-linux` que pode ser executado na máquina local e abre uma interface React bonita com logs e botões
- O **mesmo executável** copiado para um servidor Linux, rodando via cron com parâmetro `--run` para execução headless
- Sem instalar Node.js, sem dependências, sem configurações - basta copiar e executar
- Código compartilhado entre os dois modos (DRY - Don't Repeat Yourself)

Vamos construir isso passo a passo!

***

## 📋 Arquitetura da Solução

```
my-portable-app/
├── src/
│   ├── cli/
│   │   └── index.ts                 # Lógica CLI (--run flag)
│   ├── desktop/
│   │   ├── App.tsx                  # Componente React principal
│   │   └── main.ts                  # Entry point desktop
│   ├── shared/
│   │   └── utils.ts                 # Funções compartilhadas
│   └── index.ts                     # Router: detecta ambiente
├── resources/
│   ├── css/
│   │   └── style.css
│   ├── html/
│   │   └── index.html
│   ├── js/
│   │   └── neutralino.js            # API do Neutralino
│   └── icons/
│       └── icon-256x256.png
├── dist/                            # Gerado após build
├── neutralino.conf.json             # Configuração Neutralino
├── package.json
├── tsconfig.json
└── README.md
```


***

## 🚀 Setup Inicial Passo-a-Passo

### 1. Instale as Ferramentas Necessárias

```bash
# Certifique-se que tem Node.js 18+
node --version
npm --version

# Instale o CLI do Neutralino globalmente
npm install -g @neutralinojs/neu

# Verifique a instalação
neu --version
```


### 2. Crie um Novo Projeto Neutralino

```bash
# Crie o projeto
neu create my-portable-app

# Entre no diretório
cd my-portable-app

# Instale as dependências npm
npm install

# Instale dependências TypeScript e React
npm install --save-dev typescript tsx @types/node
npm install --save-dev @types/react @types/react-dom
npm install react react-dom
```


### 3. Configure o TypeScript

Crie um arquivo `tsconfig.json` na raiz do projeto:

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "jsx": "react-jsx",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "outDir": "./resources/js",
    "rootDir": "./src",
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```


### 4. Configure o Neutralino

Atualize o arquivo `neutralino.conf.json`:

```json
{
  "documentRoot": "/resources/",
  "url": "/index.html",
  "documentRoot": "/resources/",
  "url": "/index.html",
  "logging": {
    "enabled": true,
    "writeToLogFile": false
  },
  "nativeBlockList": [],
  "tokenLength": 256,
  "documentRoot": "/resources/",
  "url": "/index.html",
  "enableServer": true,
  "enableNativeAPI": true,
  "enableExtensions": false,
  "cli": {
    "resourcesPath": "/resources/",
    "extensionsPath": "/extensions/",
    "url": "/index.html",
    "documentRoot": "/resources/",
    "binaryName": "my-portable-app"
  },
  "modes": {
    "window": {
      "title": "My Portable App",
      "width": 800,
      "height": 600,
      "minWidth": 400,
      "minHeight": 300,
      "icon": "/resources/icons/icon-256x256.png"
    }
  }
}
```


***

## 💻 Implementação Completa do Código

### Arquivo 1: `src/shared/utils.ts`

Funções compartilhadas entre CLI e GUI - este é o coração da aplicação:

```typescript
/**
 * Utilitários compartilhados entre CLI e GUI
 * Contém toda a lógica de negócio
 */

export interface AppConfig {
  mode: 'cli' | 'gui';
  verbose: boolean;
  taskName?: string;
}

export interface TaskResult {
  success: boolean;
  message: string;
  duration: number;
  timestamp: string;
}

/**
 * Retorna a mensagem Hello World
 * Função simples que será usada em ambos os modos
 */
export function getHelloWorld(): string {
  return 'Hello World';
}

/**
 * Simula uma operação assíncrona
 * Pode ser substituída por chamadas reais de API, banco de dados, etc.
 */
export async function executeTask(taskName: string): Promise<TaskResult> {
  const startTime = Date.now();
  const timestamp = new Date().toISOString();

  try {
    console.log(`[${timestamp}] Iniciando tarefa: ${taskName}`);

    // Simule processamento
    await new Promise(resolve => setTimeout(resolve, 500));

    console.log(`[${timestamp}] Processando...`);

    // Simule mais processamento
    await new Promise(resolve => setTimeout(resolve, 500));

    const duration = Date.now() - startTime;

    return {
      success: true,
      message: `Tarefa "${taskName}" completada com sucesso!`,
      duration,
      timestamp,
    };
  } catch (error) {
    const duration = Date.now() - startTime;
    return {
      success: false,
      message: `Erro na tarefa "${taskName}": ${error}`,
      duration,
      timestamp,
    };
  }
}

/**
 * Parse dos argumentos da linha de comando
 * Retorna modo (CLI ou GUI) e flags adicionais
 */
export function parseArguments(args: string[]): {
  mode: 'cli' | 'gui';
  flags: Record<string, string | boolean>;
} {
  const flags: Record<string, string | boolean> = {};
  let mode: 'cli' | 'gui' = 'gui';

  for (let i = 0; i < args.length; i++) {
    const arg = args[i];

    if (arg === '--run') {
      mode = 'cli';
      flags.run = true;
    } else if (arg === '--verbose' || arg === '-v') {
      flags.verbose = true;
    } else if (arg === '--help' || arg === '-h') {
      flags.help = true;
    } else if (arg.startsWith('--')) {
      const [key, value] = arg.substring(2).split('=');
      flags[key] = value || true;
    }
  }

  return { mode, flags };
}

/**
 * Exibe mensagem de ajuda
 */
export function showHelp(): void {
  const help = `
╔══════════════════════════════════════════════════════════╗
║                  My Portable App - Help                  ║
╚══════════════════════════════════════════════════════════╝

SINTAXE:
  my-portable-app [OPÇÕES]

OPÇÕES:
  --run              Modo CLI (headless)
  -v, --verbose      Modo verbose (mais detalhes)
  --help, -h         Mostra esta mensagem
  --task=NOME        Executa uma tarefa específica

EXEMPLOS:
  # Abre a GUI
  ./my-portable-app

  # Executa em modo CLI
  ./my-portable-app --run

  # Modo CLI com saída verbose
  ./my-portable-app --run --verbose

  # Executa tarefa específica
  ./my-portable-app --run --task=backup

DOCUMENTAÇÃO:
  Para mais informações, visite: https://seu-repo.com

`;
  console.log(help);
}

/**
 * Formata número de milissegundos para formato legível
 */
export function formatDuration(ms: number): string {
  if (ms < 1000) return `${ms}ms`;
  if (ms < 60000) return `${(ms / 1000).toFixed(2)}s`;
  return `${(ms / 60000).toFixed(2)}m`;
}
```


### Arquivo 2: `src/cli/index.ts`

Modo CLI - execução headless perfeita para cron jobs:

```typescript
/**
 * Modo CLI - Execução headless
 * Ideal para cron jobs, webhooks e automação no servidor
 */

import { executeTask, getHelloWorld, formatDuration } from '../shared/utils';

interface CLIOptions {
  verbose: boolean;
  taskName?: string;
}

/**
 * Função principal do modo CLI
 */
export async function runCLI(options: CLIOptions): Promise<void> {
  const startTime = Date.now();

  try {
    if (options.verbose) {
      console.log('╔════════════════════════════════════╗');
      console.log('║   My Portable App - CLI Mode       ║');
      console.log('║   Inicializado com sucesso         ║');
      console.log('╚════════════════════════════════════╝');
      console.log('');
    }

    // Exiba a mensagem Hello World
    const helloMessage = getHelloWorld();
    console.log(`✓ ${helloMessage}`);

    if (options.verbose) {
      console.log('');
      console.log('▶ Iniciando execução de tarefas...');
      console.log('');
    }

    // Execute a(s) tarefa(s)
    const taskName = options.taskName || 'default-task';
    const result = await executeTask(taskName);

    if (options.verbose) {
      console.log(`  Status: ${result.success ? '✓ SUCESSO' : '✗ ERRO'}`);
      console.log(`  Mensagem: ${result.message}`);
      console.log(`  Duração: ${formatDuration(result.duration)}`);
      console.log(`  Timestamp: ${result.timestamp}`);
    }

    if (!result.success) {
      throw new Error(result.message);
    }

    const totalDuration = Date.now() - startTime;

    if (options.verbose) {
      console.log('');
      console.log('━'.repeat(36));
      console.log(`✓ Execução concluída em ${formatDuration(totalDuration)}`);
      console.log('━'.repeat(36));
      console.log('');
    } else {
      console.log(`OK (${formatDuration(totalDuration)})`);
    }

    // Retorne status de sucesso
    process.exit(0);
  } catch (error) {
    if (options.verbose) {
      console.error('');
      console.error('╔════════════════════════════════════╗');
      console.error('║          ERRO CRÍTICO              ║');
      console.error('╚════════════════════════════════════╝');
      console.error('');
      console.error(`✗ ${error}`);
      console.error('');
      const totalDuration = Date.now() - startTime;
      console.error(`Duração até erro: ${formatDuration(totalDuration)}`);
      console.error('');
    } else {
      console.error(`ERROR: ${error}`);
    }
    process.exit(1);
  }
}

/**
 * Wrapper para fácil execução
 */
export async function initializeCLI(args: string[]): Promise<void> {
  const verbose = args.includes('--verbose') || args.includes('-v');
  const taskMatch = args.find(arg => arg.startsWith('--task='));
  const taskName = taskMatch ? taskMatch.split('=')[1] : undefined;

  await runCLI({ verbose, taskName });
}
```


### Arquivo 3: `src/desktop/main.ts`

Entry point para o modo desktop:

```typescript
/**
 * Entry point para modo Desktop
 * Renderiza a aplicação React quando a janela Neutralino abre
 */

import React from 'react';
import { createRoot } from 'react-dom/client';
import { App } from './App';

/**
 * Inicializa a aplicação React
 */
export function initializeDesktopApp(): void {
  const rootElement = document.getElementById('root');

  if (!rootElement) {
    console.error('✗ Elemento #root não encontrado no HTML!');
    console.error('Certifique-se que o arquivo index.html contém: <div id="root"></div>');
    return;
  }

  try {
    const root = createRoot(rootElement);
    root.render(React.createElement(App));
    console.log('✓ Aplicação React renderizada com sucesso');
  } catch (error) {
    console.error('✗ Erro ao renderizar aplicação React:', error);
    rootElement.innerHTML = `
      <div style="
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
        background: #f3f4f6;
        font-family: system-ui, sans-serif;
      ">
        <div style="text-align: center;">
          <h1>❌ Erro ao Inicializar</h1>
          <p>Não foi possível renderizar a aplicação.</p>
          <pre style="
            background: #f1f5f9;
            padding: 1rem;
            border-radius: 0.5rem;
            text-align: left;
          ">${error}</pre>
        </div>
      </div>
    `;
  }
}

/**
 * Se o DOM estiver carregando, aguarde
 * Caso contrário, inicialize imediatamente
 */
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeDesktopApp);
} else {
  initializeDesktopApp();
}
```


### Arquivo 4: `src/desktop/App.tsx`

Componente React principal com interface moderna:

```typescript
/**
 * Componente React principal da aplicação Desktop
 * Interface moderna com logs em tempo real e botões de ação
 */

import React, { useEffect, useState } from 'react';
import { getHelloWorld, executeTask, formatDuration } from '../shared/utils';

/**
 * Interface para entrada de log
 */
interface LogEntry {
  id: string;
  timestamp: string;
  message: string;
  type: 'info' | 'success' | 'error' | 'warning';
}

/**
 * Componente principal
 */
export function App(): JSX.Element {
  const [logs, setLogs] = useState<LogEntry[]>([]);
  const [loading, setLoading] = useState(false);
  const [executionTime, setExecutionTime] = useState(0);

  /**
   * Adiciona entrada de log
   */
  const addLog = (
    message: string,
    type: 'info' | 'success' | 'error' | 'warning' = 'info'
  ): void => {
    const timestamp = new Date().toLocaleTimeString('pt-BR');
    const id = `${Date.now()}-${Math.random()}`;

    setLogs(prev => [...prev, { id, timestamp, message, type }]);

    // Auto-scroll para o final
    setTimeout(() => {
      const consoleElement = document.getElementById('console-output');
      if (consoleElement) {
        consoleElement.scrollTop = consoleElement.scrollHeight;
      }
    }, 0);
  };

  /**
   * Limpa o console
   */
  const clearLogs = (): void => {
    setLogs([]);
    setExecutionTime(0);
  };

  /**
   * Carrega mensagem inicial
   */
  useEffect(() => {
    addLog(getHelloWorld(), 'success');
    addLog('Aplicação inicializada', 'info');
  }, []);

  /**
   * Handler para executar tarefa
   */
  const handleExecuteTask = async (): Promise<void> => {
    setLoading(true);
    const startTime = Date.now();
    addLog('▶ Iniciando tarefa...', 'info');

    try {
      const result = await executeTask('gui-task');

      if (result.success) {
        addLog(`✓ ${result.message}`, 'success');
        addLog(`⏱ Duração: ${formatDuration(result.duration)}`, 'info');
      } else {
        addLog(`✗ ${result.message}`, 'error');
      }

      setExecutionTime(Date.now() - startTime);
    } catch (error) {
      addLog(`✗ Erro: ${error}`, 'error');
      setExecutionTime(Date.now() - startTime);
    } finally {
      setLoading(false);
    }
  };

  /**
   * Handler para exportar logs
   */
  const handleExportLogs = (): void => {
    const logsText = logs
      .map(log => `[${log.timestamp}] ${log.message}`)
      .join('\n');

    const element = document.createElement('a');
    element.setAttribute('href', `data:text/plain;charset=utf-8,${encodeURIComponent(logsText)}`);
    element.setAttribute('download', `app-logs-${Date.now()}.txt`);
    element.style.display = 'none';

    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);

    addLog('✓ Logs exportados com sucesso', 'success');
  };

  /**
   * Renderizar
   */
  return (
    <div style={styles.container}>
      {/* Header */}
      <header style={styles.header}>
        <div style={styles.headerContent}>
          <div>
            <h1 style={styles.title}>📦 My Portable App</h1>
            <p style={styles.subtitle}>GUI + CLI Multiplataforma | TypeScript + React + Neutralino</p>
          </div>
          <div style={styles.badge}>v1.0.0</div>
        </div>
      </header>

      {/* Main Content */}
      <main style={styles.main}>
        {/* Console Section */}
        <section style={styles.section}>
          <div style={styles.sectionHeader}>
            <h2>📋 Console de Execução</h2>
            <div style={styles.sectionControls}>
              <button onClick={clearLogs} style={{ ...styles.buttonSmall, backgroundColor: '#ef4444' }}>
                🗑️ Limpar
              </button>
            </div>
          </div>

          <div id="console-output" style={styles.console}>
            {logs.length === 0 ? (
              <div style={styles.emptyState}>
                <p>Nenhum log ainda. Clique em "Executar Tarefa" para começar.</p>
              </div>
            ) : (
              logs.map(log => (
                <div
                  key={log.id}
                  style={{
                    ...styles.logEntry,
                    borderLeftColor: getColorForType(log.type),
                    backgroundColor: getBackgroundForType(log.type),
                  }}
                >
                  <span style={styles.timestamp}>[{log.timestamp}]</span>
                  <span style={{ color: getTextColorForType(log.type) }}>{log.message}</span>
                </div>
              ))
            )}
          </div>

          {executionTime > 0 && (
            <div style={styles.executionInfo}>
              ⏱ Última execução: {formatDuration(executionTime)}
            </div>
          )}
        </section>

        {/* Actions Section */}
        <section style={styles.section}>
          <div style={styles.sectionHeader}>
            <h2>⚙️ Ações</h2>
          </div>

          <div style={styles.buttonGroup}>
            <button
              onClick={handleExecuteTask}
              disabled={loading}
              style={{
                ...styles.button,
                ...styles.buttonPrimary,
                opacity: loading ? 0.6 : 1,
                cursor: loading ? 'not-allowed' : 'pointer',
              }}
            >
              {loading ? '⏳ Executando...' : '▶ Executar Tarefa'}
            </button>

            <button
              onClick={handleExportLogs}
              disabled={logs.length === 0}
              style={{
                ...styles.button,
                backgroundColor: '#10b981',
                opacity: logs.length === 0 ? 0.5 : 1,
                cursor: logs.length === 0 ? 'not-allowed' : 'pointer',
              }}
            >
              📥 Exportar Logs
            </button>
          </div>
        </section>

        {/* Info Section */}
        <section style={styles.section}>
          <h2>ℹ️ Informações</h2>
          <div style={styles.infoGrid}>
            <div style={styles.infoCard}>
              <h3>Modo GUI</h3>
              <p>Esta é a versão desktop da aplicação com interface React.</p>
            </div>
            <div style={styles.infoCard}>
              <h3>Modo CLI</h3>
              <p>Execute com --run para modo headless (ideal para cron jobs).</p>
            </div>
            <div style={styles.infoCard}>
              <h3>Multiplataforma</h3>
              <p>Rode no Windows, macOS e Linux com o mesmo executável.</p>
            </div>
            <div style={styles.infoCard}>
              <h3>100% Portable</h3>
              <p>Nenhuma dependência externa. Basta copiar e executar.</p>
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer style={styles.footer}>
        <p>
          💻 TypeScript + React + Neutralino | 🌐 Multiplataforma | 🚀 Portable | 📦 Zero Dependências
        </p>
        <p style={{ marginTop: '0.5rem', fontSize: '0.875rem' }}>
          Construído com ❤️ para Windows, macOS e Linux
        </p>
      </footer>
    </div>
  );
}

/**
 * Funções auxiliares para cores
 */
function getColorForType(type: LogEntry['type']): string {
  const colors: Record<LogEntry['type'], string> = {
    success: '#10b981',
    error: '#ef4444',
    warning: '#f59e0b',
    info: '#3b82f6',
  };
  return colors[type];
}

function getBackgroundForType(type: LogEntry['type']): string {
  const backgrounds: Record<LogEntry['type'], string> = {
    success: 'rgba(16, 185, 129, 0.1)',
    error: 'rgba(239, 68, 68, 0.1)',
    warning: 'rgba(245, 158, 11, 0.1)',
    info: 'rgba(59, 130, 246, 0.1)',
  };
  return backgrounds[type];
}

function getTextColorForType(type: LogEntry['type']): string {
  const colors: Record<LogEntry['type'], string> = {
    success: '#065f46',
    error: '#7f1d1d',
    warning: '#92400e',
    info: '#1e3a8a',
  };
  return colors[type];
}

/**
 * Estilos
 */
const styles: Record<string, React.CSSProperties> = {
  container: {
    minHeight: '100vh',
    backgroundColor: '#f3f4f6',
    display: 'flex',
    flexDirection: 'column',
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif',
  },
  header: {
    backgroundColor: '#1f2937',
    color: 'white',
    padding: '2rem',
    borderBottom: '4px solid #3b82f6',
  },
  headerContent: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    maxWidth: '1000px',
    margin: '0 auto',
    width: '100%',
  },
  title: {
    margin: '0 0 0.5rem 0',
    fontSize: '2rem',
    fontWeight: 'bold',
  },
  subtitle: {
    margin: 0,
    fontSize: '0.875rem',
    opacity: 0.9,
  },
  badge: {
    backgroundColor: '#3b82f6',
    padding: '0.5rem 1rem',
    borderRadius: '0.375rem',
    fontSize: '0.875rem',
    fontWeight: '600',
  },
  main: {
    flex: 1,
    padding: '2rem',
    maxWidth: '1000px',
    margin: '0 auto',
    width: '100%',
  },
  section: {
    backgroundColor: 'white',
    borderRadius: '0.5rem',
    padding: '1.5rem',
    marginBottom: '1.5rem',
    boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)',
  },
  sectionHeader: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: '1rem',
  },
  sectionControls: {
    display: 'flex',
    gap: '0.5rem',
  },
  console: {
    backgroundColor: '#111827',
    color: '#ecf0f1',
    padding: '1rem',
    borderRadius: '0.375rem',
    fontFamily: 'Courier New, monospace',
    fontSize: '0.875rem',
    maxHeight: '400px',
    overflowY: 'auto' as const,
    marginBottom: '1rem',
    border: '1px solid #374151',
  },
  emptyState: {
    textAlign: 'center' as const,
    color: '#9ca3af',
    padding: '2rem',
    fontSize: '0.875rem',
  },
  logEntry: {
    padding: '0.5rem',
    marginBottom: '0.25rem',
    borderRadius: '0.25rem',
    borderLeft: '4px solid #3b82f6',
    display: 'flex',
    gap: '0.5rem',
  },
  timestamp: {
    color: '#9ca3af',
    fontWeight: 'bold',
    whiteSpace: 'nowrap' as const,
    minWidth: '80px',
  },
  executionInfo: {
    backgroundColor: '#f0fdf4',
    color: '#166534',
    padding: '0.75rem',
    borderRadius: '0.375rem',
    fontSize: '0.875rem',
    borderLeft: '4px solid #10b981',
  },
  buttonGroup: {
    display: 'flex',
    gap: '0.75rem',
    flexWrap: 'wrap' as const,
  },
  button: {
    border: 'none',
    padding: '0.75rem 1.5rem',
    borderRadius: '0.375rem',
    fontSize: '1rem',
    fontWeight: '600',
    cursor: 'pointer',
    boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)',
    transition: 'all 0.2s ease-in-out',
  },
  buttonPrimary: {
    backgroundColor: '#3b82f6',
    color: 'white',
  },
  buttonSmall: {
    padding: '0.5rem 1rem',
    fontSize: '0.875rem',
    borderRadius: '0.375rem',
    color: 'white',
    cursor: 'pointer',
    border: 'none',
    fontWeight: '600',
  },
  infoGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
    gap: '1rem',
  },
  infoCard: {
    backgroundColor: '#f9fafb',
    padding: '1rem',
    borderRadius: '0.375rem',
    border: '1px solid #e5e7eb',
  },
  footer: {
    backgroundColor: '#f9fafb',
    borderTop: '1px solid #e5e7eb',
    padding: '1.5rem',
    textAlign: 'center' as const,
    color: '#6b7280',
    fontSize: '0.875rem',
  },
};
```


### Arquivo 5: `src/index.ts`

Router principal - detecta ambiente e roteia para modo certo:

```typescript
/**
 * Ponto de entrada principal da aplicação
 * Detecta se está em modo CLI ou Desktop e roteia adequadamente
 */

import { parseArguments, showHelp } from './shared/utils';

/**
 * Função principal - Router
 */
async function main(): Promise<void> {
  try {
    // Detecte o ambiente
    const isNodeJS = typeof process !== 'undefined' && process.versions && process.versions.node;
    const isWeb = typeof window !== 'undefined' && typeof document !== 'undefined';

    // Se for Node.js, modo CLI
    if (isNodeJS && !isWeb) {
      const args = process.argv.slice(2);
      const { mode, flags } = parseArguments(args);

      // Verifique flags de ajuda
      if (flags.help) {
        showHelp();
        process.exit(0);
      }

      // Se modo CLI
      if (mode === 'cli') {
        const { initializeCLI } = await import('./cli');
        await initializeCLI(args);
        return;
      }
    }

    // Caso contrário, modo Desktop (GUI)
    if (isWeb) {
      const { initializeDesktopApp } = await import('./desktop/main');
      initializeDesktopApp();
      return;
    }

    console.error('✗ Ambiente desconhecido - não é Node.js nem navegador');
    process.exit(1);
  } catch (error) {
    console.error('✗ Erro crítico na inicialização:', error);
    process.exit(1);
  }
}

// Execute quando o script carregar
main();
```


### Arquivo 6: `resources/index.html`

HTML principal da aplicação:

```html
<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My Portable App</title>
    <style>
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }

      html,
      body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        width: 100%;
        height: 100%;
        background: #f3f4f6;
      }

      #root {
        width: 100%;
        min-height: 100vh;
      }

      /* Scrollbar styling */
      ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
      }

      ::-webkit-scrollbar-track {
        background: #f1f5f9;
      }

      ::-webkit-scrollbar-thumb {
        background: #cbd5e1;
        border-radius: 4px;
      }

      ::-webkit-scrollbar-thumb:hover {
        background: #94a3b8;
      }

      /* Suavizar animações */
      * {
        transition: background-color 0.2s ease-in-out;
      }
    </style>
  </head>
  <body>
    <div id="root">
      <div style="
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
        background: #f3f4f6;
        font-family: system-ui, sans-serif;
      ">
        <div style="text-align: center;">
          <p style="font-size: 1.5rem; color: #6b7280;">⏳ Carregando...</p>
        </div>
      </div>
    </div>

    <!-- API do Neutralino (fornecida pelo Neutralino) -->
    <script src="js/neutralino.js" defer></script>

    <!-- Aplicação compilada TypeScript -->
    <script type="module" src="js/index.js" defer></script>
  </body>
</html>
```


***

## 📦 Configuração do Build e Desenvolvimento

### Arquivo: `package.json`

```json
{
  "name": "my-portable-app",
  "version": "1.0.0",
  "description": "Aplicação multiplataforma GUI + CLI com Neutralino, React e TypeScript",
  "author": "Seu Nome",
  "license": "MIT",
  "main": "src/index.ts",
  "scripts": {
    "dev": "npm run compile:watch & neu run",
    "dev:cli": "tsx src/index.ts --run --verbose",
    "dev:gui": "neu run",
    "compile": "tsc",
    "compile:watch": "tsc --watch",
    "build": "npm run compile && neu build",
    "build:all": "npm run compile && neu build --release",
    "build:mac": "npm run compile && neu build --release macos-x64",
    "build:windows": "npm run compile && neu build --release windows-x64",
    "build:linux": "npm run compile && neu build --release linux-x64",
    "cli": "tsx src/index.ts --run",
    "cli:verbose": "tsx src/index.ts --run --verbose",
    "gui": "neu run",
    "clean": "rm -rf dist resources/js dist-built",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@neutralinojs/neu": "^latest",
    "@types/node": "^20.0.0",
    "@types/react": "^18.2.0",
    "@types/react-dom": "^18.2.0",
    "tsx": "^4.0.0",
    "typescript": "^5.2.0"
  },
  "keywords": [
    "neutralino",
    "react",
    "typescript",
    "portable",
    "cross-platform",
    "gui",
    "cli",
    "electron-alternative"
  ]
}
```


***

## 🚀 Workflow Completo: Desenvolvimento e Build

### 1. Setup Inicial

```bash
# Clone/crie o projeto
neu create my-portable-app
cd my-portable-app

# Instale dependências
npm install
npm install --save-dev typescript tsx @types/node @types/react @types/react-dom
npm install react react-dom

# Copie os arquivos do código acima para seus respectivos locais
# src/shared/utils.ts
# src/cli/index.ts
# src/desktop/main.ts
# src/desktop/App.tsx
# src/index.ts
# resources/index.html

# Atualize package.json e tsconfig.json conforme mostrado
```


### 2. Desenvolvimento Local

#### Modo Desktop (GUI)

```bash
# Compile TypeScript e rode o Neutralino
npm run dev

# OU apenas GUI
npm run dev:gui
```

Isso abre uma janela com a interface React. Você pode fazer edições no código TypeScript e o navegador recarrega automaticamente.

#### Modo CLI (Headless)

```bash
# Teste o modo CLI com saída verbose
npm run dev:cli

# OU simplesmente
npm run cli:verbose
```

Isso simula a execução sem interface gráfica - perfeito para testar a versão de servidor.

### 3. Build para Produção (Multiplataforma)

No Mac, compile para TODAS as plataformas:

```bash
# Compile TypeScript
npm run compile

# Build para TODAS as plataformas
npm run build:all

# Ou builds individuais
npm run build:mac
npm run build:windows
npm run build:linux
```

Os executáveis aparecerão em `dist/`:

```
dist/
├── my-portable-app-macos_x64/
│   └── My Portable App.app
├── my-portable-app-windows_x64/
│   └── my-portable-app.exe
└── my-portable-app-linux_x64/
    └── my-portable-app
```


***

## 🖥️ Como Usar a Aplicação

### Modo GUI (Desktop)

```bash
# Windows
.\dist\my-portable-app-windows_x64\my-portable-app.exe

# macOS
./dist/my-portable-app-macos_x64/My\ Portable\ App.app/Contents/MacOS/My\ Portable\ App

# Linux
./dist/my-portable-app-linux_x64/my-portable-app
```

Uma janela se abre com a interface React. Você verá:

- Console de execução mostrando "Hello World"
- Botão para executar tarefas
- Botão para exportar logs
- Informações sobre a aplicação


### Modo CLI (Headless)

```bash
# Execução simples
./my-portable-app --run

# Execução com detalhes
./my-portable-app --run --verbose

# Mostra ajuda
./my-portable-app --help
```

Output:

```
Hello World
✓ Tarefa "default-task" completada com sucesso!
OK (1002ms)
```


***

## 🐧 Deployment no Linux com Cron

### 1. Copie o executável para o servidor

```bash
# Do seu Mac
scp dist/my-portable-app-linux_x64/my-portable-app user@server:/opt/apps/

# No servidor
chmod +x /opt/apps/my-portable-app
```


### 2. Configure o Cron Job

```bash
# Edite o crontab
crontab -e

# Exemplos de configuração

# Executar diariamente às 2 da manhã
0 2 * * * /opt/apps/my-portable-app --run >> /var/log/my-app.log 2>&1

# Executar a cada 30 minutos com detalhes
*/30 * * * * /opt/apps/my-portable-app --run --verbose >> /var/log/my-app-verbose.log 2>&1

# Executar a cada 1 hora, com notificação por email
0 * * * * /opt/apps/my-portable-app --run || echo "App failed" | mail -s "Alert" admin@example.com

# Executar em múltiplos horários (2h, 14h, 22h)
0 2,14,22 * * * /opt/apps/my-portable-app --run >> /var/log/my-app.log 2>&1
```


### 3. Monitore a execução

```bash
# Veja os logs
tail -f /var/log/my-app.log

# Veja os logs verbose
tail -f /var/log/my-app-verbose.log

# Veja a lista de cron jobs
crontab -l

# Teste a execução manual
/opt/apps/my-portable-app --run --verbose
```


***

## 🐳 Build com Docker (Opcional - Para CI/CD)

Se quiser builds reproduzíveis em CI/CD, use Docker:

```dockerfile
# Dockerfile
FROM node:20-alpine

# Instale dependências
RUN apk add --no-cache curl bash git

# Instale Neutralino CLI
RUN npm install -g @neutralinojs/neu

WORKDIR /app

# Copie projeto
COPY . .

# Instale dependências do projeto
RUN npm install

# Compile e build
RUN npm run build:all

# Output dos binários compilados
CMD ["ls", "-la", "dist/"]
```

Build e execute:

```bash
docker build -t my-portable-app-builder .
docker run -v $(pwd)/dist:/app/dist my-portable-app-builder
```


***

## 🔧 GitHub Actions para Builds Automáticas

Configure CI/CD automático:

```yaml
# .github/workflows/build.yml
name: Build Multi-Platform

on:
  push:
    tags:
      - 'v*'

jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [macos-latest, ubuntu-latest, windows-latest]
        include:
          - os: macos-latest
            target: macos-x64
          - os: ubuntu-latest
            target: linux-x64
          - os: windows-latest
            target: windows-x64

    steps:
      - uses: actions/checkout@v3

      - uses: actions/setup-node@v3
        with:
          node-version: '20'

      - run: npm install
      - run: npm run compile
      - run: npm run build:${{ matrix.target }}

      - uses: softprops/action-gh-release@v1
        with:
          files: dist/**/*
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

Quando você fazer push de uma tag `v1.0.0`, isso automaticamente compila e publica os binários!

```bash
# Crie a tag e push
git tag v1.0.0
git push origin v1.0.0

# GitHub Actions faz o resto!
```


***

## 📊 Estrutura de Diretórios Completa

```
my-portable-app/
│
├── src/                                 # Código fonte TypeScript
│   ├── index.ts                         # Entry point (router)
│   ├── cli/
│   │   └── index.ts                     # Modo CLI
│   ├── desktop/
│   │   ├── main.ts                      # Entry point GUI
│   │   └── App.tsx                      # Componente React
│   └── shared/
│       └── utils.ts                     # Funções compartilhadas
│
├── resources/                           # Arquivos estáticos
│   ├── index.html                       # HTML principal
│   ├── css/
│   │   └── style.css                    # Estilos (opcional)
│   ├── js/
│   │   ├── neutralino.js                # API Neutralino (auto-gerado)
│   │   └── index.js                     # Compilado (gerado pelo tsc)
│   └── icons/
│       └── icon-256x256.png             # Ícone da app
│
├── dist/                                # Binários compilados (após build)
│   ├── my-portable-app-linux_x64/
│   ├── my-portable-app-windows_x64/
│   └── my-portable-app-macos_x64/
│
├── .github/
│   └── workflows/
│       └── build.yml                    # CI/CD (opcional)
│
├── package.json                         # Dependências npm
├── tsconfig.json                        # Configuração TypeScript
├── neutralino.conf.json                 # Configuração Neutralino
└── README.md                            # Documentação
```


***

## ✨ Características e Vantagens

### ✅ Multiplataforma

- **Windows, macOS, Linux** com um único código
- Compile para todas as plataformas do seu Mac


### ✅ Dual-Mode

- **GUI moderna** com React e TypeScript
- **CLI headless** para automação e servidores
- Código compartilhado entre os dois modos


### ✅ 100% Portable

- Sem dependências externas
- Sem instalação de Node.js necessária
- Basta copiar e executar


### ✅ Type-Safe

- TypeScript em toda a aplicação
- Autossuggestão e detecção de erros em tempo de desenvolvimento


### ✅ Leve

- Binário final: ~80-120MB (não comprimido)
- ~20-40MB quando zipado


### ✅ Zero Config

- Nenhuma configuração complexa necessária
- Funciona out-of-the-box


### ✅ Cron Ready

- Perfeito para jobs agendados no Linux
- Baixa latência e overhead mínimo

***

## 🎓 Próximos Passos e Extensões

Aqui estão ideias para expandir a aplicação:

### 1. Adicionar Banco de Dados Local

```typescript
// Usar SQLite para armazenamento local
import Database from 'better-sqlite3';

const db = new Database('app.db');
```


### 2. Sincronizar Dados Entre GUI e CLI

```typescript
// Salvar estado em arquivo JSON
const state = {
  lastExecution: new Date(),
  taskResults: [...],
};

fs.writeFileSync('state.json', JSON.stringify(state));
```


### 3. API REST Local

```typescript
// Localhost:5000 para integração
const app = express();
app.get('/api/status', (req, res) => {
  res.json({ status: 'ok' });
});
```


### 4. Auto-Update

```typescript
// Neutralino suporta auto-update
Neutralino.updater.checkForUpdates();
```


### 5. Logging Persistente

```typescript
// Winston para logging profissional
const logger = winston.createLogger({
  transports: [
    new winston.transports.File({ filename: 'app.log' })
  ]
});
```


### 6. Notificações do Sistema

```typescript
// Notificações nativas
Neutralino.notification.create({
  summary: "Tarefa concluída",
  body: "Sua tarefa foi executada com sucesso!"
});
```


***

## 🐛 Troubleshooting

### Problema: "Elemento \#root não encontrado"

```
**Solução:** Certifique-se que `resources/index.html` contém `<div id="root"></div>`
```


### Problema: TypeScript não compila

**Solução:** Verifique se `tsconfig.json` está correto e rode `npm run compile` manualmente

### Problema: Modo CLI não funciona

**Solução:** Teste com `npm run dev:cli` e verifique se `process.argv` está sendo capturado

### Problema: Executável não funciona no servidor

**Solução:**

```bash
# Verifique permissões
chmod +x /opt/apps/my-portable-app

# Verifique se é executável
file /opt/apps/my-portable-app

# Teste execução direta
/opt/apps/my-portable-app --help
```


### Problema: Cron job não executa

**Solução:**

```bash
# Verifique permissões
ls -la /opt/apps/my-portable-app

# Verifique logs do cron
grep CRON /var/log/syslog

# Redirecione saída para debug
0 2 * * * /opt/apps/my-portable-app --run >> /var/log/app.log 2>&1
```


***

## 📚 Recursos Adicionais

- **Neutralino Docs**: https://neutralino.js.org/
- **React Docs**: https://react.dev/
- **TypeScript Docs**: https://www.typescriptlang.org/
- **Cron Syntax**: https://crontab.guru/

***

## 🎉 Conclusão

Você agora tem uma **arquitetura profissional** para desenvolver e distribuir aplicações multiplataforma com:

1. ✅ Interface moderna em React
2. ✅ CLI poderosa para automação
3. ✅ Type-safety com TypeScript
4. ✅ Portabilidade total
5. ✅ Zero dependências externas
6. ✅ Deploy simples em servidores Linux

Essa abordagem é ideal para:

- 📱 Aplicações desktop leves
- 🤖 Ferramentas de automação
- 📊 Dashboards locais
- 🔧 Utilitários de sistema
- 🌐 Sincronização de dados

