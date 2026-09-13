#!/usr/bin/env python3
"""
Verificador de duplicatas para o blog (skill criar-noticia).

Checa, antes de criar um post, se a notícia já foi publicada, comparando:
  1. URL da FONTE ORIGINAL (rodape do post), normalizada
  2. Titulo semelhante (fuzzy, sem acentos/pontuacao)
  3. Colisao de slug (nome de arquivo)
  4. Imagem destacada reutilizada

IMPORTANTE: apenas a URL do rodape "Fonte original" / "Fontes originais" entra na
comparacao. Links do corpo do texto (referencias, videos, artigos citados) e links de
boilerplate (ranking de IA, licencas Creative Commons/Pexels) sao ignorados — senao
todo post que cita a mesma referencia seria marcado como duplicata.

Uso:
    python3 verificar-duplicata.py --url "<url fonte>" [--slug "<slug>"] [--titulo "<titulo>"]
    python3 verificar-duplicata.py --listar
    python3 verificar-duplicata.py --auditar      (varre todos os posts e acha fontes repetidas)

Codigos de saida:
    0 = livre, pode criar o post
    1 = DUPLICATA detectada, NAO criar (ou criar com angulo/slug diferente)
    2 = erro de uso
"""

import argparse
import difflib
import glob
import os
import re
import sys
import unicodedata
from collections import defaultdict

POSTS_DIR = os.environ.get("POSTS_DIR", "_posts")
LIMIAR_TITULO = 0.80

# Dominios/URLs que aparecem em varios posts de forma legitima (boilerplate, licencas).
# Nunca contam como "fonte duplicada".
BOILERPLATE = {
    "blog.ideias.casa/melhores-ia",
    "creativecommons.org/licenses/by/4.0",
    "pexels.com/license",
    "unsplash.com/license",
    "betterimagesofai.org/images",
}


def normalizar_url(url):
    """Normaliza URL: sem esquema, www, query, fragmento e barra final."""
    if not url:
        return ""
    u = url.strip().lower()
    u = re.sub(r"^https?://", "", u)
    u = re.sub(r"^www\.", "", u)
    u = u.split("#")[0]
    u = u.split("?")[0]
    u = u.rstrip("/")
    u = re.sub(r"/+", "/", u)
    return u


def url_boilerplate(url_norm):
    """True se a URL e boilerplate/licenca (nunca conta como fonte duplicada)."""
    if not url_norm:
        return True
    if url_norm in BOILERPLATE:
        return True
    # licencas Creative Commons em qualquer idioma/versao
    if re.match(r"^creativecommons\.org/licenses/", url_norm):
        return True
    # paginas de licenca dos bancos de imagem
    if re.match(r"^(pexels|unsplash|pixabay|freepik)\.com/(license|licenses)", url_norm):
        return True
    return False


def normalizar_texto(s):
    """Minusculas, sem acentos, sem pontuacao — para comparacao fuzzy de titulos."""
    if not s:
        return ""
    s = s.lower()
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return " ".join(s.split())


def campo(texto, nome):
    m = re.search(r'^%s:\s*["\']?(.*?)["\']?\s*$' % nome, texto, re.M)
    return m.group(1).strip() if m else ""


def extrair_fontes(texto):
    """
    Extrai as URLs do rodape de fonte. Suporta os dois formatos usados no blog:

      > **Fonte original:** [Titulo](https://...) - dominio, por autor.

      > **Fontes originais:**
      > - [Titulo](https://...) — dominio, por autor.
      > - [Titulo](https://...) — dominio, por autor.

    A URL pode estar tanto na propria linha do cabecalho ('> **Fonte original:**')
    quanto nas linhas seguintes, por isso coletamos a partir do cabecalho inclusive.
    O bloco termina no fim da citacao (linha sem '>'), no '**Imagem:**' ou num separador.
    """
    fontes = set()
    dentro = False
    for linha in texto.splitlines():
        l = linha.strip()
        if not dentro:
            if re.match(r"^>\s*\*\*Fontes?\s+origina", l, re.I):
                dentro = True
                # nao usar 'continue': a URL pode estar nesta mesma linha
            else:
                continue
        elif not l.startswith(">"):
            break  # fim da citacao

        if l.startswith(">"):
            m_imagem = re.match(r"^>\s*\*\*Imagem", l, re.I)
            m_sep = re.match(r"^>\s*-{3,}\s*$", l)
            if m_imagem or m_sep:
                break

        for m in re.finditer(r"\((https?://[^)\s]+)\)", l):
            u = normalizar_url(m.group(1))
            if u and not url_boilerplate(u):
                fontes.add(u)
    return fontes


def carregar_posts():
    posts = []
    for caminho in sorted(glob.glob(os.path.join(POSTS_DIR, "*.md"))):
        try:
            texto = open(caminho, encoding="utf-8").read()
        except OSError as e:
            print("AVISO: nao foi possivel ler %s (%s)" % (caminho, e), file=sys.stderr)
            continue

        posts.append({
            "caminho": caminho,
            "arquivo": os.path.basename(caminho),
            "titulo": campo(texto, "title"),
            "autor": campo(texto, "author"),
            "imagem": campo(texto, "image"),
            "fontes": extrair_fontes(texto),
        })
    return posts


def listar(posts):
    print("POSTS EM %s/ (%d arquivos)\n" % (POSTS_DIR, len(posts)))
    sem_rodape = 0
    for p in posts:
        print("- %s" % p["arquivo"])
        print("    titulo: %s" % (p["titulo"] or "(sem titulo)"))
        print("    autor:  %s" % (p["autor"] or "(sem autor)"))
        if p["fontes"]:
            for u in sorted(p["fontes"]):
                print("    fonte:  %s" % u)
        else:
            sem_rodape += 1
            print("    fonte:  (nenhum rodape 'Fonte original' encontrado)")
    print("\nPosts sem rodape de fonte: %d de %d" % (sem_rodape, len(posts)))


def auditar(posts):
    """Varre todos os posts e reporta fontes citadas por mais de um post."""
    por_fonte = defaultdict(list)
    for p in posts:
        for u in p["fontes"]:
            por_fonte[u].append(p["arquivo"])

    repetidas = {u: f for u, f in por_fonte.items() if len(f) > 1}

    print("AUDITORIA DE DUPLICATAS EM %s/ (%d posts)\n" % (POSTS_DIR, len(posts)))
    if not repetidas:
        print("Nenhuma fonte citada por mais de um post. OK.")
        return 0

    print("FONTES CITADAS POR MAIS DE UM POST (%d)\n" % len(repetidas))
    for u in sorted(repetidas, key=lambda x: (-len(repetidas[x]), x)):
        print("- %s" % u)
        for arquivo in sorted(repetidas[u]):
            print("      %s" % arquivo)
    print("\nCada grupo acima e uma duplicata potencial: confirme se e o mesmo")
    print("artigo-fonte republicado, ou se sao posts derivados legitimamente.")
    return 1


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--url", help="URL da fonte do novo post")
    ap.add_argument("--slug", help="slug proposto (sem data e sem .md)")
    ap.add_argument("--titulo", help="titulo traduzido proposto")
    ap.add_argument("--listar", action="store_true", help="listar todos os posts e suas fontes")
    ap.add_argument("--auditar", action="store_true", help="varrer todos os posts e achar fontes repetidas")
    args = ap.parse_args()

    posts = carregar_posts()

    if args.auditar:
        return auditar(posts)

    if args.listar:
        listar(posts)
        return 0

    if not args.url and not args.slug and not args.titulo:
        ap.error("informe --url, --slug e/ou --titulo (ou use --listar / --auditar)")

    problemas = []
    url_alvo = normalizar_url(args.url) if args.url else None

    # --- 1: mesma fonte no rodape ---
    if url_alvo:
        if url_boilerplate(url_alvo):
            print("AVISO: a URL informada e boilerplate/licenca (%s)." % url_alvo)
            print("       Ela nao e tratada como fonte e nao sera verificada.\n")
        else:
            mesmas = [p for p in posts if url_alvo in p["fontes"]]
            if mesmas:
                problemas.append(("URL DA FONTE JA PUBLICADA", mesmas))

    # --- 2: titulo semelhante ---
    if args.titulo:
        alvo = normalizar_texto(args.titulo)
        parecidos = []
        for p in posts:
            t = normalizar_texto(p["titulo"])
            if not t:
                continue
            r = difflib.SequenceMatcher(None, alvo, t).ratio()
            if r >= LIMIAR_TITULO:
                parecidos.append((r, p))
        if parecidos:
            parecidos.sort(key=lambda x: -x[0])
            problemas.append(("TITULO SEMELHANTE",
                              [p for _, p in parecidos],
                              ["%.0f%%" % (r * 100) for r, _ in parecidos]))

    # --- 3: colisao de slug ---
    slug_norm = None
    if args.slug:
        slug_norm = normalizar_texto(args.slug).replace(" ", "-")
        colisoes = [p for p in posts if slug_norm and slug_norm in p["arquivo"]]
        if colisoes:
            problemas.append(("SLUG COLIDE COM POST EXISTENTE", colisoes))

    # --- 4: imagem destacada reutilizada ---
    if slug_norm:
        imagem = "%s-featured.png" % slug_norm
        usam = [p for p in posts if p["imagem"] == imagem]
        if usam:
            problemas.append(("IMAGEM DESTACADA JA USADA", usam))

    if not problemas:
        print("OK — nenhuma duplicata encontrada.")
        print("   Posts verificados: %d" % len(posts))
        if url_alvo:
            print("   URL normalizada:   %s" % url_alvo)
        print("\nPode criar o post.")
        return 0

    print("=" * 68)
    print("DUPLICATA DETECTADA — NAO CRIE UM POST NOVO SEM RESOLVER ISTO")
    print("=" * 68)

    for item in problemas:
        tipo, posts_alvo = item[0], item[1]
        extras = item[2] if len(item) > 2 else None
        print("\n[%s]" % tipo)
        for i, p in enumerate(posts_alvo):
            sufixo = "  (similaridade %s)" % extras[i] if extras else ""
            print("   - %s%s" % (p["arquivo"], sufixo))
            if p["titulo"]:
                print("       titulo: %s" % p["titulo"])
            if url_alvo and url_alvo in p["fontes"]:
                print("       fonte:  %s" % url_alvo)

    print("\n" + "-" * 68)
    print("Como resolver:")
    print("  1. Se a fonte JA foi publicada: NAO crie um post novo.")
    print("     Avise o usuario e pergunte se quer (a) manter como esta,")
    print("     (b) EXPANDIR o post existente, ou (c) criar um angulo")
    print("     realmente novo com slug diferente.")
    print("  2. Se e apenas colisao de slug: escolha outro slug, ex.:")
    print("     <slug>-analise-critica, <slug>-ciberseguranca-critico")
    print("  3. Se a imagem ja foi usada: baixe outra imagem destacada.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
