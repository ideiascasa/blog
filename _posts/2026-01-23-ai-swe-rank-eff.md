---
layout: post
title: "O Grande Ranking das IAs para Engenharia de Software: SWE-Bench vs. Eficiência de Custo em 2026"
author: "Davi"
categories: blog
tags: [blog,tech]
image: coding.jpg
---

# O Grande Ranking das IAs para Engenharia de Software: SWE-Bench vs. Eficiência de Custo em 2026

## Introdução

A inteligência artificial chegou a um ponto crítico em janeiro de 2026. Não se trata mais de "qual IA é a melhor?" — essa pergunta é ingênua. A pergunta real é: **qual IA oferece o melhor custo-benefício para o seu caso de uso específico?**

Nos últimos meses, assistimos a uma explosão de modelos competindo em capacidade de engenharia de software (SWE-Bench), com novos players desafiando os gigantes estabelecidos. Claude Opus 4.5 continua sendo a melhor em termos absolutos de capacidade, mas novos modelos como **GLM-4.7** estão mudando radicalmente a equação de preço-performance.

Este artigo analisa as **duas perspectivas fundamentais** sobre o ranking das IAs para coding: **performance absoluta** versus **eficiência econômica**. E depois, responde à pergunta que realmente importa: **quanto você vai gastar por mês?**

---

## Parte 1: Ranking por Performance Absoluta (SWE-Bench)

### Qual IA consegue resolver os problemas mais difíceis de engenharia de software?

A métrica **SWE-Bench Verified** é o padrão-ouro da indústria. Ela mede a capacidade de um modelo em resolver problemas reais de repositórios GitHub, como corrigir bugs, implementar features, e refatorar código.

Aqui está o ranking por **capacidade bruta de SWE**:

| Rank SWE | Modelo | Criador | SWE-Bench (%) | Contexto (K tokens) | Preço Input | Preço Output | **Custo Total/1M** |
|----------|--------|---------|---------------|----------------------|-------------|-------------|------------------|
| 1 | Claude Opus 4.5 | Anthropic | **80.9%** | 200 | $5.00 | $25.00 | **$30.00** |
| 2 | GPT‑5.2 | OpenAI | **80.0%** | 400 | $1.75 | $7.00 | **$8.75** |
| 3 | Gemini 2.5 Pro | Google | **77.1%** | 1,000 | $0.075 | $0.30 | **$0.38** |
| 4 | Claude Opus 4.1 | Anthropic | **77.0%** | 200 | $15.00 | $75.00 | **$90.00** |
| 5 | Claude Sonnet 4.5 | Anthropic | **77.2%** | 200 | $3.00 | $15.00 | **$18.00** |
| 6 | Gemini 3 Pro | Google | **76.2%** | 1,000 | $1.25 | $5.00 | **$6.25** |
| 7 | Grok 4.1 | xAI | **75.0%** | 256 | $3.00 | $15.00 | **$18.00** |
| 8 | **GLM‑4.7** | Zhipu / Z.ai | **73.8%** | 200 | $0.44 | $1.74 | **$2.18** |
| 9 | Kimi K2 Thinking | Moonshot | **73.4%** | 256 | $0.39 | $1.90 | **$2.29** |
| 10 | GLM‑4.6 | Zhipu / Z.ai | **68.1%** | 200 | $0.01 | $0.03 | **$0.04** |
| 11 | Llama 4 Maverick | Meta | **68.47%** | 10,000 | $0.00 | $0.00 | **$0.00** |
| 12 | o3 | OpenAI | **69.1%** | 200 | $3.50 | $28.00 | **$31.50** |
| 13 | DeepSeek‑R1 | DeepSeek | **49.2%** | 128 | $0.14 | $0.55 | **$0.69** |

### O que vemos aqui?

- **Claude Opus 4.5 é imbatível em capacidade pura**: 80.9% em SWE-Bench significa que consegue resolver 8 de cada 10 problemas reais de GitHub que GPT-5.2 também consegue.

- **Gemini 2.5 Pro é um anomalia**: 77.1% de performance com apenas $0.38/1M tokens. Como? Porque Google pode absorver custos em escala e oferece o modelo como "perda líder" para capturar market share.

- **GLM-4.7 é o novo disruptor**: Apenas 3.1 pontos percentuais abaixo de Claude Sonnet 4.5, mas a um preço **8.3x mais barato** ($2.18 vs. $18.00).

- **Llama 4 Maverick é free**: 68.47% de performance sem pagar nada. O catch? Você precisa hospedar/inferir você mesmo.

---

## Parte 2: Ranking por Eficiência (SWE-Bench ÷ Custo)

### Qual IA oferece o melhor valor: máxima performance pela menor quantia?

Agora entra a métrica que realmente importa para pequenos times, startups e desenvolvedores individuais: **Efficiency Score = SWE-Bench (%) ÷ Custo Total por 1M tokens**.

Quanto **maior** o score, **melhor o custo-benefício**.

| Rank Eficiência | Modelo | SWE-Bench (%) | Custo/1M | **Efficiency Score** | Categoria |
|---|---|---|---|---|---|
| 1 | Llama 4 Maverick | 68.47% | $0.00 | **∞ (infinito)** | 🟢 ELITE (self-host) |
| 2 | GLM‑4.6 | 68.1% | $0.04 | **1,702.5x** | 🟢 ELITE |
| 3 | Gemini 2.5 Pro | 77.1% | $0.38 | **203.2x** | 🟢 ELITE |
| 4 | **GLM‑4.7** | 73.8% | $2.18 | **33.9x** | 🟢 EXCELENTE |
| 5 | Kimi K2 Thinking | 73.4% | $2.29 | **32.1x** | 🟢 EXCELENTE |
| 6 | DeepSeek‑R1 | 49.2% | $0.69 | **71.3x** | 🟢 MUITO BOM |
| 7 | Gemini 3 Pro | 76.2% | $6.25 | **12.2x** | 🟢 MUITO BOM |
| 8 | GPT‑5.2 | 80.0% | $8.75 | **9.1x** | 🟡 BOM |
| 9 | Claude Sonnet 4.5 | 77.2% | $18.00 | **4.3x** | 🟡 BOM |
| 10 | Grok 4.1 | 75.0% | $18.00 | **4.2x** | 🟡 BOM |
| 11 | Claude Opus 4.5 | 80.9% | $30.00 | **2.7x** | 🟡 JUSTO |
| 12 | o3 | 69.1% | $31.50 | **2.2x** | 🔴 CARO |
| 13 | Claude Opus 4.1 | 77.0% | $90.00 | **0.86x** | 🔴 MUITO CARO |

### O que muda quando você olha para eficiência?

**Chocante revelação #1**: GLM‑4.7 oferece **33.9x melhor custo-benefício que Claude Opus 4.5**, apesar de apenas 7.1% menos performance.

**Chocante revelação #2**: Gemini 2.5 Pro oferece **203x melhor eficiência que Claude Opus 4.5**, com apenas 3.8% menos SWE-Bench.

**Chocante revelação #3**: Se você conseguir fazer o self-hosting funcionar, Llama 4 Maverick tem custo-benefício infinito (zero custo API + 68.47% SWE).

---

## Parte 3: Análise de Custo Mensal — Cenário Pessoal

### Quanto você vai gastar por mês como desenvolvedor individual?

A pergunta que mais importa: **Qual é a minha conta de verdade?**

Para responder isso, precisamos de pressupostos reais sobre uso mensal. Baseado em dados da comunidade (Reddit, Discord, relatórios de plataformas):

**Desenvolvedor Individual — Uso Típico Mensal:**

- **Code completions**: 300 requisições/mês × 2,500 tokens médios = 750K tokens
- **Chat/debugging**: 50 sessões/mês × 4,000 tokens médios = 200K tokens
- **Multi-file edits**: 20 sessões/mês × 15,000 tokens médios = 300K tokens
- **Agent mode**: 5 sessões/mês × 50,000 tokens médios = 250K tokens
- **Total**: ~1.5M tokens/mês (aproximadamente 50K tokens/dia)

| Modelo | SWE % | Preço/1M | **Custo Mensal (1.5M tokens)** | Eficiência |
|--------|-------|---------|------|----------|
| Llama 4 Maverick | 68.47% | $0.00 | **$0** | ∞ |
| GLM‑4.6 | 68.1% | $0.04 | **$0.06** | 1,702.5x |
| Gemini 2.5 Pro | 77.1% | $0.38 | **$0.57** | 203.2x |
| **GLM‑4.7** | 73.8% | $2.18 | **$3.27** | 33.9x |
| Kimi K2 Thinking | 73.4% | $2.29 | **$3.44** | 32.1x |
| DeepSeek‑R1 | 49.2% | $0.69 | **$1.04** | 71.3x |
| Gemini 3 Pro | 76.2% | $6.25 | **$9.38** | 12.2x |
| GPT‑5.2 | 80.0% | $8.75 | **$13.13** | 9.1x |
| Claude Sonnet 4.5 | 77.2% | $18.00 | **$27.00** | 4.3x |
| Grok 4.1 | 75.0% | $18.00 | **$27.00** | 4.2x |
| Claude Opus 4.5 | 80.9% | $30.00 | **$45.00** | 2.7x |
| o3 | 69.1% | $31.50 | **$47.25** | 2.2x |
| Claude Opus 4.1 | 77.0% | $90.00 | **$135.00** | 0.86x |

### O Resultado: Um Desenvolvedor Individual

**Se você escolher Gemini 2.5 Pro em vez de Claude Opus 4.5:**
- Diferença de SWE-Bench: apenas 3.8% (77.1% vs 80.9%)
- Diferença de custo mensal: **$44.43** (Claude) - $0.57 (Gemini) = **economiza $43.86/mês**, ou **$526/ano**.

**Se você escolher GLM-4.7 em vez de Claude Opus 4.5:**
- Diferença de SWE-Bench: 7.1% (73.8% vs 80.9%)
- Diferença de custo mensal: $45.00 - $3.27 = **economiza $41.73/mês**, ou **$500.76/ano**.
- **Vale a pena?** Se resolvendo 73.8% dos problemas vs 80.9% funciona para você (a maioria consegue), sim.

---

## Parte 4: Análise de Custo Mensal — Cenário Enterprise

### E se você tem um time de 50 desenvolvedores?

**Empresa Média — Time de 50 Desenvolvedores — Uso Mensal Agressivo:**

Aqui, precisamos considerar que desenvolvedores seniors usam mais agents/multi-file edits do que devs juniores. Estimativa média por desenvolvedor:

- **Code completions**: 500 req/mês × 2,500 tokens = 1.25M tokens
- **Chat/debugging**: 100 sessões/mês × 5,000 tokens = 500K tokens
- **Multi-file edits**: 50 sessões/mês × 20,000 tokens = 1M tokens
- **Agent mode / autonomous coding**: 15 sessões/mês × 100,000 tokens = 1.5M tokens
- **Total por dev**: ~4.25M tokens/mês

**Total de 50 devs**: 50 × 4.25M = **212.5M tokens/mês**

| Modelo | SWE % | Preço/1M | **Custo Mensal (212.5M)** | **Custo Anual** | Eficiência |
|--------|-------|---------|------|-------|----------|
| Llama 4 Maverick (self-host) | 68.47% | $0.00 | **$0** | **$0** | ∞ |
| GLM‑4.6 | 68.1% | $0.04 | **$8,500** | **$102,000** | 1,702.5x |
| Gemini 2.5 Pro | 77.1% | $0.38 | **$80,750** | **$969,000** | 203.2x |
| **GLM‑4.7** | 73.8% | $2.18 | **$462,625** | **$5,551,500** | 33.9x |
| Kimi K2 Thinking | 73.4% | $2.29 | **$486,625** | **$5,839,500** | 32.1x |
| DeepSeek‑R1 | 49.2% | $0.69 | **$146,625** | **$1,759,500** | 71.3x |
| Gemini 3 Pro | 76.2% | $6.25 | **$1,328,125** | **$15,937,500** | 12.2x |
| GPT‑5.2 | 80.0% | $8.75 | **$1,859,375** | **$22,312,500** | 9.1x |
| Claude Sonnet 4.5 | 77.2% | $18.00 | **$3,825,000** | **$45,900,000** | 4.3x |
| Grok 4.1 | 75.0% | $18.00 | **$3,825,000** | **$45,900,000** | 4.2x |
| Claude Opus 4.5 | 80.9% | $30.00 | **$6,375,000** | **$76,500,000** | 2.7x |
| o3 | 69.1% | $31.50 | **$6,703,750** | **$80,445,000** | 2.2x |

### O Resultado: Uma Empresa com 50 Devs

**A escolha mais óbvia é Gemini 2.5 Pro:**
- SWE-Bench: 77.1% (praticamente top-tier)
- Custo anual: **$969,000**
- Por desenvolvedor/mês: **$1,615**

**Comparado com Claude Opus 4.5:**
- SWE-Bench: 80.9% (+3.8%)
- Custo anual: **$76,500,000**
- Por desenvolvedor/mês: **$127,500**

**A diferença anual: $75,531,000**.

Você poderia contratar **1,700+ novos engenheiros junior** com a economia de não usar Claude Opus 4.5 em todo o time. (Sim, é isso mesmo.)

---

## Parte 5: Conclusões — Qual Modelo Você Deve Escolher?

### Regra de Ouro por Cenário

| Seu Cenário | Melhor Modelo | Por quê | Custo Mensal (1.5M tokens) |
|---|---|---|---|
| **Desenvolvedor Individual, Budget Apertado** | **Gemini 2.5 Pro** | 77% SWE + $0.57/mês + 1M contexto | $0.57 |
| **Desenvolvedor Individual, Sem Budget Limit** | **Claude Opus 4.5** | 80.9% SWE + autonomia 20-30min | $45 |
| **Startups (< 10 devs), Custo Crítico** | **GLM‑4.7** | 73.8% SWE + $2.18/1M + open-weights | $3.27 |
| **Startups, Performance Matters** | **GPT‑5.2** | 80% SWE + 400K contexto + reasoning | $13.13 |
| **Enterprise (50+ devs), Otimizado Custo** | **Gemini 2.5 Pro em volume** | $969K/ano + suporte Google | $1,615/dev/mês |
| **Enterprise, Sem Compromisso em Performance** | **Claude Opus 4.5** | 80.9% SWE + autonomia + auditorias | $127,500/dev/mês |
| **Self-hosting Obrigatório (compliance)** | **Llama 4 Maverick** | 68.47% SWE + zero custo API + 10M contexto | $0 (infraestrutura própria) |
| **Melhor Reasoning + Coding** | **Kimi K2 Thinking** | 73.4% SWE + 42.8% HLE (agents) | $3.44 |

---

## Parte 6: A Reflexão Final — O Futuro da Engenharia de Software com IA

### O Paradoxo de 2026

Chegamos a um ponto onde **a capacidade técnica não é mais o diferenciador**. Claude Opus, GPT-5.2, Gemini, Grok, GLM-4.7 — todos conseguem resolver 70-81% dos problemas reais de engenharia de software.

**O novo diferenciador é econômico.**

A pergunta mudou de "qual modelo é melhor?" para "qual modelo me permite escalar meu time sem quebrar?"

### Os Vencedores de 2026

1. **Google** ganhou ao oferecer Gemini 2.5 Pro por praticamente nada. Eles absorvem prejuízo para derrotar concorrentes.

2. **Zhipu/Z.ai** ganhou ao oferecer open-weights + low-cost com GLM-4.7. Startups chinesas e equipes que se importam com privacidade agora têm uma opção real.

3. **OpenAI** mantém a liderança em reasoning puro (GPT-5.2 em matemática), mas perdeu em custo-benefício geral.

4. **Anthropic** oferece o "melhor em classe" em certos domínios (codificação autônoma, segurança), mas a um prêmio que cada vez menos empresas conseguem justificar.

### Os Perdedores de 2026

Modelos legados (Claude 3 Opus, GPT-4, Sonnet 4.1) estão se tornando obsoletos. E empresas que construíram produtos em torno de "melhor modelo" descobrirão que seus clientes simplesmente downgradam para modelos 5-10% piores que custam **100x menos**.

### A Realidade Econômica

Para um time de 50 desenvolvedores:

- **Claude Opus 4.5**: $76.5M/ano
- **Gemini 2.5 Pro**: $969K/ano
- **Diferença**: $75.5M

Essa é a diferença entre ter capital de risco infinito e precisar ser rentável.

### A Minha Recomendação Honesta

**Se você está construindo em 2026:**

1. **Comece com Gemini 2.5 Pro** — melhor custo-benefício absoluto. 77% de performance por $0.38/1M é uma anomalia de mercado que não vai durar.

2. **Tenha um plano B com GLM-4.7** — se Google mudar de ideia sobre preços (e eles vão), GLM-4.7 é seu backup. Open-weights, performance sólida, preço razoável.

3. **Reserve Claude Opus 4.5 para hard problems** — não coloque todo seu time nele. Use para debugging complexo, refatorações massivas, problemas com 10K+ linhas.

4. **Ignore o hype sobre o "melhor modelo"** — em 2026, "bom o suficiente" mata "melhor" 10 vezes a cada semana.

---

## Conclusão

O ranking das IAs para engenharia de software em 2026 não é um ranking linear. É uma matriz de trade-offs:

- **Performance vs. Custo**: Gemini 2.5 Pro vence. Claude Opus vence só em SWE puro.
- **Open-source vs. Proprietário**: GLM-4.7 vs Claude — depende se você quer controle ou conveniência.
- **Escala vs. Custo**: Llama 4 (self-hosted) vence se você consegue fazer a infraestrutura. Senão, é um pesadelo.

**O grande insight**: A indústria de IA passou do "qual é o melhor?" para "qual é o mais rentável?". E essa mudança é positiva — força inovação em eficiência, não só em escala.

Se você é um desenvolvedor individual, comece com **Gemini 2.5 Pro** e economize $500/ano. Se você gerencia um time, faça as contas com os números acima. Se você tem compliance/privacidade rigorosos, faça o download de **Llama 4 ou GLM-4.7** e hospede você mesmo.

## Apêndice: Tabelas de Referência Rápida

### Tabela A: Ranking por SWE-Bench (Performance Pura)

| Rank | Modelo | SWE % | Custo/1M |
|---|---|---|---|
| 1 | Claude Opus 4.5 | 80.9% | $30 |
| 2 | GPT-5.2 | 80.0% | $8.75 |
| 3 | Gemini 2.5 Pro | 77.1% | $0.38 |
| 4 | Claude Opus 4.1 | 77.0% | $90 |
| 5 | Claude Sonnet 4.5 | 77.2% | $18 |
| 6 | Gemini 3 Pro | 76.2% | $6.25 |
| 7 | Grok 4.1 | 75.0% | $18 |
| 8 | GLM-4.7 | 73.8% | $2.18 |
| 9 | Kimi K2 | 73.4% | $2.29 |
| 10 | GLM-4.6 | 68.1% | $0.04 |
| 11 | Llama 4 | 68.47% | $0 |
| 12 | o3 | 69.1% | $31.50 |
| 13 | DeepSeek-R1 | 49.2% | $0.69 |

### Tabela B: Ranking por Eficiência (Melhor Custo-Benefício)

| Rank | Modelo | SWE % | Eficiência | Categoria |
|---|---|---|---|---|
| 1 | Llama 4 Maverick | 68.47% | ∞ | Open-source |
| 2 | GLM-4.6 | 68.1% | 1,702.5x | Elite |
| 3 | Gemini 2.5 Pro | 77.1% | 203.2x | Elite |
| 4 | GLM-4.7 | 73.8% | 33.9x | Excelente |
| 5 | Kimi K2 | 73.4% | 32.1x | Excelente |
| 6 | DeepSeek-R1 | 49.2% | 71.3x | Muito Bom |
| 7 | Gemini 3 Pro | 76.2% | 12.2x | Muito Bom |
| 8 | GPT-5.2 | 80.0% | 9.1x | Bom |
| 9 | Claude Sonnet 4.5 | 77.2% | 4.3x | Bom |
| 10 | Grok 4.1 | 75.0% | 4.2x | Bom |
| 11 | Claude Opus 4.5 | 80.9% | 2.7x | Justo |
| 12 | o3 | 69.1% | 2.2x | Caro |
| 13 | Claude Opus 4.1 | 77.0% | 0.86x | Muito Caro |

---
[^4_1]: https://bentoml.com/llm/inference-optimization/llm-inference-metrics

[^4_2]: https://conikeec.substack.com/p/the-token-trap-why-your-favorite

[^4_3]: https://www.augmentcode.com/tools/8-top-ai-coding-assistants-and-their-best-use-cases

[^4_4]: https://artificialanalysis.ai/methodology/performance-benchmarking

[^4_5]: https://www.reddit.com/r/LLMDevs/comments/1im8tel/how_many_tokens_are_you_using_per_month/

[^4_6]: https://www.superblocks.com/blog/enterprise-ai-app-generation

[^4_7]: https://developer.nvidia.com/blog/llm-benchmarking-fundamental-concepts/

[^4_8]: https://www.reddit.com/r/ChatGPT/comments/1ievup8/how_many_tokens_do_you_use_for_ai_coding_per_month/

[^4_9]: https://www.builder.io/blog/best-ai-tools-2026

[^4_10]: https://www.reddit.com/r/LocalLLaMA/comments/162pgx9/what_do_yall_consider_acceptable_tokens_per/

[^4_11]: https://smarterarticles.co.uk/the-real-cost-of-vibe-coding-when-ai-over-delivers-on-your-dime

[^4_12]: https://playcode.io/blog/best-ai-coding-assistants-2026

[^4_13]: https://intuitionlabs.ai/articles/llm-api-pricing-comparison-2025

[^4_14]: https://getdx.com/blog/ai-coding-tools-implementation-cost/

[^4_15]: https://www.reddit.com/r/datascience/comments/1q85xuw/whats_your_2026_data_science_coding_stack_ai/



[^3_1]: https://www.linkedin.com/posts/vk-maurya_ai-llm-softwareengineering-activity-7410571617254244352-Kevq

[^3_2]: https://automatio.ai/models/glm-4-7

[^3_3]: https://ai-primer.com/en/engineer/reports/2025-12-22

[^3_4]: https://atalupadhyay.wordpress.com/2025/12/23/glm-4-7-zhipu-ais-game-changing-open-source-model/

[^3_5]: https://www.cometapi.com/the-guide-to-claude-opus-4--4-5-api-pricing-in-2026/

[^3_6]: https://www.finout.io/blog/claude-pricing-in-2026-for-individuals-organizations-and-developers

[^3_7]: https://rahulkolekar.com/openai-api-pricing-in-2026-a-practical-guide-models-tokens-tiers-tools/

[^3_8]: https://openai.com/api/pricing/

[^3_9]: https://www.getmaxim.ai/articles/gemini-3-pro-vs-claude-opus-4-5-vs-gpt-5-the-ultimate-frontier-model-comparison/

[^3_10]: https://sumgenius.ai/blog/gpt-5-1-vs-gemini-3-vs-claude-opus-4-5-comparison-2025/

[^3_11]: https://intuitionlabs.ai/articles/llm-api-pricing-comparison-2025

[^3_12]: https://masterconcept.ai/blog/gemini-1-5-pro-1-5-flash-price-drop-down-with-more-updated-models/

[^3_13]: https://robotmunki.com/blog/llm-landscape.html

[^3_14]: https://www.glbgpt.com/hub/claude-ai-plans-2026/

[^3_15]: https://sparkco.ai/blog/anthropic-claude-vs-openai-gpt-a-deep-dive-comparison

[^3_16]: https://cientistasdigitais.com/inteligencia-artificial/grok-4-supera-openai-google-e-anthropic-e-lidera-benchmarks-de-ia/

[^3_17]: https://llm-stats.com/models/glm-4.7

[^3_18]: https://pandaily.com/kimi-k2-thinking-ranks-no-2-globally-no-1-among-open-source-models-in-latest-artificial-analysis-report

[^3_19]: https://skywork.ai/blog/agent/kimi-k2-vs-gpt5-reasoning/

[^3_20]: https://aigazine.com/startups/glm-46-benchmark-shows-major-leap-in-ai-reasoning-ig--a

[^3_21]: https://blog.kilo.ai/p/glm-46-a-data-driven-look-at-chinas

[^3_22]: https://arbisoft.com/blogs/llama-4-a-bold-leap-forward-or-a-misstep

[^3_23]: https://ai.meta.com/blog/llama-4-multimodal-intelligence/

[^3_24]: https://www.youtube.com/watch?v=RFTqeFpclx8

[^3_25]: https://www.siliconflow.com/articles/benchmark

[^3_26]: https://www.artificialintelligence-news.com/news/baidu-ernie-x1-and-4-5-turbo-high-performance-low-cost/

[^3_27]: https://www.datacamp.com/blog/ernie-4-5-x1

[^3_28]: https://artificialanalysis.ai/models/mistral-large-2

[^3_29]: https://pricepertoken.com

[^3_30]: https://regional.chinadaily.com.cn/wic/2026-01/20/c_1155829.htm

[^3_31]: https://simonwillison.net/2025/Oct/15/claude-haiku-45/

[^3_32]: https://caylent.com/blog/claude-haiku-4-5-deep-dive-cost-capabilities-and-the-multi-agent-opportunity

[^3_33]: https://blog.promptlayer.com/an-analysis-of-google-models-gemini-1-5-flash-vs-1-5-pro/

[^3_34]: https://artificialanalysis.ai/models/gemini-1-5-flash

[^3_35]: https://mistral.ai/news/mixtral-8x22b

[^3_36]: https://www.reddit.com/r/Bard/comments/1fxsr7b/gemini_15_flash_8b_half_the_price_of_15_flash/

[^3_37]: https://huggingface.co/zai-org/GLM-4.7

[^3_38]: https://macaron.im/blog/what-is-glm-4-7

[^3_39]: https://vertu.com/ar/نمط-الحياة/glm-4-7-vs-gpt-5-1-vs-claude-sonnet-4-5-ai-coding-model-comparison/

[^3_40]: https://docs.z.ai/guides/llm/glm-4.7

[^3_41]: https://www.reddit.com/r/singularity/comments/1qh802r/zai_launches_glm47flash_30b_coding_model_592/

[^3_42]: https://artificialanalysis.ai/models/glm-4-7-non-reasoning

[^3_43]: https://binaryverseai.com/glm-4-7-flash-benchmarks-setup-pricing-vs-qwen3/

[^3_44]: https://www.facebook.com/0xSojalSec/posts/glm-47-just-dropped-and-the-benchmark-jumps-are-substantial-129-on-swe-bench-mul/1401953338125732/

[^3_45]: https://z.ai/blog/glm-4.7

[^3_46]: https://www.youtube.com/watch?v=NKGiDGBgtqQ

