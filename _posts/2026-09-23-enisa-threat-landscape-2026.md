---
layout: post
title: "ENISA Threat Landscape 2026: ransomware e exploração de vulnerabilidades no topo — e a IA entrando em toda a kill chain"
author: "autor bot"
categories: blog
tags: [blog,ia,seguranca,ciberseguranca,analise,regulacao,tecnologia]
image: enisa-threat-landscape-2026-featured.jpg
---

A ENISA, a agência da União Europeia para a cibersegurança, publicou em **setembro de 2026** a edição 2026 do seu *ENISA Threat Landscape* (ETL). O relatório tem 101 páginas, classificação **TLP:CLEAR** e licença CC BY 4.0 — ou seja, pode ser lido e reaproveitado por qualquer um, o que é raro e bem-vindo num documento desse tipo. A base é concreta: **8 257 incidentes** coletados e analisados, a partir de fontes abertas e de informação anonimizada enviada por Estados-Membros e por participantes do ENISA Cyber Partnership Programme.

Para Juhan Lepassaar, diretor executivo da ENISA, o valor do documento está menos na lista de ameaças e mais na leitura das dependências entre elas: "A análise destaca como as ameaças se tornam mais interconectadas e como os grupos de ameaça espalham o seu impacto pelo mapa mais amplo de serviços digitais e infraestruturas. Ter consciência dessas dinâmicas subjacentes é fundamental se queremos implementar as soluções certas e manter um alto nível de resiliência em nossa economia digital."

Vale dizer de saída o que o próprio documento avisa: o **período de análise passou a ser o ano-calendário**, cobrindo **1º de janeiro a 31 de dezembro de 2025**. Como a edição anterior usava outro recorte, há **seis meses de sobreposição** entre os dois relatórios. A ENISA também ampliou o número de atividades criminosas rastreadas — o que mexeu nos números absolutos, mas, segundo a agência, "não alterou substancialmente as tendências e rankings" da edição anterior. Quem comparar as duas edições precisa ter isso em mente.

## O retrato geral: muito ruído, pouco impacto — e uma exceção

Os dois tipos de incidente mais registrados seguem sendo os mesmos: **DDoS com 51,3%** e **acesso não autorizado com 39,5%**. Entre as técnicas de engenharia social, o phishing continua folgado na frente, com **77,8%**, seguido por spam malicioso (*malspam*), com 13%.

Mas o dado mais interessante do capítulo de visão geral é uma assimetria que o relatório não esconde. Olhando pela **motivação** dos ataques, o cenário se inverte:

| Objetivo avaliado | Participação nos incidentes |
|---|---|
| Ideológico | **57,3%** |
| Financeiro | **29,3%** |
| Ciberespionagem | **cerca de 6%** |

A atividade ideológica é a que mais aparece — e é justamente a que produz menos dano. O relatório classifica os DDoS como ataques de **baixo impacto**, moldados por desenvolvimentos geopolíticos e declarações políticas. A ENISA vai além e cita o seu próprio relatório de investimentos em NIS: representantes de organizações europeias de setores de alta criticidade descrevem DDoS como **"ruído"**, enquanto o **ransomware domina as preocupações organizacionais**.

"Atividades com motivação financeira (29,3% de todos os incidentes registrados), em especial o ransomware, permaneceram os incidentes de maior impacto no curto prazo", resume o documento. E acrescenta o outro lado: embora represente menos casos, a **ciberespionagem é a ameaça estratégica mais relevante no médio e longo prazo**. Há ainda um detalhe metodológico que explica boa parte do "ruído": nos registros de hacktivismo, **apenas 23,8% das reivindicações de ataque foram confirmadas por verificações independentes de disponibilidade**. Ou seja, mais de três quartos das alegações públicas não se sustentam — muita coisa é operação de informação, não de indisponibilidade real.

## Setores: administração pública na frente, e a saúde só aparece em uma das fontes

O ranking dos setores mais visados na UE é estável em relação ao ano anterior:

| Setor | Participação |
|---|---|
| Administração pública | **31,8%** |
| Serviços empresariais | **8,5%** |
| Transporte | **8%** |
| Manufatura | **6,9%** |
| Finanças / bancos | **5,6%** |

Um número que dimensiona a relevância da regulação: **entidades essenciais e importantes somam cerca de 73% do total de eventos registrados**, o que, para a ENISA, "confirma a pertinência da abordagem da NIS2". No setor de administração pública, a composição chama atenção — **81,8% dos incidentes são DDoS ideológicos**, com impacto normalmente limitado a indisponibilidade temporária de portais. Os grupos mais ativos ali são o pró-Rússia **NoName057(16)**, o **Dark Storm Team** e o **Mr. Hamza**.

O relatório faz uma comparação que merece leitura cuidadosa. Quando se olha o que os **Estados-Membros reportaram sob a NIS2** em 2025 — **1 954 eventos** até 14 de julho de 2026, dos quais **941 por "ações maliciosas"**, com cerca de **50% sem causa-raiz identificada** —, o top 5 muda de figura: administração pública, **saúde**, **infraestrutura digital**, bancos e transporte. Saúde e infraestrutura digital não aparecem no top 5 da coleta por fontes abertas. A explicação da ENISA é honesta: escopos, limiares e condições de reporte diferentes. É um bom lembrete de que **todo ranking de ameaças é também um ranking de quem reporta**.

## Ransomware: a criptografia perdeu espaço para a extorsão

Se há uma seção que justifica a leitura integral do relatório, é a de ransomware. O dado que salta é a mudança de técnica: a exfiltração por canais de comando e controle (T1041, na taxonomia MITRE ATT&CK) aparece em **73,3%** dos casos observados, enquanto a **criptografia de dados para causar impacto (T1486) caiu para 13,7%**.

O modelo de negócio mudou de "criptografar e cobrar" para "roubar e ameaçar publicar". Isso tem consequência prática direta: uma estratégia de defesa centrada em *backup* e recuperação cobre apenas uma fração do risco. Se o dado já saiu, restaurar o sistema não resolve nada.

Entre os grupos, o **top 5 na UE é Qilin, SafePay, Akira, INC Ransom e Hunters International**. A dinâmica de cada um ao longo de 2025 foi irregular: Akira começou o ano em ritmo alto e desacelerou; **Qilin registrou um pico significativo em outubro de 2025** (motivo não identificado); SafePay teve dois picos, **22 reivindicações em maio e 26 em dezembro**; e o Hunters International saiu de **uma única reivindicação em fevereiro para 52 em abril**, comportamento que os analistas associaram a uma transição para extorsão pura, hipótese que não se confirmou depois.

O Qilin merece um parágrafo. O grupo passou a usar táticas de pressão psicológica, incluindo um recurso chamado **"call lawyer"**, que simula uma escalada jurídica contra a vítima. A ENISA é explícita sobre por que isso é particularmente eficaz na Europa: **as obrigações de reporte de incidentes e as exigências do GDPR provavelmente funcionam como incentivo adicional para a vítima pagar**. É um exemplo de manual de como o atacante adapta a extorsão ao ambiente regulatório em que a vítima vive — e uma inversão perversa: a norma que deveria proteger acaba se tornando pressão de negociação.

Dois outros vetores de pressão aparecem no documento. Em junho de 2025, variantes do **EDRKillShifter** começaram a ser embutidas em vários conjuntos de ransomware como serviço (Medusa, Qilin, DragonForce, Lynx, BlackSuit, RansomHub e INC), atacando a própria ferramenta de defesa. E **33 organizações europeias foram identificadas como vítimas repetidas** — **44% delas por ransomware e 40% por violação de dados** —, padrão que a ENISA associa provavelmente a **falta de práticas de restauração após a resposta ao incidente**.

Geograficamente, as reivindicações de ransomware na UE se concentram na **Alemanha (26,5%), França (14,7%), Itália (13,6%), Espanha (12,2%) e Países Baixos (4,7%)**. Na ponta oposta, **Lituânia (0,1%)** e Estônia, Letônia, Bulgária e Eslováquia (**0,3%** cada). Por setor, a **manufatura lidera com 25,2%**, seguida por serviços empresariais (18,7%), administração pública (6,7%), saúde e o setor de produção e distribuição de alimentos.

Um caso ilustra o que "impacto" significa na prática: em setembro de 2025, o grupo **Everest** explorou acesso FTP indevido à infraestrutura do software de check-in **vMUSE**, da Collins Aerospace, e exfiltrou **mais de 1,5 milhão de registros de passageiros** e **3 637 registros de funcionários de companhias aéreas**, provocando disrupção severa de voos e fechamento de aeroportos na Europa. Outro: o ataque de ransomware a um **fornecedor de TI sueco afetou cerca de 200 municípios e autoridades regionais**.

## Vulnerabilidades: o volume cresceu 22% e o tempo encurtou

O capítulo 7 traz os números que conectam o relatório ao trabalho diário de qualquer equipe de infraestrutura:

- **Mais de 48 mil novas vulnerabilidades** com identificador CVE publicadas em 2025 — **aumento de 22%** em relação ao ano anterior;
- **71%** dos CVEs documentados têm **"rede" como vetor de ataque**, o que sublinha o risco de exploração remota em sistemas expostos à internet;
- distribuição por severidade CVSS: **9% críticas, 30% altas, 49% médias, 3% baixas** e 9% sem pontuação;
- **245 vulnerabilidades** foram adicionadas ao catálogo de exploradas conhecidas (KEV) da CISA no período.

O relatório também registra que os atacantes seguem conseguindo **armamentizar vulnerabilidades recém-divulgadas em janelas de tempo cada vez menores**. Os alvos preferenciais são consistentes: **infraestrutura corporativa, dispositivos de borda, ferramentas de desenvolvimento** e dispositivos **IoT e de borda legados sem correção**, com D-Link, Zyxel, DASAN, Huawei, Realtek e Netgear citados nominalmente. Entre os casos europeus, aparecem **FortiGate** (CVE-2024-21762 e CVE-2024-55591, usadas pelo Qilin e pelo INC Ransom), **Oracle E-Business Suite** (CVE-2025-61882, explorada pelo Cl0p em esquema de extorsão pura) e **React2Shell** (CVE-2025-55182).

Há uma nota institucional relevante: desde **novembro de 2025**, a ENISA passou a operar como **Root CVE**, tornando-se ponto central de contato do programa CVE para autoridades nacionais e da UE — além de manter a **EUVD**, a base europeia de vulnerabilidades.

## A IA: de assistente a fase da kill chain

O trecho mais citado da cobertura de imprensa é também o mais bem calibrado do documento. A avaliação central da ENISA é que, em 2025, **os atacantes usaram principalmente ferramentas de IA de nível consumidor para ampliar habilidades que já tinham**, e não para obter capacidades revolucionárias. "Os relatos de 2025 indicam que os atacantes usam principalmente ferramentas de IA de nível consumidor para ampliar habilidades existentes e adaptar vetores de ataque, e não para alcançar capacidades revolucionárias", afirma o texto.

Só que a frase seguinte muda o tom: melhorias de modelo **já estão acelerando a descoberta e a exploração de vulnerabilidades**. E a projeção é forte:

> "A ENISA avalia que a inteligência artificial muito provavelmente apoiará cada vez mais operações maliciosas [...] é também provável que 2026 veja um número maior de fases da *kill chain* diretamente habilitadas por IA, com possível experimentação de provas de conceito com o humano fora do *loop*."

Os exemplos concretos que sustentam o alerta são notáveis:

- uma **intrusão em nuvem assistida por IA** teria alcançado **acesso administrativo em 8 minutos**;
- o grupo de ransomware **Gentlemen**, ativo na UE, usou **assistentes de codificação com IA para desenvolver o painel RaaS** do grupo;
- um **site falso do Claude AI** foi usado para distribuir malware — ou seja, a marca do próprio modelo virou isca;
- a **Anthropic** relatou um grupo ligado a um Estado usando um **sistema de IA agêntico** numa campanha contra alvos internacionais não identificados, com um número limitado de compromissos bem-sucedidos;
- a técnica **"AI in the Middle"** demonstrou que serviços de IA baseados na web podem ser abusados como **proxies de comando e controle**, dando furtividade e resiliência à infraestrutura do atacante;
- surgiram métodos "industrializados" para garantir **acesso confiável, barato e anonimizado a camadas premium de LLMs**.

O relatório trata a IA também como **alvo**, e não só como ferramenta. Aplicações de IA com acesso a arquivos, credenciais, sessões de navegador ou ambientes de desenvolvimento viraram superfície de ataque — há registro de extensões maliciosas de assistentes de IA coletando **históricos de conversa** com LLMs. É a tese que o blog vem acompanhando de outros ângulos: a autonomia dos agentes transforma o próprio agente em vetor. Para quem busca se orientar nesse cenário de rápida evolução, nossa [análise comparativa dos melhores modelos de IA](https://blog.ideias.casa/melhores-ia) acompanha e avalia as principais opções disponíveis no mercado — e ajuda a separar o que é capacidade real do que é marketing de segurança.

Vale registrar o número que talvez melhor traduza o ano de 2025, e que está no capítulo de manipulação de informação: **27% dos incidentes detectados pelo Serviço Europeu de Ação Externa (EEAS) envolveram TTPs relacionadas a IA** — um salto de **41 para 147 casos**, crescimento de aproximadamente **259%** em um ano. Atores de FIMI russos e chineses, segundo o documento, "incorporaram plenamente" ferramentas de IA às suas operações para acelerar a produção de conteúdo e escalar a influência com menos recursos.

O capítulo também descreve um deslocamento estratégico: a Rússia tratou a manipulação de informação como **instrumento central de poder estatal**, redirecionando o foco dos Estados Unidos para a Europa. As campanhas de FIMI acompanharam ações híbridas escalatórias — incursões de drones, sabotagem e ataques a infraestrutura crítica na **Polônia, Romênia, Lituânia e Estônia** —, com o objetivo declarado de moldar a percepção pública e testar a resposta europeia. No total, o EEAS identificou **540 incidentes de FIMI** no período, com **88% da atividade concentrada na plataforma X** e **65% dos casos sem atribuição**.

Do lado institucional, a Comissão Europeia publicou o **Plano de Ação da UE para Cibersegurança e Inteligência Artificial**, apoiado no AI Act, no Cyber Resilience Act, na NIS2 e no Cyber Solidarity Act. No mesmo dia, a ENISA divulgou a sua visão sobre cibersegurança na era da IA de fronteira. As peças regulatórias estão sendo encaixadas; o que ainda não existe é evidência de que a velocidade de defesa acompanhe a de exploração.

## Engenharia social: quando o ataque abusa do processo legítimo

O capítulo sobre crime cibernético reforça uma mudança de padrão que vem sendo notada há alguns trimestres. A avaliação da ENISA é que as campanhas passaram a se apoiar cada vez mais em **plataformas de comunicação confiáveis** e em **mecanismos legítimos de autenticação**, em vez de explorar apenas falhas técnicas. Duas técnicas simbolizam esse deslocamento:

- **ClickFix** — a vítima é induzida a "consertar" um problema e acaba executando comandos PowerShell que foram automaticamente copiados para a área de transferência. Foi prevalente em 2025, com a variante **FileFix**;
- **phishing de código de dispositivo** (*device code phishing*) — o alvo é conduzido a um fluxo de autenticação legítimo para conceder acesso ao atacante. Campanhas em larga escala usaram **Signal e WhatsApp** para o contato inicial personalizado.

Há também números que dimensionam a industrialização da fraude. **77% dos domínios de phishing foram registrados especificamente para viabilizar ataques**, e o total de domínios de phishing **cresceu 38% em um ano**. O **Smishing Triad** mantém **cerca de 25 mil domínios ativos em qualquer janela de oito dias**. O **Tycoon 2FA** foi o kit de phishing mais observado globalmente no período, operando como estrutura *adversary-in-the-middle* para burlar a autenticação multifator. A ENISA aponta responsabilidade explícita nessa cadeia: "registros e registradores têm responsabilidade significativa na detecção e mitigação desse abuso".

Outro dado com consequência direta para quem trabalha em empresas europeias: a **impersonação de autoridades fiscais e serviços digitais de governo foi observada em pelo menos nove Estados-Membros**, com iscas previsíveis — restituição de imposto, avisos de pagamento em atraso, atualização de dados bancários. E há um caso que interessa especialmente ao blog: o **Famous Chollima**, ligado à Coreia do Norte, usa **perfis falsos de LinkedIn gerados por IA** e **pacotes npm trojanizados** para se infiltrar em empresas de defesa e governo — inclusive na UE —, com o golpe do "trabalhador de TI remoto". O comprometimento de bibliotecas populares e pacotes npm, como a campanha **Shai-Hulud**, foi tamanho que a ENISA publicou em **março de 2026** um **aviso técnico sobre o uso seguro de gerenciadores de pacotes**.

## Rússia na frente, e a convergência que dificulta atribuição

O capítulo de ameaças ligadas a Estados traz o mapa da ciberespionagem contra a UE. Foram observados **52 conjuntos de intrusão distintos** ativos no bloco. A distribuição por nexo de atribuição:

| Nexo | Participação |
|---|---|
| Rússia | **47,6%** |
| China | **15,5%** |
| Coreia do Norte (DPRK) | **14,1%** |
| Irã | **9%** |
| Não atribuídos | **cerca de 1,5%** |

Os alvos acompanham a geopolítica: **administração pública (29,4%)**, manufatura (9,8%), infraestrutura digital (8,2%), sociedade civil (7%) e transporte (5,5%). O **APT29** mirou entidades diplomáticas e ministérios de Relações Exteriores; o **APT28** focou governos centrais e organizações de defesa; e o **DragonFly** executou em **dezembro de 2025** um ataque coordenado contra o setor de energia, **com uso de um *wiper*** — um destruidor de dados, não um espião. Do lado chinês, o **Salt Typhoon** ganhou confirmação pública: em junho de 2025, a Viasat confirmou um comprometimento, e em agosto um aviso conjunto de autoridades europeias, americanas e britânicas descreveu operações sobrepostas ao grupo contra **telecomunicações, governo, transporte e sistemas militares em mais de 80 países**.

A conclusão do relatório, porém, aponta para um problema que nenhum ranking captura: os três ecossistemas — crime, hacktivismo e Estados — **estão convergindo nas ferramentas e nos caminhos de acesso**. O caso exemplar é o **Moonstone Sleet**, ligado a um Estado, usando o ransomware **Qilin**. "Os mesmos vetores de acesso, ferramentas e abordagens operacionais" tornam a imputação e a análise de ameaça mais difíceis, e o cenário, nas palavras da ENISA, "virtualmente inflado e disperso". O grupo **Babuk2** é outro sintoma: reivindicações fabricadas ou recicladas contra alvos militares e de defesa, funcionando parcialmente como corretor de acesso inicial.

## O que fazer com isso

O relatório não traz um capítulo formal de recomendações, mas as orientações estão distribuídas e convergem para um ponto central: **como os três tipos de ator usam os mesmos caminhos, mitigar o ator da moda vale menos do que fechar as fraquezas comuns**. Destilando o documento em decisões:

1. **Cobrir exfiltração, não só criptografia.** Com T1041 em 73,3% e T1486 em 13,7%, controle de dados egressos, segmentação e detecção de exfiltração passam à frente da obsessão com *backup*.
2. **Priorizar borda e legado.** 71% dos CVEs têm vetor de rede; appliances de VPN e firewall e dispositivos IoT/edge sem correção continuam sendo o caminho mais barato para o atacante.
3. **Revisar a restauração, não só a resposta.** As 33 organizações europeias revitimizadas apontam para falha na prática de reconstrução pós-incidente.
4. **Tratar o fator humano como processo, não como treinamento.** ClickFix e *device code phishing* abusam de fluxos legítimos; a defesa precisa mudar o processo, não apenas avisar o usuário.
5. **Assumir a dependência de terceiros como risco próprio.** Fornecedores de software, MSPs, plataformas de nuvem e ambientes de atendimento continuam sendo alvos de alto valor para impacto em cascata — o fornecedor sueco que parou 200 municípios é a prova.
6. **Proteger o stack de segurança.** Ataques a ferramentas EDR e o abuso de drivers vulneráveis (BYOVD) mostram que a camada de defesa virou alvo de primeira classe.
7. **Tratar a IA como superfície de ataque.** Aplicações de IA com acesso a arquivos, credenciais e sessões precisam do mesmo rigor de revisão que qualquer sistema privilegiado.

Para quem quiser ir além do resumo — e a leitura vale muito — o PDF oficial é aberto e está linkado abaixo. A edição 2026 tem uma qualidade que não é comum em relatórios institucionais: ela diz explicitamente onde os dados são frágeis. A ressalva de que campanhas de ciberespionagem são documentadas com atraso que varia de **seis meses a mais de quatro anos**, e a observação de que **aumento de reporte nem sempre significa aumento de atividade**, são o tipo de honestidade metodológica que faz o documento valer como fonte primária, e não apenas como material de divulgação.

---

> **Fonte original:** [ENISA Threat Landscape 2026 highlights ransomware, vulnerability exploitation, AI-enabled attacks across EU organizations](https://industrialcyber.co/reports/enisa-threat-landscape-2026-highlights-ransomware-vulnerability-exploitation-ai-enabled-attacks-across-eu-organizations/) — industrialcyber.co (Industrial Cyber), 23 de setembro de 2026, por Anna Ribeiro.
>
> **Comunicado de imprensa da ENISA (citado na nota de leitura abaixo):** [Exploring the evolution of the cyber threat landscape: How dependencies weaken our digital resilience](https://www.enisa.europa.eu/news/exploring-the-evolution-of-the-cyber-threat-landscape-how-dependencies-weaken-our-digital-resilience) — enisa.europa.eu, 22 de setembro de 2026.
>
> **Fonte primária (documento completo, lido na íntegra):** [ENISA Threat Landscape 2026 — Final](https://www.enisa.europa.eu/sites/default/files/2026-09/ENISA%20Threat%20Landscape%202026_Final.pdf) — enisa.europa.eu, setembro de 2026, 101 páginas, autoria ENISA. Período coberto: 1º de janeiro a 31 de dezembro de 2025. Base: 8 257 incidentes. ISBN 978-92-9204-807-5, DOI 10.2824/0806036, classificação TLP:CLEAR, licença [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
>
> **Página de publicação da ENISA:** [ENISA Threat Landscape 2026](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026) — enisa.europa.eu.
>
> **Fontes citadas pelo próprio relatório, consultadas como referência cruzada:** [ENISA NIS360 2026](https://www.enisa.europa.eu/sites/default/files/2026-05/ENISA%20NIS360%202026.pdf) (zona de risco cibernético da administração pública) · [ENISA NIS Investments 2025](https://www.enisa.europa.eu/publications/nis-investments-2025) (DDoS como "ruído", ransomware como preocupação dominante) · [ENISA Technical Advisory on Package Managers](https://www.enisa.europa.eu/sites/default/files/2026-03/ENISA%20Technical%20Advisory%20-%20Package_Managers_Final.pdf) (março de 2026) · [Plano de Ação da UE para Cibersegurança e IA](https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1544).
>
> **Nota de leitura — divergência verificada entre as duas fontes da própria ENISA.** Comparando o comunicado de imprensa da agência (22 de setembro de 2026) com o corpo do PDF final, os percentuais não batem:
>
> | Métrica | Comunicado de imprensa | PDF final (documento primário) |
> |---|---|---|
> | Crime cibernético no total de eventos | **36%** | **29,3%** |
> | Ransomware | **40%** | **47,3%** (dentro das reivindicações financeiras) |
> | Violações de dados | **31%** | **36%** |
> | Fraude e impersonação | **19%** | **13,3%** |
> | Atores estatais por operações de intrusão | **87%** | **81,7%** |
> | Fraude de investimento online (EBA, 2024) | **4 bilhões de euros** | **4,2 bilhões de euros** |
>
> Os denominadores e as categorias não são os mesmos entre as duas publicações, e os números se contradizem. A própria cobertura de imprensa herdou a mistura: o texto da Industrial Cyber abre atribuindo 36%/40%/31%/19% ao relatório e, mais adiante no mesmo artigo, reproduz corretamente os 29,3% do resumo executivo. **Este post segue os números do documento final**, que é a fonte primária — mas quem citar a ENISA deve indicar qual das duas fontes está usando.
>
> **Imagem:** Globo terrestre suspenso sobre uma mão, com o Brasil e a América do Sul em destaque, por Maurício Mascaro, via [Pexels](https://www.pexels.com/photo/selective-focus-photo-of-globe-floating-over-a-hand-4870334/), licenciada sob a [Pexels License](https://www.pexels.com/license/).

---

👉 **Veja também nossa análise comparativa dos melhores modelos de IA em:** [blog.ideias.casa/melhores-ia](https://blog.ideias.casa/melhores-ia)
