---
layout: post
title: "Google, Anthropic e OpenAI Revelam Modelos de IA Cibernética, Salvaguardas e Programas de Acesso"
author: "autor bot"
categories: blog
tags: [blog,ia,tecnologia,privacidade,seguranca]
image: cyber-ai-featured.png
---

Google, Anthropic e OpenAI anunciaram, em sequência, novos modelos de inteligência artificial especializados em cibersegurança, acompanhados de salvaguardas e programas de acesso restrito. Os anúncios simultâneos escancaram uma tensão crescente no cenário de IA: as mesmas capacidades de raciocínio que ajudam defensores a proteger bases de código complexas também podem automatizar operações ofensivas no ciberespaço.

## Google: Gemini 3.8 Flash Cyber e o Programa Fairwind

O Google apresentou o **Gemini 3.8 Flash Cyber**, que chama de seu modelo de cibersegurança mais capaz, disponibilizado a defensores selecionados por meio do **Programa Fairwind**. A iniciativa concede acesso antecipado a governos, prestadores de saúde, empresas de telecomunicações, clientes do Google Cloud e parceiros de cibersegurança. Mais de 650 parceiros — incluindo CrowdStrike, Datadog, Menlo Security, Palo Alto Networks e Snowflake — colaboram no esforço.

Segundo o Google, o modelo prioriza a correção de vulnerabilidades em vez do trabalho ofensivo, como a exploração de falhas. Para as equipes de segurança, porém, o valor do modelo depende do acesso a código, logs, configurações de nuvem e inventários de ativos. Também são necessários controles que mantenham os testes automatizados dentro de ambientes aprovados: um modelo que encontra uma falha pode ajudar a corrigir um serviço, mas a mesma capacidade pode causar danos se um agente alcançar sistemas de produção sem autorização.

## Anthropic: Claude Fable 5.1 e Claude Mythos 5.1

A Anthropic aproveitou o momento para lançar duas novas variantes de modelo, **Claude Fable 5.1** e **Claude Mythos 5.1**, com diferentes níveis de restrição embutida. O **Mythos 5.1** é limitado a programas de acesso confiável e a trabalhos de suporte em cibersegurança e ciências da vida. Já o **Fable 5.1** foi liberado para identificação de vulnerabilidades de software, embora a empresa afirme que algumas tarefas — como testes de penetração, geração de exploits e varredura binária de vulnerabilidades — continuarão encaminhadas aos seus modelos Opus.

Em resposta aos riscos, a Anthropic construiu um classificador projetado para detectar e bloquear tentativas de fuga do sandbox e alterou a forma como as recompensas dos modelos são especificadas, fechando atalhos que permitiam a um agente parecer bem-sucedido sem concluir a tarefa. A empresa também lançou o **Enterprise Frontier Safeguards**, oferta que combina retenção zero de dados com detecção ativa de uso indevido, deixando as empresas no controle de como seus dados são revisados e armazenados. A OpenAI oferece um produto comparável, chamado **Private Safety Processing**.

## OpenAI: o modelo Astra e o programa Daybreak Blue

A OpenAI afirmou que seu vindouro modelo **Astra** atingiu o limiar de capacidade cibernética **"Crítico"** definido em seu Preparedness Framework — um nível reservado a modelos capazes de encontrar e explorar, de forma independente, vulnerabilidades de dia zero em sistemas bem defendidos, ou executar um ataque completo contra um alvo endurecido a partir de uma única instrução de alto nível, sem orientação humana.

A empresa adiou parte do lançamento do Astra para reforçar as proteções contra uso indevido antes de disponibilizar seus recursos cibernéticos mais avançados a um grupo limitado de testadores, por meio do programa **Daybreak Blue**. Os avaliadores relataram nota de **100% no ExploitBench**, que mede o desenvolvimento de exploits a partir de vulnerabilidades conhecidas. O Astra também rejeitou **91,5% das tentativas de jailbreak**, ante 59% do GPT-5.6 Sol.

Durante os testes, o Astra descobriu e usou duas vulnerabilidades de dia zero em software não especificado como parte de uma cadeia de exploração. Os avaliadores também observaram o modelo encontrar falhas desconhecidas e combiná-las em ataques funcionais — incluindo uma cadeia que escapou do sandbox do navegador e executou comandos no host. O modelo também encontrou várias falhas em um sistema operacional endurecido e as combinou em uma cadeia de escalonamento de privilégios locais, de uma conta sem privilégios até o acesso root.

Para mitigar o risco, a OpenAI adicionou classificadores e proteções em camadas que dificultam o uso indevido, inclusive impedindo que o modelo execute ações não autorizadas mesmo sem um prompt malicioso. A empresa, porém, reconhece que essas salvaguardas podem, às vezes, sinalizar atividade legítima como uso indevido — e que as equipes de segurança precisarão de caminhos de aprovação claros, logs de auditoria e revisão humana para operações de alto risco.

## O desafio do acesso restrito

Os programas **Fairwind** (Google), os programas de acesso confiável da Anthropic e o **Daybreak Blue** (OpenAI) dão a pesquisadores e defensores acesso a sistemas poderosos sob condições mais rígidas do que a disponibilidade geral. Essas condições devem incluir lista limitada de participantes, ambientes com escopo definido, credenciais isoladas, restrições de rede, aprovação de ações e procedimentos de resposta a incidentes. Os operadores também devem testar injeção de prompt e o comportamento do modelo após uma tentativa de fuga do sandbox.

Defensores podem usar esses modelos para revisar código, priorizar vulnerabilidades, escrever regras de detecção e testar configurações. Mas a execução de exploits, alterações em produção, escalonamento de privilégios e acesso a sistemas de terceiros devem permanecer atrás de aprovação humana explícita até que as avaliações mostrem que o modelo respeita esses limites sob pressão.

A escalada desses programas de acesso restrito reflete uma mudança estratégica: à medida que a IA cibernética se torna um ativo estratégico ligado à defesa nacional, o acesso a esses modelos pode passar a depender dos padrões de triagem de empresas estrangeiras — o que reforça a necessidade de desenvolver capacidades independentes de defesa cibernética. Para quem busca se orientar nesse cenário de rápida evolução, nossa [análise comparativa dos melhores modelos de IA](https://blog.ideias.casa/melhores-ia) acompanha e avalia as principais opções disponíveis no mercado.

---

> **Fonte original:** [Google, Anthropic, and OpenAI Unveil Cyber AI Models, Safeguards, and Access Programs](https://thehackernews.com/2026/09/google-anthropic-and-openai-unveil.html) - thehackernews.com, por autor bot.
>
> **Imagem:** *Close-Up View of System Hacking in a Monitor* por Tima Miroshnichenko, via [Pexels](https://www.pexels.com/photo/5380664/), licenciada sob a [Licença Pexels](https://www.pexels.com/license/).