---
layout: post
title: "Governança de IA em missão crítica: monitorar o que não pode falhar, como fazemos com aviões"
slug: governanca-ia-missao-critica
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

## O que a aviação construiu — e o que a IA ainda não tem

Vale ser justo com o estado atual da regulação: o desenho não está ausente. A aviação civil o organizou em torno de dois instrumentos. O **Anexo 19 da ICAO** (*Safety Management*) exige de cada Estado um *State Safety Programme*, cujos quatro componentes são política e objetivos de segurança, gestão de risco de segurança, garantia de segurança e promoção da segurança — elevados a norma no Capítulo 3. O mesmo anexo define o quadro de **SMS** dos provedores de serviço, com os mesmos quatro componentes desdobrados em doze elementos. O **Anexo 13** trata da investigação de acidentes e incidentes.

Do lado da IA, o equivalente parcial já existe. O Regulamento Europeu de IA (AI Act) obriga fornecedores de sistemas de **alto risco** a manter um sistema de **monitoramento pós-comercialização** (Artigo 72), que deve coletar, documentar e analisar de forma ativa e sistemática dados sobre o desempenho real do sistema ao longo de toda a sua vida útil, com base em um plano formal. E o Artigo 73 exige o **relato de incidentes graves** às autoridades de vigilância de mercado: em até 15 dias após o fornecedor estabelecer nexo causal, em 2 dias nos casos de infração generalizada ou de disrupção de infraestrutura crítica (Art. 3(49)(b)) e em até 10 dias em caso de morte de uma pessoa. No mesmo artigo, está previsto que o fornecedor, sem demora, "realize as investigações necessárias" sobre o incidente grave.

Ou seja: telemetria contínua e relato obrigatório já são exigíveis. O problema está em outros pontos, e é aí que a analogia com a aviação deixa de ser metáfora e vira lacuna concreta.

### 1. Quem investiga é quem é investigado

Na aviação, a regra é o oposto do Artigo 73. O Anexo 13 é categórico em dois padrões: "o único objetivo da investigação de um acidente ou incidente é a prevenção", e "não é propósito desta atividade atribuir culpa ou responsabilidade" (§3.1). E mais: "cabe ao Estado estabelecer uma autoridade de investigação de acidentes **independente** das autoridades de aviação civil e de outras entidades que possam interferir na condução ou na objetividade da investigação" (§3.2). O §5.4 acrescenta que essa autoridade tem independência e autoridade irrestrita sobre a condução da investigação.

O *Manual of Aircraft Accident and Incident Investigation* (Doc 9756) explica o motivo histórico, e ele é exatamente o motivo pelo qual o modelo do AI Act preocupa: durante os primeiros anos da aviação, as investigações eram feitas pelos **mesmos funcionários responsáveis pela supervisão de segurança**. "Ao longo dos anos, esse arranjo se mostrou inadequado, porque surgiram conflitos quando as conclusões da investigação identificavam deficiências no desempenho das próprias funções de supervisão."

É a descrição precisa do Artigo 73: a investigação fica com o fornecedor, que é a parte cuja conduta está sob exame. O setor aéreo não adotou a independência por escrúpulo filosófico — adotou porque a alternativa, na prática, não funcionou.

### 2. O que se aprende não vira conhecimento público

O Anexo 13 exige, entre os elementos da investigação, a "disseminação pública e tempestiva da informação factual" (§5.4, alínea c) e a conclusão do **Relatório Final** (alínea f). A lição de um acidente é publicada para que a indústria inteira não repita o erro.

O relato do Artigo 73 vai para as autoridades de vigilância de mercado do Estado-membro onde o incidente ocorreu — não para um repositório público de lições aprendidas. Sem isso, cada organização comete de novo o erro que outra já cometeu, e o setor aéreo resolveu esse problema décadas atrás precisamente porque a repetição era fatal.

### 3. Não há autorização que possa ser suspensa por desempenho

Nenhum operador aéreo mantém a permissão de voar indefinidamente por ter sido aprovado uma vez. Nos Estados Unidos, uma **diretriz de aeronavegabilidade** (14 CFR Parte 39) é uma "regra legalmente exigível" que se aplica a uma aeronave, motor, hélice ou componente sempre que exista uma "condição insegura" provável de ocorrer em outros produtos do mesmo tipo. Quem opera um produto que não atende à diretriz aplicável **está em violação** — e viola novamente a cada operação.

No AI Act, o monitoramento pós-comercialização deve avaliar a conformidade contínua, mas falta o elo de *enforcement* que transforma desempenho degradado em suspensão de operação. O Anexo 19 é explícito quanto ao que se deve monitorar: entre os objetivos da garantia de segurança está "monitorar continuamente seus processos e seu ambiente operacional para detectar mudanças ou desvios que possam introduzir riscos de segurança ou a **degradação dos controles de risco já existentes**". Um modelo aprovado em janeiro e degradado em julho segue autorizado, e provavelmente ninguém sabe qual versão está no ar.

### 4. O risco que não mata ninguém — e ainda assim quebra a operação

Há uma lacuna anterior a todas essas, e ela é a mais consequente para quem opera infraestrutura crítica: **o regime de incidente grave da IA só enxerga dano físico.**

A definição do Artigo 3(49) tem quatro alíneas — morte ou dano grave à saúde de uma pessoa; disrupção grave e irreversível da gestão ou operação de infraestrutura crítica; violação de obrigações de direito da União destinadas a proteger direitos fundamentais; e dano grave à propriedade ou ao meio ambiente. Leia de novo: **não há nenhuma alínea de dano econômico, financeiro ou de continuidade de negócio**. Um sistema de IA que causa prejuízo devastador sem machucar ninguém, sem derrubar infraestrutura crítica e sem dano material relevante não é, pela letra da norma, um incidente grave — e portanto não precisa ser reportado a ninguém.

O contraste com o setor financeiro mostra que o critério existe e é viável. O DORA (Regulamento UE 2022/2554) classifica incidentes relacionados a TIC com um critério explícito de **impacto econômico**: o limiar é atingido quando "os custos e perdas incorridos pela entidade financeira em razão do incidente excederam ou provavelmente excederão 100 mil euros". É um número, não uma metáfora. O que falta é estender essa lógica — critérios econômicos objetivos e reportáveis — para a IA em operações críticas além do setor financeiro.

E não se trata de hipótese. Em 1º de agosto de 2012, a corretora americana Knight Capital sofreu um erro no seu sistema automatizado de roteamento de ordens: 212 ordens de varejo foram processadas por um código defeituoso que gerou milhões de ordens-filhas, resultando em 4 milhões de execuções em 154 ações, mais de 397 milhões de ações negociadas, **em cerca de 45 minutos**. Quando o sistema parou, a empresa tinha assumido uma posição comprada de aproximadamente 3,5 bilhões de dólares e uma posição vendida de cerca de 3,15 bilhões. A perda final, conforme a ordem da SEC, foi de **mais de 460 milhões de dólares**, com problemas de capital líquido (*net capital problems*). **Nenhuma morte, nenhum ferido, nenhuma infraestrutura crítica derrubada.** Pela taxonomia do Artigo 3(49), esse é o tipo de evento que pode passar em branco — e foi um dos episódios mais caros da história do mercado americano.

O argumento a favor de monitorar esse tipo de caso não é paternalismo regulatório. Sistemas críticos se conectam: um serviço de pagamento, um provedor de nuvem, um fornecedor de autenticação, um sistema de folha de pagamento. A falência de uma peça pequena e não monitorada pode propagar dano por toda a cadeia — e resultado econômico é, ele mesmo, uma forma de dano sistêmico. Se o objetivo da governança de IA é evitar que sistemas causem dano em escala, deixar de fora o dano que quebra empresas e cadeias inteiras é escolher a cegueira.

Some-se a isso a limitação de escopo: o regime europeu alcança sistemas de alto risco colocados no mercado da União. Um sistema de IA que opera a rede elétrica de um país asiático, africano ou latino-americano pode não estar sujeito a nada equivalente — e as duas notícias desta semana são, ambas, sobre países que estão apenas começando a escrever suas regras.

## O ponto de convergência

O que Filipinas e Bangladesh expõem, cada um à sua maneira, é que a governança de IA está sendo construída de fora para dentro: primeiro o marco legal, depois a coordenação institucional, depois — talvez — a capacidade técnica de observar o que os sistemas fazem. Nos sistemas que não podem falhar, a ordem precisa ser inversa. Sem observar, não há responsabilização real; sem responsabilização, o marco de governança é um documento bem redigido sobre algo que ninguém consegue medir.

A aviação levou décadas de acidentes para chegar ao desenho que hoje parece óbvio, e a IA está sendo colocada em operações críticas em uma fração desse tempo. A questão não é reinventar a roda: é decidir se a IA que opera o que não pode falhar merece o mesmo rigor que dedicamos a um avião — investigação independente de quem opera, relatório público, autorização que pode ser suspensa por desempenho, transparência sobre qual versão está no ar e gente capacitada como último controle antes do dano. E, como o caso Knight Capital mostra, "não pode falhar" deve incluir sistemas cuja falha não mata ninguém, mas pode quebrar uma empresa, uma cadeia de fornecedores e a vida de quem depende dela. A alternativa é continuar descobrindo os problemas pelo modo mais caro possível.

Para quem busca se orientar nesse cenário de rápida evolução, nossa [análise comparativa dos melhores modelos de IA](https://blog.ideias.casa/melhores-ia) acompanha e avalia as principais opções disponíveis no mercado.

---

> **Fonte original:** [Stratbase: PH should strengthen cybersecurity, AI governance](https://newsinfo.inquirer.net/2304368/stratbase-ph-should-strengthen-cybersecurity-ai-governance) - newsinfo.inquirer.net, por Dianne Sampang (INQUIRER.net, 13 de setembro de 2026).
>
> **Fonte original:** [The next decade of cyber resilience will depend on skills and awareness, says Kaspersky APAC chief](https://www.thedailystar.net/news/technology/news/the-next-decade-cyber-resilience-will-depend-skills-and-awareness-says-kaspersky-apac-chief-4271826) - thedailystar.net, por Md. Zahidur Rabbi.
>
> **Fontes de referência consultadas (aviação):** [Annex 13 — Aircraft Accident and Incident Investigation](https://www.bazl.admin.ch/dam/bazl/en/dokumente/Fachleute/Regulationen_und_Grundlagen/icao-annex/icao_annex_13_aircraftaccidentandincidentinvestigation.pdf.download.pdf/AN13_cons.pdf) (ICAO, 13ª edição) · [Manual of Aircraft Accident and Incident Investigation, Doc 9756](https://www.icao.int/sites/default/files/safety/airnavigation/AIG/Documents/9756_p1_cons_en.pdf) (ICAO) · [Safety Management — SARPs e Safety Management Manual](https://www.icao.int/safety-management/standards-and-recommended-practices-sarps) (ICAO) · [14 CFR Parte 39 — Airworthiness Directives](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-39) (FAA).
>
> **Fontes de referência consultadas (regulação de IA e risco financeiro):** [Regulamento (UE) 2024/1689 (AI Act), Artigos 3(49), 72 e 73](https://artificialintelligenceact.eu/article/73/) · [Regulamento Delegado do DORA sobre classificação de incidentes de TIC — critério de impacto econômico](https://digital-operational-resilience.org/regulations/ict-incidents-classification/chapter-ii/) · [Ordem da SEC no caso Knight Capital Americas LLC (2013)](https://www.sec.gov/litigation/admin/2013/34-70694.pdf) · [Calendário de aplicação do AI Act](https://artificialintelligenceact.eu/implementation-timeline/)
>
> **Imagem:** Torre de controle de tráfego aéreo com cúpula de vidro e antenas de comunicação sobre um edifício de escritórios, por Olivier Amyot, via [Unsplash](https://unsplash.com/photos/fY8kO-FiqNE), licenciada sob a [Unsplash License](https://unsplash.com/license).

---

👉 **Veja também nossa análise comparativa dos melhores modelos de IA em:** [blog.ideias.casa/melhores-ia](https://blog.ideias.casa/melhores-ia)
