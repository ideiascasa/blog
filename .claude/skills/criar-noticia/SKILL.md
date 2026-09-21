---
name: criar-noticia
description: Criar uma notícia em português do Brasil no blog
  a partir de um link, citando a fonte, extraindo autor e imagem.
  Também verifica (por julgamento, não por script) se a notícia já foi
  publicada antes de criar o post.
metadata:
  author: zot-blog
  version: "1.2"
---

# Skill: Criar Notícia no Blog

Quando o usuário pedir para criar uma notícia no blog a partir de uma URL, siga o workflow abaixo.

## Fluxo completo

> **Ordem importa:** execute o **passo 0 (verificação de duplicata) ANTES de tudo**.
> Nunca baixe imagem, traduza texto nem crie arquivo antes de saber que a notícia
> não foi publicada. O passo 0 é barato; publicar duplicata não tem desfazer fácil.
> A decisão de duplicata é **semântica** — leia os posts candidatos e julgue, não
> confie apenas em busca por texto.

### 0. Verificar se a notícia JÁ FOI PUBLICADA (obrigatório, primeiro passo)

Antes de qualquer outra coisa, verifique se a notícia já está no blog. **Não baixe imagem
nem escreva o post antes disso** — publicar duplicata não tem desfazer fácil.

> **O veredito é seu, por julgamento.** Comandos de busca servem apenas para **levantar
> candidatos** em `_posts/`. A decisão de "isto é a mesma notícia" é **semântica** e deve
> ser tomada lendo os candidatos — nunca delegue a decisão a um `grep` ou a um script.
> Igualdade de texto é só o caso mais óbvio; o caso perigoso é o que se parece diferente.

#### 0.1. Levantar candidatos (busca mecânica — só rascunho)

Rode a partir da raiz do repositório:

```bash
# mesma URL de fonte? (sem esquema, www, query, fragmento e barra final)
CHAVE=$(echo "<url>" | sed -e 's|^https*://||' -e 's|^www\.||' -e 's|?.*||' -e 's|#.*||' -e 's|/*$||')
grep -rn "$CHAVE" _posts/

# mesmo slug? (arquivo, com e sem data)
ls _posts/*<slug>* 2>/dev/null

# palavras-chave do assunto — nomes de empresas, produtos, pessoas, eventos
# é aqui que se acham duplicatas que NÃO compartilham a URL
for t in "<entidade-1>" "<entidade-2>" "<entidade-3>"; do
  grep -ril "$t" _posts/ 2>/dev/null
done | sort -u

# quem publicou por último neste blog (contexto do que é recente)
ls -t _posts/ | head -15
```

#### 0.2. Julgar (a parte que a IA faz)

Para **cada candidato** retornado, leia o `title` e a **primeira linha do corpo** do arquivo
(e o rodapé de fonte, se existir) e responda a estas perguntas:

1. **Mesma matéria?** Os dois posts cobrem *o mesmo fato* — o mesmo anúncio, o mesmo
   incidente, o mesmo estudo, o mesmo lançamento?
2. **Mesma origem editorial?** O texto deriva do mesmo artigo-fonte, mesmo quando a URL é
   outra (sindicagem, republicação, mesmo *press release* distribuído a vários veículos)?
3. **Mesmo recorte?** Ou são fatos distintos que apenas compartilham empresas ou tema?

**Considere duplicata quando: o fato central é o mesmo E o post novo não acrescenta
ângulo, dados ou análise.** Mesmo com URL diferente, dois posts que traduzem o mesmo
anúncio de fornecedor são duplicata.

**Não é duplicata** (e não deve ser bloqueado) quando:

- o post existente apenas **cita** a mesma empresa, modelo ou referência em outro contexto;
- o fato é **novo** mas o tema é recorrente (ex.: *a coletânea semanal de produtos* muda a
  cada semana — mesmo domínio, URLs e conteúdo diferentes = post novo legítimo);
- o post novo **aprofunda ou analisa** o que o existente só noticiou — aí vale seguir como
  *actualização* ou oferecer a expansão do post antigo.

#### 0.3. Decidir

**Se for duplicata, NÃO crie um `_posts/` novo.** Avise o usuário, diga qual post já cobre
o fato, explique por que você considera duplicata e ofereça as opções:

1. **Manter como está** — o conteúdo já está no ar; nada a fazer.
2. **Expandir o post existente** — acrescentar seções/ângulo novo ao arquivo já publicado.
3. **Criar um ângulo realmente novo** — só se o usuário confirmar; use slug diferente
   (ex.: `<slug>-analise-critica`) e deixe claro no texto que deriva da mesma fonte.

**Não decida sozinho por criar um post novo**, e **não decida sozinho por bloquear** quando
houver dúvida — dúvida é motivo para perguntar, não para presumir.

**Registre a conclusão em uma linha** (ex.: `Duplicata verificada em 2026-09-13: candidatos
A, B lidos; mesma notícia de SEP-11 = duplicata` ou `sem correspondência, tema novo`) logo
antes do passo 1, para que o raciocínio fique auditável.

#### 0.4. Exemplo de julgamento (caso real deste blog)

Buscar `"agentes de IA"` em `_posts/` retorna vários candidatos, entre eles:

- `2026-09-09-agentes-ia-soc-credenciais.md` — Zscaler lança SOC agêntico
- `2026-09-11-identidade-agentes-ia.md` — coletânea semanal de produtos (Akeyless, Orchid, Scytale, Securin)

**Isto NÃO é duplicata.** Mesmo tema, mesmas semanas, mesmas expressões de busca — mas são
**fatos diferentes** (um lançamento específico vs. uma rodada de anúncios). Bloquear por
coincidência de palavras-chave seria falso positivo.

Compare com o caso que **é** duplicata: reapresentar a URL
`helpnetsecurity.com/2026/09/11/new-infosec-products-of-the-week-september-11-2026`
identifica o **mesmo fato** já publicado — aí sim, pare.

A diferença não está no texto da busca: está em **ler os dois posts e julgar o fato**.

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

### 2.1. Normalizar a imagem para 1024x600 (obrigatório, sem exceção)

**Toda imagem de destaque deste blog tem exatamente 1024x600 px** — a proporção da
referência `assets/img/spools.jpg`. Nenhum post pode ser publicado com imagem em outra
medida, seja porque o download veio em outra proporção ou porque o arquivo é reaproveitado.

```bash
# ajusta o conteúdo, preservando nome e caminho do arquivo (cover fit, corte central)
scripts/normalize_post_image.sh assets/img/<slug>-featured.png
```

Regras:

- **Escopo: só a imagem de capa.** Imagens usadas **dentro** do corpo do post
  (`![...](assets/img/x.png)`) **não** são cortadas para 1024x600 — há diagramas verticais
  no acervo (ex.: `f2c2076f.png`, 784x3000) que seriam destruídos. Para essas, apenas
  preserve a proporção; o CSS (`img { max-width: 100% }`) já limita a largura.
- **Cover fit, nunca distorção**: redimensiona proporcionalmente e corta o excesso no
  centro. Não estique, não comprima e **não** coloque barras/letterbox.
- **Preserve o nome do arquivo** — ele faz parte da URL publicada. Normalizar é sobrescrever
  o conteúdo; nunca renomeie para `...-1024x600.png`.
- Escolha na origem uma imagem **paisagem e com pelo menos 1024 px de largura** (ideal
  1600 px ou mais). Imagens menores são ampliadas e perdem nitidez.
- Ao usar imagem que **já existe** em `assets/img` (reaproveitada de outro post), normalize
  antes: pode estar fora do padrão.
- Ao final, confirme o resultado:

  ```bash
  sips -g pixelWidth -g pixelHeight assets/img/<slug>-featured.png   # deve dizer 1024 e 600
  ```

- O `sips` **não grava WebP**. Se a imagem baixada for `.webp`, o script converte o conteúdo
  para JPEG **mantendo o mesmo nome** — o arquivo continua servido normalmente, então o
  `image:` do post continua igual. Prefira baixar em `.jpg`/`.png` quando possível.

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
image: <slug>-featured.png   # arquivo 1024x600 obrigatoriamente (ver passo 2.1)
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

### 4. Revisão de formatação (obrigatório antes do commit)

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

### 4.1. Reverificação do padrão de imagem (obrigatório antes do commit)

Rode o auditor do repositório e garanta que ele termina com **exit code 0**:

```bash
scripts/check_post_images.sh
```

O script (somente leitura) lista todos os posts com a imagem declarada, as dimensões reais
em `assets/img/` e o status de cada uma. Qualquer linha `DIVERGENTE`, `AUSENTE` ou
`SEM IMAGEM` significa post fora do padrão: rode `scripts/normalize_post_image.sh` no
arquivo indicado e verifique de novo. **Não commite enquanto o auditor não retornar OK.**

Para conferir visualmente antes de publicar (folha de contato em PDF, com miniaturas e
dimensões, destacando o que está fora do padrão):

```bash
python3 scripts/review_post_images.py   # grava /tmp/review_post_images.pdf
```

### 5. Reverificação de duplicata (obrigatório antes do commit)

O passo 0 julgou o *título e slug propostos*. Se o título, o slug, a URL de fonte ou o
**recorte da notícia** mudaram durante a redação, o julgamento pode ter ficado
desatualizado. **Repita o passo 0 inteiro** — candidatos e julgamento — com os valores finais.

Só prossiga para o commit se você concluir que é notícia nova. Se no meio da redação você
perceber que o post ficou muito próximo de outro já publicado, volte ao passo 0.3 e ofereça
as opções ao usuário — não commite por conta própria.

### 6. Commit e push

Após criar os arquivos (e só depois do passo 5 retornar `OK`):

```bash
git add _posts/<data>-<slug>.md assets/img/<slug>-featured.png
git commit -m "Novo post: <título>"
git push
```

O `git status` deste ponto em diante não pode mostrar imagens modificadas — se mostrar, é
sinal de que alguma imagem ainda está fora de 1024x600 (rode o passo 4.1 de novo).

## Regras obrigatórias

- Todo o conteúdo do post deve ser em **português do Brasil**
- **Cite a fonte** no rodapé (URL original, domínio, autor)
- **Atribua a imagem** no rodapé (artista, fonte, licença)
- Siga o formato dos posts existentes em `_posts/`
- **Toda imagem de destaque tem exatamente 1024x600 px** (proporção da referência
  `assets/img/spools.jpg`), sempre por cover fit — nunca esticada, nunca com barras
- **Nunca renomeie a imagem para ajustar o padrão**: preserve o nome (a URL é pública) e
  sobrescreva só o conteúdo, com `scripts/normalize_post_image.sh`
- **Valide com `scripts/check_post_images.sh` (exit 0) antes de commit/push**
- Use a data atual no nome do arquivo (YYYY-MM-DD)
- **Categorias e tags devem ser dinâmicas**, analisando o conteúdo do artigo — nunca use valores fixos
- Reaproveite tags existentes sempre que possível para criar relacionamento entre posts
- Use Swarm para executar multiplas tarefas
- **Nunca publique a mesma notícia duas vezes** — julgue no passo 0 e reavalie no passo 5
- **A verificação de duplicata é um julgamento, não um `grep`**: buscas mecânicas apenas
  levantam candidatos; a decisão é ler os posts e comparar o fato, o recorte e a origem
- **Duplicata não é só slug repetido**: a mesma notícia publicada duas vezes gera
  duplicata no site, no índice e no feed RSS, mesmo com arquivos, URLs e títulos diferentes
- **Duplicata semântica também conta**: o mesmo anúncio ou *press release* republicado por
  outro veículo é a mesma notícia — compare o fato relatado, não apenas o link
- Em caso de **dúvida**, pergunte ao usuário — não decida sozinho nem por criar, nem por bloquear
- Se concluir que é duplicata, **pare e pergunte** antes de escrever qualquer arquivo