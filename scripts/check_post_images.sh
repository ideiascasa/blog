#!/usr/bin/env bash
#
# check_post_images.sh — Auditoria do padrão de imagens de capa dos posts do blog.
#
# PROPÓSITO
#   Verifica, para cada arquivo em `_posts/*.md`, se o front matter declara um
#   campo `image: nome-do-arquivo.ext`, se esse arquivo existe em `assets/img/`
#   e se ele tem EXATAMENTE 1024x600 pixels (proporção 1,707:1, igual à
#   referência `assets/img/spools.jpg`).
#
#   Este script é SOMENTE LEITURA: nunca cria, move, renomeia, reescreve,
#   comprime ou normaliza imagens nem posts. Não faz commit e não faz push.
#
# USO
#   scripts/check_post_images.sh [--verbose | --quiet | --help]
#
#   --verbose   Mostra também a lista completa de imagens de `assets/img` que
#               não são referenciadas por nenhum post (e outras notas extras).
#   --quiet     Mostra apenas o resumo e os problemas (DIVERGENTE/AUSENTE/
#               SEM IMAGEM); omite as linhas OK e IGNORADA, os avisos e as notas.
#   --help      Exibe esta ajuda.
#
#   Pode ser executado de qualquer diretório: a raiz do repositório é derivada
#   da própria localização do script (com fallback para `git rev-parse`).
#
# EXCEÇÕES
#   A variável IMAGENS_IGNORADAS (abaixo) lista nomes de arquivo cujo desvio do
#   padrão é conhecido e tolerado (artefatos históricos cuja normalização
#   danificaria o layout). Elas aparecem com status IGNORADA: não contam como
#   DIVERGENTE e NÃO alteram o exit code. Hoje: bluebox.png (logo 300x134 do
#   post de 2024, usada como imagem de capa).
#
# DEPENDÊNCIAS
#   Somente ferramentas já presentes no macOS: bash, grep, awk, sed, sort, comm,
#   mktemp, wc e `sips` (para ler as dimensões das imagens). Nada é instalado.
#
# EXIT CODES
#   0  Todas as imagens declaradas existem e medem 1024x600 (as IGNORADAS não
#      contam e podem estar fora do padrão).
#   1  Existe pelo menos um status DIVERGENTE, AUSENTE ou SEM IMAGEM.
#   2  Erro de uso (argumento inválido) ou dependência ausente (sips).
#
# SAÍDA
#   Tabela alinhada: post | arquivo de imagem | existe? | dimensões | proporção | status
#   Status possíveis: OK | IGNORADA | DIVERGENTE | AUSENTE | SEM IMAGEM
#   Ao final, um resumo com a contagem de cada status e avisos (não são erros):
#   posts sem `image:` e imagens de `assets/img` não referenciadas.
#

set -uo pipefail

# ---------------------------------------------------------------- configuração
LARGURA_ESPERADA=1024
ALTURA_ESPERADA=600
DIR_IMG_REL="assets/img"

# Imagens cujo desvio do padrão é conhecido e tolerado. Liste os nomes de
# arquivo exatamente como aparecem no campo `image:` do front matter, separados
# por espaço. Elas recebem status IGNORADA e não entram na contagem de
# DIVERGENTE nem no exit code. Mantenha esta lista curta e justificada.
IMAGENS_IGNORADAS="bluebox.png"

VERBOSE=0
QUIET=0

# verifica se um nome de arquivo está em IMAGENS_IGNORADAS
esta_ignorada() {
  case " ${IMAGENS_IGNORADAS} " in
    *" $1 "*) return 0 ;;
    *)        return 1 ;;
  esac
}

uso() {
  # imprime o bloco de comentários do topo (ignora o shebang), do começo até a
  # primeira linha de código; o range é dinâmico para não truncar ao editar o header
  awk 'NR == 1 { next } /^#/ { sub(/^# ?/, ""); print; next } { exit }' "$0" \
    | awk 'NF { encontrou = 1 } encontrou'
}

# ------------------------------------------------------------------- argumentos
for arg in "$@"; do
  case "$arg" in
    --verbose) VERBOSE=1 ;;
    --quiet)   QUIET=1 ;;
    --help|-h) uso; exit 0 ;;
    *)
      printf 'erro: argumento desconhecido: %s\n' "$arg" >&2
      printf 'uso: %s [--verbose | --quiet | --help]\n' "$(basename "$0")" >&2
      exit 2
      ;;
  esac
done

if [ "$VERBOSE" -eq 1 ] && [ "$QUIET" -eq 1 ]; then
  printf 'erro: --verbose e --quiet são mutuamente exclusivos\n' >&2
  exit 2
fi

if ! command -v sips >/dev/null 2>&1; then
  printf 'erro: comando "sips" não encontrado (necessário para ler as dimensões)\n' >&2
  exit 2
fi

# ------------------------------------------------------------- raiz do repositório
# 1) tenta pelo diretório do próprio script (../ a partir de scripts/);
# 2) se não houver _posts, tenta `git rev-parse --show-toplevel`.
DIR_SCRIPT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RAIZ="$(cd "$DIR_SCRIPT/.." && pwd)"

if [ ! -d "$RAIZ/_posts" ]; then
  if command -v git >/dev/null 2>&1; then
    TOPO="$(git -C "$DIR_SCRIPT" rev-parse --show-toplevel 2>/dev/null || true)"
    if [ -n "$TOPO" ] && [ -d "$TOPO/_posts" ]; then
      RAIZ="$TOPO"
    fi
  fi
fi

if [ ! -d "$RAIZ/_posts" ]; then
  printf 'erro: não encontrei o diretório _posts (raiz detectada: %s)\n' "$RAIZ" >&2
  exit 2
fi

DIR_POSTS="$RAIZ/_posts"
DIR_IMG="$RAIZ/$DIR_IMG_REL"

# --------------------------------------------------------- utilitários de largura
# `printf %-Ns` alinha por BYTES; os títulos "DIMENSÕES" e "PROPORÇÃO" têm
# caracteres multibyte (2 bytes cada). Estas funções permitem compensar a
# diferença bytes-vs-caracteres ao imprimir o cabeçalho.
byte_len() { printf '%s' "$1" | LC_ALL=C wc -c | tr -d ' '; }
char_len() { printf '%s' "$1" | wc -m | tr -d ' '; }

# --------------------------------------------------------------- arquivos temporários
TMP_DADOS="$(mktemp -t check_imgs_dados.XXXXXX)"   # registros TSV de cada post
TMP_REF="$(mktemp -t check_imgs_ref.XXXXXX)"       # imagens referenciadas
TMP_ARQS="$(mktemp -t check_imgs_arq.XXXXXX)"      # arquivos existentes em assets/img
TMP_ORFAS="$(mktemp -t check_imgs_orf.XXXXXX)"     # imagens não referenciadas
TMP_SEMIMG="$(mktemp -t check_imgs_semimg.XXXXXX)" # posts sem `image:`
trap 'rm -f "$TMP_DADOS" "$TMP_REF" "$TMP_ARQS" "$TMP_ORFAS" "$TMP_SEMIMG"' EXIT

# ------------------------------------------------------------------- acumuladores
total_posts=0
n_ok=0
n_divergente=0
n_ignorada=0
n_ausente=0
n_sem_imagem=0

# 1) avaliação post a post -------------------------------------------------------
for POST in "$DIR_POSTS"/*.md; do
  # glob sem correspondência: ignora
  [ -e "$POST" ] || continue

  nome_post="$(basename "$POST")"
  total_posts=$((total_posts + 1))

  # --- extrai `image:` SOMENTE do front matter --------------------------------
  # Front matter = bloco delimitado por linhas `---` no início do arquivo.
  # Só a PRIMEIRA ocorrência de `^image:` dentro do bloco é considerada.
  imagem="$(awk '
    NR == 1 && $0 ~ /^---[[:space:]]*$/ { dentro = 1; next }
    dentro && $0 ~ /^---[[:space:]]*$/   { exit }
    dentro && /^image:[[:space:]]*/ {
      sub(/^image:[[:space:]]*/, "")
      sub(/[[:space:]]+$/, "")
      # remove aspas simples ou duplas envolventes
      if ($0 ~ /^".*"$/ || $0 ~ /^'"'"'.*'"'"'$/) $0 = substr($0, 2, length($0) - 2)
      gsub(/^[[:space:]]+|[[:space:]]+$/, "")
      print
      exit
    }
  ' "$POST")"

  # --- post sem `image:` no front matter --------------------------------------
  if [ -z "$imagem" ]; then
    n_sem_imagem=$((n_sem_imagem + 1))
    printf '%s\n' "$nome_post" >> "$TMP_SEMIMG"
    printf '%s\t%s\t%s\t%s\t%s\t%s\n' \
      "$nome_post" "(nenhuma)" "-" "-" "-" "SEM IMAGEM" >> "$TMP_DADOS"
    continue
  fi

  # registra a referência (usada depois para achar imagens órfãs)
  printf '%s\n' "$imagem" >> "$TMP_REF"

  caminho_img="$DIR_IMG/$imagem"

  # --- imagem em exceção conhecida (não conta como DIVERGENTE) ------------------
  ignorada=0
  if esta_ignorada "$imagem"; then
    ignorada=1
  fi

  # --- imagem inexistente ------------------------------------------------------
  if [ ! -f "$caminho_img" ]; then
    n_ausente=$((n_ausente + 1))
    printf '%s\t%s\t%s\t%s\t%s\t%s\n' \
      "$nome_post" "$imagem" "não" "-" "-" "AUSENTE" >> "$TMP_DADOS"
    continue
  fi

  # --- dimensões via sips ------------------------------------------------------
  dims="$(sips -g pixelWidth -g pixelHeight "$caminho_img" 2>/dev/null)"
  largura="$(printf '%s\n' "$dims" | awk '/pixelWidth:/  { print $2; exit }')"
  altura="$(printf '%s\n' "$dims"  | awk '/pixelHeight:/ { print $2; exit }')"

  if ! printf '%s' "$largura" | grep -qE '^[0-9]+$' \
    || ! printf '%s' "$altura" | grep -qE '^[0-9]+$'; then
    # formato não raster (ex.: svg, webm) ou arquivo ilegível: sips devolve
    # valores não inteiros (ex.: 626.000). Não é possível comparar; marca DIVERGENTE
    # (ou IGNORADA, se estiver na lista de exceções).
    if [ "$ignorada" -eq 1 ]; then
      status="IGNORADA"
      n_ignorada=$((n_ignorada + 1))
    else
      status="DIVERGENTE"
      n_divergente=$((n_divergente + 1))
    fi
    printf '%s\t%s\t%s\t%s\t%s\t%s\n' \
      "$nome_post" "$imagem" "sim" "?" "?" "$status" >> "$TMP_DADOS"
    continue
  fi

  # proporção com 3 casas (o cálculo em awk evita problemas de locale)
  proporcao="$(awk -v w="$largura" -v h="$altura" \
    'BEGIN { if (h > 0) printf "%.3f", w / h; else print "?" }')"

  if [ "$ignorada" -eq 1 ]; then
    status="IGNORADA"
    n_ignorada=$((n_ignorada + 1))
  elif [ "$largura" -eq "$LARGURA_ESPERADA" ] && [ "$altura" -eq "$ALTURA_ESPERADA" ]; then
    status="OK"
    n_ok=$((n_ok + 1))
  else
    status="DIVERGENTE"
    n_divergente=$((n_divergente + 1))
  fi

  printf '%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$nome_post" "$imagem" "sim" "${largura}x${altura}" "$proporcao" "$status" >> "$TMP_DADOS"
done

# 2) imagens de assets/img não referenciadas ------------------------------------
if [ -d "$DIR_IMG" ]; then
  (cd "$DIR_IMG" && ls -1) | sort -u > "$TMP_ARQS"
fi
sort -u "$TMP_REF" > "$TMP_REF.ord"
comm -23 "$TMP_ARQS" "$TMP_REF.ord" > "$TMP_ORFAS"
rm -f "$TMP_REF.ord"
n_arquivos_img="$(wc -l < "$TMP_ARQS" | tr -d ' ')"
n_orfas="$(wc -l < "$TMP_ORFAS" | tr -d ' ')"

# 3) impressão da tabela (larguras derivadas dos dados) --------------------------
# Colunas de texto assumem ao menos 20 (post) e 8 (imagem) caracteres.
read -r w_post w_img < <(awk -F'\t' '
  { if (length($1) > a) a = length($1); if (length($2) > b) b = length($2) }
  END { printf "%d %d\n", (a < 20 ? 20 : a), (b < 8 ? 8 : b) }' "$TMP_DADOS")

w_dims=9    # "2164x1454" cabe em 9
w_prop=9    # "1.707" cabe em 9

FMT=" %-${w_post}s  %-${w_img}s  %-6s  %-${w_dims}s  %-${w_prop}s  %s\n"
HDR_DIM="DIMENSÕES"; HDR_PROP="PROPORÇÃO"
h_dim=$(( w_dims + $(byte_len "$HDR_DIM") - $(char_len "$HDR_DIM") ))
h_prop=$(( w_prop + $(byte_len "$HDR_PROP") - $(char_len "$HDR_PROP") ))

imprime_cabecalho() {
  # shellcheck disable=SC2059
  printf " %-${w_post}s  %-${w_img}s  %-6s  %-${h_dim}s  %-${h_prop}s  %s\n" \
    "POST" "IMAGEM" "EXISTE" "$HDR_DIM" "$HDR_PROP" "STATUS"
  awk -v n=$(( w_post + w_img + w_dims + w_prop + 26 )) \
    'BEGIN { s = ""; for (i = 0; i < n; i++) s = s "-"; print " " s }'
}

imprime_linhas() {
  while IFS=$'\t' read -r p i e d pr st; do
    [ -n "${st:-}" ] || continue
    if [ "$QUIET" -eq 1 ]; then
      case "$st" in
        OK|IGNORADA) continue ;;
      esac
    fi
    # shellcheck disable=SC2059
    printf "$FMT" "$p" "$i" "$e" "$d" "$pr" "$st"
  done < "$TMP_DADOS"
}

imprime_cabecalho
imprime_linhas

# 4) resumo ----------------------------------------------------------------------
printf '\n'
printf 'RESUMO\n'
printf '  posts analisados ............................ %d\n' "$total_posts"
printf '  OK (1024x600) ............................... %d\n' "$n_ok"
printf '  IGNORADA (exceção conhecida) ................ %d\n' "$n_ignorada"
printf '  DIVERGENTE .................................. %d\n' "$n_divergente"
printf '  AUSENTE (não existe em %s) ... %d\n' "$DIR_IMG_REL" "$n_ausente"
printf '  SEM IMAGEM (post sem `image:`) .............. %d\n' "$n_sem_imagem"
printf '  arquivos em %s .................. %d\n' "$DIR_IMG_REL" "$n_arquivos_img"
printf '  arquivos em %s não referenciados %d\n' "$DIR_IMG_REL" "$n_orfas"
printf '  esperado: %dx%d (proporção 1024/600 = %.3f)\n' \
  "$LARGURA_ESPERADA" "$ALTURA_ESPERADA" \
  "$(awk -v w="$LARGURA_ESPERADA" -v h="$ALTURA_ESPERADA" 'BEGIN { printf "%.3f", w / h }')"

# 5) avisos (não afetam o exit code por si só) -----------------------------------
if [ "$QUIET" -eq 0 ]; then
  printf '\nAVISOS (não são erros)\n'

  if [ "$n_sem_imagem" -gt 0 ]; then
    printf '  - posts sem `image:` no front matter (%d):\n' "$n_sem_imagem"
    sed 's/^/      * /' "$TMP_SEMIMG"
  else
    printf '  - nenhum post sem `image:` no front matter.\n'
  fi

  if [ "$n_orfas" -gt 0 ]; then
    printf '  - %d arquivo(s) em %s não referenciado(s) por nenhum post (pode ser intencional: logos, ícones, assets de layout).\n' \
      "$n_orfas" "$DIR_IMG_REL"
    if [ "$VERBOSE" -eq 1 ]; then
      sed 's/^/      * /' "$TMP_ORFAS"
    else
      printf '      (use --verbose para listar)\n'
    fi
  else
    printf '  - todos os arquivos de %s são referenciados por algum post.\n' "$DIR_IMG_REL"
  fi

  if [ "$VERBOSE" -eq 1 ]; then
    printf '  - referências repetidas (mesma imagem em mais de um post):\n'
    dups="$(sort "$TMP_REF" | uniq -d)"
    if [ -n "$dups" ]; then
      printf '%s\n' "$dups" | sed 's/^/      * /'
    else
      printf '      (nenhuma)\n'
    fi
  fi
fi

# 6) exit code -------------------------------------------------------------------
if [ "$n_divergente" -gt 0 ] || [ "$n_ausente" -gt 0 ] || [ "$n_sem_imagem" -gt 0 ]; then
  exit 1
fi
exit 0