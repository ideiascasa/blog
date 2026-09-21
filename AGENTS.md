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
