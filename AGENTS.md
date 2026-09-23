# AGENTS.md

Regras para agentes de IA (Claude, zot, copilots, sub-agentes) trabalhando neste repositório.

## Regra fundamental: NÃO INSTALE NADA SEM PERMISSÃO

**É proibido instalar qualquer software, pacote, dependência, gem, biblioteca ou ferramenta na máquina do usuário sem pedir permissão explícita antes.**

Isso vale para qualquer coisa, incluindo (mas não limitado a):

- `gem install` (Ruby/RubyGems)
- `npm install` / `pnpm add` / `yarn add` (Node)
- `pip install` / `pipx` / `poetry add` / `uv add` (Python)
- `brew install` / `brew upgrade` (macOS)
- `cargo install`, `go install`, `apt install`
- Modificadores de ambiente como `--user-install`, `--global`, ou instalações em `~/.gem`, `~/.npm`, `~/.local`, `~/.cargo`, `~/.venv`, etc.
- Docker images, `npx` de pacotes não presentes, download de binários

### Por quê

O ambiente do usuário não é descartável. Instalações:

- poluem diretórios pessoais (`~/.gem`, `~/.npm`, …) e deixam lixo difícil de reverter;
- podem conflitar com versões já existentes e quebrar outros projetos;
- gastam tempo e banda sem autorização;
- são irreversíveis na prática se o agente não registrar exatamente o que instalou.

### O que fazer em vez disso

1. **Verifique antes de instalar.** Confirme se a ferramenta já está disponível (`command -v jekyll`, `gem list`, `node -e`, etc.).
2. **Se faltar, PARE e pergunte.** Explique o que precisa, por quê, o comando exato e onde seria instalado. Espere um "sim".
3. **Prefira alternativas que não instalam nada.** Ex.: validar ordenação lendo o código-fonte de uma dependência no GitHub; usar as ferramentas web; rodar lógica equivalente em `ruby -e`/`python3 -c` com a stdlib.
4. **Se instalar por autorização, registre tudo.** Anote o comando exato e a lista de pacotes/diretórios criados, para permitir limpeza completa depois.

### Se você já instalou algo sem permissão

Avise o usuário imediatamente, liste exatamente o que foi criado (caminhos e timestamps) e ofereça desinstalar.

## Nunca remova software do sistema sem permissão

Simétrico à regra acima: não apague o que você não instalou. Em particular:

- O **Ruby do sistema macOS** (`/usr/bin/ruby`, `/System/Library/Frameworks/Ruby.framework`) é parte do sistema operacional. Nunca remova.
- Remova apenas os diretórios/pacotes cuja criação você pode comprovar (por timestamp e caminho) que foram feitos pela sua própria instalação.

## Pesquisa externa: use o `ketch`

O sistema já tem o **`ketch`** instalado (`/opt/homebrew/bin/ketch`, Homebrew) — um CLI
*stateless* de pesquisa para agentes: busca web, busca de código em OSS, documentação de
bibliotecas e extração de páginas HTML/PDF para markdown. Um binário, sem daemon, sem
servidor. Ele **substitui** `curl | pandoc`, abrir aba de navegador e, na maioria dos casos,
as ferramentas genéricas de busca/fetch.

**Regra de uso:** para qualquer pergunta que precise de fonte viva (notícia, opinião, preço,
versão atual de software, código real em repositórios públicos, documentação de biblioteca),
**tente primeiro o `ketch`** — mesma versão em qualquer sessão, saída limpa em markdown/YAML,
`--json` em todo comando, cache local e códigos de saída documentados. Versão conferida
nesta máquina: **v0.18.1** (MIT, Go, repo `1broseidon/ketch`, manual em `ketch.run`).

**Quando o `ketch` estiver indisponível** (`command -v ketch` falha), retornar exit `4`
(upstream fora do ar) ou exit `5` (falta configuração), **volte aos meios normais**:
`openrouter_web_fetch` / `openrouter_web_search`, `curl`, ou o navegador — e diga no resumo
que houve fallback e por quê. Não insista três vezes na mesma chamada que já falhou.

```bash
command -v ketch                 # confirma que existe antes de contar com ele
ketch version                    # versão, commit e build (não usa config: nunca falha por env)
ketch config                     # JSON com config efetiva e backends ativos — descoberta de capacidades
ketch doctor                     # health check ao vivo de backends, browser e cache (exit 5 = algo quebrado)
ketch search "termo" --limit 5   # busca web; backend padrão `auto` é uma cadeia keyless, funciona sem API key
```

### Comandos que importam

| Comando | Para quê |
|---|---|
| `ketch search "q" --limit 5` | páginas/opiniões/notícias atuais. `--scrape` traz o conteúdo completo de cada resultado |
| `ketch search "q" --multi` | federa backends com rank fusion. Lista explícita **exige** o `=` (`--multi=brave,exa`); `--random` funciona igual e ambos excluem `-b` |
| `ketch scrape <url...>` | página → markdown. Aceita várias URLs, arquivo de URLs, array JSON ou stdin |
| `ketch extract` | HTML já baixado via pipe (`curl -L <url> \| ketch extract`) — não faz fetch nem cache |
| `ketch code "regex ou literal" --lang go` | código real em repositórios públicos, com repo e linha |
| `ketch docs "assunto" --library /org/repo` | documentação versionada de biblioteca (Context7) |
| `ketch crawl <url> --depth 2` | várias páginas de um site de uma vez (dedupe e streaming) |
| `ketch tag show <tag>` | fontes salvas com `--tag` em sessões anteriores |

- **PDFs funcionam** em `ketch scrape` (press releases e relatórios são extraídos para texto).
- **Páginas que só renderizam com JS** caem automaticamente em Chrome headless — mesma saída.
- **Domínio nu engatilha `/llms.txt`**: `ketch scrape https://exemplo.com` pode devolver o
  `llms.txt` do site em vez da home. O campo `title` revela a troca; `--no-llms-txt` desliga.
- `ketch code` é útil para a dica do próprio repo de **validar comportamento lendo o código-fonte
  de uma dependência no GitHub** (mais barato que instalar a gem para testar).

### Disciplina de uso (obrigatória)

1. **Limite todo fetch.** `--max-chars 4000`–`8000` (mais `--trim` para tirar a sintaxe
   markdown) em qualquer página que você não conhece: uma página sem limite pode custar ~25k
   tokens. Pular o limite exige um motivo de uma linha.
2. **Cite toda afirmação.** Síntese sem URL de origem não é entrega — vale em especial para
   os posts do blog, cujo rodapé precisa de fonte (ver a skill `criar-noticia`).
3. **Códigos de saída são fluxo de controle**, não texto para rezar:
   `0` ok · `2` input inválido — inclui nome de backend inexistente (corrija a chamada;
   repetir igual nunca funciona) ·
   `3` nada encontrado (mude a query/seletor) · `4` falha de upstream/rede (rodeie para outro
   backend ou tente **uma** vez mais) · `5` pré-requisito ausente (pare e configure —
   `ketch doctor`) · `6` cancelado/timeout (refaça com escopo menor).
4. **Proponha antes de mutar.** `ketch config set …`, `ketch browser install`, `cache clear`
   e `ketch crawl --background` são **ações de operador** — caem na *Regra fundamental* lá em
   cima: descreva o comando exato e espere um "sim". Nunca mexa num valor já configurado e
   funcionando.
5. **`--json` para parsear, `--minimal` para economizar.** Toda chamada devolve YAML
   frontmatter + conteúdo; `--json` dá objeto estruturado e `--minimal` ~metade do tamanho.
6. **`--tag <slug-do-post>`** em `search`/`scrape`/`code`/`docs` guarda as fontes de um post
   para reuso posterior (`ketch tag show <slug>`), sobrevivendo à expiração do cache.

### Pegadinhas conhecidas

- **Scrape em lote reporta falha por URL dentro de uma chamada bem-sucedida**: o exit é `0`
  com `error` no resultado individual. Confira **cada entrada**, não só o exit code.
- **`ketch docs` resolve nunca volta vazio**: nome errado devolve correspondência difusa
  confiante. Confira se o match corresponde mesmo à biblioteca pedida.
- **Regex é por backend**: `grepapp` e `sourcegraph` aceitam, `github` rejeita.
- **O cache de páginas (bbolt, TTL 72h) é compartilhado**: cada processo abre o arquivo só
  por transação (corrigido na v0.18.1 — antes um `ketch mcp serve` segurava o lock a vida
  toda). Em versões anteriores à v0.18.1, um servidor MCP antigo degrada o cache do CLI.
- **Nesta máquina o fallback de browser está desligado**: `ketch doctor` aponta
  `browser: chrome misconfigured` (não há `chrome` no `$PATH`). Scraping HTTP normal
  funciona; páginas 100% renderizadas por JS podem vir incompletas — o `ketch scrape`
  emite um `warn:` nesse caso. Ativar o browser é ação de operador (ver abaixo).
- **`crawl` interrompido com SIGINT sai com `0`** e resultados parciais, por design.
- **Config**: `ketch config path` aponta o arquivo (neste macOS,
  `~/Library/Application Support/ketch/config.json`); flags > env `KETCH_*` > arquivo > padrão.

### Nunca instale nem configure o `ketch` por conta própria

O `ketch` já está instalado — verifique com `command -v ketch` **antes** de sugerir qualquer
instalação. Se faltar, ou se um backend precisar de API key (`ketch doctor` mostra
`no_key`/`misconfigured`), siga a *Regra fundamental* no topo: **pare, explique e pergunte**
(comando exato e onde ele grava). `brew install ketch`, `ketch browser install` (baixa um
Chromium) e `ketch config set …_api_key` **não** são executáveis sem autorização explícita.

## Padrão de imagem dos posts (obrigatório)

Toda imagem de **destaque** de um post (campo `image:` no front matter) deve ter **exatamente
1024x600 px** — a mesma proporção da imagem de referência **`assets/img/spools.jpg`**.
Vale para imagens novas e para as já publicadas quando forem tocadas.

- **Escopo:** a regra é da imagem de **capa**. Imagens usadas **dentro do corpo** do post
  (diagramas, prints, gráficos: `![...](assets/img/x.png)`) **não** entram no 1024x600 —
  cortá-las para essa proporção destruiria conteúdo (há diagramas verticais no acervo).
  Para as inline, apenas preserve a proporção (`max-width: 100%` já cuida do layout).

- O ajuste é **cover fit**: redimensiona proporcionalmente e **corta o excesso no centro**.
  Nunca distorça (esticar/comprimir) e nunca adicione barras ou letterbox.
- Corrigir um arquivo:

  ```bash
  scripts/normalize_post_image.sh assets/img/<arquivo>   # aceita vários arquivos
  ```

- **Rode o script apenas nos arquivos fora do padrão.** Ele sempre re-encoda (JPEG é com
  perda), então passar uma imagem que **já** está 1024x600 só degrada e engorda o arquivo,
  sem ganho de layout. Confirme com `check_post_images.sh` / `sips` antes. Não é preciso
  renomear, mover nem editar o `image:` do post — só o conteúdo muda.

- Validar **todos** os posts antes de publicar (somente leitura):

  ```bash
  scripts/check_post_images.sh        # exit 0 = tudo em 1024x600
  ```

- Revisar visualmente (folha de contato em PDF com miniaturas e dimensões):

  ```bash
  python3 scripts/review_post_images.py   # grava /tmp/review_post_images.pdf
  ```

- **Nunca renomeie** a imagem para ajustar o padrão: o nome faz parte da URL publicada.
  Normalizar é **sobrescrever o conteúdo**, preservando nome e caminho.
- Imagens menores que 1024x600 são **ampliadas** pelo cover fit. É aceitável para não
  quebrar o padrão, mas o ideal é baixar uma imagem maior na origem (as imagens são
  exibidas com no máximo ~1024 px de largura em telas retina).
- O `sips` **não grava WebP** (falha). Ao normalizar um `.webp`, converta o **conteúdo**
  para JPEG mantendo o **mesmo nome de arquivo** (`assets/img/x.webp` continua existindo e
  continua sendo servido; `file` mostra JPEG). Não é preciso mexer no `image:` do post.
- As ferramentas são `sips` (já vem no macOS) e `python3` (stdlib + PyMuPDF). **Não instale
  nada** para isso — ver a regra fundamental no topo deste arquivo.

## Publicação

Este blog publica via GitHub Pages no branch `gh-pages`. Um push em `gh-pages` publica em produção.

**Você pode e deve fazer `push` quando a tarefa envolver publicar um post.** Não peça permissão para cada envio: se o usuário pediu para criar/publicar a notícia, o push faz parte da entrega. Anuncie no resumo final o que foi enviado (commit, arquivos, destino), para que a publicação fique auditável.

Antes de qualquer push:

1. Verifique `git status` — não inclua arquivos gerados/untracked alheios à tarefa (ex.: `__pycache__/`, caches).
2. Rode `git fetch origin` e confira se está `behind`. O branch recebe commits automáticos (`chore: atualiza leaderboard [skip ci]` em `_data/leaderboard.*`); publique sempre sobre o topo mais recente.
   - Se estiver `[ahead N, behind M]`, faça `git rebase origin/gh-pages` antes do push. Se houver conflito, **pare e resolva com o usuário** — nunca use `push --force` em `gh-pages`.
3. Confirme que o build do Jekyll não quebrou (front matter válido, `image:` apontando para arquivo existente em `assets/img/`).
4. Rode `scripts/check_post_images.sh` e confirme que **toda** imagem de post está em
   1024x600 (padrão descrito em *Padrão de imagem dos posts*, acima).

Só **não** faça push quando o usuário pedir explicitamente para segurar, ou quando o post estiver em revisão aguardando aprovação de conteúdo.

## Ordenação de posts (Jekyll)

Posts são ordenados por data e, em caso de **empate de data**, pelo nome do arquivo — e a lista é **invertida** na exibição (`site.posts` usa `sort { |a, b| b <=> a }`).

Consequência: **o nome de arquivo alfabeticamente MAIOR aparece primeiro.** Para um post subir ao topo entre empatados, use um prefixo maior (ex.: `z-`), não `a-`.

Para mudar a ordenação **sem** quebrar a URL publicada, defina `slug:` no front matter — o permalink `/:title` usa esse campo, não o nome do arquivo.
