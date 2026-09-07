---
name: criar-noticia
description: Criar uma notícia em português do Brasil no blog
  a partir de um link, citando a fonte, extraindo autor e imagem.
metadata:
  author: zot-blog
  version: "1.0"
---

# Skill: Criar Notícia no Blog

Quando o usuário pedir para criar uma notícia no blog a partir de uma URL, siga o workflow abaixo.

## Fluxo completo

### 1. Obter conteúdo da URL

Use a ferramenta `openrouter_web_fetch` para navegar até a URL fornecida pelo usuário e obter o conteúdo completo da página, incluindo título, autor(es) e data de publicação.

Se não conseguir identificar o autor, use **"autor bot"**.

### 2. Encontrar imagem destacada

Use `openrouter_web_search` para encontrar uma imagem relevante e livre de direitos sobre o tema do artigo.

Downloads possíveis:
- **Unsplash** (https://unsplash.com) — use a API de download direto: `https://unsplash.com/photos/<id>/download?force=true`
- **Pexels** (https://www.pexels.com)
- **Better Images of AI** (https://betterimagesofai.org) — imagens CC-BY

Baixe a imagem com `curl -L -o assets/img/<slug>-featured.png <url>`.

### 3. Criar o post em markdown

Crie o arquivo em `_posts/<data>-<slug>.md` seguindo este formato exato.

#### 3.0.1. Categorias e tags dinâmicas (obrigatório)

Analise o conteúdo do artigo e determine **categorias e tags relevantes** para conectar este post com outros do blog. Não use valores fixos.

**Categorias** disponíveis no blog (use a mais adequada):
- `blog` — artigos, notícias, análises, tutoriais
- `case` — estudos de caso

**Tags** — escolha tags específicas do conteúdo, usando sempre tags já existentes no blog quando fizerem sentido, para criar relacionamento entre posts:

Tags existentes: `ai`, `analise`, `ia`, `privacidade`, `seguranca`, `tecnologia`, `sec`, `browser`, `agentes-ia`, `ai-agents`, `conformidade`, `regulacao`, `sample`, `spring-boot`, `junie`

**Regras:**
- Sempre inclua `blog` ou `case` como **primeira tag** (correspondendo à categoria)
- Inclua `ia` como tag se o artigo mencionar inteligência artificial
- Inclua `analise` se o artigo fizer análise comparativa ou review
- Use no mínimo 2 e no máximo 8 tags
- Crie **novas tags** em português, no singular, com hífen para separar palavras (ex: `rede-neural`, `ciberseguranca`, `privacidade-dados`) quando o tema não se encaixar nas tags existentes

Exemplos:
- Artigo sobre IA e cibersegurança → `categories: blog` / `tags: [blog,ia,seguranca,tecnologia]`
- Artigo sobre ferramentas SAST → `categories: blog` / `tags: [blog,sec,analise]`

```markdown
---
layout: post
title: "<título traduzido>"
author: "<autor extraído ou 'autor bot'>"
categories: <categoria>
tags: [<tag1>,<tag2>,...]
image: <slug>-featured.png
---

<conteúdo do artigo em português do Brasil>

---

> **Fonte original:** [<título original>](<url>) - <domínio>, por <autor>.
>
> **Imagem:** <descrição da imagem> por <artista>, via [<fonte>](<url da fonte>), licenciada sob [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (ou licença aplicável).
```

### 3.1. Menção ao ranking de IA (obrigatório para artigos sobre IA)

Se o artigo for sobre **inteligência artificial**, **modelos de IA**, **ferramentas de IA** ou qualquer tema relacionado, você **deve incluir o link** `https://blog.ideias.casa/melhores-ia` no post.

**Prioridade:** encaixe o link no **melhor lugar possível dentro do texto**, de forma natural e contextual — por exemplo, ao mencionar comparações entre modelos, ao falar sobre escolha de ferramentas de IA, ou ao concluir uma seção que lista múltiplos modelos.

👉 **Exemplo de encaixe natural:**
> "Para quem busca se orientar nesse cenário de rápida evolução, nossa [análise comparativa dos melhores modelos de IA](https://blog.ideias.casa/melhores-ia) acompanha e avalia as principais opções disponíveis no mercado."

Insira, tambem, o link ao final do post, após o rodapé da fonte e imagem:

```markdown
---

👉 **Veja também nossa análise comparativa dos melhores modelos de IA em:** [blog.ideias.casa/melhores-ia](https://blog.ideias.casa/melhores-ia)
```

### 4. Commit e push

Após criar os arquivos:

```bash
git add _posts/<data>-<slug>.md assets/img/<slug>-featured.png
git commit -m "Novo post: <título>"
git push
```

## Regras obrigatórias

- Todo o conteúdo do post deve ser em **português do Brasil**
- **Cite a fonte** no rodapé (URL original, domínio, autor)
- **Atribua a imagem** no rodapé (artista, fonte, licença)
- Siga o formato dos posts existentes em `_posts/`
- Use a data atual no nome do arquivo (YYYY-MM-DD)
- **Categorias e tags devem ser dinâmicas**, analisando o conteúdo do artigo — nunca use valores fixos
- Reaproveite tags existentes sempre que possível para criar relacionamento entre posts
- Use Swarm para executar multiplas tarefas

### 3.5. Revisão de formatação (obrigatório antes do commit)

Antes de fazer commit, **revise o arquivo do post** verificando os seguintes pontos:

1. **Caracteres especiais corrompidos** — verifique se não há caracteres Unicode quebrados (como travessões `—` transformados em `e2 80 94` não interpretados, ou hífens `‑` aparecendo como `e2 80 91`). Use travessão padrão `—` (U+2014, HTML `&mdash;`) ou hífen comum `-`.
2. **Anglicismos** — substitua termos como "unprecedented" por "sem precedentes", "endurecido" por "protegido" (quando não for jargão técnico), etc.
3. **Símbolo de cifrão (`$`) — nunca use `$` ou `US$` no markdown do post**, pois o cifrão conflita com a sintaxe matemática/LaTeX do Jekyll (pode renderizar como "US
10
p
o
r
"). Em vez disso, **escreva o nome da moeda por extenso**: "10 dólares", "50 dólares", etc. Se o artigo não deixar clara a moeda, assuma "dólares".
4. **Preços numéricos** — verifique se números com unidades não estão quebrados em linhas separadas.
5. **Hífens e travessões** — use `—` (travessão) para separar orações, não hífen simples `-`.
6. **Leia o post completo em voz alta no terminal** (ou mentalmente) para detectar problemas de fluxo ou quebra de linha inesperada.

Se encontrar problemas, corrija-os antes de prosseguir para o commit.

### 6. Verificação de colisão de slug

Antes de criar o arquivo, verifique se já existe um post com slug semelhante no diretório `_posts/`:

```bash
ls _posts/*<slug>* 2>/dev/null || echo "slug livre"
```

Se houver colisão, use um slug diferente (ex: adicione um sufixo descritivo como `-ciberseguranca-critico`).