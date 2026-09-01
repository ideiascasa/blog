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

Crie o arquivo em `_posts/<data>-<slug>.md` seguindo este formato exato:

```markdown
---
layout: post
title: "<título traduzido>"
author: "<autor extraído ou 'autor bot'>"
categories: blog
tags: [blog,ia,tecnologia,privacidade]
image: <slug>-featured.png
---

<conteúdo do artigo em português do Brasil>

---

> **Fonte original:** [<título original>](<url>) - <domínio>, por <autor>.
>
> **Imagem:** <descrição da imagem> por <artista>, via [<fonte>](<url da fonte>), licenciada sob [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (ou licença aplicável).
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
- Use Swarm para executar multiplas tarefas