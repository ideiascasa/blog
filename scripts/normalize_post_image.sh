#!/bin/bash
#
# normalize_post_image.sh — normaliza imagens de destaque de posts para 1024x600
#
# PROPÓSITO
#   Todas as imagens de destaque dos posts deste blog Jekyll (assets/img/*)
#   devem ter exatamente 1024x600 px, a mesma proporção de
#   assets/img/spools.jpg. Este script aplica um "cover fit" (preenche o alvo
#   sem distorcer, cortando o excesso no centro, SEM barras/padding) e
#   re-encoda na qualidade desejada.
#
# USO
#   scripts/normalize_post_image.sh [opções] <arquivo> [<arquivo>...]
#
# OPÇÕES
#   --width N     largura alvo  (default: 1024)
#   --height N    altura alvo   (default: 600)
#   --quality Q   qualidade JPEG 0-100 (default: 85)
#   --dry-run     não altera nada; imprime o que faria
#   -h, --help    mostra esta ajuda
#
# DEPENDÊNCIAS
#   Apenas ferramentas já presentes no macOS: /usr/bin/sips, awk, sed, bash.
#   Nada é instalado. Nenhum `commit` é feito.
#
# COMO FUNCIONA
#   Para cada arquivo, lê as dimensões com `sips -g pixelWidth -g pixelHeight`.
#   Seja W/H o alvo e w/h o original:
#     - w/h > W/H (mais larga): recorta a largura para floor(h*W/H) mantendo h.
#     - w/h < W/H (mais estreita): recorta a altura para floor(w*H/W) mantendo w.
#     - já exato: apenas re-encoda (idempotente).
#   O crop do sips (`sips -c ALTURA LARGURA`) é centralizado por padrão; depois
#   um `sips -z ALTURA LARGURA` garante o tamanho exato. Usamos `floor` (nunca
#   ceil/round) para o crop nunca exceder as dimensões reais da imagem.
#
# FORMATOS
#   .jpg/.jpeg -> JPEG na qualidade pedida.
#   .png       -> PNG; se o original NÃO tiver canal alpha (hasAlpha: no),
#                 grava JPEG no mesmo arquivo (o NOME é preservado: .png
#                 continua .png, pois renomear quebraria URLs publicadas).
#   .webp      -> o sips não sabe escrever webp (falha com exit 13). O conteúdo
#                 é convertido para JPEG e substitui o conteúdo do .webp
#                 original, mantendo o nome. Um AVISO é impresso.
#
# SEGURANÇA
#   Nunca apagamos o original antes de ter o resultado pronto: tudo é gerado em
#   arquivos temporários (`-o`) e só então movido sobre o original. Nome,
#   caminho e permissões do arquivo são preservados.
#
set -u

WIDTH=1024
HEIGHT=600
QUALITY=85
DRY_RUN=0

usage() {
    sed -n '2,20p' "$0" | sed 's/^# \{0,1\}//'
    cat <<'EOF'

Exemplos:
  scripts/normalize_post_image.sh assets/img/foto.jpg
  scripts/normalize_post_image.sh --dry-run assets/img/*.png
  scripts/normalize_post_image.sh --width 1200 --height 700 --quality 80 img.jpg
EOF
}

die() { printf 'ERRO: %s\n' "$*" >&2; exit 1; }

# ---------------------------------------------------------------- argumentos
FILES=()
while [ $# -gt 0 ]; do
    case "$1" in
        --width)   [ $# -ge 2 ] || die "--width exige um valor";  WIDTH="$2";   shift 2 ;;
        --height)  [ $# -ge 2 ] || die "--height exige um valor"; HEIGHT="$2";  shift 2 ;;
        --quality) [ $# -ge 2 ] || die "--quality exige um valor"; QUALITY="$2"; shift 2 ;;
        --dry-run) DRY_RUN=1; shift ;;
        -h|--help) usage; exit 0 ;;
        --) shift; while [ $# -gt 0 ]; do FILES+=("$1"); shift; done ;;
        -*) die "opção desconhecida: $1 (use -h para ajuda)" ;;
        *)  FILES+=("$1"); shift ;;
    esac
done

[ "${#FILES[@]}" -gt 0 ] || { usage; exit 1; }

is_uint() { case "$1" in ''|*[!0-9]*) return 1 ;; *) return 0 ;; esac; }
is_uint "$WIDTH"   || die "--width deve ser inteiro positivo: $WIDTH"
is_uint "$HEIGHT"  || die "--height deve ser inteiro positivo: $HEIGHT"
is_uint "$QUALITY" || die "--quality deve ser inteiro 0-100: $QUALITY"
[ "$WIDTH"  -gt 0 ] || die "--width deve ser > 0"
[ "$HEIGHT" -gt 0 ] || die "--height deve ser > 0"
[ "$QUALITY" -le 100 ] || die "--quality deve estar entre 0 e 100"

SIPS=/usr/bin/sips
[ -x "$SIPS" ] || die "sips não encontrado em $SIPS"

TMPDIR_RUN="$(mktemp -d "${TMPDIR:-/tmp}/normalize_post_image.XXXXXX")" || die "não consegui criar diretório temporário"
cleanup() { rm -rf "$TMPDIR_RUN"; }
trap cleanup EXIT INT TERM

# ------------------------------------------------------------------ helpers
file_bytes() { stat -f%z "$1" 2>/dev/null || wc -c <"$1" | tr -d ' '; }

# Lê uma propriedade do sips. Retorna vazio se não for imagem.
sips_prop() {
    _f="$1"; _p="$2"
    "$SIPS" -g "$_p" "$_f" 2>/dev/null | awk -F': *' -v k="$_p" '$1 ~ k"$" {print $2}' | head -1
}

bytes_to_kb() { awk -v b="$1" 'BEGIN { printf "%.1f", b/1024 }'; }

# --------------------------------------------------------------- acumuladores
TOTAL_BEFORE=0
TOTAL_AFTER=0
ROW_FILE=(); ROW_BEFORE=(); ROW_AFTER=(); ROW_SAVE=(); ROW_NOTE=()
FAILED=0

printf 'normalize_post_image.sh — alvo %sx%s, qualidade %s%s\n' \
    "$WIDTH" "$HEIGHT" "$QUALITY" "$([ "$DRY_RUN" -eq 1 ] && echo ' (dry-run)')"
echo

for f in "${FILES[@]}"; do
    if [ ! -e "$f" ]; then
        printf 'ERRO: arquivo não existe: %s\n' "$f" >&2
        FAILED=1
        continue
    fi
    if [ ! -f "$f" ]; then
        printf 'ERRO: não é um arquivo regular: %s\n' "$f" >&2
        FAILED=1
        continue
    fi

    ow="$(sips_prop "$f" pixelWidth)"
    oh="$(sips_prop "$f" pixelHeight)"
    if ! is_uint "$ow" || ! is_uint "$oh" || [ "$ow" -le 0 ] || [ "$oh" -le 0 ]; then
        printf 'ERRO: não é uma imagem legível pelo sips: %s\n' "$f" >&2
        FAILED=1
        continue
    fi

    ext="$(printf '%s' "${f##*.}" | tr '[:upper:]' '[:lower:]')"
    before_bytes="$(file_bytes "$f")"

    # ---- decide o crop (floor sempre, para nunca exceder as dimensões reais)
    # comparamos w/h com W/H via produto cruzado (inteiros, sem float)
    lhs=$(( ow * HEIGHT ))   # w * H
    rhs=$(( oh * WIDTH ))    # h * W
    crop_h=$oh
    crop_w=$ow
    if [ "$lhs" -gt "$rhs" ]; then
        # mais larga que o alvo -> corta largura, mantém altura
        crop_w=$(( oh * WIDTH / HEIGHT ))   # floor
        crop_h=$oh
    elif [ "$lhs" -lt "$rhs" ]; then
        # mais estreita que o alvo -> corta altura, mantém largura
        crop_h=$(( ow * HEIGHT / WIDTH ))   # floor
        crop_w=$ow
    fi
    # crop não pode estourar as dimensões reais nem ser zero
    [ "$crop_w" -gt "$ow" ] && crop_w=$ow
    [ "$crop_h" -gt "$oh" ] && crop_h=$oh
    [ "$crop_w" -lt 1 ] && crop_w=1
    [ "$crop_h" -lt 1 ] && crop_h=1

    # ---- define formato de saída
    out_format="jpeg"
    rename_note=""
    webp_mode=0
    case "$ext" in
        jpg|jpeg) out_format="jpeg" ;;
        png)
            has_alpha="$(sips_prop "$f" hasAlpha)"
            if [ "$has_alpha" = "yes" ]; then
                out_format="png"
            else
                out_format="jpeg"   # png sem alpha -> grava jpeg no MESMO nome
                rename_note="jpeg no nome .png"
            fi
            ;;
        webp) out_format="jpeg"; webp_mode=1; rename_note="webp->jpeg (nome .webp mantido)" ;;
        *)
            printf 'AVISO: extensão desconhecida (.%s); assumindo JPEG na saída: %s\n' "$ext" "$f" >&2
            out_format="jpeg"
            ;;
    esac

    plan="crop ${crop_w}x${crop_h} -> resize ${WIDTH}x${HEIGHT} (${out_format})"

    if [ "$DRY_RUN" -eq 1 ]; then
        printf '  [dry-run] %s: %sx%s -> %s\n' "$f" "$ow" "$oh" "$plan"
        ROW_FILE+=("$f")
        ROW_BEFORE+=("$(printf '%sx%s %s KB' "$ow" "$oh" "$(bytes_to_kb "$before_bytes")")")
        ROW_AFTER+=("$(printf '%sx%s -' "$WIDTH" "$HEIGHT")")
        ROW_SAVE+=("-")
        ROW_NOTE+=("$rename_note")
        continue
    fi

    # ---- trabalho em temporários; nada toca o original até o fim
    # O sips NÃO escreve webp de jeito nenhum (exit 13) e, pior, infere o formato
    # de saída a partir do formato da ORIGEM (ignora a extensão de -o). Por isso
    # todo arquivo .webp passa primeiro por uma conversão explícita para JPEG.
    TMPEXT="jpg"; [ "$out_format" = "png" ] && TMPEXT="png"
    tmp_crop="$TMPDIR_RUN/crop.$$.$RANDOM.$TMPEXT"
    tmp_final="$TMPDIR_RUN/final.$$.$RANDOM.$TMPEXT"
    rm -f "$tmp_crop" "$tmp_final"

    SRC="$f"
    if [ "$webp_mode" -eq 1 ]; then
        tmp_src="$TMPDIR_RUN/src.$$.$RANDOM.jpg"
        rm -f "$tmp_src"
        if ! "$SIPS" -s format jpeg "$f" -o "$tmp_src" >/dev/null 2>&1; then
            printf 'ERRO: falha ao converter webp para JPEG: %s\n' "$f" >&2
            FAILED=1; continue
        fi
        SRC="$tmp_src"
    fi

    if [ "$crop_w" -ne "$ow" ] || [ "$crop_h" -ne "$oh" ]; then
        if ! "$SIPS" -c "$crop_h" "$crop_w" -s format "$out_format" "$SRC" -o "$tmp_crop" >/dev/null 2>&1; then
            printf 'ERRO: falha no crop de %s (sips -c %s %s)\n' "$f" "$crop_h" "$crop_w" >&2
            rm -f "$tmp_crop" "$tmp_final"; FAILED=1; continue
        fi
    else
        cp "$SRC" "$tmp_crop"
    fi

    # resize exato + formato/qualidade (sempre sobrescreve o tmp de saída)
    if [ "$out_format" = "png" ]; then
        if ! "$SIPS" -z "$HEIGHT" "$WIDTH" -s format png "$tmp_crop" -o "$tmp_final" >/dev/null 2>&1; then
            printf 'ERRO: falha ao gerar PNG %sx%s de %s\n' "$WIDTH" "$HEIGHT" "$f" >&2
            rm -f "$tmp_crop" "$tmp_final"; FAILED=1; continue
        fi
    else
        if ! "$SIPS" -z "$HEIGHT" "$WIDTH" -s format jpeg -s formatOptions "$QUALITY" "$tmp_crop" -o "$tmp_final" >/dev/null 2>&1; then
            printf 'ERRO: falha ao gerar JPEG %sx%s de %s\n' "$WIDTH" "$HEIGHT" "$f" >&2
            rm -f "$tmp_crop" "$tmp_final"; FAILED=1; continue
        fi
    fi

    # valida o resultado antes de tocar no original
    nw="$(sips_prop "$tmp_final" pixelWidth)"
    nh="$(sips_prop "$tmp_final" pixelHeight)"
    if [ "$nw" != "$WIDTH" ] || [ "$nh" != "$HEIGHT" ]; then
        printf 'ERRO: resultado inesperado %sx%s (esperado %sx%s) para %s — original preservado\n' \
            "${nw:-?}" "${nh:-?}" "$WIDTH" "$HEIGHT" "$f" >&2
        rm -f "$tmp_crop" "$tmp_final"; FAILED=1; continue
    fi
    if [ ! -s "$tmp_final" ]; then
        printf 'ERRO: resultado vazio para %s — original preservado\n' "$f" >&2
        rm -f "$tmp_crop" "$tmp_final"; FAILED=1; continue
    fi

    # ---- substitui o conteúdo preservando nome, caminho e permissões
    orig_mode="$(stat -f%Lp "$f" 2>/dev/null || echo '')"
    if ! cp "$tmp_final" "$f"; then
        printf 'ERRO: falha ao gravar %s — original preservado\n' "$f" >&2
        rm -f "$tmp_crop" "$tmp_final"; FAILED=1; continue
    fi
    [ -n "$orig_mode" ] && chmod "$orig_mode" "$f" 2>/dev/null

    [ "$webp_mode" -eq 1 ] && printf 'AVISO: conteúdo convertido para JPEG (nome .webp mantido): %s\n' "$f" >&2

    after_bytes="$(file_bytes "$f")"
    if [ "$before_bytes" -gt 0 ]; then
        save_pct="$(awk -v b="$before_bytes" -v a="$after_bytes" 'BEGIN { printf "%+.1f%%", (a-b)*100/b }')"
    else
        save_pct="-"
    fi

    TOTAL_BEFORE=$(( TOTAL_BEFORE + before_bytes ))
    TOTAL_AFTER=$(( TOTAL_AFTER + after_bytes ))

    ROW_FILE+=("$f")
    ROW_BEFORE+=("$(printf '%sx%s %s KB' "$ow" "$oh" "$(bytes_to_kb "$before_bytes")")")
    ROW_AFTER+=("$(printf '%sx%s %s KB' "$nw" "$nh" "$(bytes_to_kb "$after_bytes")")")
    ROW_SAVE+=("$save_pct")
    ROW_NOTE+=("$rename_note")

    rm -f "$tmp_crop" "$tmp_final"
    printf '  ok: %s — %s\n' "$f" "$plan"
done

# ------------------------------------------------------------------- tabela
echo
if [ "${#ROW_FILE[@]}" -gt 0 ]; then
    fw=4; bw=6; aw=6
    for i in "${!ROW_FILE[@]}"; do
        [ "${#ROW_FILE[$i]}" -gt "$fw" ] && fw="${#ROW_FILE[$i]}"
        [ "${#ROW_BEFORE[$i]}" -gt "$bw" ] && bw="${#ROW_BEFORE[$i]}"
        [ "${#ROW_AFTER[$i]}" -gt "$aw" ] && aw="${#ROW_AFTER[$i]}"
    done

    hdr="$(printf "%-${fw}s  %-${bw}s  %-${aw}s  %9s  %s" "ARQUIVO" "ANTES" "DEPOIS" "ECONOMIA" "NOTA")"
    printf '%s\n' "$hdr"
    printf '%s\n' "$(printf '%*s' "${#hdr}" '' | tr ' ' '-')"
    for i in "${!ROW_FILE[@]}"; do
        printf "%-${fw}s  %-${bw}s  %-${aw}s  %9s  %s\n" \
            "${ROW_FILE[$i]}" "${ROW_BEFORE[$i]}" "${ROW_AFTER[$i]}" \
            "${ROW_SAVE[$i]}" "${ROW_NOTE[$i]}"
    done

    if [ "$DRY_RUN" -eq 0 ]; then
        echo
        printf 'TOTAL: antes %s KB (%s bytes)  ->  depois %s KB (%s bytes)\n' \
            "$(bytes_to_kb "$TOTAL_BEFORE")" "$TOTAL_BEFORE" \
            "$(bytes_to_kb "$TOTAL_AFTER")"  "$TOTAL_AFTER"
        if [ "$TOTAL_BEFORE" -gt 0 ]; then
            awk -v b="$TOTAL_BEFORE" -v a="$TOTAL_AFTER" \
                'BEGIN { printf "TOTAL: variação %+.1f%%\n", (a-b)*100/b }'
        fi
    fi
fi

if [ "$DRY_RUN" -eq 1 ]; then
    echo
    echo '(dry-run: nenhum arquivo foi alterado)'
fi

exit "$FAILED"