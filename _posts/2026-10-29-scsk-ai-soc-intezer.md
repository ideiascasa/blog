---
layout: post
title: "IA descarta 95% dos alertas de segurança em teste interno: o AI SOC Service da SCSK Security evita o “chute” dos chatbots"
author: "autor bot"
categories: blog
tags: [blog, ia, seguranca, sec, agentes-ia, tecnologia, analise]
image: scsk-ai-soc-intezer-featured.jpg
---

A [SCSK Security](https://scsksecurity.co.jp/press_release_aisoc/), braço de segurança do grupo de TI
japonês SCSK, lançou em 28 de outubro de 2026 o **AI SOC Service**, um serviço gerenciado que põe a
inteligência artificial no trabalho que consome o dia de um analista: a triagem dos alertas que chegam
ao SOC — *Security Operations Center*, a central que monitora ameaças à segurança da informação de uma
empresa 24 horas por dia. Segundo o comunicado da empresa, na validação em ambiente próprio — cerca de
30 mil alertas por semana, um a cada 20 segundos — a plataforma descartou automaticamente
cerca de 95% dos alertas, sem intervenção humana, e reduziu o tempo médio de análise inicial de
uma a duas horas por alerta para dois minutos.

O anúncio combina duas experiências: a plataforma autônoma de análise de segurança da
[Intezer](https://intezer.com/), empresa israelense fundada em 2015, e o conhecimento operacional
acumulado pelo SOC da própria SCSK Security — o grupo reúne cerca de mil especialistas em segurança,
segundo a empresa. O serviço opera 24 horas por dia, sete dias por semana, e promete algo que o
mercado persegue há anos: transformar a montanha de alertas que se acumula em qualquer centro de
operações em uma fila pequena de casos que realmente merecem atenção humana.

## Como funciona: triagem automática sobre a infraestrutura que o cliente já tem

O detalhe mais estratégico da arquitetura do serviço é o que ele **não** faz: ele não substitui o SIEM (a
plataforma que centraliza e cruza os registros de segurança da empresa), o EDR (o software que vigia
os computadores e responde a ameaças neles) nem o XDR (a versão ampliada dessas ferramentas, que
também cobre rede, nuvem e identidade). O AI SOC Service entra no fluxo depois delas: recebe os
alertas que essas ferramentas já geraram e assume a etapa de análise que hoje depende de pessoas.

Alertas vindos de computadores, servidores, redes e ambientes de nuvem entram na triagem automática
independentemente da severidade atribuída pela plataforma de monitoramento. Inclusive os classificados
como de baixa prioridade — que nas operações tradicionais formam a zona perigosa de “detectado, mas
ninguém olhou”. É aí, segundo a empresa, que se escondem os primeiros sinais de uma intrusão.

a IA avalia a natureza da ameaça e o escopo do impacto, descarta sem ação o que não oferece perigo
real — “descartar” é o jargão do setor: marcar o alerta como resolvido sem passar por humano — e
encaminha os casos que precisam subir para um analista do SOC da SCSK Security (os chamados
escalonamentos). Cabe a esses analistas a decisão final, com o resultado da IA e as evidências em
mão: notificar incidentes importantes, investigar o alcance, apoiar a contenção e a recuperação.

Segundo o próprio comunicado, a triagem manual de um alerta leva, em média, de uma a duas horas; com o
serviço, a análise inicial caiu para dois minutos na validação no ambiente da própria SCSK Security.
O próprio comunicado registra uma ressalva: os números vêm do ambiente
interno da empresa, com cerca de 30 mil alertas por semana, e **não garantem eficácia** em ambientes
de clientes — o resultado real, diz o texto, varia conforme o ambiente e o escopo monitorado.

## Por que não usar só um LLM: a aposta em evidências forenses

O diferencial que a própria SCSK Security reivindica está no modo de decidir: em vez do “chute
estatístico” de um LLM — os grandes modelos de linguagem que alimentam chatbots como o ChatGPT —, a
determinação sai de evidências verificáveis. Segundo a descrição da Intezer, a análise usa duas
tecnologias: a “Code DNA”, que compara o código de um malware com uma base de ameaças conhecidas em
nível quase genético, e a perícia automática de memória — o exame do que está rodando na máquina no
momento da detecção, como um perito diante do computador ligado. É essa segunda técnica que, segundo
a empresa, detecta ameaças que não deixam arquivos no disco, como os ataques *fileless*, que rodam
direto na memória.

O resultado vem acompanhado das provas — o trecho de código que coincidiu com a base de ameaças e o
comportamento observado na memória — que podem virar documentação de incidente. É com esse argumento
que a empresa mira ambientes regulados, nos quais toda decisão de segurança precisa deixar rastro
auditorável.

Itai Tevet, cofundador e CEO da Intezer, afirma no comunicado que a combinação da tecnologia de nível
forense da empresa com o conhecimento avançado de SOC da SCSK Security permite investigar todos os
alertas, sem lacunas, e entregar determinações com base em evidências — liberando os analistas para
as ameaças que realmente exigem resposta e para o trabalho proativo.

## O contexto: a corrida pela automação do SOC

O lançamento chega no meio de uma onda de iniciativas que aplicam IA generativa e agentes autônomos
às operações de segurança. A [Microsoft argumentou no Digital Defense Report 2026](https://blog.ideias.casa/microsoft-ddr-2026-ia-atacantes-soc/)
que a IA está mudando a “física da cibersegurança” — o equilíbrio de tempo, custo e escala entre
atacantes e defensores — e que o SOC precisa adotá-la como ferramenta essencial; a [Zscaler lançou em
setembro de 2026 um SOC “agêntico”](https://blog.ideias.casa/agentes-ia-soc-credenciais/), em que
programas de IA — os agentes — executam tarefas de análise e resposta sob supervisão humana. O que
diferencia a proposta da SCSK Security é o posicionamento: um **serviço gerenciado** sobre uma
plataforma de terceiro, em vez de um produto para o cliente operar, e a promessa de julgamentos
baseados em evidências forenses, não em probabilidades de modelo de linguagem.

O painel de mercado que acompanha o anúncio, do veículo Futurum Group, situa o momento: em levantamento
próprio com 229 fabricantes e revendedores de tecnologia de segurança, 62,4% apostam na
cibersegurança como motor de crescimento em 2026. Vale tratar esses números como pano de fundo: vêm de
levantamentos de um analista de mercado com interesses comerciais no setor — o texto do Futurum,
aliás, é declaradamente gerado por modelo de linguagem, sem revisão editorial humana — e não de uma
métrica independente.

O Futurum calcula ainda a economia da automação: dos 30 mil alertas semanais do teste, os 5%
restantes — cerca de 1.500 casos por semana — é o que sobraria para os analistas humanos, e a
compressão de uma a duas horas para dois minutos significaria que o mesmo time daria conta de 30 a 60
vezes mais alertas no mesmo tempo.

Para quem acompanha de perto a corrida dos modelos de linguagem — que o AI SOC Service evita usar,
mas que segue em cheio nos SOC —, nossa [análise comparativa dos melhores modelos de IA](https://blog.ideias.casa/melhores-ia)
avalia as principais opções disponíveis no mercado.

## O que observar daqui para frente

O comunicado deixa claro que este é o primeiro passo de um plano maior: a SCSK Security quer transformar
o AI SOC Service no núcleo de um “SOC de próxima geração”, expandir o escopo do que a IA analisa,
ampliar as integrações com produtos de segurança e levar o serviço para fora do Japão — um plano
anunciado sem data prometida. A pergunta que fica é se o índice de 95% de descarte automático, medido
apenas no ambiente da própria empresa, se sustenta na diversidade de ambientes reais dos clientes —
com SIEMs e EDRs de gerações e configurações diferentes. A resposta deve vir dos próximos meses: se
forem publicadas métricas de produção reais, se o serviço aparecer em novos países e como os
concorrentes de segurança gerenciada vão reagir no preço. Se o número sobreviver fora do ambiente da
própria SCSK, o analista que passava uma a duas horas por alerta passará a dedicar a semana aos cerca
de 1.500 casos em que a IA admitiu não poder decidir sozinha.

---

> **Fonte original:** [SCSK Security's AI SOC Closes 95% of Alerts Automatically](https://futurumgroup.com/insights/scsk-securitys-ai-soc-closes-95-of-alerts-automatically/) - futurumgroup.com, por FuturumAI (conteúdo gerado por modelo de linguagem, sem revisão editorial humana, conforme declaração do próprio site).
>
> **Fonte primária:** [SCSKセキュリティ、AIを活用した次世代SOCサービス「AI SOCサービス」を提供開始](https://scsksecurity.co.jp/press_release_aisoc/) - SCSK Security, comunicado oficial de 28/10/2026 (em japonês).
>
> **Fontes complementares:** [IT Leaders](https://it.impress.co.jp/articles/-/29945), por Yoshimi Hikawa, 29/10/2026; [Cloud Watch](https://cloud.watch.impress.co.jp/docs/news/2151873.html), por Hideki Mitsuyanagi, 29/10/2026; [BUSINESS NETWORK](https://businessnetwork.jp/article/38207), 28/10/2026.
>
> **Imagem de capa:** [Goddard TV Control Room](https://commons.wikimedia.org/wiki/File:Goddard_TV_Control_Room_-_39040983012.jpg), por NASA Hubble, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Goddard_TV_Control_Room_-_39040983012.jpg), licenciada sob [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/).

---

👉 **Veja também nossa análise comparativa dos melhores modelos de IA em:** [blog.ideias.casa/melhores-ia](https://blog.ideias.casa/melhores-ia)
