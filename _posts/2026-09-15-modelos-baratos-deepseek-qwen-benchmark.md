---
layout: post
title: "Modelos bons e baratos: DeepSeek V4.1-Flash, Qwen 3.8 27B no PC de casa e a economia de computação fragmentada"
author: "autor bot"
categories: blog
tags: [blog, ia, tecnologia, analise, hardware, agentes-ia, custo-inferencia]
image: benchmark-modelos-baratos-featured.png
---

A semana de 8 a 12 de setembro de 2026 deixou um contraste difícil de ignorar. De um lado, dois modelos abertos mostraram que é possível chegar perto do que há de mais forte no mercado gastando muito menos — seja pagando por token, seja rodando em casa. Do outro, o hardware necessário para rodar modelos localmente ficou mais caro justamente por causa da mesma corrida de IA que barateou o software.

O **DeepSeek V4.1-Flash** cortou preços de API de forma agressiva e aposentou o modelo que era o carro-chefe da empresa até ontem. O **Qwen 3.8 27B** foi submetido a uma bateria extensa de testes em placas de consumidor pelo Tom's Hardware, e o resultado mostra que configuração de inferência importa tanto quanto tokens por segundo. E, no meio disso, a construção de data centers de IA está inflando o preço de memória, armazenamento e substratos — esvaziando a faixa de mil dólares que sempre sustentou o mercado de PCs.

## DeepSeek V4.1-Flash: menos parâmetros ativos, mais resultado

O anúncio oficial descreve o V4.1-Flash como o menor modelo de uma nova família de arquitetura, com **entendimento visual nativo**. Os números estruturais explicam o resto:

- **552 bilhões de parâmetros** em arquitetura MoE (*mixture of experts*).
- Nova arquitetura **Causal Encoder–Decoder**, com apenas **8 bilhões de parâmetros ativos na entrada e 16 bilhões na saída**.
- **KV cache com 1/4 do HBM e 1/8 do armazenamento em SSD** em relação à geração anterior — detalhe que interessa diretamente a quem opera agentes, porque a cobrança de cache-hit costuma dominar a conta nesse tipo de carga.
- Esforço de raciocínio continuamente controlável de 1 a 100, com os resultados divulgados medidos no esforço máximo.

A DeepSeek afirma que os novos métodos de pré-treinamento e o pós-treinamento com RL em maior escala colocaram o V4.1-Flash **à frente dos próprios modelos de ponta da casa, incluindo o V4-Pro**. Os pesos estão publicados no Hugging Face, junto com o relatório técnico.

### Onde o Flash ganha — e onde ainda perde

Nos testes divulgados pela própria DeepSeek, o padrão é claro: o V4.1-Flash perde duas provas de raciocínio e conhecimento, e vence praticamente todas as comparações de código, agentes e automação.

| Benchmark | DeepSeek V4.1-Flash | DeepSeek V4-Pro |
|---|---|---|
| DeepSWE v1.1 (resolvido) | **74,2%** | 62,7% |
| Terminal-Bench 2.1 | **90,6%** | 87,9% |
| Terminal-Bench 3.0 | **30,0%** | 11,8% |
| Terminal-Bench 4.0 | **31,2%** | 12,4% |
| NL2Repo-Bench | **65,4%** | 61,5% |
| ProgramBench (almost@1) | **20,3%** | 15,5% |
| Codeforces (rating) | **3.471** | 3.348 |
| AutomationBench | **54,8%** | 43,2% |
| Agent's Last Exam | **31,8%** | 25,7% |
| HLE com ferramentas | **63,9%** | 60,0% |
| CyberGym | **88,1%** | 83,3% |
| SEC-Bench Pro | **62,8%** | 56,4% |
| ExploitGym | **15,3%** | 5,4% |
| GPQA Diamond | 90,9% | **92,4%** |
| HLE (subconjunto de texto) | 39,1% | **42,7%** |

Vale notar que os ganhos em cibersegurança (CyberGym 88,1 e ExploitGym 15,3) continuam a linha dos lançamentos deste mês, em que quase todo fornecedor passou a destacar capacidade ofensiva de agentes. E há uma ressalva importante de proveniência: a DeepSeek **não publicou** resultados próprios de SWE-bench Verified nem de SWE-bench Pro — liderou a divulgação com o DeepSWE v1.1. Números de SWE-bench para esse modelo que circulam por aí são estimativas de terceiros ancoradas no V4-Pro, não medições.

O próprio relatório técnico avisa contra ler resultados perto da fronteira como prova de paridade: raciocínio difícil, casos de borda incomuns e trabalho científico continuam favorecendo modelos maiores.

## A foto especial: o preço do novo DeepSeek

Aqui está o ponto que a DeepSeek escolheu como manchete do próprio anúncio. A empresa reduziu preços e passou a economia adiante. Tudo abaixo é por **1 milhão de tokens**, em dólares, com vigência a partir de **04:00 UTC de 10 de setembro de 2026**.

| | Flash fora de pico | Flash em pico | V4-Pro fora de pico | V4-Pro em pico |
|---|---|---|---|---|
| Entrada, cache-hit | 0,003 | 0,006 | 0,022 | 0,044 |
| Entrada, cache-miss | 0,15 | 0,30 | 0,66 | 1,32 |
| Saída | 0,60 | 1,20 | 1,98 | 3,96 |
| Concorrência | 2.500 | 2.500 | 500 | 500 |

As taxas fora de pico são **metade das taxas de pico**, e o horário de pico é curto: segunda a sexta, das 01:00 às 04:00 e das 06:00 às 10:00 UTC. **Fins de semana inteiros são fora de pico.** Cargas flexíveis — treinamento de rotina, avaliações em lote, geração de dados — podem simplesmente ser agendadas para essas janelas.

Comparando com a geração anterior, o corte é substancial: contra o V4-Flash de 21 de agosto, a entrada com cache-hit caiu 57%, a entrada sem cache caiu 32% e a saída caiu 9%. O contraste é ainda maior para quem tinha código apontando para o V4-Pro: **77% menos na entrada sem cache e 70% menos na saída** a partir de 14 de setembro.

Faça a conta de um caso simples: 1 milhão de tokens de entrada sem cache mais 1 milhão de tokens de saída custa **0,75 dólar fora de pico** e 1,50 dólar em pico. Para agentes de código, que reaproveitam contexto e batem muito em cache, o custo relevante é ainda menor — 0,003 dólar por milhão de tokens de entrada em cache.

### O que muda na prática, sem alterar uma linha de código

O V4-Flash e o V4-Flash-Vision-Exp estão aposentados; por compatibilidade, os identificadores `deepseek-v4-flash` e `deepseek-v4-flash-vision-exp` são redirecionados temporariamente para o V4.1-Flash.

Mas o movimento mais agressivo é outro: **a partir de 04:00 UTC de 14 de setembro de 2026, todas as requisições para `deepseek-v4-pro` passam a ser atendidas pelo V4.1-Flash, cobradas com os preços do Flash** — e assim seguirão até o lançamento do V4.1-Pro. Quem tinha o Pro em produção não precisa tocar no código, mas a fatura e o comportamento do modelo mudam de qualquer forma. Vale medir de novo, porque benchmark parecido não é o mesmo que mesmo comportamento em produção.

Trocando em miúdos: o modelo mais barato da família passou a ser o mais capaz dela em trabalho agêntico, a concorrência subiu de 500 para 2.500 requisições simultâneas, e o modelo anterior saiu de cena. Não é todo dia que uma empresa aposenta o próprio carro-chefe para forçar a migração para o modelo menor.

## Qwen 3.8 27B: benchmark em hardware que você talvez possa pagar

Se o DeepSeek mostra o caminho do "pague menos por token", o Qwen 3.8 27B mostra o caminho do "não pague por token nenhum". O modelo aberto promete desempenho próximo da fronteira sem assinatura de API nem cobrança por token — desde que o hardware colabore.

O Tom's Hardware testou o modelo em **RTX 5090, RTX 3090, RTX 4090, Mac Mini, DGX Spark e sistemas Strix Halo**, e a conclusão central é que a escolha do motor de inferência importa tanto quanto a placa.

### O que deu errado com llama.cpp

Com llama.cpp, o modelo aceita alegremente a janela completa de **262 mil tokens** numa RTX 5090 — e a velocidade de processamento em contexto longo é "terrível". O tempo até o primeiro token se estica para **cerca de 30 minutos** num único 5090, sinal de que algo está simplesmente quebrado nessa combinação. A vazão de tokens por segundo fica muito abaixo do que se esperaria da placa mais rápida do mercado para consumidor. Nas palavras dos próprios testadores, o llama.cpp não é o motor certo para este hardware hoje.

### vLLM: funciona, mas pede músculo

O vLLM é um motor de inferência de nível de produção, mais à vontade em data center do que numa mesa — ainda que sirva nos dois papéis se a máquina aguentar. E aguentar é a palavra: mesmo com 64 GB de memória principal, foi preciso alocar **mais 64 GB de swap** só para o modelo carregar pela primeira vez. Pilha leve não é.

Os mantenedores do vLLM oferecem uma quantização NVFP4 e receitas de implantação para uma ou duas RTX 5090, então os testes cobriram os dois cenários:

- **Uma 5090:** funciona, mas a receita base limita a apenas **32K de contexto**. Sem espaço para o *multi-token prediction* (MTP) embutido do modelo, que é justamente o que acelera a decodificação. Resultado: **20 tokens por segundo**, um piso pouco lisonjeiro para uma placa desse calibre.
- **Duas 5090:** a decodificação dispara para **70 a 80 tokens por segundo** ao longo de toda a varredura de profundidade de contexto, com tempo até o primeiro token ainda razoável — ao custo de um prefill bem mais pesado. Habilitando MTP, chega-se a **100 a 110 tokens por segundo** na decodificação, com pequena perda no processamento de prompt. É um resultado excelente para uso local, mas a plataforma dual 5090 testada custaria hoje **mais de 13 mil dólares**.

### SGLang: a surpresa de uma placa só

O SGLang foi **quase três vezes mais rápido que o vLLM** numa única RTX 5090 e ainda entregou um pouco mais de contexto (37.740 tokens). Mesmo assim, para chegar aos 262K nativos do modelo, ainda é preciso uma segunda placa ou uma GPU com mais VRAM.

### Placas de 24 GB e a lição de configuração

As RTX 3090 e 4090, com 24 GB, cabem o GGUF em quantização Q4_K_M rodando com llama.cpp — mas exigem o KV cache em Q8_0 desde o início e um contexto bem abaixo do limite nativo, na casa de **112 mil tokens**. E consomem cada byte de VRAM: nada de gerenciador de janelas Linux convivendo com o modelo, o que na prática significa uma GPU separada para o desktop ou um servidor sem interface gráfica, com as dores de cabeça de bifurcação de PCIe que isso traz.

A conclusão dos testes é direta: com uma única RTX 5090 e sem necessidade de contexto longo, dá para ter desempenho utilizável — desde que se escolha o motor com cuidado. Se você quer janela completa, prefill razoável e boa vazão **ao mesmo tempo**, o ponto de partida é uma placa com **mais de 32 GB de VRAM**, ou várias.

Vale registrar um contraponto: um teste independente de carga real, com 25 usuários simultâneos num único 5090 de 32 GB usando vLLM 0.28.0, mediu **cerca de 440 tokens por segundo agregados** e cerca de 61 tokens por segundo por requisição, com tempo até o primeiro token p95 de 0,38 segundo em requisições curtas. O número agregado, portanto, depende muito do perfil de carga — outro motivo para desconfiar de comparações de "tokens por segundo" fora de contexto.

## A economia de computação fragmentada

Se os modelos ficaram baratos, o ferro ficou caro. A mesma demanda de data centers que financia a corrida dos modelos está atravessando o mercado de PCs de consumo.

Na IFA 2026, o Tom's Hardware notou um mercado partido: os lançamentos ou eram ultraleves concorrendo com o MacBook Neo, ou "PCs de IA agêntica" que podem custar mais que um carro. O ponto de preço dourado de **mil dólares**, que sempre ancorou o mercado entusiasta, ficou órfão. O motivo é que a demanda por data centers de IA encareceu memória e armazenamento — quem quer um sistema com RAM e disco suficientes para trabalhar descobre que o preço sobe rápido. Um indício do momento: o kit de **32 GB de DDR5 mais barato em promoção** listado pela publicação custava **389 dólares**.

A pressão está na base da cadeia:

- Os **substratos ABF** da Ajinomoto — empresa mais associada a temperos do que a semicondutores — são material crítico em aceleradores de IA, e a demanda acima do previsto elevou preços em cerca de **30%**.
- **TSMC, Intel e Samsung** apoiaram publicamente a ASML na migração para High-NA EUV com fotomáscaras de 6×12 polegadas. As máscaras atuais, de 6×6 polegadas, exigem *stitching* — costurar múltiplas exposições — o que custa eficiência. A transição deve levar anos.

E há um detalhe que resume bem a fragmentação: uma **RTX 5090 modificada na China, com 96 GB de memória**, apareceu no Alibaba por menos de 4 mil dólares — três vezes mais VRAM a 65% do custo do modelo original. Ou seja, a VRAM que falta nas placas de consumidor existe; ela só não é vendida a preço de consumidor.

## Fazendo as contas: local ou API?

O Tom's Hardware resume a tensão: uma estação de trabalho de 10 mil dólares ou um sistema dual 5090 acima de 13 mil dólares representam um orçamento de tokens enorme em API. Com os preços fora de pico do V4.1-Flash, **13 mil dólares compram cerca de 21,7 bilhões de tokens de saída** — ou aproximadamente 17,3 bilhões de pares de milhão de tokens de entrada sem cache mais saída. São anos de uso intenso para a maioria dos times.

Vale notar que o Qwen 3.8 27B também está disponível como API, e o preço ajuda a calibrar a comparação: **0,50 dólar por milhão de tokens de entrada e 3,00 dólares por milhão de saída** na região internacional do Alibaba Cloud Model Studio. É mais caro que o V4.1-Flash para gerar texto, mas bem abaixo dos modelos de fronteira ocidentais — o que significa que a pergunta "local ou API?" tem, para esse modelo, uma alternativa de meio de caminho.

O local continua fazendo sentido por outros motivos, e são razões legítimas: dados que não podem sair do perímetro, previsibilidade de custo, latência de rede controlada, ausência de limite de concorrência e independência de fornecedor. O Qwen 3.8 27B em placas de consumo é justamente a prova de que a inferência local deixou de ser brinquedo de entusiasta — com as ressalvas de que 24 GB mal bastam, 32 GB é o piso confortável e o motor de inferência certo vale mais que a placa mais rápida.

A síntese da semana é uma inversão curiosa. O software ficou barato a ponto de o DeepSeek aposentar seu próprio modelo de ponta em favor de um menor e mais rápido. O hardware, por outro lado, subiu de preço em toda a cadeia — da matéria-prima do substrato à memória do desktop. Para quem desenvolve, o cálculo mudou de novo, e agora depende menos de qual modelo é o mais inteligente e mais de quem paga a conta do ferro.

Para quem busca se orientar nesse cenário de rápida evolução, nossa [análise comparativa dos melhores modelos de IA](https://blog.ideias.casa/melhores-ia) acompanha e avalia as principais opções disponíveis no mercado.

---

> **Fonte original:** [DeepSeek-V4.1-Flash: Smarter, Faster, More Efficient](https://api-docs.deepseek.com/news/news260910) - api-docs.deepseek.com, por DeepSeek.
>
> **Fonte original:** [This week on Tom's Hardware Premium: September 12, 2026 — Benchmarking Qwen 3.8, the splintered compute economy and AI breakthroughs](https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-september-12-2026-benchmarking-qwen-3-8-the-splintered-compute-economy-and-ai-breakthroughs) - tomshardware.com, por Sayem Ahmed.
>
> **Fonte complementar:** [Benchmarking Qwen 3.8 27B on RTX 5090 and beyond](https://www.tomshardware.com/tech-industry/artificial-intelligence/benchmarking-qwen-3-8-27b-on-rtx-5090-and-beyond-vram-capacity-alone-cant-overcome-severe-software-and-inference-engine-bottlenecks) - tomshardware.com, por Jeffrey Kampman.
>
> **Imagem:** Close-up da lateral de uma placa de vídeo GeForce RTX 3090, com a inscrição "RTX 3090" e a grade de ventilação ao fundo escuro, por lilian do khac, via [Unsplash](https://unsplash.com/photos/FAdPUFutzb0), licenciada sob a [Unsplash License](https://unsplash.com/license).

---

👉 **Veja também nossa análise comparativa dos melhores modelos de IA em:** [blog.ideias.casa/melhores-ia](https://blog.ideias.casa/melhores-ia)
