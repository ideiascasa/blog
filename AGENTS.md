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

## Publicação

Este blog publica via GitHub Pages no branch `gh-pages`. Um push em `gh-pages` publica em produção.

**Você pode e deve fazer `push` quando a tarefa envolver publicar um post.** Não peça permissão para cada envio: se o usuário pediu para criar/publicar a notícia, o push faz parte da entrega. Anuncie no resumo final o que foi enviado (commit, arquivos, destino), para que a publicação fique auditável.

Antes de qualquer push:

1. Verifique `git status` — não inclua arquivos gerados/untracked alheios à tarefa (ex.: `__pycache__/`, caches).
2. Rode `git fetch origin` e confira se está `behind`. O branch recebe commits automáticos (`chore: atualiza leaderboard [skip ci]` em `_data/leaderboard.*`); publique sempre sobre o topo mais recente.
   - Se estiver `[ahead N, behind M]`, faça `git rebase origin/gh-pages` antes do push. Se houver conflito, **pare e resolva com o usuário** — nunca use `push --force` em `gh-pages`.
3. Confirme que o build do Jekyll não quebrou (front matter válido, `image:` apontando para arquivo existente em `assets/img/`).

Só **não** faça push quando o usuário pedir explicitamente para segurar, ou quando o post estiver em revisão aguardando aprovação de conteúdo.

## Ordenação de posts (Jekyll)

Posts são ordenados por data e, em caso de **empate de data**, pelo nome do arquivo — e a lista é **invertida** na exibição (`site.posts` usa `sort { |a, b| b <=> a }`).

Consequência: **o nome de arquivo alfabeticamente MAIOR aparece primeiro.** Para um post subir ao topo entre empatados, use um prefixo maior (ex.: `z-`), não `a-`.

Para mudar a ordenação **sem** quebrar a URL publicada, defina `slug:` no front matter — o permalink `/:title` usa esse campo, não o nome do arquivo.
