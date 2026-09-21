#!/usr/bin/env python3
"""Gera uma FOLHA DE CONTATO (contact sheet) em PDF para revisão humana das
imagens de destaque dos posts do blog Jekyll.

Uso:
    python3 scripts/review_post_images.py [--out ARQUIVO.pdf] [--cols 4]
                                          [--thumb-width 220] [--only-posts]

O script é SOMENTE LEITURA: nunca altera posts nem imagens em assets/img.
Dependência única: PyMuPDF (import fitz). Nada mais é necessário.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import fitz  # PyMuPDF

# ---------------------------------------------------------------------------
# Constantes de configuração
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parents[1]
IMGDIR = ROOT / "assets" / "img"
POSTS_DIR = ROOT / "_posts"

# Padrão de imagem de destaque do blog (proporção 1024x600).
STANDARD_W, STANDARD_H = 1024, 600

# Formatos que não são imagens raster e devem ser ignorados silenciosamente.
IGNORED_SUFFIXES = {".webm", ".svg"}

# Marca de aviso. O glifo "⚠" (U+26A0) NÃO existe nas fontes base-14 do PDF
# (helv/hebo) — o MuPDF o substitui por "·". Por isso usamos a alternativa
# textual permitida, "[!]", e reforçamos o aviso com cor vermelha na célula.
WARN = "[!]"

# Métricas de layout, em pontos (1 pt = 1/72 pol).
PAGE_W, PAGE_H = fitz.paper_size("a4")  # A4 retrato: 595 x 842 pt
MARGIN = 36.0
HEADER_H = 34.0
GUTTER = 10.0          # espaço horizontal entre colunas
ROW_GAP = 14.0         # espaço vertical entre linhas da grade
CELL_PAD = 5.0
TEXT_SIZE = 8.0        # linha pequena (WxH, KB, proporção)
NAME_SIZE = 8.5        # nome do arquivo (negrito)
LINE_H = 10.0          # altura de cada linha de texto

COLOR_BORDER = (0.72, 0.72, 0.72)   # borda normal da célula
COLOR_WARN = (0.80, 0.25, 0.05)     # borda/texto de aviso
COLOR_TEXT = (0.15, 0.15, 0.15)
COLOR_MUTED = (0.42, 0.42, 0.42)
COLOR_GUIDE = (0.55, 0.55, 0.85)    # linha-guia horizontal da grade

# Altura máxima de uma miniatura. Garante que uma linha da grade caiba sempre
# em uma página, mesmo para imagens com proporção extrema (ex.: 100x5000).
# Sem este teto, uma única linha estouraria a A4 e o conteúdo seria desenhado
# fora da página.
MAX_THUMB_H = PAGE_H - 2 * MARGIN - HEADER_H - ROW_GAP - (2 * CELL_PAD + 4.0 + 3 * LINE_H)

# Cache de fontes (usado para medir texto e decidir truncamento).
_FONTS: dict[str, fitz.Font] = {}


def _font(name: str) -> fitz.Font:
    """Devolve (com cache) uma fonte base-14 do PyMuPDF pelo nome."""
    if name not in _FONTS:
        _FONTS[name] = fitz.Font(name)
    return _FONTS[name]


def fit_text(text: str, fontname: str, size: float, max_width: float) -> str:
    """Encurta `text` com "..." até caber em `max_width` pontos."""
    font = _font(fontname)
    if font.text_length(text, size) <= max_width:
        return text
    sufixo = "..."
    lo, hi = 0, len(text)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if font.text_length(text[:mid] + sufixo, size) <= max_width:
            lo = mid
        else:
            hi = mid - 1
    return (text[:lo] + sufixo) if lo > 0 else sufixo


# ---------------------------------------------------------------------------
# Leitura dos posts (front matter)
# ---------------------------------------------------------------------------

def read_front_matter_image(post_path: Path) -> str | None:
    """Devolve o valor do primeiro `image:` do front matter (bloco ---...---).

    Retorna None quando o post não declara imagem. Qualquer `image:`
    subsequente (ou fora do bloco) é ignorado.
    """
    try:
        linhas = post_path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError as exc:  # arquivo ilegível: não quebra o script
        print(f"aviso: não foi possível ler {post_path}: {exc}", file=sys.stderr)
        return None

    # Localiza o delimitador de abertura do front matter.
    if not linhas or linhas[0].strip() != "---":
        return None

    for linha in linhas[1:]:
        if linha.strip() == "---":  # fim do front matter
            break
        chave, sep, valor = linha.partition(":")
        if sep and chave.strip() == "image":
            valor = valor.strip().strip('"').strip("'")
            return valor or None
    return None


def collect_items(only_posts: bool) -> list[dict]:
    """Monta a lista de itens a revisar, já ordenada por nome de imagem.

    Cada item: {"image", "path", "post", "referenced"}.
    """
    itens: list[dict] = []
    referenciadas: set[str] = set()  # basenames citados por algum post

    for post_path in sorted(POSTS_DIR.glob("*.md")):
        nome_img = read_front_matter_image(post_path)
        if not nome_img:
            continue
        referenciadas.add(Path(nome_img).name)
        itens.append(
            {
                "image": Path(nome_img).name,
                "path": IMGDIR / nome_img,
                "post": post_path.stem,  # nome do post = arquivo sem .md
                "referenced": True,
            }
        )

    if not only_posts:
        # Acrescenta as demais imagens de assets/img, marcadas como não referenciadas.
        for img_path in sorted(IMGDIR.rglob("*")):
            if not img_path.is_file() or img_path.suffix.lower() in IGNORED_SUFFIXES:
                continue
            rel = img_path.relative_to(IMGDIR)
            if img_path.name in referenciadas or str(rel) in referenciadas:
                continue
            itens.append(
                {
                    "image": img_path.name,
                    "path": img_path,
                    "post": None,  # sem post associado
                    "referenced": False,
                }
            )

    # Ordena por nome de arquivo da imagem (chave estável e legível).
    itens.sort(key=lambda it: (it["image"].lower(), it["post"] or ""))
    return itens


# ---------------------------------------------------------------------------
# Inspeção e preparo das imagens
# ---------------------------------------------------------------------------

def probe_image(path: Path) -> dict:
    """Lê dimensões reais e tamanho em KB. Nunca levanta exceção."""
    info = {"width": None, "height": None, "kb": 0.0, "error": None}
    try:
        info["kb"] = path.stat().st_size / 1024.0
    except OSError as exc:
        info["error"] = f"arquivo inacessível: {exc}"
        return info
    try:
        pm = fitz.Pixmap(str(path))  # lê só a estrutura para obter W/H
        info["width"], info["height"] = pm.width, pm.height
        del pm
    except Exception as exc:  # imagem corrompida, formato não suportado, etc.
        info["error"] = str(exc)
    return info


def make_thumbnail(path: Path, thumb_width: float):
    """Devolve um Pixmap reduzido para a miniatura (ou None em caso de erro).

    A redução usa `shrink(fator)` (fator inteiro, o único aceito no MuPDF).
    Nada é gravado em disco: o Pixmap é inserido direto no PDF.
    """
    try:
        pm = fitz.Pixmap(str(path))
    except Exception:
        return None

    try:
        # Descarta o canal alfa: evita fundo transparente virar preto no PDF.
        if pm.alpha:
            pm = fitz.Pixmap(pm, 0)
        # CMYK não é aceito diretamente por insert_image em todos os casos.
        if pm.colorspace is not None and pm.colorspace.n == 4:
            pm = fitz.Pixmap(fitz.csRGB, pm)
        # Alvo ~2x a largura exibida, para miniatura nítida em tela/impressão.
        alvo_px = max(1.0, thumb_width * 2.0)
        fator = int(round(pm.width / alvo_px))
        if fator > 1:
            pm.shrink(fator)
        return pm
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Desenho do PDF
# ---------------------------------------------------------------------------

def desenhar_cabecalho(page: fitz.Page, pagina: int, total: int, cols: int,
                       thumb_width: float, n_itens: int, apenas_posts: bool) -> float:
    """Escreve o cabeçalho da página e devolve o Y do topo da grade."""
    escopo = "somente posts" if apenas_posts else "posts + assets/img não referenciadas"
    page.insert_text(
        (MARGIN, MARGIN + 9),
        "Folha de contato - imagens de destaque",
        fontname="hebo",
        fontsize=12,
        color=COLOR_TEXT,
    )
    page.insert_text(
        (MARGIN, MARGIN + 22),
        f"{n_itens} imagens | {cols} colunas | miniatura {int(thumb_width)}pt | "
        f"padrao {STANDARD_W}x{STANDARD_H} | escopo: {escopo}",
        fontname="helv",
        fontsize=7.5,
        color=COLOR_MUTED,
    )
    page.insert_text(
        (PAGE_W - MARGIN - 60, MARGIN + 9),
        f"pagina {pagina}/{total}",
        fontname="helv",
        fontsize=9,
        color=COLOR_MUTED,
    )
    # Linha horizontal separando o cabeçalho da grade.
    page.draw_line(
        fitz.Point(MARGIN, MARGIN + HEADER_H - 6),
        fitz.Point(PAGE_W - MARGIN, MARGIN + HEADER_H - 6),
        color=COLOR_MUTED,
        width=0.5,
    )
    return MARGIN + HEADER_H


def dimensoes_thumb(thumb_w: float, info: dict) -> tuple[float, float]:
    """Devolve (largura, altura) da miniatura, sem distorcer a imagem.

    A largura-alvo é `thumb_w` e a altura é proporcional. Se a proporção for
    extrema a ponto de a altura passar de `MAX_THUMB_H`, ambos os lados são
    reduzidos pelo mesmo fator (a proporção original é preservada).
    """
    if info["width"] and info["height"]:
        proporcao = info["height"] / info["width"]
    else:
        proporcao = STANDARD_H / STANDARD_W  # caixa de aviso textual

    largura = thumb_w
    altura = thumb_w * proporcao
    if altura > MAX_THUMB_H:
        fator = MAX_THUMB_H / altura
        largura *= fator
        altura = MAX_THUMB_H
    return largura, altura


def altura_celula(thumb_w: float, info: dict) -> float:
    """Altura total da célula (miniatura + bloco de texto)."""
    _, thumb_h = dimensoes_thumb(thumb_w, info)
    return CELL_PAD * 2 + thumb_h + 4.0 + 3 * LINE_H


def desenhar_celula(page: fitz.Page, x: float, y: float, col_w: float, thumb_w: float,
                    item: dict, info: dict, pixmap) -> None:
    """Desenha uma célula: miniatura, textos e moldura."""
    celula = fitz.Rect(x, y, x + col_w, y + altura_celula(thumb_w, info))

    ilegivel = info["error"] is not None
    fora_padrao = (
        not ilegivel
        and (info["width"], info["height"]) != (STANDARD_W, STANDARD_H)
    )
    cor = COLOR_WARN if (ilegivel or fora_padrao) else COLOR_BORDER

    # Moldura fina em volta da célula.
    page.draw_rect(celula, color=cor, width=0.5 if not cor == COLOR_WARN else 0.9)

    img_x = x + CELL_PAD
    img_y = y + CELL_PAD

    # Geometria da miniatura (proporcional, com teto de altura).
    draw_w, draw_h = dimensoes_thumb(thumb_w, info)

    if ilegivel or pixmap is None:
        # Célula de aviso textual: não quebra o script nem o PDF.
        caixa = fitz.Rect(img_x, img_y, img_x + draw_w, img_y + draw_h)
        page.draw_rect(caixa, color=COLOR_WARN, width=0.4, fill=(0.99, 0.94, 0.92))
        page.insert_text((img_x + 4, img_y + 14), f"{WARN} imagem ilegivel",
                         fontname="hebo", fontsize=8, color=COLOR_WARN)
        msg = fit_text(info["error"] or "erro desconhecido", "helv", 6.5, max(20.0, draw_w - 8))
        page.insert_text((img_x + 4, img_y + 26), msg, fontname="helv", fontsize=6.5,
                         color=COLOR_WARN)
        text_y = caixa.y1 + 4 + NAME_SIZE
    else:
        # Miniatura proporcional (sem distorção), largura `thumb_w` ou menos.
        alvo = fitz.Rect(img_x, img_y, img_x + draw_w, img_y + draw_h)
        page.insert_image(alvo, pixmap=pixmap, keep_proportion=True)
        text_y = img_y + draw_h + 4 + NAME_SIZE

    # 1) Nome do arquivo em negrito (com a marca de aviso, quando aplicável).
    nome = f"{WARN} {item['image']}" if (ilegivel or fora_padrao) else item["image"]
    page.insert_text(
        (x + CELL_PAD, text_y),
        fit_text(nome, "hebo", NAME_SIZE, col_w - 2 * CELL_PAD),
        fontname="hebo",
        fontsize=NAME_SIZE,
        color=cor if (ilegivel or fora_padrao) else COLOR_TEXT,
    )

    # 2) Linha pequena: WxH, tamanho em KB e proporção com 3 casas.
    if info["width"] and info["height"]:
        proporcao = info["width"] / info["height"] if info["height"] else 0.0
        detalhe = (
            f"{info['width']}x{info['height']} | "
            f"{info['kb']:.1f} KB | {proporcao:.3f}"
        )
    else:
        detalhe = f"?x? | {info['kb']:.1f} KB | -"
    page.insert_text(
        (x + CELL_PAD, text_y + LINE_H),
        fit_text(detalhe, "helv", TEXT_SIZE, col_w - 2 * CELL_PAD),
        fontname="helv",
        fontsize=TEXT_SIZE,
        color=COLOR_MUTED,
    )

    # 3) Origem do item: nome do post ou "(não referenciada)".
    origem = item["post"] if item["referenced"] else "(não referenciada)"
    page.insert_text(
        (x + CELL_PAD, text_y + 2 * LINE_H),
        fit_text(origem, "helv", TEXT_SIZE, col_w - 2 * CELL_PAD),
        fontname="helv",
        fontsize=TEXT_SIZE,
        color=COLOR_MUTED,
    )


def gerar_pdf(itens: list[dict], infos: list[dict], out_path: Path, cols: int,
              thumb_width: float, apenas_posts: bool) -> int:
    """Monta o PDF em páginas A4 retrato. Devolve o número de páginas."""
    doc = fitz.open()
    largura_util = PAGE_W - 2 * MARGIN
    col_w = (largura_util - (cols - 1) * GUTTER) / cols
    thumb_w = min(thumb_width, col_w - 2 * CELL_PAD)  # nunca estoura a coluna

    # Agrupa os itens em linhas da grade.
    linhas = [list(range(i, min(i + cols, len(itens)))) for i in range(0, len(itens), cols)]
    if not linhas:
        page = doc.new_page(width=PAGE_W, height=PAGE_H)
        page.insert_text((MARGIN, MARGIN + 20), "Nenhuma imagem encontrada.",
                         fontname="hebo", fontsize=12, color=COLOR_TEXT)
        doc.save(str(out_path))
        doc.close()
        return 1

    # Calcula quantas páginas serão necessárias (para numerar "página X/Y").
    paginas_idx: list[list[list[int]]] = [[]]
    y = MARGIN + HEADER_H
    limite = PAGE_H - MARGIN
    for linha_idx in linhas:
        alt = max(altura_celula(thumb_w, infos[i]) for i in linha_idx)
        if y + alt > limite:
            paginas_idx.append([])
            y = MARGIN + HEADER_H
        paginas_idx[-1].append(linha_idx)
        y += alt + ROW_GAP
    total_paginas = len(paginas_idx)

    for num_pagina, pag_linhas in enumerate(paginas_idx, start=1):
        page = doc.new_page(width=PAGE_W, height=PAGE_H)
        desenhar_cabecalho(page, num_pagina, total_paginas, cols, thumb_w,
                           len(itens), apenas_posts)
        y = MARGIN + HEADER_H
        limite = PAGE_H - MARGIN

        for linha_idx in pag_linhas:
            alt = max(altura_celula(thumb_w, infos[i]) for i in linha_idx)

            # Linha-guia horizontal no topo de cada linha da grade, para o
            # revisor comparar alinhamento e proporção entre as imagens.
            page.draw_line(
                fitz.Point(MARGIN, y),
                fitz.Point(PAGE_W - MARGIN, y),
                color=COLOR_GUIDE,
                width=0.4,
            )

            for pos, idx in enumerate(linha_idx):
                x = MARGIN + pos * (col_w + GUTTER)
                item, info = itens[idx], infos[idx]
                pix = None
                if info["error"] is None:
                    pix = make_thumbnail(item["path"], thumb_w)
                    if pix is None:
                        # Pixmap falhou apesar do probe: marca como ilegível.
                        info = dict(info, error="miniatura não pôde ser gerada")
                desenhar_celula(page, x, y, col_w, thumb_w, item, info, pix)

            # Linha-guia no pé da linha, fechando a faixa.
            page.draw_line(
                fitz.Point(MARGIN, y + alt),
                fitz.Point(PAGE_W - MARGIN, y + alt),
                color=COLOR_GUIDE,
                width=0.4,
            )
            y += alt + ROW_GAP

    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(out_path))
    doc.close()
    return total_paginas


# ---------------------------------------------------------------------------
# Entrada principal
# ---------------------------------------------------------------------------

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Gera uma folha de contato em PDF para revisão das imagens de destaque.",
    )
    parser.add_argument("--out", default="/tmp/review_post_images.pdf",
                        help="PDF de saída (padrão: /tmp/review_post_images.pdf)")
    parser.add_argument("--cols", type=int, default=4,
                        help="número de colunas da grade (padrão: 4)")
    parser.add_argument("--thumb-width", type=float, default=220.0,
                        help="largura da miniatura em pontos (padrão: 220)")
    parser.add_argument("--only-posts", action="store_true",
                        help="inclui apenas imagens referenciadas por _posts/*.md")
    args = parser.parse_args(argv)
    if args.cols < 1:
        parser.error("--cols deve ser >= 1")
    if args.thumb_width <= 0:
        parser.error("--thumb-width deve ser > 0")
    return args


def main() -> int:
    args = parse_args()
    out_path = Path(args.out)

    # 1) Coleta os itens (posts + imagens não referenciadas, conforme o escopo).
    itens = collect_items(only_posts=args.only_posts)

    # 2) Inspeciona cada imagem (dimensões reais e tamanho em KB).
    infos = [probe_image(item["path"]) for item in itens]

    # 3) Monta o PDF.
    paginas = gerar_pdf(itens, infos, out_path, args.cols, args.thumb_width,
                        args.only_posts)

    # 4) Resumo no stdout.
    ilegiveis = [it for it, inf in zip(itens, infos) if inf["error"]]
    fora = [
        (it, inf)
        for it, inf in zip(itens, infos)
        if inf["error"] is None and (inf["width"], inf["height"]) != (STANDARD_W, STANDARD_H)
    ]

    print(f"total de imagens na folha de contato: {len(itens)}")
    print(f"fora do padrao {STANDARD_W}x{STANDARD_H}: {len(fora)}")
    print(f"ilegiveis (celula de aviso): {len(ilegiveis)}")
    print(f"paginas do PDF: {paginas}")
    print(f"PDF gerado: {out_path}")
    if fora:
        print("fora do padrao:")
        for it, inf in fora:
            origem = it["post"] if it["referenced"] else "(não referenciada)"
            print(f"  - {it['image']} ({inf['width']}x{inf['height']}) <- {origem}")
    if ilegiveis:
        print("ilegiveis:")
        for it in ilegiveis:
            print(f"  - {it['image']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())