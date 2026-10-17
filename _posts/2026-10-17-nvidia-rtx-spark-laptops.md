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

A NVIDIA promete até 1 petaflop de desempenho de IA em FP4 — um petaflop equivale a mil trilhões de operações por segundo, e FP4 significa que cada número é guardado com apenas 4 bits, uma precisão reduzida que acelera a inferência (o uso de um modelo já treinado) mas não é comparável aos cálculos científicos em FP32. O número é teórico e usa esparsidade, como a própria Microsoft anota nas letras miúdas do Surface. A arquitetura Arm é a mesma família usada em celulares e nos chips M da Apple; ela não executa nativamente os programas x86, feitos para processadores Intel e AMD.

A ficha oficial, publicada pela [NVIDIA](https://www.nvidia.com/en-us/products/rtx-spark/specifications/), separa as três versões do chip. As linhas marcadas com nota vêm de outras fontes, porque a página de especificações não as publica:

| Especificação | Laptop N1X (topo) | Laptop N1X (entrada) | Desktop N1X |
|---|---|---|---|
| GPU | Blackwell RTX, 6.144 núcleos CUDA | Blackwell RTX, 5.120 núcleos CUDA | Blackwell RTX, 6.144 núcleos CUDA |
| CPU | Grace, 20 núcleos (10 Cortex-X925 + 10 Cortex-A725) | Grace, 18 núcleos | Grace, 20 núcleos |
| NPU | NVIDIA NPU | NVIDIA NPU | não listada |
| Memória unificada | até 128 GB LPDDR5X | até 32 GB LPDDR5X | até 128 GB LPDDR5X |
| Barramento de memória | 256 bits | 256 bits | 256 bits |
| Velocidade da memória | 9.400 MT/s (¹) | 9.400 MT/s (¹) | não divulgada (¹) |
| Banda de memória | cerca de 300 GB/s (²) | cerca de 300 GB/s (²) | não divulgada (²) |
| Ligação entre CPU e GPU | NVLink-C2C, 600 GB/s (³) | não divulgada (³) | não divulgada (³) |
| Consumo (TDP) | 45 a 80 W | 45 a 80 W | 140 W |
| Desempenho de IA | 1 petaflop FP4, com esparsidade (⁴) | 827 teraflops FP4 (⁴) | 1 petaflop FP4, com esparsidade (⁴) |

(¹) A NVIDIA não publica a velocidade em MT/s. O valor de 9.400 MT/s aparece nas fichas dos fabricantes, como a da [Dell](https://www.storagereview.com/news/dell-xps-16-creator-edition-rtx-spark-n1x-windows-gb300-pro-precision) e a da [Lenovo](https://psref.lenovo.com/syspool/Sys/PDF/Yoga/Yoga_Pro_9_15N1X11/Yoga_Pro_9_15N1X11_Spec.PDF). Nada confirma que o desktop de 140 W use a mesma memória — nesse caso, é silêncio da fonte, não especificação.

(²) Os 300 GB/s vêm do [guia de portabilidade da própria NVIDIA](https://docs.nvidia.com/rtx-spark/rtx-spark-porting-guide/latest/overview.html), que descreve o chip dos laptops: a interface tem 256 bits de largura, com banda de 300 GB/s. O valor exato de 9.400 MT/s num barramento de 256 bits dá 300,8 GB/s; a NVIDIA arredonda para 300. Para o desktop, a NVIDIA não divulga banda.

(³) Os 600 GB/s do NVLink-C2C **não são banda de memória** — são a velocidade da ligação entre as duas metades do chip, e aparecem no comunicado de junho associados à versão de 6.144 núcleos. A NVIDIA não divulga esse número para a variante de entrada nem para o desktop.

(⁴) Os números de IA são teóricos e usam esparsidade — um recurso que faz o chip pular as contas com zero. A Microsoft anota isso nas letras miúdas do Surface; a página da NVIDIA traz 827 teraflops para a variante de entrada na tabela, mas 784 teraflops no metadado da mesma página — não há como saber qual é o número pretendido.

A MediaTek colaborou no desenvolvimento da CPU, e os 20 núcleos são 10 Cortex-X925 e 10 Cortex-A725 — núcleos Arm padrão licenciados, não um projeto próprio como o Oryon da Qualcomm. O processador como um todo, porém, foi codesenhado pela NVIDIA com a MediaTek, e é essa combinação com a GPU que a empresa vende. Nos testes independentes, a CPU fica atrás dos chips da Apple em tarefas de um e de vários núcleos — um desempenho aquém do preço, ainda que isso não meça o desempenho nas cargas de IA.

A GPU é a parte mais forte: são 6.144 núcleos CUDA, a mesma contagem da RTX 5070 de mesa. Nos testes do The Verge, o desempenho em jogos ficou entre uma RTX 5070 e uma RTX 5060 para laptops. CUDA, a plataforma de software da NVIDIA para computação em GPU, é o que torna o ecossistema da empresa difícil de replicar.

Há duas variantes do chip. A de entrada tem 18 núcleos de CPU e 5.120 núcleos CUDA, com 24 GB a 32 GB de memória nas configurações de lançamento — a NVIDIA lista o teto de 32 GB, mas fichas de fabricantes como a Dell e a Lenovo chegam a citar 64 GB. A de topo mantém os 20 núcleos de CPU e sobe para os 6.144 núcleos CUDA. Os modelos de 128 GB divulgados até agora — como o Surface Laptop Ultra e o ProArt P16 — usam a variante de topo; as configurações de entrada do Surface Laptop Ultra e do ProArt P14, de 2.599,99 dólares, trazem 24 GB. Essa distinção importa: a configuração de entrada não tem a mesma capacidade de rodar modelos grandes que a de 5.899 ou 6.999 dólares.

A memória unificada é o argumento central. Em um laptop comum, a CPU usa a RAM do sistema e a GPU usa a VRAM dedicada, a memória própria da placa de vídeo; carregar um modelo grande exige copiar dados entre as duas ou torcer para ele caber na VRAM. No RTX Spark, CPU e GPU endereçam o mesmo espaço — 128 GB, quatro a oito vezes a memória de um notebook comum. É a mesma ideia que a Apple usa nos chips da série M e que a AMD adotou no Ryzen AI Max. A diferença é que a NVIDIA traz para essa arquitetura o mesmo ecossistema de software que domina a IA em data centers.

## A memória é o campo de batalha

A memória unificada resolve a pergunta “o modelo cabe?”. Quem decide se ele roda *rápido* é outra coisa: a **largura de banda**, a quantidade de dados que o chip consegue ler da memória por segundo. Não adianta caber 128 GB se a GPU passa o tempo esperando pelos dados.

Três unidades aparecem na tabela abaixo. **Bits** são a largura do caminho entre a memória e o chip — quantos dados viajam de uma vez; 256 bits é o dobro de 128. **MT/s** é a velocidade dessa travessia, em milhões de transferências por segundo. **GB/s**, a banda, é o resultado das duas: largura × velocidade ÷ 8. E “banda teórica” é o teto do barramento — na prática, o aplicativo nunca extrai tudo isso.

| Plataforma | Memória unificada | Barramento (bits) | Velocidade (MT/s) | Banda teórica (GB/s) |
|---|---|---|---|---|
| NVIDIA RTX Spark N1X (laptop) | LPDDR5X, até 128 GB | 256 | 9.400 | cerca de 300 |
| NVIDIA DGX Spark (GB10) | LPDDR5X, 128 GB | 256 | 8.533 | 273 |
| AMD Ryzen AI Max+ 395 (Strix Halo) | LPDDR5X, até 128 GB | 256 | 8.000 | 256 |
| AMD Ryzen AI Max+ Pro 495 (Gorgon Halo) | LPDDR5X, até 192 GB | 256 | 8.533 | 273 |
| Qualcomm Snapdragon X2 Elite Extreme | LPDDR5X, 128+ GB (máx.) | 192 | 9.523 | 228 |
| Apple M5 | não divulgado | não divulgado | não divulgada | 153 |
| Apple M5 Pro | não divulgado | não divulgado | não divulgada | 307 |
| Apple M5 Max (GPU de 32 núcleos) | não divulgado | não divulgado | não divulgada | 460 |
| Apple M5 Max (GPU de 40 núcleos) | não divulgado | não divulgado | não divulgada | 614 |

Fontes: [NVIDIA](https://www.nvidia.com/en-us/products/rtx-spark/specifications/), [guia de portabilidade do RTX Spark](https://docs.nvidia.com/rtx-spark/rtx-spark-porting-guide/latest/overview.html) e [documentação do DGX Spark](https://docs.nvidia.com/dgx/dgx-spark/hardware.html); [ficha do Ryzen AI Max+ 395](https://www.amd.com/en/products/processors/desktops/ryzen/ryzen-ai-halo/ryzen-ai-max-plus-395.html) e [ficha do Ryzen AI Max+ Pro 495](https://www.amd.com/en/products/processors/desktops/ryzen/ryzen-ai-halo/ryzen-ai-max-plus-pro-495.html); [Product Brief do Snapdragon X2 Elite](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Snapdragon-X2-Elite-Product-Brief.pdf); [especificações do MacBook Pro](https://www.apple.com/macbook-pro/specs/) para os chips M5.

A leitura é direta. O RTX Spark tem a maior banda do grupo entre as plataformas de PC que não são da Apple: cerca de 10% acima do DGX Spark, também da NVIDIA, e perto de 17% acima do Ryzen AI Max+ 395. Mas perde com folga para o Apple M5 Max, que chega a 614 GB/s na configuração de GPU de 40 núcleos — o dobro da banda do superchip da NVIDIA. O M5 Pro, com 307 GB/s, praticamente empata com o RTX Spark em banda de memória. O Snapdragon X2 Elite Extreme é o caso oposto: tem a memória mais rápida da tabela, 9.523 MT/s, mas o barramento mais estreito entre as plataformas Windows, 192 bits, o que o deixa em 228 GB/s — ainda assim acima dos 153 GB/s do Apple M5 de entrada, o menor número da lista.

A conta vale entre plataformas de memória unificada. Um laptop gamer com placa de vídeo discreta tem banda muito maior, mas só dentro dos 24 GB de VRAM — o que não resolve carregar um modelo que não cabe ali. E os 300 GB/s do RTX Spark saem de uma faixa de 45 a 80 W, contra os 140 W do desktop da mesma família.

Duas observações finais sobre a tabela. A AMD **publica** a banda: 256 GB/s para o Ryzen AI Max+ 395 e 273 GB/s para o AI Max+ Pro 495, os dois com barramento de 256 bits — a diferença entre eles é só a velocidade da memória, 8.000 contra 8.533 MT/s. Já a Qualcomm lista 128+ GB como capacidade máxima do controlador, mas a configuração do Snapdragon X2 Elite Extreme usada nos testes vem com 48 GB; a Qualcomm disse à [PCWorld](https://www.pcworld.com/article/2921747/qualcomm-snapdragon-x2-elite-extremes-memory-mystery-explained.html) que a quantidade é escolha de cada fabricante, não uma exigência do chip.

Não há número oficial de banda por núcleo de GPU (nem por SM, as unidades internas do processador gráfico) em nenhuma dessas plataformas — qualquer divisão desse tipo é estimativa nossa, não especificação. E a Apple não divulga barramento, velocidade nem tipo de memória dos chips M: publica apenas a banda resultante.

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

O RTX Spark não é o único caminho para a memória unificada, e a tabela acima mostra por quê. A AMD tem a vantagem de rodar programas x86 sem emulação. A Qualcomm aposta em produtividade, bateria e nos recursos Copilot+. A Apple, com memória unificada há anos, segue na frente em eficiência energética e desempenho de CPU. E a NVIDIA oferece a combinação que nenhum deles traz ao mesmo tempo: GPU de classe RTX, até 128 GB de memória unificada e CUDA nativo em Windows. Para quem testa ou roda modelos grandes, é uma proposta difícil de replicar — e cara demais e desnecessária para quem só vai navegar, escrever e fazer planilhas.

## O que vem depois

A NVIDIA planeja desktops compactos RTX Spark para novembro de 2026 — a mesma plataforma, em um chassi feito para ficar ligado 24 horas por dia. Também apresentou uma prévia do DGX Station for Windows, uma estação de trabalho de mesa com 748 GB de memória compartilhada entre CPU e GPU — quase seis vezes os 128 GB do notebook — e até 20 petaflops FP4, o equivalente a 20 laptops RTX Spark. Não há data de venda para este produto.

O sucesso do RTX Spark, porém, não será medido apenas em unidades vendidas. O preço alto, a CPU abaixo dos concorrentes e a experiência de IA local ainda imatura tornam o produto um artigo de nicho — pelo menos até que mais aplicativos e agentes aproveitem a memória extra. O que a NVIDIA conseguiu foi ser a primeira a combinar 128 GB de memória unificada com CUDA em Windows, e pressionar Intel, AMD e Qualcomm a responder. Se essa configuração virar padrão, o lançamento de 16 de outubro pode vir a ser lembrado como o dia em que a NVIDIA deixou de vender apenas a GPU.

---

> **Ponto de partida:** [Nvidia RTX Spark Laptops Debut at 2.599 dólares, Hit 6 OEMs](https://tech-insider.org/nvidia-rtx-spark-windows-laptop-market-entry-2026/) e [NVIDIA RTX Spark Laptops Launch at 2.599 dólares, 128GB](https://tech-insider.org/nvidia-rtx-spark-laptops-launch-2599-128gb-2026/) — tech-insider.org, por Nadia Dubois e Elias Virtanen. São textos agregadores; os fatos foram conferidos nas fontes abaixo.
>
> **Fontes primárias e apuração:** [NVIDIA Newsroom, 16/10/2026](https://nvidianews.nvidia.com/news/nvidia-rtx-spark-pcs-available-today-a-new-beginning-for-windows-pcs); [NVIDIA Newsroom, 01/06/2026](https://nvidianews.nvidia.com/news/nvidia-microsoft-windows-pcs-agents-rtx-spark); [NVIDIA Blog, 07/10/2026](https://blogs.nvidia.com/blog/local-ai-rtx-spark-microsoft-windows-event/); [HP, 07/10/2026](https://www.hp.com/us-en/newsroom/press-releases/2026/hp-leads-the-expansion-of-the-local-ai-era-from-gb300-ai-workstations-to-rtx-spark-windows-pcs.html); [The Verge, 16/10/2026](https://www.theverge.com/tech/1012748/nvidia-rtx-spark-windows-arm-laptops-asus-hp-lenovo-impressions); [The Verge — review do Surface Laptop Ultra](https://www.theverge.com/tech/1012628/microsoft-surface-laptop-ultra-review); [PCWorld, 08/10/2026](https://www.pcworld.com/article/3256085/here-are-all-the-rtx-spark-laptops-available-at-launch-going-up-to-7000.html); [Tom's Hardware, 16/10/2026](https://www.tomshardware.com/laptops/nvidia-rtx-spark-devices-are-now-officially-on-sale-secure-the-surface-laptop-ultra-or-other-rtx-spark-laptops-here-starting-at-usd2-599-where-to-buy-pricing-and-availability-revealed-on-several-models); [Engadget, 05/06/2026](https://www.engadget.com/2187889/nvidia-rtx-spark-chip-could-give-windows-its-true-apple-silicon-moment).
>
> **Imagem:** notebook aberto com tela iluminada no escuro, por Ludovic Delot, via [Unsplash](https://unsplash.com/photos/a-laptop-computer-with-a-glowing-screen-in-the-dark-pW6Q2ifY87M), sob a [Licença Unsplash](https://unsplash.com/license).
>
> *Preços de varejo nos Estados Unidos, sem impostos, sujeitos a variação por configuração e região. Não há, até a publicação, data ou preço de lançamento no Brasil.*

---

👉 **Veja também nossa análise comparativa dos melhores modelos de IA em:** [blog.ideias.casa/melhores-ia](https://blog.ideias.casa/melhores-ia)
