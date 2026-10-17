---
layout: post
title: "NVIDIA deixa de vender apenas a GPU: RTX Spark chega aos laptops a partir de 2.599 dólares"
author: "autor bot"
categories: blog
tags: [blog,ia,tecnologia,hardware,analise,agentes-ia,computacao-local]
image: rtx-spark-nvidia-laptops-featured.jpg
---

Durante duas décadas, “NVIDIA dentro do laptop” significou uma GPU — a placa de vídeo, o processador gráfico — ao lado de uma CPU escolhida pelo fabricante. A partir de 16 de outubro de 2026, essa divisão de trabalho começou a mudar: os primeiros laptops com o **NVIDIA RTX Spark** chegaram às lojas dos Estados Unidos por 2.599,99 dólares, e o chip que a empresa chama de superchip é, na prática, o computador inteiro projetado por ela. O RTX Spark reúne num só pacote um processador Grace de arquitetura Arm, uma GPU Blackwell RTX e até 128 GB de memória unificada — um único bloco de RAM usado ao mesmo tempo pela CPU e pela GPU. Segundo a NVIDIA, a proposta é rodar modelos de IA e agentes localmente, sem depender da nuvem, em laptops de 14 a 16 polegadas com Windows 11.

A diferença é que, agora, a NVIDIA entrega aos fabricantes não apenas uma GPU discreta para colocar ao lado de um processador Intel ou AMD, mas o projeto completo — CPU, GPU, interconexão, memória e boa parte do software. Os OEMs — os fabricantes que montam e vendem os PCs, como ASUS, Dell e Lenovo — continuam responsáveis por design, fabricação, varejo e suporte. A NVIDIA não lançou um laptop com a própria marca. Ainda assim, a empresa que construiu seu império vendendo componentes para os computadores dos outros quer definir a arquitetura do computador inteiro.

## O que foi anunciado

A NVIDIA confirmou a disponibilidade dos laptops RTX Spark em [comunicado de 16 de outubro](https://nvidianews.nvidia.com/news/nvidia-rtx-spark-pcs-available-today-a-new-beginning-for-windows-pcs). O chip foi [apresentado em junho, no Computex](https://nvidianews.nvidia.com/news/nvidia-microsoft-windows-pcs-agents-rtx-spark), e chegou ao varejo em outubro. São seis fabricantes no lançamento — ASUS, Dell, HP, Lenovo, Microsoft e MSI — com modelos adicionais da Acer e da Gigabyte previstos para depois.

Entre os modelos com preço confirmado nos Estados Unidos, a linha parte de 2.599,99 dólares, mas os valores variam bastante conforme o modelo e a configuração:

| Modelo | Tela | Configuração de entrada | Preço inicial (EUA) |
|---|---|---|---|
| Microsoft Surface Laptop Ultra | 15", 3:2, 3270 x 2180 | 18 núcleos de CPU · 24 GB de RAM · 512 GB de SSD | 2.599,99 dólares |
| ASUS ProArt P14 | 14", OLED 2880 x 1800 | 18 núcleos · 24 GB · 512 GB | 2.599,99 dólares |
| ASUS ProArt P16 | 16", OLED 4K | 24 GB · 512 GB | 2.799,99 dólares |
| HP OmniBook Ultra 16 | 16", OLED 3K | 32 GB · 1 TB | 3.199,99 dólares |
| Lenovo Yoga 9n 2 em 1 | 16", OLED 2880 x 1800 | 18 núcleos · 32 GB · 512 GB | 2.999,99 dólares |
| Dell XPS 16 Creator Edition | 16", OLED 3200 x 2000 | 32 GB · 512 GB | 3.799,99 dólares |

Os valores foram divulgados pela [PCWorld](https://www.pcworld.com/article/3256085/here-are-all-the-rtx-spark-laptops-available-at-launch-going-up-to-7000.html) na pré-venda e conferidos pelo [Tom's Hardware](https://www.tomshardware.com/laptops/nvidia-rtx-spark-devices-are-now-officially-on-sale-secure-the-surface-laptop-ultra-or-other-rtx-spark-laptops-here-starting-at-usd2-599-where-to-buy-pricing-and-availability-revealed-on-several-models) no dia do lançamento. A HP confirmou os preços no [próprio comunicado](https://www.hp.com/us-en/newsroom/press-releases/2026/hp-leads-the-expansion-of-the-local-ai-era-from-gb300-ai-workstations-to-rtx-spark-windows-pcs.html) de 7 de outubro; a Lenovo divulgou 2.999,99 dólares para o Yoga 9n 2 em 1.

No topo da linha, o Surface Laptop Ultra com 128 GB e 1 TB chega a 5.899,99 dólares, e o ASUS ProArt P16 com 128 GB e 2 TB alcança 6.999,99 dólares, segundo [The Verge](https://www.theverge.com/tech/1012748/nvidia-rtx-spark-windows-arm-laptops-asus-hp-lenovo-impressions). É território de estação de trabalho, não de notebook fino de consumo — e o preço de entrada compra 24 GB de memória, não os 128 GB que dão sentido à plataforma.

A MSI chegou ao lançamento com o Prestige N16 Flip AI+, um conversível de 16 polegadas com até 128 GB de memória, a partir de 3.299,99 dólares segundo a imprensa especializada. Nos Estados Unidos, porém, as listagens de pré-venda apontavam entrega para o fim de dezembro — ou seja, o modelo foi anunciado na primeira leva, mas não estava necessariamente pronta-entrega no primeiro dia. O mesmo vale para configurações de topo de outros fabricantes. A HP também colocou o OmniBook X 14, de 14 polegadas, a 2.999,99 dólares.

Em design, a NVIDIA fala em máquinas a partir de 14 mm de espessura e 1,36 kg. Na prática, os modelos anunciados vão de 1,48 kg (ProArt P14) a 2,22 kg (OmniBook Ultra 16) — mais pesados do que a promessa da plataforma indica, mas ainda dentro do território de notebooks de alto desempenho.

## O que tem dentro do superchip

O RTX Spark não é um processador tradicional com uma GPU separada. A NVIDIA montou um único pacote com duas metades: uma CPU Grace de até 20 núcleos e uma GPU Blackwell RTX com até 6.144 núcleos CUDA — as unidades de cálculo da placa de vídeo, que não se comparam em número aos núcleos do processador. As duas metades são ligadas pela NVLink-C2C, a interconexão proprietária da NVIDIA, a 600 GB/s. A memória é um único bloco de LPDDR5X — o tipo de RAM de baixo consumo usado em notebooks finos — compartilhado entre CPU e GPU, que chega a 128 GB.

A NVIDIA promete até 1 petaflop de desempenho de IA em FP4 — um petaflop equivale a mil trilhões de operações por segundo, e FP4 significa que cada número é guardado com apenas 4 bits, uma precisão reduzida que acelera a inferência (o uso de um modelo já treinado) mas não é comparável aos cálculos científicos em FP32. A arquitetura Arm é a mesma família usada em celulares e nos chips M da Apple; ela não executa nativamente os programas x86, feitos para processadores Intel e AMD.

A MediaTek colaborou no desenvolvimento da CPU, e os 20 núcleos são 10 Cortex-X925 e 10 Cortex-A725 — núcleos Arm padrão licenciados, não um projeto próprio como o Oryon da Qualcomm. O processador como um todo, porém, foi codesenhado pela NVIDIA com a MediaTek, e é essa combinação com a GPU que a empresa vende. Nos testes independentes, a CPU fica atrás dos chips da Apple em tarefas de um e de vários núcleos — um desempenho aquém do preço, ainda que isso não meça o desempenho nas cargas de IA.

A GPU é a parte mais forte: são 6.144 núcleos CUDA, a mesma contagem da RTX 5070 de mesa. Nos testes do The Verge, o desempenho em jogos ficou entre uma RTX 5070 e uma RTX 5060 para laptops. CUDA, a plataforma de software da NVIDIA para computação em GPU, é o que torna o ecossistema da empresa difícil de replicar.

Há duas variantes do chip. A de entrada tem 18 núcleos de CPU e 5.120 núcleos CUDA, com 24 GB a 32 GB de memória nas configurações de lançamento. A de topo mantém os 20 núcleos de CPU e sobe para os 6.144 núcleos CUDA. Os modelos de 128 GB divulgados até agora — como o Surface Laptop Ultra e o ProArt P16 — usam a variante de topo; os Surface e ProArt P14 de 2.599 dólares trazem 24 GB. Essa distinção importa: a configuração de entrada não tem a mesma capacidade de rodar modelos grandes que a de 5.899 ou 6.999 dólares.

A memória unificada é o argumento central. Em um laptop comum, a CPU usa a RAM do sistema e a GPU usa a VRAM dedicada, a memória própria da placa de vídeo; carregar um modelo grande exige copiar dados entre as duas ou torcer para ele caber na VRAM. No RTX Spark, CPU e GPU endereçam o mesmo espaço — 128 GB, quatro a oito vezes a memória de um notebook comum. É a mesma ideia que a Apple usa nos chips da série M e que a AMD adotou no Ryzen AI Max. A diferença é que a NVIDIA traz para essa arquitetura o mesmo ecossistema de software que domina a IA em data centers.

## A promessa da IA local — e o que os testes mostram

A NVIDIA afirma que o RTX Spark consegue rodar modelos de até 120 bilhões de parâmetros — cada parâmetro é um dos valores internos que definem o comportamento da rede neural; quanto mais parâmetros, maior e mais capaz o modelo, mas também mais pesado — com janelas de contexto de até 1 milhão de tokens (as unidades de texto que o modelo consegue processar de uma vez; 1 milhão de tokens equivale a centenas de milhares de palavras, vários livros). Tudo isso inteiramente no dispositivo.

A empresa cita ainda o Qwen 3.8 Flash Next, um modelo de 125 bilhões de parâmetros que ativa cerca de 51 bilhões por vez, como exemplo do que cabe na máquina. É essa ativação parcial que permite que um modelo maior que o teto citado rode no equipamento: nem todos os parâmetros são acionados a cada resposta. Esses números são da própria NVIDIA: até agora, não há benchmark independente amplamente divulgado que confirme o desempenho em modelos desse porte.

O que já existe são os testes de uma semana da imprensa especializada. O The Verge usou cinco laptops RTX Spark e publicou um balanço no dia do lançamento. A experiência com agentes — programas de IA que executam tarefas em etapas, usando ferramentas, em vez de apenas responder perguntas — foi descrita como “beta”: ao rodar o Qwen3.8-27B no Surface Laptop Ultra, uma tarefa simples, converter arquivos PNG em JPG, levou minutos, com as ventoinhas no máximo e o chassi esquentando. Em outro teste, um agente passou 30 minutos trabalhando e terminou com um erro. Na [avaliação do Surface Laptop Ultra](https://www.theverge.com/tech/1012628/microsoft-surface-laptop-ultra-review), a nota foi 6 de 10, com o desempenho de CPU entre os pontos negativos.

A bateria também exige ressalvas. O The Verge mediu cerca de sete horas no Surface Laptop Ultra em uso com modelos locais, apps variados e jogos; com tarefas mais leves, a média subiu para dez horas ou mais. No ASUS ProArt P16, com bateria de 99,9 Wh — praticamente o limite que companhias aéreas permitem levar na cabine sem autorização —, o teste de trabalho real durou de cinco a cinco horas e quarenta minutos. São números razoáveis para um laptop dessa potência, mas longe da ideia de um servidor de IA que roda o dia inteiro longe da tomada.

Em jogos, o desempenho é mais competitivo do que a CPU sugere. Nos títulos testados pelo The Verge, a maioria rodou perto de 60 fps (quadros por segundo) em 1440p, resolução acima do Full HD, com configurações médias e DLSS no modo performance — DLSS é o recurso da NVIDIA que gera a imagem em resolução menor e a amplia por IA. Alguns jogos exigem configurações baixas, e títulos com anti-cheat — Battlefield, Call of Duty, Valorant e League of Legends — ainda dependem de versões compatíveis com Arm.

A compatibilidade de programas melhorou muito desde a primeira geração de PCs Copilot+, o selo da Microsoft para computadores com IA local. Nos testes do The Verge, o emulador Prism — uma camada que traduz instruções x86 para Arm — deu conta da maioria dos programas. A NVIDIA diz que o RTX Spark tem suporte a 97% dos 15 mil pacotes Python mais usados e que trouxe o primeiro PyTorch com CUDA para Windows on Arm. Para desenvolvedores, esse é o ponto que realmente diferencia a plataforma.

## Por que isso importa

O RTX Spark muda a relação entre a NVIDIA e os fabricantes. A empresa agora define a CPU, a GPU, a memória e a pilha de software, e entrega uma plataforma de referência para os OEMs adaptarem. É uma fatia muito maior da cadeia de valor — e uma pressão direta sobre Intel, AMD e Qualcomm, que historicamente controlam o “cérebro” do PC.

Isso não significa que a NVIDIA virou uma fabricante de laptops. Não há um notebook com a marca NVIDIA, e a empresa não anunciou planos de vender um. Ela continua dependendo dos parceiros para fabricar, distribuir e dar suporte. O movimento é o de uma empresa que quer ser dona da plataforma por dentro, não da marca na tampa. A lógica comercial sugere que os OEMs aceitaram porque mantêm o cliente, a marca e a margem de varejo, enquanto a NVIDIA fica com a arquitetura e o ecossistema — mas nenhum fabricante se pronunciou sobre essa conta nesta apuração.

Há também uma questão de momento. O lançamento ocorre num período de [escassez de memória que já derrubou os embarques de PCs](https://blog.ideias.casa/escassez-hardware-pcs-memoria-ia) e encareceu componentes. Colocar 128 GB de LPDDR5X em um laptop é uma aposta contra a escassez: a NVIDIA está vendendo justamente o recurso que ficou mais caro. Isso limita o volume e empurra os preços para cima, mas também cria uma faixa em que poucos concorrentes conseguem competir de igual para igual.

## A concorrência não desapareceu

O RTX Spark não é o único caminho para a memória unificada. A AMD vende o Ryzen AI Max, que na geração Strix Halo chegou a 128 GB de memória unificada e, na linha AI Max 400, chega a 192 GB — com a vantagem de rodar programas x86 sem emulação, segundo a [Engadget](https://www.engadget.com/2187889/nvidia-rtx-spark-chip-could-give-windows-its-true-apple-silicon-moment). A Qualcomm aposta no Snapdragon X2 Elite, também com até 128 GB de LPDDR5X e foco em produtividade, bateria e recursos Copilot+; em desempenho por núcleo (single-core), a Qualcomm tende a levar vantagem sobre o RTX Spark, segundo a [PCWorld](https://www.pcworld.com/article/3154920/nvidia-has-the-muscle-but-qualcomm-may-have-the-better-ai-pc-brain.html). A Apple, com os chips M5, M5 Pro e M5 Max, já oferece memória unificada há anos e continua na frente em eficiência energética e desempenho de CPU, como mostram os [testes do The Verge](https://www.theverge.com/tech/1012748/nvidia-rtx-spark-windows-arm-laptops-asus-hp-lenovo-impressions).

O que o RTX Spark acrescenta é uma combinação que nenhum deles oferece ao mesmo tempo: GPU de classe RTX, até 128 GB de memória unificada e CUDA nativo em Windows. Para quem testa ou roda modelos grandes, isso é uma proposta difícil de replicar. Para quem quer um laptop premium para navegar, escrever e fazer planilhas, é caro demais e desnecessário.

## O que vem depois

A NVIDIA planeja desktops compactos RTX Spark para novembro de 2026 — a mesma plataforma, em um chassi feito para ficar ligado 24 horas por dia. Também apresentou uma prévia do DGX Station for Windows, uma estação de trabalho de mesa com 748 GB de memória compartilhada entre CPU e GPU — quase seis vezes os 128 GB do notebook — e até 20 petaflops FP4, o equivalente a 20 laptops RTX Spark. Não há data de venda para este produto.

O sucesso do RTX Spark, porém, não será medido apenas em unidades vendidas. O preço alto, a CPU abaixo dos concorrentes e a experiência de IA local ainda imatura tornam o produto um artigo de nicho — pelo menos até que mais aplicativos e agentes aproveitem a memória extra. O que a NVIDIA conseguiu foi ser a primeira a combinar 128 GB de memória unificada com CUDA em Windows, e pressionar Intel, AMD e Qualcomm a responder. Se essa configuração virar padrão, o lançamento de 16 de outubro pode vir a ser lembrado como o dia em que a NVIDIA deixou de vender apenas a GPU.

---

> **Ponto de partida:** [Nvidia RTX Spark Laptops Debut at 2.599 dólares, Hit 6 OEMs](https://tech-insider.org/nvidia-rtx-spark-windows-laptop-market-entry-2026/) e [NVIDIA RTX Spark Laptops Launch at 2.599 dólares, 128GB](https://tech-insider.org/nvidia-rtx-spark-laptops-launch-2599-128gb-2026/) — tech-insider.org, por Nadia Dubois e Elias Virtanen. São textos agregadores; os fatos foram conferidos nas fontes abaixo.
>
> **Fontes primárias e apuração:** [NVIDIA Newsroom, 16/10/2026](https://nvidianews.nvidia.com/news/nvidia-rtx-spark-pcs-available-today-a-new-beginning-for-windows-pcs); [NVIDIA Newsroom, 01/06/2026](https://nvidianews.nvidia.com/news/nvidia-microsoft-windows-pcs-agents-rtx-spark); [NVIDIA Blog, 07/10/2026](https://blogs.nvidia.com/blog/local-ai-rtx-spark-microsoft-windows-event/); [HP, 07/10/2026](https://www.hp.com/us-en/newsroom/press-releases/2026/hp-leads-the-expansion-of-the-local-ai-era-from-gb300-ai-workstations-to-rtx-spark-windows-pcs.html); [The Verge, 16/10/2026](https://www.theverge.com/tech/1012748/nvidia-rtx-spark-windows-arm-laptops-asus-hp-lenovo-impressions); [The Verge — review do Surface Laptop Ultra](https://www.theverge.com/tech/1012628/microsoft-surface-laptop-ultra-review); [PCWorld, 08/10/2026](https://www.pcworld.com/article/3256085/here-are-all-the-rtx-spark-laptops-available-at-launch-going-up-to-7000.html); [Tom's Hardware, 16/10/2026](https://www.tomshardware.com/laptops/nvidia-rtx-spark-devices-are-now-officially-on-sale-secure-the-surface-laptop-ultra-or-other-rtx-spark-laptops-here-starting-at-usd2-599-where-to-buy-pricing-and-availability-revealed-on-several-models); [Engadget, 05/06/2026](https://www.engadget.com/2187889/nvidia-rtx-spark-chip-could-give-windows-its-true-apple-silicon-moment).
>
> **Imagem:** “The AI Race”, de Gloria Mendoza, via [Better Images of AI](https://betterimagesofai.org/images?artist=GloriaMendoza), licenciada sob [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). A obra mostra corredores formados por placas de circuito e componentes de hardware — metáfora da corrida da IA que a NVIDIA tenta liderar com o RTX Spark.
>
> *Preços de varejo nos Estados Unidos, sem impostos, sujeitos a variação por configuração e região. Não há, até a publicação, data ou preço de lançamento no Brasil.*

---

👉 **Veja também nossa análise comparativa dos melhores modelos de IA em:** [blog.ideias.casa/melhores-ia](https://blog.ideias.casa/melhores-ia)
