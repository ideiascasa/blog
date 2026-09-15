---
layout: post
title: "Governança de IA em missão crítica: monitorar o que não pode falhar, como fazemos com aviões"
author: "autor bot"
categories: blog
tags: [blog,ia,seguranca,governanca-ia,missao-critica,conformidade,regulacao,tecnologia]
image: governanca-ia-missao-critica-featured.png
---

Duas notícias publicadas na mesma semana, em dois pontos distantes da Ásia, apontam para a mesma encruzilhada. Nas Filipinas, um think tank cobra do governo coordenação para implementar o primeiro marco de governança de IA do país. Em Bangladesh, o executivo-chefe da Kaspersky para a Ásia-Pacífico diz que a próxima década de resiliência cibernética dependerá de gente, não de software. Lidas em conjunto, as duas posições descrevem um vazio que nenhuma das duas resolve sozinha: quem responde quando um sistema de IA que opera infraestrutura crítica erra?

## Filipinas: o primeiro marco de governança de IA e o alerta sobre ciberdefesa

O think tank Stratbase Institute pediu ao governo filipino que reforce sua segurança cibernética diante de ataques recentes e afirmou que os órgãos competentes precisam atuar de forma coordenada para implementar adequadamente o primeiro marco de governança de inteligência artificial do país.

O Departamento de Economia, Planejamento e Desenvolvimento (DepDev) anunciou recentemente que pretende publicar o marco ainda em setembro, após apresentar o plano final ao presidente Ferdinand Marcos Jr. O documento deve cobrir o uso de ferramentas de IA em setores sensíveis, como educação, saúde e infraestrutura pública.

O Stratbase classificou o marco como um passo "oportuno e importante", capaz de dar às agências públicas "uma direção comum para o uso de IA, ao mesmo tempo em que protege direitos, mantém a supervisão humana e garante responsabilização".

Para Dindo Manhit, presidente do Stratbase Institute, empoderamento por IA não é distribuir licenças de software: "exige dados governamentais precisos e sistematicamente organizados, processos redesenhados e servidores públicos capacitados a tomar decisões mais rápidas e mais bem informadas, permanecendo responsáveis". Ele defende que DepDev, o Departamento de Tecnologia da Informação e Comunicações e demais agências atuem em coordenação, e que parcerias com o setor privado e a academia sejam tratadas como parte da infraestrutura — não como acessório.

O pano de fundo é desfavorável. O próprio Stratbase chama atenção para ataques cibernéticos contra várias agências governamentais nos últimos meses. "À medida que o governo conecta mais sistemas e usa mais dados, as agências precisam fortalecer continuamente suas defesas, testar seus planos de resposta a incidentes e proteger as informações dos cidadãos", disse Manhit.

## Bangladesh: a resiliência depende de competência, não de ferramenta

A entrevista de Adrian Hia ao The Daily Star caminha na mesma direção, por outro ângulo. O diretor-geral da Kaspersky para a Ásia-Pacífico — que antes passou por Zscaler, VMware, Oracle e Sun Microsystems — trata a transformação digital de Bangladesh como irreversível e a cibersegurança como parte do mesmo movimento, não como uma etapa posterior. Em 2025, a empresa registrou aproximadamente 500 mil arquivos maliciosos detectados por dia.

Questionado sobre o que torna um ecossistema de cibersegurança atraente para investimento estrangeiro, Hia listou talento qualificado, políticas e regulações efetivas, cooperação público-privada, conscientização e organizações que tratam segurança como prioridade de negócio — e acrescentou previsibilidade. Já ao responder o que distingue os países que avançam mais rápido na região, a resposta foi a mesma em outra escala: eles adotam uma abordagem coordenada e de longo prazo, investindo em legislação, resposta a incidentes e formação de pessoas, não apenas em tecnologia.

Sobre IA, o diagnóstico de Hia é direto: "em muitos casos, a segurança não acompanhou o ritmo da adoção de IA". Organizações focam a oportunidade e deixam de lado como atacantes podem explorar sistemas de IA e como a própria IA acelera ataques. Daí o princípio que ele resume em uma frase — "se uma organização está investindo em IA, também precisa investir em proteger essa IA".

Hia também oferece um caminho prático para o dilema entre soberania de dados e dependência de fornecedores estrangeiros: em vez de escolher entre defesa forte e controle nacional, classificar dados por sensibilidade. Informações altamente sensíveis de governo e de infraestrutura crítica ficam sob controle local estrito; dados de menor risco podem usar nuvem e serviços globais de confiança. O restante da receita inclui exigir diversidade de fornecedores com opções de saída, e avaliar provedores por transparência e verificabilidade, não apenas pela sede. Por fim, se tivesse de escolher uma única prioridade para a próxima década, Hia escolheria construir conscientização e competências em cibersegurança em escala — porque "a tecnologia continuará mudando, mas as pessoas seguirão sendo parte crítica da equação de segurança".

## O que falta nas duas agendas: um regime de monitoramento

Nenhuma das duas notícias propõe o que a engenharia de segurança já resolveu em outros domínios. A aviação comercial não é segura porque pilotos e fabricantes são mais disciplinados que a média. É segura porque o setor construiu, ao longo de décadas, um regime de vigilância sobre si mesmo: telemetria contínua de sistemas críticos, registro obrigatório do que aconteceu (a caixa-preta), investigação independente de cada evento, relatório público e — o ponto decisivo — a obrigação de corrigir antes de voltar a operar.

O paralelo com IA aplicada a infraestrutura crítica é quase literal, e as duas notícias mostram exatamente onde o paralelo se rompe. O marco filipino fala em supervisão humana e responsabilização, mas supervisão humana sem telemetria é confiança, não controle: quem supervisiona precisa ver o que o sistema faz, com que confiança, com que dados e por qual caminho de decisão. A conversa de Hia fala em monitorar sistemas de IA e investir em protegê-los, mas monitoramento de segurança responde a "isto foi comprometido?" — não a "isto está decidindo corretamente?".

São perguntas distintas, e a segunda é a que ninguém está fazendo em escala:

- **Trilha de auditoria de decisões.** Todo sistema de IA que opera ou aconselha operação em infraestrutura crítica — energia, água, saúde, transporte, finanças — deveria registrar entradas, versão do modelo, justificativa e resultado. Equivalente à caixa-preta, e igualmente obrigatório.
- **Relato obrigatório de incidentes.** Não só vazamentos de dados. Uma decisão automatizada que causou dano material, uma alucinação que virou ordem de serviço, um modelo que degradou silenciosamente após uma atualização — todos deveriam entrar em um registro reportável.
- **Investigação independente e pública.** O aprendizado do setor aéreo vem de investigações conduzidas por quem não é o operador nem o fabricante. Um regime de governança de IA sem terceiro independente herda o conflito de interesse que já conhecemos de auditorias de conformidade autorreguladas.
- **Padrões de desempenho contínuo, não homologação de uma vez.** Um modelo aprovado em janeiro pode estar degradado em julho. A autorização para operar deveria ser condicional ao monitoramento contínuo, revisável e revogável.
- **Competência humana como requisito de operação, não como treinamento de RH.** Se Hia está certo — e a evidência aponta que está —, gente capacitada é o último controle antes do dano. Isso transforma treinamento em exigência de licenciamento, exatamente como horas de voo e certificação de tipo.

Há um argumento previsível contra tudo isso: custo, lentidão, burocracia sufocando a inovação. O setor aéreo ouviu o mesmo argumento e escolheu a segurança de qualquer forma, porque a alternativa era um acidente por trimestre. Vale lembrar quanto tempo levou para chegar lá — e que a IA generativa está sendo colocada em operações de missão crítica em uma fração desse tempo, muitas vezes sem que ninguém saiba dizer qual versão do modelo está no ar hoje.

## O ponto de convergência

O que Filipinas e Bangladesh expõem, cada um à sua maneira, é que a governança de IA está sendo construída de fora para dentro: primeiro o marco legal, depois a coordenação institucional, depois — talvez — a capacidade técnica de observar o que os sistemas fazem. Nos sistemas que não podem falhar, a ordem precisa ser inversa. Sem observar, não há responsabilização real; sem responsabilização, o marco de governança é um documento bem redigido sobre algo que ninguém consegue medir.

A boa notícia é que o desenho existe e está testado há décadas em outro domínio. Falta decidir se a IA que opera o que não pode falhar merece o mesmo rigor que dedicamos a um avião — ou se vamos continuar descobrindo os problemas pelo modo mais caro possível.

Para quem busca se orientar nesse cenário de rápida evolução, nossa [análise comparativa dos melhores modelos de IA](https://blog.ideias.casa/melhores-ia) acompanha e avalia as principais opções disponíveis no mercado.

---

> **Fonte original:** [Stratbase: PH should strengthen cybersecurity, AI governance](https://newsinfo.inquirer.net/2304368/stratbase-ph-should-strengthen-cybersecurity-ai-governance) - newsinfo.inquirer.net, Inquirer News (assinatura de redação).
>
> **Fonte original:** [The next decade of cyber resilience will depend on skills and awareness, says Kaspersky APAC chief](https://www.thedailystar.net/news/technology/news/the-next-decade-cyber-resilience-will-depend-skills-and-awareness-says-kaspersky-apac-chief-4271826) - thedailystar.net, The Daily Star, em entrevista com Adrian Hia.
>
> **Imagem:** Torre de controle de tráfego aéreo com cúpula de vidro e antenas de comunicação sobre um edifício de escritórios, por Olivier Amyot, via [Unsplash](https://unsplash.com/photos/fY8kO-FiqNE), licenciada sob a [Unsplash License](https://unsplash.com/license).

---

👉 **Veja também nossa análise comparativa dos melhores modelos de IA em:** [blog.ideias.casa/melhores-ia](https://blog.ideias.casa/melhores-ia)
