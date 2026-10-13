# Dossiê (MESCLADO) — Gartner *Hype Cycle for Secure AI, 2026* e a NeuralTrust

> **Este arquivo é a fusão de `dossie-neuraltrust.md` + `dossie-secure-ai-gartner.md`** (um único
> dossiê para uma única notícia do dia). Os dois rascunhos anteriores tratavam o **mesmo fato-âncora**
> e por isso foram consolidados antes da redação final e antes dos revisores.
> Regra aplicada: **uma notícia por dia — leads irmãos viram um dossiê e um post** (skill
> `criar-noticia`, passo 0.5).

**Fato-âncora (único):** em **12 de outubro de 2026**, a Gartner publicou o **primeiro *Hype Cycle for
Secure AI*** e, na categoria **AI Runtime Defense**, nomeou a espanhola **NeuralTrust** como *Sample
Vendor*. No mesmo dia saiu o relatório-irmão *Hype Cycle for AI-Driven Cybersecurity, 2026*.

**Objeto:** relatório *Gartner Hype Cycle for Secure AI, 2026* — primeira edição; analistas **Jeremy
D'Hoinne, Dionisio Zumerle e Jeff Arias**; ID **G00846820** — e a menção da NeuralTrust à categoria
**AI Runtime Defense**.
**Documento (página oficial):** <https://www.gartner.com/en/documents/8487445> (HTTP 403).

**Data da apuração:** 13 de outubro de 2026.
**Método:** fontes levantadas ao vivo com `ketch search/scrape` (v0.19.0/v0.18.1) e `curl`; fontes
vivas salvas com `--tag neuraltrust-secure-ai` **e** `--tag secure-ai-gartner` (reuso via
`ketch tag show neuraltrust-secure-ai` / `ketch tag show secure-ai-gartner`). Todo trecho é literal,
extraído da página no momento da coleta. Onde não houve confirmação, está escrito "não encontrado".

**Nota metodológica (crítica):** a página da Gartner devolve **HTTP 403** a scraping direto (`curl`,
`ketch scrape`). Não há snapshot no Wayback Machine para `/en/documents/8487445` nem para
`/en/reviews/market/ai-application-security`. Portanto, **todo conteúdo atribuído ao relatório vem
de terceiros que o citam** — nunca de leitura direta do original. Isso está sinalizado em cada item.

**Status de verificação:** existem hoje duas fontes de fornecedor que descrevem este Hype Cycle
(NeuralTrust e Akto) e **nenhuma reportagem de imprensa independente** localizada. O relatório tem
menos de 48 horas de publicado, o que explica — mas não elimina — a lacuna.

**Verificação de duplicata:** nenhum post em `_posts/` menciona NeuralTrust, TrustGuard ou "runtime
defense" antes de 13/10/2026 (grep `-ril` retornou vazio). **Ressalva registrada pelo usuário:** o
post `_posts/2026-09-21-gartner-tendencias-governo-2026.md` (tendências de tecnologia no governo,
de 14/09/2026) é **notícia anterior e distinta** — não é irmão desta. Ver *Lacunas* (item 16).

---

## 1. O relatório e o relatório-irmão

- **[NeuralTrust — site oficial (parte interessada)]** — "Named Sample Vendor in Hype Cycle for
  Secure AI" — NeuralTrust Team, 13 de outubro de 2026 —
  <https://neuraltrust.ai/news/gartner-hype-cycle-for-secure-ai-2026> — trecho literal: *"Gartner
  published the first-ever Hype Cycle for Secure AI on 12 October 2026, authored by Jeremy D'Hoinne,
  Dionisio Zumerle, and Jeff Arias (G00846820)."* / *"NeuralTrust is listed as a Sample Vendor in AI
  Runtime Defense, one of ten vendors in a category rated High benefit, 5-20% market penetration, and
  Emerging maturity."* / *"AI Runtime Defense is positioned at the Peak of Inflated Expectations, the
  point of maximum visibility and investment concentration."*

- **Relatório-irmão (mesma data, 12/10/2026):** *Hype Cycle for AI-Driven Cybersecurity, 2026* —
  <https://www.gartner.com/en/documents/8487545> (**HTTP 403**; ID citado por terceiros como
  **G00854093**). Autoria declarada por terceiro: Jeremy D'Hoinne, **Craig Porter, Josh Murphy e
  Christine Lee**.
  - **[NeuralTrust]** — "Named Sample Vendor in Hype Cycle for AI-Driven Cybersecurity" — 13/10/2026 —
    <https://neuraltrust.ai/news/gartner-hype-cycle-for-ai-driven-cybersecurity-2026> — trecho
    literal: *"On 12 October 2026, Gartner published two landmark Hype Cycle reports simultaneously.
    One (the Hype Cycle for Secure AI) maps the technologies that protect AI systems. The other […]
    maps the inverse: the AI technologies and strategies that strengthen the cybersecurity program
    itself."* / *"It is the first edition of this report, authored by Jeremy D'Hoinne, Craig Porter,
    Josh Murphy, and Christine Lee."*
  - Mesma fonte, números que **só ela reproduz**: *"58% of cybersecurity leaders say generative AI
    delivers significant innovation; 72% say current AI security products are too expensive relative
    to the value they deliver"*; *"63% of organisations are evaluating in-house development of AI
    cybersecurity tools rather than buying from vendors"*; e projeção *"by 2030, 80% of large
    enterprises will rely on custom-built AI cybersecurity tools"*.
  - **Divergência de autoria registrada:** a Akto atribui o *profile* de AI Runtime Defense a
    **D'Hoinne, Avivah Litan e Dionisio Zumerle** (num **outro** relatório, o de AI Governance
    Technologies). Não é necessariamente contraditório (autores do relatório ≠ autores do capítulo,
    e são relatórios distintos), mas **não há como conciliar sem o original**.

---

## 2. Reportagem independente da imprensa especializada

**NÃO ENCONTRADO.** Buscou-se — sem resultado — cobertura editorial específica do *Hype Cycle for
Secure AI, 2026* em SecurityWeek, Help Net Security, CSO Online, The Register, Infosecurity Magazine
e Dark Reading (`ketch search` backend padrão e `--multi=exa`, `openrouter_web_search` e checagem de
HTTP). Os veículos apareceram apenas em matérias *adjacentes*:

- **[SecurityWeek]** — "AI and Cybersecurity – Everything You Wanted to Know, But Were Afraid to Ask"
  — 16/06/2026 — <https://www.securityweek.com/ai-and-cybersecurity-everything-you-wanted-to-know-but-were-afraid-to-ask/>
  — **não menciona** o Hype Cycle for Secure AI.
- **[Help Net Security]** — "Gartner predicts the technologies set to transform 2026" — 23/10/2025 —
  <https://www.helpnetsecurity.com/2025/10/23/gartner-2026-technology-trends/> — Hype Cycle de
  Tendências Tecnológicas 2026, não o de Secure AI.
- **[Computing]** — "Gartner: AI is changing cybersecurity faster than cloud ever did" — 30/09/2026 —
  <https://www.computing.co.uk/news/2026/ai/ai-is-changing-cybersecurity-faster-than-cloud-ever-did>
  — **HTTP 403**; cito título/URL/data da indexação.
- **[Infosecurity Magazine]** — "AI Issues Will Drive Half of Incident Response Efforts by 2028, Says
  Gartner" — <https://www.infosecurity-magazine.com/news/ai-issues-half-incident-response>.

**Conclusão:** a única divulgação substantiva deste relatório é **de fornecedores que se declaram
listados**, com interesse comercial direto no enquadramento.

---

## 3. "Sample Vendors" — quem são e quantos

**Fonte primária (interessada):** a NeuralTrust é a única fonte que publica a **lista nominal
completa** da categoria AI Runtime Defense.

- **[NeuralTrust]** — "Named Sample Vendor in Hype Cycle for AI-Driven Cybersecurity" — 13/10/2026 —
  <https://neuraltrust.ai/news/gartner-hype-cycle-for-ai-driven-cybersecurity-2026> — trecho
  literal: *"NeuralTrust is one of ten Sample Vendors listed by Gartner in the AI Runtime Defense
  category across both reports. The full list includes Akto, Check Point Software Technologies, F5,
  HiddenLayer, Lasso, Noma Security, Pillar Security, SentinelOne, and TrojAI."*
  - Interpretação: **10 fornecedores**, sendo nove nomeados **mais a própria NeuralTrust**. A empresa
    diz que a lista de dez vale "nos dois relatórios" (Secure AI **e** AI-Driven Cybersecurity).
  - **Atributos públicos da categoria** (mesma fonte): *"rated High benefit, 5-20% market penetration,
    and Emerging maturity"*; posicionada no **Peak of Inflated Expectations**.

**Confirmações independentes parciais** (cada fornecedor citando-se, em *outros* relatórios da
Gartner — evidência de que o padrão "Sample Vendor" se repete, mas **não** confirmação desta lista):

- **[Akto]** — "Akto Named a Sample Vendor for AI Runtime Defense in the 2026 Gartner® Hype Cycle™ for
  AI Governance Technologies" — Krishanu, 18/08/2026 —
  <https://www.akto.io/blog/akto-in-gartner-hype-cycle-ai-governance-2026> — trecho literal: *"Akto is
  listed as a Sample Vendor for AI Security Testing, alongside Adversa AI, Check Point Software,
  Enkrypt AI, F5, HiddenLayer, Mindgard, Palo Alto Networks, Pillar Security, and SentinelOne."*
  (categoria **AI Security Testing**, no Hype Cycle for AI Services 2026 — método, não a lista.)
- **[Pillar Security]** — LinkedIn — *"We are excited to be recognized as a Sample Vendor in the 2026
  Gartner® Hype Cycle™ for Application Security, in both AI Security Testing and AI Runtime Defense!"*
  — <https://www.linkedin.com/posts/pillarsecurity_we-are-excited-to-be-recognized-as-a-sample-activity-7486389848434589697-myT9>
- **[Lasso]** — "Lasso Named in Gartner's Hype Cycle for Artificial Intelligence, 2026" — 14/09/2026 —
  <https://www.lasso.security/blog/lasso-named-in-gartners-hype-cycle-for-artificial-intelligence-2026>.
- **[Zenity]** — "Zenity Named in Two Categories in the 2026 Gartner® Hype Cycle™ for Agentic AI" —
  15/04/2026 — <https://zenity.io/company-overview/newsroom/company-news/zenity-named-in-two-categories-in-the-2026-gartner-r-hype-cycle-tm-for-agentic-ai>.

**Sobre fornecedores hipotetizados:** Akto, Lasso, HiddenLayer e SentinelOne **aparecem** na lista da
NeuralTrust; **Lakera, Protect AI, Prompt Security, Zenity e OneLayer não aparecem** em nenhuma fonte
que os ligue ao *Hype Cycle for Secure AI, 2026* (têm menções a **outros** documentos).

---

## 4. Definição de "AI Runtime Defense"

**Nenhuma página de glossário da Gartner é acessível** (`/en/reviews/...` e `/en/research/methodologies/...`
devolvem 403; sem snapshot no Wayback). O que existe são **citações de terceiros**, com redação
convergente entre fontes independentes — plausível, mas não substitui a fonte primária.

> Gartner define AI Runtime Defense como tecnologia que *"implements intent-based policy enforcement
> and anomaly detection for AI applications and models"*.

- **[NeuralTrust]** — "Named Sample Vendor in Gartner Hype Cycle for AI Governance Technologies, 2026"
  — 10/08/2026 — <https://neuraltrust.ai/news/neuraltrust-gartner-hype-cycle-ai-governance-technologies-2026>
  — trecho literal: *"Gartner defines AI Runtime Defense as technology that 'implements intent-based
  policy enforcement and anomaly detection for AI applications and models', exactly what TrustGuard
  does."* (**Atribuído a outro relatório** — AI Governance Technologies, 2026, ID G00851828.)
- **[Akto]** — 18/08/2026 (link acima) — trecho literal: *"The AI Runtime Defense profile, written by
  Jeremy D'Hoinne, Avivah Litan, and Dionisio Zumerle, covers intent-based policy enforcement and
  anomaly detection for AI applications and models."*
- **Descrição como *feature* obrigatória de mercado (Gartner Peer Insights)** — "Best AI Application
  Security Reviews 2026", atualizado março/2026,
  <https://www.gartner.com/reviews/market/ai-application-security> — trecho literal (via *snippet*; a
  página devolve 403): *"AI runtime defense: Deployed to detect anomalies and attacks in AI
  application inputs and outputs, with capabilities to block threats in real time, integrate with
  existing security tools for blocking, and alert the SOC to initiate incident response."* —
  **snippet não confirmado por leitura direta.**
- **Descrição orientada a agentes** (a categoria "evoluindo para proteger agentes, não só chatbots"):
  a mesma definição citada aponta que essas ferramentas estão *"evolving to protect AI **agents**, not
  just LLM-based chatbots"* — agentes que executam ações exigem detecção de baixa latência e baixa
  taxa de falsos positivos.

---

## 5. Números do relatório reproduzidos por terceiros

**Resultado: os três números (33%, 50%, 47%) têm como ÚNICA fonte localizada a NeuralTrust.** Nenhuma
outra fonte os reproduz (buscas dedicadas, várias formulações, backend padrão e `--multi=exa`).

- **[NeuralTrust]** — "Named Sample Vendor in Hype Cycle for Secure AI" — 13/10/2026 —
  <https://neuraltrust.ai/news/gartner-hype-cycle-for-secure-ai-2026> — trecho literal: *"33% of
  organisations have already deployed customer-facing GenAI agents in production; 50% of CISOs say
  they are uncertain about the long-term costs of securing those deployments"* e, no corpo, *"47% of
  security organisations have already diverted budget toward AI runtime defense."*
- **Projeções com prazo:** *"by 2028, organisations skipping preproduction offensive testing will face
  twice as many cybersecurity incidents as proactive organisations"* (chegou a circular como "twice as
  many"); e, contraintuitiva, *"by 2027, enterprises' costs from abuses of 'task-oriented' AI agents
  will be at least four times greater than those caused by multi-agent systems"*.
- Os mesmos 33% e 50% repetem-se, com a mesma redação, no *release* irmão da **mesma empresa** — o que
  **não** constitui segunda fonte (é a mesma organização).

**Contexto adicional da Gartner (números de mercado, não do relatório):** ver §11.

**Risco de confusão registrado:** existe um "47%" da **Omdia** (monitoramento e log de atividade de IA,
via CybrSecMedia, 02/10/2026) que é **indicador diferente** do "47% que redirecionou orçamento para
runtime defense" da NeuralTrust. **Não confundir.**

---

## 6. Críticas, disclaimer padrão da Gartner e equilíbrio

### 6a. Disclaimer oficial (fonte primária, via Wayback Machine)

- **[Gartner / Content Compliance Policy]** — captura de 07/07/2026 —
  <http://web.archive.org/web/20260707184343/https://www.gartner.com/en/about/policies/content-compliance>
  — trecho literal: *"Gartner does not endorse any company, vendor, product or service depicted in its
  publications, and does not advise technology users to select only those vendors with the highest
  ratings or other designation. Gartner publications consist of the opinions of Gartner's business and
  technology insights organization and should not be construed as statements of fact. […]"*
- **Usos permitidos** (mesma página): *"Hype Cycle — When promoting inclusion, you may use words such
  as: Acknowledged / Identified / Named / Placed / Positioned / Recognized. You may promote
  retrospective inclusion. […] If stating inclusion in the report, include the Objectivity Disclaimer."*
- **Usos proibidos** (mesma página): *"Don't use: […] The research or insights as an endorsement or a
  competitive weapon. All claims of 'validation', 'testament', 'evidence' […] must appear as your
  company's opinion and not as a Gartner endorsement. […] Any words or phrases that give the impression
  that you are 'featured', 'highlighted', 'spotlighted' […] Any text, references, or images to imply
  that inclusion is an award."*

### 6b. Variante antiga do disclaimer, usada pela própria NeuralTrust

- **[NeuralTrust]** — 13/10/2026 — trecho literal: *"Gartner does not endorse any vendor, product or
  service depicted in its research publications, and does not advise technology users to select only
  those vendors with the highest ratings or other designation. Gartner research publications consist
  of the opinions of Gartner's research organization and should not be construed as statements of
  fact."* (redação mais antiga, em tensão com a versão atual da política).

### 6c. Críticas ao modelo Hype Cycle

- **[Wikipedia — "Gartner hype cycle"]** — revisão de 24/08/2026 —
  <https://en.wikipedia.org/wiki/Gartner_hype_cycle> — trecho literal: *"The hype cycle's veracity has
  been largely disputed, with studies pointing to it being inconsistently true at best."* / *"[…] it is
  not a cycle, that the outcome does not depend on the nature of the technology itself, that it is not
  scientific in nature."*
- **[Wikipedia, citando The Economist (2024)]** — mesma página — trecho literal: *"Tracing breakthrough
  technologies over time, only a small share—perhaps a fifth—move from innovation to excitement to
  despondency to widespread adoption. […] of all the forms of tech which fall into the trough of
  disillusionment, six in ten do not rise again."*
- **[Burn It Down Marketing]** — "Gartner: The Final Boss of Everything Wrong With Marketing" — Clark
  Barron, 15/04/2025 — <https://burnitdown.marketing/gartner-the-final-boss-of-everything-wrong-with-marketing/>
  — trecho literal: *"What's actually behind the curtain? A racket."* **Ressalva: texto opinativo e
  agressivo, sem apuração — exemplo de crítica existente, não fonte factual.**
- **[Brightwork Research & Analysis]** — 13/06/2017 (atualizado 25/01/2024) —
  <https://www.brightworkresearch.com/gartner-research-compares-real-research-entities/> — trecho
  literal: *"Gartner positions itself as a research entity. However, compared with real research
  entities, Gartner performs poorly."* **Ressalva: a Brightwork tem posição editorial declaradamente
  anti-Gartner, dados não verificáveis.**

### 6d. O contraponto (importante para equilíbrio)

- **[IIAR> — Institute of Influencer & Analyst Relations]** — "Do you need to pay Gartner to be in the
  Magic Quadrant?" — David Rossiter, 11/03/2016 —
  <https://analystrelations.org/2016/03/11/do-you-need-to-pay-gartner-to-be-in-the-magic-quadrant/> —
  trecho literal: *"I have never seen or heard of any evidence that says you can buy your way on to a
  Magic Quadrant. […] You cannot buy the opinion of a Gartner analyst."*
- **[Akto]** — releitura do "Peak of Inflated Expectations" em relatório irmão — 18/08/2026 — trecho
  literal: *"Sitting at the peak is not a compliment, and pretending the category is finished helps
  nobody, because the obstacles Gartner lists are the same ones our customers raise in evaluations."*
  (Contrapõe o enquadramento otimista da NeuralTrust.)

---

## 7. A empresa NeuralTrust

- **[NeuralTrust — site oficial]** — "NeuralTrust raises $20M to secure the growing swarm of AI agents
  in the enterprise" — 17 de junho de 2026 — <https://neuraltrust.ai/news/neuraltrust-raises-20m> —
  trecho literal: *"BARCELONA, June 17, 2026 NeuralTrust/ — NeuralTrust, the platform to secure AI
  agents, today announced a $20 million seed round, the largest cybersecurity seed financing raised by
  an EU company to date."*
  - Fundadores: *"CEO Joan Vendrell led AI deployment and security as Chief Data Officer at Mango,
    after roles at Amazon and McKinsey; CTO Victor Garcia led security architecture in regulated
    telecom and banking; and COO Alejandro Domingo led AI transformation as an Associate Partner at
    McKinsey."*
  - Clientes e porte: *"NeuralTrust's customers include AirEuropa, Abanca, Iberia, and Banc Sabadell,
    alongside other global banks, airlines, energy companies, and government agencies. 92% report
    annual revenues above $1B, with 80% based in Europe and 20% international."*
  - ARR: *"in the first quarter of 2026, NeuralTrust doubled its full-year 2025 ARR."*
- **[Tracxn]** — consulta em 13/10/2026 —
  <https://platform.tracxn.com/a/d/company/65e619536dd4f25e88dad346/neuraltrust> — trecho literal:
  *"Founded Year: 2022 | Founders: Alejandro Domingo Co-Founder & COO Victor Garcia Co-Founder Joan
  Vendrell Farreny CEO & Co-Founder"* / *"Employee Count Official: 35 | Location City: Barcelona |
  Stage: Seed"*.
- **[Dealroom]** — consulta em 13/10/2026 — <https://dealroom.co/companies/neuraltrust> — trecho
  literal: *"Security and governance platform for enterprise AI agents Barcelona, Spain Founded 2022
  Cybersecurity Valuation $50–100M Last recorded · 2026 Revenue <$1M Latest reported FY Headcount <100
  Total funding $10–50M"*. **Atenção:** o "Revenue <$1M" é da NeuralTrust; o ">$1B" da PR é porte do
  *cliente* — não confundir.
- **[Crunchbase]** — consulta em 13/10/2026 — <https://www.crunchbase.com/organization/neuraltrust> —
  trecho literal: *"Founded obfuscated obfuscation Private Seed Barcelona, Catalonia, Spain 101-250
  neuraltrust.ai Cyber Security Generative AI Software"*. **Limitação:** fundação ofuscada sem login;
  equipe (101-250) diverge do Tracxn (35) e do Dealroom (<100).
- **[The Next Web]** — "NeuralTrust raised $20M to police the AI agents companies can't even count" —
  Cristian Dina, 18 de junho de 2026 —
  <https://thenextweb.com/news/neuraltrust-20-million-seed-ai-agent-security> — trecho literal: *"The
  seed round, worth €17.2mn, was led by Munich's Alstin Capital, with VentureFriends, Seaya, Kibo
  Ventures, Banc Sabadell, the EA Ventures Plug and Play Fund and Finaves, plus public money from the
  European Innovation Council and Spain's research agency. NeuralTrust calls it the largest
  cybersecurity seed round ever raised by an EU company, a claim worth a pinch of salt, but not an
  outlandish one."*
- **[Tech.eu]** — Tamara Djurickovic, 17 de junho de 2026 —
  <https://tech.eu/2026/06/17/neuraltrust-closes-20m-to-expand-ai-agent-security-platform/> — trecho
  literal: *"Founded by Joan Vendrell (CEO), Victor Garcia (CTO), and Alejandro Domingo (COO),
  NeuralTrust provides a unified platform that enables organisations to discover, monitor, govern, and
  secure AI agents across their environments."*
- **[EU-Startups]** — "Barcelona-based NeuralTrust raises €17.2 million to secure and govern enterprise
  AI agents" — Rahul Raj, 17 de junho de 2026 —
  <https://www.eu-startups.com/2026/06/barcelona-based-neuraltrust-raises-e17-2-million-to-secure-and-govern-enterprise-ai-agents>.
- **[NeuralTrust — site oficial]** — "NeuralTrust Opens New London Office…" — 7 de setembro de 2026 —
  <https://neuraltrust.ai/news/neuraltrust-opens-new-london-office> — trecho literal: *"LONDON, Sept.
  7, 2026 /NeuralTrust/ — NeuralTrust, the Barcelona headquartered platform for securing AI agents,
  today announced a new, dedicated office in London."*
- **[PR Newswire (release oficial NeuralTrust)]** — "NeuralTrust Named a Pioneer in Gartner EMQ for AI
  Application Security" — 17 de setembro de 2026 —
  <https://www.prnewswire.com/news-releases/neuraltrust-named-a-pioneer-in-gartner-emq-for-ai-application-security-302882527.html>
  — trecho literal: *"NeuralTrust is headquartered in Barcelona and operates offices in London and New
  York […] The company opened its London office in September 2026."*
- **[Morningstar — republicação do PR Newswire]** — mesmo release, 17/09/2026 —
  <https://www.morningstar.com/news/pr-newswire/20260917ny50951/neuraltrust-named-a-pioneer-in-gartner-emq-for-ai-application-security>.

**Síntese da empresa:** Barcelona (sede), escritórios em Londres (set/2026) e, segundo material
próprio, Nova York; fundada em 2022 por Joan Vendrell (CEO), Victor Garcia (CTO) e Alejandro Domingo
(COO); seed de **US$ 20 milhões** (≈ €17,2 mi) em 17/06/2026, liderado pela **Alstin Capital**
(Munique), com VentureFriends, Seaya, Kibo Ventures, Banc Sabadell, EA Ventures Plug and Play Fund e
Finaves (IESE), além de aporte público do European Innovation Council e da AEI. Tamanho de equipe:
dados divergentes (35 / 101-250 / <100) — ver *Lacunas*.

---

## 8. Produtos

### TrustGuard — motor de segurança em runtime (o produto que a Gartner enquadra em AI Runtime Defense)

- **[NeuralTrust — página oficial do produto]** — "AI Agent Security for Enterprise - TrustGuard" —
  consulta em 13/10/2026 — <https://neuraltrust.ai/ai-agent-security> — trecho literal: *"TrustGuard
  inspects every interaction and stops attacks at the moment of execution — on every surface where
  your agents run: gateways, SDKs, browsers, and platforms."* / *"AI agents don't just respond, they
  execute. Prompt injection, poisoned tool results, and rogue agent calls arrive as plain language.
  TrustGuard enforces before they reach your system."*
- **[NeuralTrust — documentação oficial]** — <https://docs.neuraltrust.ai/trustguard/overview> —
  trecho literal: fluxo *"1 Collect […] 2 Detect […] 3 Enforce — Allow, block or transform in-flight —
  or alert only, depending on fidelity. 4 Observe — Findings surface where you already look, linked
  back to the full trace."* TrustGuard **não é um gateway** (não roteia tráfego nem chama provedores).

### TrustGate — gateway de agentes

- **[NeuralTrust — página oficial do produto]** — <https://neuraltrust.ai/ai-gateway> — trecho literal:
  *"One gateway for every call your agents make: to models, MCP servers, tools, and other agents.
  Secured by default."*
- **[PR Newswire (release oficial)]** — 17/06/2026 — trecho literal: *"TrustGate, an agent gateway
  that brokers every LLM, MCP, and tool call, becomes the single enforcement point through which all
  agent traffic flows."*

### TrustLens — gestão de postura dos agentes

- **[NeuralTrust — página oficial do produto]** — <https://neuraltrust.ai/agent-posture-management> —
  trecho literal: *"TrustLens discovers every agent in your enterprise, tracks what they're configured
  to do, and records what they actually do — and surfaces the risks that emerge from both."*
  - **Inconsistência (fonte primária):** a documentação oficial lista **três** produtos (TrustGate,
    TrustGuard, TrustTest); o release do seed e o PR do EMQ listam **quatro** (com TrustLens). Ver
    *Lacunas*.

### TrustTest — red teaming e avaliação

- **[NeuralTrust — página oficial do produto]** — <https://neuraltrust.ai/red-teaming> — trecho
  literal: *"TrustTest is a red-teaming and evaluation framework that attacks your LLMs and agents with
  state-of-the-art adversarial techniques, then grades how they hold up."*
- **[NeuralTrust — documentação oficial]** — <https://docs.neuraltrust.ai/platform/overview> — trecho
  literal: *"These docs cover three products: TrustGate (AI agent gateway), TrustGuard (runtime
  security), and TrustTest (AI red teaming)."*

---

## 9. Histórico de menções da Gartner (o padrão de marketing)

2026 acumulou **sete** reconhecimentos Gartner citados pela própria NeuralTrust (seis Hype
Cycles/radares + um Market Quadrant). Cada um com URL e trecho:

| # | Relatório Gartner | Publicação / post | Categoria |
|---|---|---|---|
| 1 | Hype Cycle for Data Security Technologies, 2026 (G00846824) | 23/06 → post 02/07/2026 | AI Runtime Defense |
| 2 | Hype Cycle for Application Security, 2026 (G00846821) | 21/07 → post 23/07/2026 | AI Runtime Defense |
| 3 | Hype Cycle for Infrastructure Security, 2026 (G00846830) | 23/07 → post 27/07/2026 | AI Runtime Defense |
| 4 | Hype Cycle for AI Governance Technologies, 2026 (G00851828) | 07/08 → post 10/08/2026 | AI Runtime Defense |
| 5 | Emerging Tech Impact Radar: AI Cybersecurity Ecosystem (G00846953) | 05/10 → post 06/10/2026 | AI Application Security |
| 6 | **Hype Cycle for Secure AI, 2026 (G00846820)** | 12/10 → post 13/10/2026 | **AI Runtime Defense** |
| 7 | **Hype Cycle for AI-Driven Cybersecurity, 2026** | 12/10 → post 13/10/2026 | **AI Runtime Defense** |
| 8 | Emerging Market Quadrant (EMQ) for AI Application Security | post 17/09/2026 | Pioneer (melhor europeia) |

- **[NeuralTrust]** — 02/07/2026 — <https://neuraltrust.ai/news/gartner-hype-cycle-data-security-2026>
  — trecho literal: *"Published on 23 June 2026 […] (ID G00846824) by Gartner analyst Andrew Bales […]
  NeuralTrust has been named a Sample Vendor in the Hype Cycle for Data Security Technologies, 2026, in
  the AI Runtime Defense category."*
- **[NeuralTrust]** — 23/07/2026 — <https://neuraltrust.ai/news/gartner-hype-cycle-for-application-security-2026>
  — trecho literal: *"NeuralTrust is named as a sample vendor for AI Runtime Defense, which is At the
  Peak with High benefit rating and 5-20% enterprise adoption."*
- **[NeuralTrust]** — 27/07/2026 —
  <https://neuraltrust.ai/news/neuraltrust-named-sample-vendor-in-gartner-hype-cycle-for-infrastructure-security-2026>
  — trecho literal: *"recognized as a Sample Vendor in AI Runtime Defense in the Gartner Hype Cycle for
  Infrastructure Security, 2026 (ID G00846830, published July 23, 2026, authored by Theo de Feligonde
  and Charlie Winckless)."*
- **[NeuralTrust]** — 10/08/2026 —
  <https://neuraltrust.ai/news/neuraltrust-gartner-hype-cycle-ai-governance-technologies-2026> —
  trecho literal, definindo "Sample Vendor": *"Gartner Hype Cycle reports identify technology
  categories that Gartner analysts believe are relevant to enterprise buyers. Within each category,
  Gartner lists Sample Vendors as representative providers of that technology. Inclusion is an
  editorial recognition based on Gartner analyst research and market observation."*
- **[NeuralTrust]** — 06/10/2026 —
  <https://neuraltrust.ai/news/neuraltrust-in-gartner-emerging-tech-impact-radar-2026> — trecho
  literal: *"named a Sample Vendor in the AI Application Security profile of the Gartner Emerging Tech
  Impact Radar: AI Cybersecurity Ecosystem (ID G00846953, published 5 October 2026)."* / *"Gartner
  forecasts $16.4 billion in end-user spend on securing AI solutions by 2030."* (número atribuído à
  Gartner **só por essa fonte**).
- **[NeuralTrust]** — 13/10/2026 — <https://neuraltrust.ai/news/gartner-hype-cycle-for-ai-driven-cybersecurity-2026>
  (ver §1).
- **[Gartner — páginas de documento (paywall)]** — `8487545` (AI-Driven Cybersecurity) e `8461645`
  (Emerging Tech Impact Radar) — **HTTP 403**, conteúdo interno inacessível.
- **[PR Newswire (EMQ)]** — 17/09/2026 — trecho literal: *"The Emerging Market Quadrant Pioneer
  designation adds to a year of Gartner recognition for NeuralTrust, which has also been named a Sample
  Vendor in the Gartner Hype Cycle for Application Security 2026, […] AI Governance Technologies 2026,
  […] Infrastructure Security 2026, and […] Data Security 2026. The company has also been included in
  the Gartner Market Guide for AI Gateways and the Gartner Market Guide for Guardian Agents."*

**Padrão observado:** a NeuralTrust publica um post de marketing por menção, com estrutura repetida
(lead "Gartner has named NeuralTrust a Sample Vendor…", bloco "TL;DR", seção explicando a categoria,
remate vendendo o TrustGuard). Corroborado por terceiro: **[The Next Web]** — Cristian Dina, 18/06/2026
— *"Gartner, which NeuralTrust quotes liberally, predicts 40 per cent of enterprises will pull back
autonomous agents by 2027 over governance gaps spotted only after something breaks."*

---

## 10. Concorrentes diretos e consolidação (a categoria virou ativo de aquisição)

- **[Palo Alto Networks]** — "Palo Alto Networks Completes Acquisition of Protect AI" — 22 de julho de
  2025 — <https://www.paloaltonetworks.com/company/press/2025/palo-alto-networks-completes-acquisition-of-protect-ai>.
  (Preço ~US$ 500 mi **não confirmado em fonte primária**.)
- **[Cisco]** — absorveu a **Robust Intelligence** em 2024 (valor não divulgado).
- **[Check Point]** — "Check Point Acquires Lakera to Deliver End-to-End AI Security for Enterprises" —
  16 de setembro de 2025 —
  <https://www.checkpoint.com/es/press-releases/check-point-acquires-lakera-to-deliver-end-to-end-ai-security-for-enterprises/>.
- **[Calcalist]** — <https://www.calcalistech.com/ctechnews/article/rj5bc1vige> — 16 de setembro de
  2025 — negócio Lakera/Check Point de **cerca de 300 milhões de dólares** (número forte).
- **[SentinelOne]** — "SentinelOne to Acquire Prompt Security" — 5 de agosto de 2025 —
  <https://www.sentinelone.com/press/sentinelone-to-acquire-prompt-security>.
- **[HiddenLayer]** — 100 milhões de dólares em Série B, setembro de 2026 —
  <https://www.hiddenlayer.com/news/hiddenlayer-100m-series-b-ai-security>.
- **[Zenity]** — 125 milhões em Série C, agosto de 2026 —
  <https://zenity.io/press-release/zenity-raises-125-million-to-secure-the-era-of-1-billion-ai-agents>.
- **[Lasso Security]** — 30 milhões, setembro de 2026 —
  <https://www.lasso.security/resources/lasso-security-announces-future-of-ai-security-with-cpu-based-guardrails>.
- **Diferenciação que a NeuralTrust vende: geografia** — ser a opção **europeia**, não americana, para
  bancos e governos que precisam manter a segurança dos agentes no continente (mesma lógica do
  escritório de Londres).

**Players independentes e números públicos:** HiddenLayer, Zenity e Lasso levantam capital em escala
muito maior que o seed da NeuralTrust (números dos próprios comunicados).

---

## 11. Mercado e números (fontes nomeadas)

- **[Gartner — press release (não acessível diretamente; 403)]** — "Gartner Forecasts the Market for
  Securing AI Will Reach $4.8 Billion in 2027" — Gartner, 26 de agosto de 2026 —
  <https://www.gartner.com/en/newsroom/press-releases/2026-08-26-gartner-forecasts-the-market-for-securing-ai-will-reach-almost-5-billion-in-2027>.
  Teor capturado por cobertura independente:
  - **[DigitalToday (Coreia)]** — "Gartner sees AI security market growing 69 percent next year" —
    Chi-gyu Hwang, 01/09/2026 —
    <https://www.digitaltoday.co.kr/en/view/98610/gartner-sees-ai-security-market-growing-69-percent-next-year>
    — trecho literal: *"Gartner forecast on Sept. 1 that the AI security market will reach about
    $4.783 billion in 2027, up about 69 percent from 2026, and expand to about $7.7 billion in 2028."*
    / *"attacks exploiting access control weaknesses and prompt injection will account for more than
    half of successful cyberattacks targeting AI agents by 2029."* / *"AI application security is
    forecast to remain the largest area of spending in 2027, reaching about $851 million. AI usage
    control is expected to follow at about $749 million."*
  - **[IT Brief Asia]** — "Gartner sees securing AI market hit USD $4.8bn in 2027" — Mark Tarre,
    27/08/2026 — <https://itbrief.asia/story/gartner-sees-securing-ai-market-hit-usd-4-8bn-in-2027> —
    trecho literal: *"Gartner expects the market for securing AI to reach almost USD $4.8 billion in
    2027, up 68.7% from 2026. Spending in the category is projected to rise further to nearly USD $7.7
    billion in 2028."* **Limitação:** HTTP 406 ao scrape (conteúdo via snippet).
  - **[AI2Work]** — "Gartner: Securing AI Spending to Nearly Double to $4.8 Billion" — 01/09/2026 —
    <https://ai2.work/blog/gartner-securing-ai-spending-to-nearly-double-to-4-8-billion> — trecho
    literal: *"Gartner projects the securing AI market at $2.835 billion in 2026 and $4.783 billion in
    2027 — 68.7% growth — reaching roughly $7.7 billion by 2028"*.
  - **[CRN Asia]** — "Gartner predicts spending on securing AI to grow 68.7% in 2027" — D.K.,
    28/08/2026 —
    <https://www.crnasia.com/news/2026/cybersecurity/gartner-predicts-spending-on-securing-ai-to-grow-68-7-in-2027>.
  - **Divergência de datas:** release datado 26/08/2026 no URL, mas a cobertura fala "Sept. 1" — não
    reconciliado.
- **[MarketsandMarkets]** — "AI TRiSM Market … Global Forecast to 2031" — consulta em 13/10/2026 —
  <https://www.marketsandmarkets.com/report-search-page.asp?rpt=ai-risk-management-software-market> —
  trecho literal: *"The AI Trust, Risk, and Security Management (AI TRiSM) market is projected to grow
  from USD 3.09 billion in 2026 to USD 11.61 billion by 2031 at a CAGR of 30.3%."* (lista NeuralTrust
  entre as empresas do mercado.) — **escopo diferente** de "segurança de IA".
- **[Grand View Research]** — "AI In Cybersecurity Market Size To Reach $93.75Bn By 2030" — novembro de
  2024 — <https://www.grandviewresearch.com/press-release/global-artificial-intelligence-cybersecurity-market>
  — **escopo mais amplo** ("IA na cibersegurança", não "segurança de IA"): usar só como contraste.
- **[CybrSecMedia]** — "AI Is Moving Faster Than Enterprise Security…" — Bill Brenner, 02/10/2026 —
  <https://www.cybrsecmedia.com/ai-is-moving-faster-than-enterprise-security-organizations-are-spending-to-catch-up/>
  — trecho literal: *"47% monitor and log AI activity"* (**indicador da Omdia**, DIFERENTE do 47% da
  NeuralTrust — ver §5).

---

## 12. Incidentes reais que justificam a categoria

- **[InfoWorld]** — "GitHub AI agent leaks private repositories via prompt injection attack" — Gyana
  Swain, 8 de julho de 2026 —
  <https://www.infoworld.com/article/4194468-github-ai-agent-leaks-private-repositories-via-prompt-injection-attack-2.html>
  — trecho literal: *"A prompt injection attack can trick GitHub's preview Agentic Workflows into
  retrieving content from private repositories and publishing it publicly […] according to new research
  from Noma Security."* / *"The attack did not rely on stolen credentials, malware, or software
  vulnerabilities. Instead, an attacker embedded hidden instructions within a GitHub Issue submitted to
  a public repository."* Ataque batizado **GitLost**.
  - **[Noma Security — pesquisa original]** — "GitLost: How We Tricked GitHub's AI Agent into Leaking
    Private Repos" — Sasi Levi, 6 de julho de 2026 —
    <https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos>.
- **[OWASP GenAI Security Project]** — "GenAI and Agentic AI Exploit Roundup Q3 2026" — OWASP GenAI
  Project Editor, 8 de outubro de 2026 —
  <https://genai.owasp.org/2026/10/08/genai-and-agentic-ai-exploit-roundup-q3-2026/> — trecho literal:
  *"Coverage period: July 1, 2026 through September 30, 2026. […] The seven entries include three
  connected components of the OpenAI campaign, three Anthropic incidents, and one research-demonstrated
  Copilot exploit family."* / *"Prompt-level instructions alone do not establish a secure boundary."*
  - **Ressalva da própria fonte:** *"It is not an exhaustive report or an official OWASP publication."*
- **[OCDE — AI Incidents Monitor]** — "Widespread Prompt Injection Attacks Exploit Enterprise AI
  Systems" — OCDE.AI (texto rotulado "[AI generated]"), incidente de 28 de junho de 2026 —
  <https://oecd.ai/en/incidents/2026-06-28-d957> — trecho literal: *"Prompt injection attacks targeting
  large language models and AI agents have impacted over 90 organizations, leading to credential and
  cryptocurrency theft, data exfiltration, and security breaches."*
  - **[Forbes]** — "Prompts Are The New Malware As Enterprise AI Defenses Fall Behind" — Janakiram
    MSV, 29 de junho de 2026 —
    <https://www.forbes.com/sites/janakirammsv/2026/06/29/prompts-are-the-new-malware-as-enterprise-ai-defenses-fall-behind>
    — **HTTP 403**; número atribuído a relatório da CrowdStrike **não verificado em fonte primária**.
- **[Cloud Security Alliance — blog]** — "SearchLeak: Copilot Data Exfiltration Exploited" — Dolev
  Taler (Varonis), 24 de junho de 2026 —
  <https://cloudsecurityalliance.org/blog/2026/06/24/searchleak-how-we-turned-m365-copilot-into-a-one-click-data-exfiltration-weapon>.
- **[arXiv — pré-print]** — "EchoLeak: The First Real-World Zero-Click Prompt Injection Exploit in a
  Production LLM System" — <https://arxiv.org/html/2509.10540v1> — trecho literal: *"This paper
  presents an in-depth case study of EchoLeak (CVE-2025-32711), a zero-click prompt injection
  vulnerability in Microsoft 365 Copilot that enabled remote, unauthenticated data exfiltration via a
  single crafted email."*
- **[arXiv — pesquisa própria da NeuralTrust (autopromocional, mas com credibilidade acadêmica)]** —
  "The Echo Chamber Multi-Turn LLM Jailbreak" — Ahmad Alobaid, Martí Jordà Roca (NeuralTrust), Carlos
  Castillo (ICREA/UPF), Joan Vendrell (NeuralTrust), novembro de 2025 —
  <https://arxiv.org/pdf/2601.05742>.

---

## 13. Reconhecimentos de outros analistas (contexto)

- **[KuppingerCole / NeuralTrust]** — "NeuralTrust Leader in 2025 KuppingerCole Compass for Gen AI
  Defense" — <https://neuraltrust.ai/news/2025-kuppingercole-generative-ai-defense-leadership-compass>
  — trecho literal: *"recognized as a Leader in the 2025 KuppingerCole Leadership Compass for
  Generative AI Defense."*
- **[PR Newswire (release oficial NeuralTrust)]** — "NeuralTrust recognized as a Star in the
  MarketsandMarkets Agentic AI Security Quadrant" — 26 de maio de 2026 —
  <https://www.prnewswire.com/news-releases/neuraltrust-recognized-as-a-star-in-the-marketsandmarkets-agentic-ai-security-quadrant-302782126.html>
  — trecho literal: *"recognized as a Star in the MarketsandMarkets Agentic AI Security Market, Global
  Forecast to 2032 Company Evaluation Matrix for AI Security Specialists/Startups, 2025."*

---

## Lacunas (o que NÃO foi possível confirmar)

1. **Nenhuma reportagem da imprensa independente** sobre o *Hype Cycle for Secure AI, 2026* (§2).
2. **A lista nominal dos dez Sample Vendors** tem **uma única origem** — a NeuralTrust, parte
   interessada. Não há segunda fonte nem confirmação pela Gartner (documento 403).
3. **A quantidade "dez fornecedores"** não foi confirmada por nenhuma fonte independente.
4. **Nenhum fornecedor além da NeuralTrust** se declarou publicamente listado **neste** relatório.
5. **Definição "oficial" de AI Runtime Defense não verificável na fonte** — as citações referem-se a
   **outro** relatório (AI Governance Technologies, 2026).
6. **Os números 33%, 50% e 47% não têm confirmação além da NeuralTrust.** E o "47%" da Omdia é outro
   indicador.
7. **Nenhum comunicado oficial da Gartner** (press release, "Smarter With Gartner") sobre este Hype
   Cycle foi localizado.
8. **Documento, glossário, política de conteúdo ao vivo e metodologia** devolvem 403; a política foi
   lida via snapshot de 07/07/2026 — **pode ter mudado**.
9. **Nada liga Lakera, Protect AI, Prompt Security, Zenity ou OneLayer** à categoria AI Runtime Defense
   **deste** relatório.
10. **Posição exata/benefit rating/maturidade/penetração** vêm exclusivamente da NeuralTrust (e, para
    outro relatório, da Akto).
11. **Data exata de fundação:** "2022" (Tracxn/Dealroom), Crunchbase ofusca sem login; sem registro
    societário. Dia/mês não confirmados.
12. **Tamanho real da equipe:** divergência (35 / 101-250 / <100) — não resolvido; dizer apenas
    "startup em estágio seed" ou qualificar a faixa.
13. **Receita/valuation:** Dealroom indica "Revenue <$1M" e "Valuation $50–100M" (não confirmado pela
    empresa). A empresa só diz que dobrou o ARR de 2025 no 1º tri/2026. Sem receita nominal pública.
14. **Rodadas anteriores:** nenhuma localizada antes do seed de jun/2026 (o seed é descrito como o
    primeiro); aporte público anterior (EIC, AEI) citado sem valores.
15. **TrustTest/TrustLens — inconsistência de portfólio** (três vs. quatro produtos) não esclarecida.
16. **Sobre o post de 21/09/2026** (`gartner-tendencias-governo-2026.md`): o usuário o citou como
    exemplo. Ele **não** é irmão desta notícia — é a lista de tendências de tecnologia **no governo**
    (press release de 14/09/2026, analista Dean Lacheca), publicada em 21/09. **Não deve ser fundido**
    com este post. A regra "uma notícia por dia" foi violada **hoje (13/10)**, com dois posts do mesmo
    fato-âncora (Secure AI + NeuralTrust), e é isso que esta fusão corrige. Se o usuário quiser
    mesclar os dois posts do Gartner (21/09 + 13/10) num único, é decisão dele — o fato-âncora é
    distinto e a data publicada de 21/09 não pode ser reescrita.
17. **Datas do press release de mercado da Gartner:** URL datado 26/08/2026 vs. cobertura "Sept. 1".
18. **Números de "AI security market":** $4,8 bi (2027) e $7,7 bi (2028) vêm de cobertura jornalística
    (403 no original); $16,4 bi (2030) vem **só** da atribuição da NeuralTrust à Gartner. Distinguir.
19. **Nova York:** o PR do EMQ (set/2026) cita escritórios em "London and New York"; o blog de Londres
    só menciona "Barcelona headquartered" + Londres. Endereço de NY não confirmado.
20. **Grafias dos fundadores:** "Joan Vendrell Farreny" (Tracxn) vs. "Joan Vendrell"; "Alejandro Domingo
    Salvador" (AI World). Nomes de meio não confirmados.
21. **Preços de aquisição não confirmados em fonte primária:** Protect AI/Palo Alto (~US$ 500 mi só via
    Geekwire), Robust Intelligence/Cisco e Prompt Security/SentinelOne (undisclosed). Só Lakera/Check
    Point tem número forte (~US$ 300 mi, Calcalist).

---

### Anexo — arquivos/consultas para reproduzir

- Fontes vivas salvas com `ketch ... --tag neuraltrust-secure-ai` **e** `ketch ... --tag secure-ai-gartner`.
- Verificação de link: `curl -sIL -o /dev/null -w "%{http_code}\n" <url>` — usado em
  `gartner.com/en/documents/8487445` (**403**), `gartner.com/reviews/market/ai-application-security`
  (**403**), etc.
- Disponibilidade no Wayback:
  `curl -s "http://archive.org/wayback/available?url=gartner.com/en/documents/8487445"` → **sem
  snapshot** (13/10/2026).
- Nenhum software foi instalado durante a apuração.
