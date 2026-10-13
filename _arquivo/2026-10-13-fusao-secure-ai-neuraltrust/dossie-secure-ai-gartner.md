# Dossiê — "Gartner Hype Cycle for Secure AI, 2026"

**Objeto:** relatório *Gartner Hype Cycle for Secure AI, 2026* — primeira edição; publicado em **12 de outubro de 2026**; analistas **Jeremy D'Hoinne, Dionisio Zumerle e Jeff Arias**; ID **G00846820**.
**Documento (página oficial):** https://www.gartner.com/en/documents/8487445
**Data da apuração:** 13 de outubro de 2026.
**Nota metodológica:** a página da Gartner devolve **HTTP 403** a scraping direto (`curl`, `ketch scrape`). Não há snapshot no Wayback Machine para `/en/documents/8487445` nem para `/en/reviews/market/ai-application-security` (consultado em 13/10/2026). Portanto, **todo conteúdo atribuído ao relatório neste dossiê vem de terceiros que o citam** — nunca de leitura direta do original. Isso está sinalizado em cada item.

**Status de verificação:** existem hoje duas fontes de fornecedor que descrevem este Hype Cycle (NeuralTrust e Akto) e **nenhuma fonte de imprensa independente** localizada. O relatório tem menos de 48 horas de publicado, o que explica — mas não elimina — a lacuna.

---

## 1. Reportagem independente da imprensa especializada

**NÃO ENCONTRADO.**

Busquei — sem resultado — por cobertura editorial específica do *Hype Cycle for Secure AI, 2026* em SecurityWeek, Help Net Security, CSO Online, The Register, Infosecurity Magazine e Dark Reading, usando `ketch search` (backend padrão e `--multi=exa`), `openrouter_web_search` e checagem de HTTP. Os veículos apareceram apenas em matérias *adjacentes* (mercado de segurança de IA, Hype Cycles anteriores), nunca sobre este relatório.

Registro das buscas vazias (títulos dos resultados mais próximos, nenhum sobre o Hype Cycle for Secure AI):

- **[SecurityWeek]** — "AI and Cybersecurity – Everything You Wanted to Know, But Were Afraid to Ask" — 16/06/2026 — https://www.securityweek.com/ai-and-cybersecurity-everything-you-wanted-to-know-but-were-afraid-to-ask/ — cobertura geral de segurança de IA; **não menciona** o Hype Cycle for Secure AI.
- **[Help Net Security]** — "Gartner predicts the technologies set to transform 2026" — 23/10/2025 — https://www.helpnetsecurity.com/2025/10/23/gartner-2026-technology-trends/ — Hype Cycle de Tendências Tecnológicas 2026, não o de Secure AI.
- **[Computing]** — "Gartner: AI is changing cybersecurity faster than cloud ever did" — 30/09/2026 — https://www.computing.co.uk/news/2026/ai/ai-is-changing-cybersecurity-faster-than-cloud-ever-did — matéria da Gartner sobre IA em cibersegurança (não o Hype Cycle for Secure AI); **HTTP 403** à tentativa de leitura, portanto cito apenas título/URL/data da indexação.
- **[Infosecurity Magazine]** — "AI Issues Will Drive Half of Incident Response Efforts by 2028, Says Gartner" — https://www.infosecurity-magazine.com/news/ai-issues-half-incident-response — cobertura de previsão da Gartner, não do Hype Cycle.

**Conclusão:** a única divulgação substantiva deste relatório, até o momento, é **de fornecedores que se declaram listados** (ver item 2), com interesse comercial direto no enquadramento.

---

## 2. "Sample Vendors" — quem são e quantos

**Fonte primária (interessada):** a NeuralTrust é a única fonte que publica a **lista nominal completa** da categoria AI Runtime Defense. É parte com interesse direto (se declara listada), logo o dado precisa dessa ressalva.

- **[NeuralTrust]** — "Named Sample Vendor in Hype Cycle for AI-Driven Cybersecurity" — NeuralTrust Team, 13/10/2026 — https://neuraltrust.ai/news/gartner-hype-cycle-for-ai-driven-cybersecurity-2026 — trecho literal: *"NeuralTrust is one of ten Sample Vendors listed by Gartner in the AI Runtime Defense category across both reports. The full list includes Akto, Check Point Software Technologies, F5, HiddenLayer, Lasso, Noma Security, Pillar Security, SentinelOne, and TrojAI."*

Interpretação do trecho: **10 fornecedores no total**, sendo nove nomeados explicitamente (Akto, Check Point Software Technologies, F5, HiddenLayer, Lasso, Noma Security, Pillar Security, SentinelOne, TrojAI) **mais a própria NeuralTrust**. A NeuralTrust diz que essa lista de dez vale "nos dois relatórios" (Secure AI **e** AI-Driven Cybersecurity — ver item 6). "one of ten" + 9 nomes + NeuralTrust = 10, consistente.

**Atributos públicos da categoria AI Runtime Defense** (mesma reportagem, seção "TL;DR", referindo-se ao Hype Cycle for Secure AI):

- **[NeuralTrust]** — "Named Sample Vendor in Hype Cycle for Secure AI" — NeuralTrust Team, 13/10/2026 — https://neuraltrust.ai/news/gartner-hype-cycle-for-secure-ai-2026 — trecho literal: *"NeuralTrust is listed as a **Sample Vendor in AI Runtime Defense**, one of ten vendors in a category rated High benefit, 5-20% market penetration, and Emerging maturity"* e *"AI Runtime Defense is positioned at the **Peak of Inflated Expectations**, the point of maximum visibility and investment concentration"*.

**Confirmações independentes parciais** (cada fornecedor citando-se, em *outros* relatórios da Gartner — evidência de que o padrão de listagem "Sample Vendor" se repete, mas **não** confirmação da lista deste relatório):

- **[Akto]** — "Akto Named a Sample Vendor for AI Runtime Defense in the 2026 Gartner® Hype Cycle™ for AI Governance Technologies" — Krishanu, 18/08/2026 — https://www.akto.io/blog/akto-in-gartner-hype-cycle-ai-governance-2026 — trecho literal: *"Akto is listed as a Sample Vendor for AI Security Testing, alongside Adversa AI, Check Point Software, Enkrypt AI, F5, HiddenLayer, Mindgard, Palo Alto Networks, Pillar Security, and SentinelOne."* (Nota: essa lista é da categoria **AI Security Testing**, no Hype Cycle for AI Services 2026 — não da categoria AI Runtime Defense deste relatório. Serve como evidência de método, não como fonte da lista do item 2.)
- **[Pillar Security]** — publica em LinkedIn que foi listada em **AI Runtime Defense** e **AI Security Testing** no *Hype Cycle for Application Security, 2026* (outro relatório) — https://www.linkedin.com/posts/pillarsecurity_we-are-excited-to-be-recognized-as-a-sample-activity-7486389848434589697-myT9 — trecho literal: *"We are excited to be recognized as a Sample Vendor in the 2026 Gartner® Hype Cycle™ for Application Security, in both AI Security Testing and AI Runtime Defense!"*
- **[Lasso]** — "Lasso Named in Gartner's Hype Cycle for Artificial Intelligence, 2026" — 14/09/2026 — https://www.lasso.security/blog/lasso-named-in-gartners-hype-cycle-for-artificial-intelligence-2026 — trecho literal: *"Lasso is named as a sample vendor under AI Governance Technologies, alongside Boomi, Databricks, Google, IBM, Microsoft, OneTrust, ServiceNow, and Zenity."* (Hype Cycle distinto.)
- **[Zenity]** — "Zenity Named in Two Categories in the 2026 Gartner® Hype Cycle™ for Agentic AI" — 15/04/2026 — https://zenity.io/company-overview/newsroom/company-news/zenity-named-in-two-categories-in-the-2026-gartner-r-hype-cycle-tm-for-agentic-ai — listada em *Guardian Agents* e *Agentic AI Security* (Hype Cycle distinto).

**Sobre "quantos fornecedores a categoria tem":** o único número público localizado é *"ten"*, da NeuralTrust (item acima). **Não há segunda fonte independente** que confirme o número.

**Sobre os fornecedores que você citou como hipótese:** Akto, Lasso, HiddenLayer e SentinelOne **aparecem** na lista da NeuralTrust; **Lakera, Protect AI, Prompt Security, Zenity e OneLayer não aparecem** em nenhuma fonte que os ligue ao *Hype Cycle for Secure AI, 2026*. Para Lakera, Protect AI e Zenity encontrei apenas menções a **outros** documentos da Gartner (Market Guide AI TRiSM, Emerging Market Quadrant, Hype Cycle for Agentic AI). Não encontrei nenhuma evidência de que estejam na categoria AI Runtime Defense deste relatório.

---

## 3. Definição oficial de "AI Runtime Defense"

**Nenhuma página de glossário da Gartner é acessível** (`gartner.com/en/reviews/...` e `/en/research/methodologies/...` devolvem 403; sem snapshot no Wayback para o glossário). O que existe são **citações da definição por terceiros**, com redação convergente entre fontes independentes — o que reforça a plausibilidade, mas não substitui a fonte primária.

Definição citada (redação que se repete entre duas fontes distintas):

> Gartner define AI Runtime Defense como tecnologia que *"implements intent-based policy enforcement and anomaly detection for AI applications and models"*.

- **[NeuralTrust]** — "NeuralTrust Named a Sample Vendor in Gartner Hype Cycle for AI Governance Technologies, 2026" — NeuralTrust Team, 10/08/2026 — https://neuraltrust.ai/news/neuraltrust-gartner-hype-cycle-ai-governance-technologies-2026 — trecho literal: *"Gartner defines AI Runtime Defense as technology that 'implements intent-based policy enforcement and anomaly detection for AI applications and models', exactly what TrustGuard does."* (Atribuído por NeuralTrust ao **Hype Cycle for AI Governance Technologies, 2026**, ID G00851828, publicado 07/08/2026 — **relatório diferente** do objeto deste dossiê.)
- **[Akto]** — "Akto Named a Sample Vendor for AI Runtime Defense in the 2026 Gartner® Hype Cycle™ for AI Governance Technologies" — Krishanu, 18/08/2026 — https://www.akto.io/blog/akto-in-gartner-hype-cycle-ai-governance-2026 — trecho literal: *"The AI Runtime Defense profile, written by Jeremy D'Hoinne, Avivah Litan, and Dionisio Zumerle, covers intent-based policy enforcement and anomaly detection for AI applications and models."* (Também o Hype Cycle for AI Governance Technologies.)

**Descrição de "AI runtime defense" como *feature* obrigatória de mercado no Gartner Peer Insights** (fonte Gartner, mas acessível somente via *snippet* de buscador — a página devolve 403 e não há snapshot):

- **[Gartner Peer Insights]** — "Best AI Application Security Reviews 2026" — atualizado março/2026 — https://www.gartner.com/reviews/market/ai-application-security — trecho literal (via snippet; não verificado por leitura direta): *"AI runtime defense: Deployed to detect anomalies and attacks in AI application inputs and outputs, with capabilities to block threats in real time, integrate with existing security tools for blocking, and alert the SOC to initiate incident response. Required capabilities include: a) Guardrails: E…"* — **sinalizo como snippet não confirmado.**

**Não encontrado:** uma página de glossário/definição oficial da própria Gartner, acessível e verificável, para o verbete "AI Runtime Defense". As duas definições citadas acima vêm de fornecedores e referem-se a **outro** relatório (AI Governance Technologies, 2026), não ao Hype Cycle for Secure AI.

---

## 4. Números do relatório reproduzidos por terceiros

**Resultado: os três números (33%, 50%, 47%) têm como ÚNICA fonte localizada a NeuralTrust.** Nenhuma outra fonte os reproduz. Buscas dedicadas (várias formulações de query, backend padrão e `--multi=exa`) retornaram apenas a NeuralTrust e material sem relação.

Os números, conforme declarados:

- **[NeuralTrust]** — "Named Sample Vendor in Hype Cycle for Secure AI" — NeuralTrust Team, 13/10/2026 — https://neuraltrust.ai/news/gartner-hype-cycle-for-secure-ai-2026 — trecho literal: *"**33%** of organisations have already deployed customer-facing GenAI agents in production; **50%** of CISOs say they are uncertain about the long-term costs of securing those deployments"* e, no corpo, *"**47% of security organisations have already diverted budget toward AI runtime defense**, which means this is not a speculative investment category."*

Os mesmos 33% e 50% repetem-se, com a mesma redação, no *release* irmão da mesma empresa (mesma data), o que **não** constitui segunda fonte — é a mesma organização:

- **[NeuralTrust]** — "Named Sample Vendor in Hype Cycle for AI-Driven Cybersecurity" — NeuralTrust Team, 13/10/2026 — https://neuraltrust.ai/news/gartner-hype-cycle-for-ai-driven-cybersecurity-2026 — trecho literal: *"What they found is a market simultaneously racing ahead and falling behind: **33% of organisations have already deployed customer-facing GenAI agents in production**, yet **50% of CISOs say they are not confident about the long-term costs** of securing those deployments."*

**Contexto adicional da Gartner (fonte primária, mas não são os números acima)** — úteis para o post sem substituir os 33/50/47:

- **[Gartner Newsroom]** — "Gartner Forecasts the Market for Securing AI Will Reach $4.8 Billion in 2027" — 26/08/2026 — https://www.gartner.com/en/newsroom/press-releases/2026-08-26-gartner-forecasts-the-market-for-securing-ai-will-reach-almost-5-billion-in-2027 — trecho literal (via snippet): *"The market for securing AI is growing rapidly, projected to reach almost $4.8 billion in 2027, a 68.7% increase over 2026, according to Gartner, Inc. […] By 2028, the market is forecast to reach almost $7.7 billion."*
- **[AI2Work]** — "Gartner: Securing AI Spending to Nearly Double to $4.8 Billion" — AI2Work Editorial Team, 01/09/2026 — https://ai2.work/blog/gartner-securing-ai-spending-to-nearly-double-to-4-8-billion — trecho literal: *"Gartner projects the securing AI market at $2.835 billion in 2026 and $4.783 billion in 2027 — 68.7% growth — reaching roughly $7.7 billion by 2028"*.
- **[CRN Asia]** — "Gartner predicts spending on securing AI to grow 68.7% in 2027" — D.K., 28/08/2026 — https://www.crnasia.com/news/2026/cybersecurity/gartner-predicts-spending-on-securing-ai-to-grow-68-7-in-2027 — trecho literal (via snippet): *"Spending on tools that secure enterprise AI will reach almost US$4.8 billion next year, with AI usage control and application security drawing a wave of new vendors into the two fastest-growing segments."*
- **[ITBrief AU]** — "Gartner sees securing AI market hit USD $4.8bn in 2027" — Mark Tarre, 27/08/2026 — https://itbrief.com.au/story/gartner-sees-securing-ai-market-hit-usd-4-8bn-in-2027

**Estatística de mercado independente, sobre o mesmo tema (não é do relatório):** cobertura de pesquisa Omdia (set/2026) por um veículo setorial, útil como contraponto de dados:

- **[CybrSecMedia]** — "AI Is Moving Faster Than Enterprise Security. Organizations Are Spending to Catch Up" — Bill Brenner, 02/10/2026 — https://www.cybrsecmedia.com/ai-is-moving-faster-than-enterprise-security-organizations-are-spending-to-catch-up/ — trecho literal: *"Forty-seven percent said […] 47% monitor and log AI activity"* — **atenção: esse "47%" é outro indicador (monitoramento e log de atividade de IA), da Omdia, e NÃO o "47% que redirecionou orçamento para runtime defense" da NeuralTrust.** São números distintos que coincidem; não confundir.

---

## 5. Críticas e ressalvas ao valor de ser "Sample Vendor" + disclaimer padrão da Gartner

### 5a. O disclaimer oficial da Gartner (fonte primária, via Wayback Machine)

A Gartner publica a redação obrigatória — o **"Objectivity Disclaimer"** — na *Content Compliance Policy*. Não há snapshot do Hype Cycle em si, mas há snapshot da política:

- **[Gartner / Content Compliance Policy]** — "Content Compliance Policy" — captura de 07/07/2026 (Wayback Machine) — http://web.archive.org/web/20260707184343/https://www.gartner.com/en/about/policies/content-compliance — trecho literal: *"For this research, use verbatim, industry-general quotes, and properly attribute the insights to Gartner. Be sure to include the expert-opinion Objectivity Disclaimer if you promote inclusion in the report: **Gartner does not endorse any company, vendor, product or service depicted in its publications, and does not advise technology users to select only those vendors with the highest ratings or other designation. Gartner publications consist of the opinions of Gartner's business and technology insights organization and should not be construed as statements of fact. Gartner disclaims all warranties, expressed or implied, with respect to this publication, including any warranties of merchantability or fitness for a particular purpose.**"*

Restrições explícitas da Gartner ao uso comercial de "Sample Vendor" no Hype Cycle (mesma página):

- **[Gartner / Content Compliance Policy]** — trecho literal: *"Hype Cycle — When promoting inclusion, you may use words such as: Acknowledged / Identified / Named / Placed / Positioned / Recognized. You may promote retrospective inclusion. […] If stating inclusion in the report, include the Objectivity Disclaimer."*
- **[Gartner / Content Compliance Policy]** — trecho literal: *"Don't use: Content that is about specific companies […] The research or insights as an endorsement or a competitive weapon. All claims of 'validation', 'testament', 'evidence' (or other words with the same meaning) must appear as your company's opinion and not as a Gartner endorsement. […] Any words or phrases that give the impression that you are 'featured', 'highlighted', 'spotlighted' or imply any of these. Any text, references, or images to imply that inclusion is an award."*

### 5b. A variante antiga do disclaimer, usada pela própria NeuralTrust

O *release* da NeuralTrust reproduz a redação mais antiga (e mais conhecida) do disclaimer, agora **em tensão com a versão atual** da política — discrepância digna de nota editorial:

- **[NeuralTrust]** — "Named Sample Vendor in Hype Cycle for Secure AI" — 13/10/2026 — https://neuraltrust.ai/news/gartner-hype-cycle-for-secure-ai-2026 — trecho literal: *"Gartner does not endorse any vendor, product or service depicted in its research publications, and does not advise technology users to select only those vendors with the highest ratings or other designation. Gartner research publications consist of the opinions of Gartner's research organization and should not be construed as statements of fact."*

### 5c. Críticas ao próprio modelo Hype Cycle

- **[Wikipedia — "Gartner hype cycle"]** — verbete, revisão de 24/08/2026 — https://en.wikipedia.org/wiki/Gartner_hype_cycle — trecho literal: *"The hype cycle's veracity has been largely disputed, with studies pointing to it being inconsistently true at best."* e, na seção *Criticisms of the model*: *"There have been numerous criticisms of the hype cycle model. Prominent among them are that it is not a cycle, that the outcome does not depend on the nature of the technology itself, that it is not scientific in nature […] A related criticism is that the 'cycle' has no real benefits to the development or marketing of new technologies and merely comments on pre-existing trends."*
- **[Wikipedia, citando The Economist (2024)]** — mesma página — trecho literal: *"We find, in short, that the cycle is a rarity. Tracing breakthrough technologies over time, only a small share—perhaps a fifth—move from innovation to excitement to despondency to widespread adoption. […] of all the forms of tech which fall into the trough of disillusionment, six in ten do not rise again."*
- **[Burn It Down Marketing]** — "Gartner: The Final Boss of Everything Wrong With Marketing" — Clark Barron, 15/04/2025 — https://burnitdown.marketing/gartner-the-final-boss-of-everything-wrong-with-marketing/ — trecho literal: *"Gartner wraps itself in the language of research—the posturing of intellectual authority, the aesthetics of objectivity. Whitepapers. Forecasts. Quadrants. What's actually behind the curtain? A racket."* — **ressalva: é um texto de marketing, opinativo e agressivo, sem apuração; cito como exemplo de crítica existente, não como fonte factual.**
- **[Brightwork Research & Analysis]** — "How Gartner Research Compares to Real Research Entities" — Primary Researcher, 13/06/2017 (atualizado 25/01/2024) — https://www.brightworkresearch.com/gartner-research-compares-real-research-entities/ — trecho literal: *"Gartner positions itself as a research entity. However, compared with real research entities, Gartner performs poorly."* — **ressalva: a Brightwork tem posição editorial declaradamente anti-Gartner ("Notice of Lack of Financial Bias… one of the only independent sources on Gartner"), com dados não verificáveis; cito como crítica, não como fato.**

### 5d. A defesa / o contraponto (importante para equilíbrio)

- **[IIAR> — Institute of Influencer & Analyst Relations]** — "Do you need to pay Gartner to be in the Magic Quadrant?" — David Rossiter, 11/03/2016 — https://analystrelations.org/2016/03/11/do-you-need-to-pay-gartner-to-be-in-the-magic-quadrant/ — trecho literal: *"I have never seen or heard of any evidence that says you can buy your way on to a Magic Quadrant. Nor does the amount of money you spend influence where you appear on the MQ."* e *"You don't need to spend any money to brief a Gartner analyst. […] You cannot buy the opinion of a Gartner analyst."*
- **[Akto]** — releitura do significado prático de estar no "Peak of Inflated Expectations" em relatório irmão — 18/08/2026 — https://www.akto.io/blog/akto-in-gartner-hype-cycle-ai-governance-2026 — trecho literal: *"Sitting at the peak is not a compliment, and pretending the category is finished helps nobody, because the obstacles Gartner lists are the same ones our customers raise in evaluations."* (Contrapõe o enquadramento otimista da NeuralTrust: *"The Peak is not a warning"*.)

---

## 6. Fato adicional relevante: há um relatório-irmão publicado no mesmo dia

Na mesma data (12/10/2026), a Gartner publicou um segundo Hype Cycle inaugural, o **Hype Cycle for AI-Driven Cybersecurity, 2026** — útil porque os dois se citam e as listas da categoria AI Runtime Defense são declaradas idênticas.

- **[Gartner]** — "Hype Cycle for AI-Driven Cybersecurity, 2026" — https://www.gartner.com/en/documents/8487545 — **HTTP 403**; ID citado por terceiro como **G00854093**.
- **[NeuralTrust]** — "Named Sample Vendor in Hype Cycle for AI-Driven Cybersecurity" — 13/10/2026 — https://neuraltrust.ai/news/gartner-hype-cycle-for-ai-driven-cybersecurity-2026 — trecho literal: *"On 12 October 2026, Gartner published two landmark Hype Cycle reports simultaneously […] The other, the **Gartner Hype Cycle for AI-Driven Cybersecurity, 2026** […] is the first edition of this report, authored by Jeremy D'Hoinne, Craig Porter, Josh Murphy, and Christine Lee."*
  - Mesma fonte, números que **só ela reproduz**: *"58% of cybersecurity leaders say generative AI delivers significant innovation; 72% say current AI security products are too expensive relative to the value they deliver"* e *"63% of organisations are evaluating in-house development of AI cybersecurity tools rather than buying from vendors"* e *"by 2030, **80% of large enterprises** will rely on custom-built AI cybersecurity tools"*.

**Alerta de discrepância entre fontes sobre a autoria do *profile* da categoria:** a NeuralTrust atribui o relatório Secure AI a **D'Hoinne, Zumerle e Jeff Arias**; a Akto atribui o *profile* de AI Runtime Defense a **D'Hoinne, Avivah Litan e Dionisio Zumerle**. Os dois não são necessariamente contraditórios (autores do relatório ≠ autores do capítulo da categoria, e são relatórios diferentes), mas **não há como conciliar isso sem o original** — registre-se a divergência.

---

## Lacunas (o que NÃO foi possível confirmar)

1. **Nenhuma reportagem da imprensa independente** (SecurityWeek, Help Net Security, CSO, The Register, Infosecurity, Dark Reading, etc.) sobre o *Hype Cycle for Secure AI, 2026*. O relatório é de 12/10/2026 e a apuração é de 13/10/2026; a ausência pode ser de tempo, mas **no momento não existe cobertura editorial localizada**.
2. **A lista nominal dos dez "Sample Vendors"** de AI Runtime Defense tem **uma única origem** — a NeuralTrust, que é parte interessada. Não há segunda fonte, nem confirmação pela Gartner (documento 403).
3. **A quantidade "dez fornecedores"** não foi confirmada por nenhuma fonte independente.
4. **Nenhum fornecedor além da NeuralTrust** se declarou publicamente listado **neste** relatório (nem Akto, nem Lasso, nem HiddenLayer, nem SentinelOne, nem Noma, nem Check Point, nem F5, nem TrojAI). As menções desses nomes vêm todas da lista publicada pela NeuralTrust ou de **outros** relatórios da Gartner.
5. **A definição "oficial" de AI Runtime Defense pela Gartner não é verificável na fonte:** as duas citações existentes referem-se ao *Hype Cycle for AI Governance Technologies, 2026* (outro relatório), e a página de Peer Insights que descreve "AI runtime defense" só é acessível por *snippet* (403 ao acessar; sem snapshot no Wayback).
6. **Os números 33%, 50% e 47% não têm confirmação além da NeuralTrust.** Nenhuma outra fonte os reproduz. (E o "47%" da Omdia, sobre monitoramento/log, é um indicador **diferente** — risco real de confusão.)
7. **Nenhum comunicado oficial da Gartner** (press release, post "Smarter With Gartner", página de artigo) sobre este Hype Cycle foi localizado até agora — o padrão da casa é publicar releases para Hype Cycles importantes (ex.: IA 2025/2026), o que reforça que a cobertura é, por ora, assimétrica.
8. **Não foi possível ler o documento 8487445, o glossário da Gartner, a política de conteúdo atual ao vivo nem a metodologia do Hype Cycle** por acesso direto: todos devolvem 403. A política de conteúdo foi lida via snapshot de 07/07/2026 — **pode ter mudado** desde então.
9. **Não foi encontrada evidência** ligando Lakera, Protect AI, Prompt Security, Zenity ou OneLayer à categoria AI Runtime Defense deste relatório, apesar de busca nominal.
10. **Não foi possível confirmar** posição exata, "benefit rating", maturidade e penetração de mercado da categoria pela própria Gartner — esses atributos vêm exclusivamente da NeuralTrust (e, para outro relatório, da Akto).

---

### Anexo — arquivos/consultas para reproduzir

- Fontes vivas salvas com `ketch ... --tag secure-ai-gartner` (reprodutível via `ketch tag show secure-ai-gartner`).
- Verificações de existência de link: `curl -sIL -o /dev/null -w "%{http_code}\n" <url>` — usado em `gartner.com/en/documents/8487445` (**403**), `gcomdr.pdo.aws.gartner.com/en/documents/8487445` (**403**), `emt.gartnerweb.com/en/documents/8487445` (**403**), `gartner.com/reviews/market/ai-application-security` (**403**).
- Disponibilidade no Wayback: `curl -s "http://archive.org/wayback/available?url=gartner.com/en/documents/8487445"` → **sem snapshot** (13/10/2026).
- Nenhum software foi instalado durante a apuração.
