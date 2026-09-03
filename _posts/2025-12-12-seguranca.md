---
layout: post
title: "Violações da LGPD e Proteção de Dados no Mundo: O Desafio Global da IA"
author: "Davi"
categories: blog
tags: [blog,privacidade,regulacao,seguranca,ia,lgpd]
image: secperson.jpg
---

A inteligência artificial tem se tornado um dos maiores desafios para a proteção de dados pessoais em escala global. Desde o treinamento de grandes modelos de linguagem até sistemas de reconhecimento facial, as tecnologias de IA estão gerando um novo cenário de violações de privacidade que desafia as estruturas regulatórias tradicionais. A Lei Geral de Proteção de Dados (LGPD) brasileira, assim como a General Data Protection Regulation (GDPR) europeia e outras legislações globais, ainda lutam para acompanhar a velocidade de inovação e os riscos reais apresentados por esses sistemas. Enquanto isso, multas recordes são impostas, dados pessoais são expostos em larga escala e a confiança dos cidadãos em organizações continua a ser abalada por violações flagrantes que combinam negligência técnica com ambição comercial desmedida.

## O Cenário Global de Violações de Proteção de Dados

A onda de violações de dados envolvendo tecnologias de IA não é apenas um problema brasileiro ou europeu. Trata-se de um desafio sistêmico que permeia jurisdições e continentes. Em 2024, o número de incidentes de segurança envolvendo IA saltou 56,4% em relação ao ano anterior, com nearly half of all breaches envolvendo dados pessoais identificáveis (PII) de clientes. Essa aceleração não é coincidência: é resultado direto da explosão no uso de modelos de linguagem generativa, sistemas de recomendação baseados em IA e tecnologias de reconhecimento facial que dependem fundamentalmente do processamento de enormes volumes de dados pessoais.[^1_1]

Os maiores reguladores de dados do mundo, desde a Autoridade Nacional de Proteção de Dados (ANPD) do Brasil até a Comissão de Proteção de Dados da Irlanda, reconhecem que as estruturas regulatórias existentes não cobrem adequadamente os riscos emergentes da IA. A ANPD, em particular, realizou em 2025 um estudo preliminar sobre IA generativa que destacou lacunas críticas: questões sobre a legalidade do web scraping para treinar modelos, a responsabilidade quando sistemas de IA geram dados pessoais em seus resultados (conhecidos como "alucinações"), e o desafio de aplicar direitos de dados em contextos de processamento altamente automatizado.[^1_2]

## LGPD: O Cenário Brasileiro de Enforcement

A ANPD iniciou seu enforcement mais agressivo a partir de 2023, marcando uma mudança fundamental na abordagem regulatória. O primeiro caso de multa por violação da LGPD ocorreu em 2023, envolvendo a Telekall Infoservice, pequena empresa de telecomunicações que processava dados pessoais sem base legal, falhou em designar um Data Protection Officer (DPO) e obstruiu investigações. Embora a multa fosse pequena em termos absolutos – apenas BRL 14.400 (~\$2.960) – seu valor simbólico foi enorme: sinalizava que nenhuma empresa, independentemente do tamanho, está imune ao enforcement regulatório.[^1_3]

Desde então, a ANPD aplicou multas totalizando BRL 98 milhões (~\$20 milhões) entre 2023 e 2025. Estruturalmente, as penalidades sob a LGPD podem atingir até 2% da receita anual de uma empresa no Brasil, com teto de BRL 50 milhões por violação. As sanções não-pecuniárias podem ser ainda mais severas: bloqueio de dados, exclusão permanente de informações coletadas, e divulgação pública da violação – o que causa dano reputacional muitas vezes maior que qualquer multa.[^1_4][^1_5][^1_3]

Setores como saúde, finanças e empresas de tecnologia com foco em IA têm sido os principais alvos da ANPD. Isso ocorre porque essas organizações típicamente processam grandes volumes de dados sensíveis e, frequentemente, utilizam essas informações para treinar sistemas de inteligência artificial. A autoridade brasileira reconhece que, enquanto a LGPD oferece princípios fundamentais como finalidade, necessidade e segurança, aplicá-los a sistemas de IA generativa requer interpretação cuidadosa e orientações específicas ainda em desenvolvimento.[^1_6][^1_3]

## IA Generativa e LGPD: O Caso do ChatGPT

O caso mais emblemático de tensão entre IA e proteção de dados envolve a OpenAI e seu ChatGPT. Em julho de 2023, a ANPD abriu investigação formal sobre como o ChatGPT cumpria as obrigações da LGPD após receber reclamações públicas. Os problemas identificados eram numerosos e sistêmicos: a falta de base legal clara para processar dados de usuários europeus durante o treinamento do modelo, ausência de transparência sobre quais dados pessoais foram utilizados, impossibilidade de exercer direitos de acesso e exclusão, e a incapacidade do usuário de corrigir informações imprecisas geradas pelo sistema.[^1_7][^1_8]

Pesquisadores brasileiros e internacionais apontaram que o ChatGPT viola múltiplos artigos da LGPD. O Princípio da Transparência (Art. 6, IV da LGPD) exige que os titulares de dados recebam "informações claras, precisas e facilmente acessíveis sobre a realização do tratamento e os respectivos agentes de tratamento". Porém, a OpenAI não fornecia sequer informações básicas sobre quais dados pessoais eram coletados, como eram armazenados, com quem eram compartilhados ou por quanto tempo seriam retidos.[^1_8][^1_9]

A situação se tornou tão preocupante que a Itália, cujo regulador Garante tem sido historicamente mais agressivo que a ANPD, bloqueou temporariamente o acesso ao ChatGPT em março de 2023, citando violações de GDPR. Embora o bloqueio tenha sido levantado após negociações, investigações subsequentes resultaram em uma multa de €15 milhões contra a OpenAI em dezembro de 2024, justificada pela falta de base legal para processamento de dados europeus, ausência de verificação real de idade de menores e insuficiência nas medidas de transparência.[^1_10][^1_11][^1_7]

## Estudo Preliminar da ANPD sobre IA Generativa

Reconhecendo a urgência da questão, a ANPD publicou em 2025 um estudo preliminar que busca estabelecer marcos para conformidade com a LGPD em sistemas de IA generativa. O documento identifica quatro cenários críticos de processamento de dados:[^1_2]

**1. Treinamento de modelos com dados coletados da web**: A ANPD confirma que dados pessoais publicamente disponíveis continuam protegidos pela LGPD. Operações de web scraping devem ter base legal específica (consentimento ou uma das hipóteses dos artigos 7 ou 11) e devem respeitar os princípios de boa fé, limitação de finalidade, adequação e necessidade. Muitas empresas que desenvolvem IA argumentam que dados "públicos" não merecem proteção, mas a ANPD refuta firmemente essa posição.[^1_2]

**2. Processamento de dados durante a interação do usuário com o modelo**: Quando um usuário interage com um chatbot generativo fornecendo seus dados (mesmo em prompts), esses dados são processados e frequentemente armazenados para melhorar o sistema. A ANPD destaca a necessidade de transparência clara e direitos exercitáveis nesse contexto.[^1_2]

**3. Geração de dados pessoais na saída do modelo**: Um dos cenários mais complexos envolve quando o sistema de IA gera ou infere informações pessoais em suas respostas. Se um usuário pergunta "quem é João Silva?" e o sistema gera informações sobre múltiplas pessoas com esse nome, incluindo dados potencialmente imprecisos ou sensíveis, uma cadeia de responsabilidade deve ser estabelecida entre o desenvolvedor da IA, a plataforma que oferece o serviço e o usuário que fez a consulta.[^1_2]

**4. Alucinações prejudiciais de IA**: Quando modelos criam informações falsas mas específicas sobre indivíduos (por exemplo, atribuindo crimes ou condutas desonestas inexistentes a uma pessoa), isso pode violar direitos à dignidade e personalidade, gerando potencial responsabilidade civil e regulatória.[^1_2]

## Violações de GDPR e Multas Recordes na Europa

Enquanto isso, a Europa continua a ser o epicentro da aplicação rigorosa de proteção de dados. Em 2024, as autoridades de proteção de dados da UE emitiram €1,2 bilhões em multas por violações de GDPR, com muitos casos envolvendo diretamente tecnologias de IA ou seus usos indevidos.[^1_12]

**O caso Meta/Facebook**: A Meta Platforms enfrentou a maior multa de proteção de dados da história: €1,2 bilhão em maio de 2023 por transferências ilegais de dados de usuários europeus para os EUA sem salvaguardas adequadas. Separadamente, em janeiro de 2023, foi multada em €390 milhões por exigir que usuários aceitassem publicidade personalizada baseada em IA como condição para usar o Facebook e Instagram, quando na verdade tal publicidade não era essencial aos serviços básicos de rede social. Mais recentemente, em setembro de 2024, foi novamente multada em €91 milhões por armazenar senhas de usuários em texto sem encriptação, uma falha de segurança elementar que viola o Art. 32 da GDPR sobre medidas técnicas e organizacionais adequadas.[^1_13][^1_14]

**O caso Clearview AI**: Talvez nenhum caso melhor ilustre os perigos da IA sem regulação que o Clearview AI, uma empresa que criou uma base de dados de reconhecimento facial com mais de 40 bilhões de imagens coletadas ilegalmente da web. O Clearview realizava "scraping" de fotos de perfil de redes sociais, sites de notícias e outras fontes públicas sem consentimento, depois vendo acesso a essa base de dados a agências de aplicação da lei. Em maio de 2022, a autoridade de proteção de dados do Reino Unido multou Clearview em USD 9 milhões. A Holanda, em setembro de 2024, impôs a multa maior: €30,5 milhões, proibindo empresas holandesas de usar os serviços de Clearview. Investigações similares em França, Itália, Grécia e Austrália resultaram em multas adicionais e proibições.[^1_15][^1_11][^1_16][^1_12]

O Clearview AI também violava gravemente a lei de privacidade da Califórnia (CCPA). Uma análise realizada por Consumer Watchdog demonstrou que o Clearview era incapaz de honrar solicitações de opt-out porque seus sistemas automaticamente re-coletavam imagens de indivíduos que já tinham ordenado exclusão. Além disso, como o Clearview nunca verificava a idade dos indivíduos nas imagens que colecionava, estava de fato construindo um banco de dados de crianças sem consentimento dos pais, violando proteções federais e estaduais específicas para menores.[^1_16]

**O caso OpenAI/ChatGPT na Itália**: Além da investigação brasileira, a Itália multou OpenAI em €15 milhões em dezembro de 2024. A multa específica foi por falta de transparência sobre como dados eram coletados e usados para treinar o ChatGPT, ausência de verificação real de idade de menores (permitindo que crianças criassem contas), e falta de base legal adequada para o processamento de dados de cidadãos europeus.[^1_11][^1_10]

## Regulações Globais: GDPR, CCPA, PIPL e DPDPA

Enquanto a LGPD brasileira ainda desenvolve sua jurisprudência e enforcement sobre IA, outras regiões implementam marcos regulatórios complementares. O GDPR europeu permanece o modelo mais rigoroso e influente globalmente. A GDPR estabeleceu o precedente de multas colosais e de aplicação consistente que incentiva conformidade genuína. Suas exigências sobre consentimento explícito, bases legais claras, direitos de dados e avaliações de impacto de privacidade tornaram-se o padrão internacional.[^1_17][^1_18]

Nos Estados Unidos, a Califórnia liderou com a CCPA em 2018, que protege residentes californianos com direitos de conhecer, deletar e optar por não participar do compartilhamento de dados pessoais. A lei incluiu proteções especiais para dados biométricos, diretamente relevantes para tecnologias de reconhecimento facial baseadas em IA. Porém, a aplicação da CCPA tem sido desigual; muitos aplicativos móveis continuam violando suas disposições. Um estudo demonstrou que 80% dos aplicativos analisados coletavam identificadores persistentes sem divulgação adequada, 30% coletavam dados de geolocalização e 26% coletavam dados sensoriais, tudo frequentemente sem consentimento claro.[^1_19][^1_20][^1_21]

A China promulgou a Lei de Proteção da Privacidade de Informações Pessoais (PIPL) em 2021, que, embora inspirada no GDPR, reflete prioridades diferentes. A PIPL exige rigorosa localização de dados especialmente para "operadores de infraestrutura crítica" e dados considerados sensíveis pelo governo. Enquanto o GDPR enfatiza direitos individuais dos titulares de dados, a PIPL prioriza segurança nacional e controle estatal, permitindo ao governo avaliar transferências de dados e impor restrições que vão além da privacidade. Para IA, essa abordagem significa que sistemas de IA chineses podem estar sujeitos a escrutínio governamental mais intenso, mas também podem ter menos liberdade para inovar em direções que o estado considere arriscadas.[^1_22][^1_23]

A Índia, reconhecendo os desafios específicos de seus mercados, implementou a Lei de Proteção de Dados Digitais Pessoais (DPDPA) em 2023. Estudos iniciais apontam lacunas críticas da DPDPA em regular IA, especialmente quanto à transparência de algoritmos, correção de vieses em IA e responsabilidade por tomada de decisão automatizada.[^1_24]

## Os Desafios Técnicos e Legais da IA e Proteção de Dados

### Web Scraping e Treinamento de Modelos

Um dos maiores pontos de tensão envolve a coleta de dados para treinar modelos de IA. Empresas como Google, OpenAI e Meta argumentam que o web scraping de dados publicamente disponíveis é lícito e necessário para desenvolver sistemas de IA. Porém, reguladores globais discordam fundamentalmente.

Em agosto de 2023, 12 autoridades internacionais de proteção de dados e privacidade – incluindo a ANPD, ICO do Reino Unido e OAIC da Austrália – emitiram uma declaração conjunta criticando o web scraping em larga escala de plataformas sociais. Observaram que empresas estavam coletando dados pessoais em escala massiva para revender a terceiros (potencialmente atores maliciosos) com fins lucrativos, elevando risco de fraude de identidade, ataques cibernéticos direcionados e uso não autorizado de dados para fins políticos ou de inteligência estrangeira.[^1_25]

A questão legal é complexa: dados tecnicamente públicos (um perfil aberto no LinkedIn, uma foto compartilhada no Facebook) ainda são dados pessoais sob a LGPD e GDPR. Processá-los para fins de treinar IA requer base legal. Consentimento é raramente obtido explicitamente. A alternativa legal – "interesse legítimo" – é também contestável, pois tribunais e reguladores cada vez mais exigem demonstração clara de que o benefício para a empresa supera o direito à privacidade dos indivíduos.[^1_18][^1_26][^1_2]

### Viés Algorítmico e Discriminação

Um segundo desafio emergente envolve viés e discriminação em sistemas de IA. A detecção de viés frequentemente requer análise de dados sensíveis especialmente protegidos sob a GDPR e LGPD (por exemplo, raça, gênero, religião, saúde). Porém, a GDPR Art. 9 proíbe explicitamente o processamento de tais dados sem consentimento explícito ou excepções muito restritas.[^1_27]

A UE AI Act, que entrou em vigor parcialmente em 2025, permite que desenvolvedores de sistemas de IA de alto risco processem dados especiais "na medida estritamente necessária para fins de garantir monitoramento, detecção e correção de vieses". Contudo, essa permissão pode estar em tensão com a GDPR, deixando organizações em dilema: ou falham em testar adequadamente vieses (violando a AI Act) ou processam dados sensíveis (violando GDPR).[^1_27]

Casos reais ilustram as consequências práticas. Um algoritmo de contratação da Amazon foi descoberto discriminando mulheres porque foi treinado em dados históricos de um setor dominado por homens. Um sistema de detecção de fraude da State Farm foi processado por discriminar segurados negros, porque seus dados de treinamento funcionavam como proxy para raça. Algoritmos de policiamento preditivo foram documentados como desproporcionalmente direcionando comunidades de minorias.[^1_28][^1_29]

### Memorização e Vazamento de Dados em LLMs

Um terceiro desafio envolve a memorização involuntária de dados sensíveis por modelos de linguagem grandes. Pesquisas demonstram que LLMs memorizam strings únicos – emails, números de identidade, contas bancárias – particularmente quando esses dados aparecem raramente nos dados de treinamento. Esses dados podem então vazar através de prompts, outputs, ou rastros de execução de ferramentas em sistemas multi-agente.[^1_1]

A PROTECTO.AI, em seu relatório 2025 sobre privacidade de IA, identificou que 26% das organizações admitem que dados sensíveis chegam a sistemas públicos de IA, mas apenas 17% implementam controles técnicos para bloquear ou monitorar tal uso. Quando um gerente de atendimento ao cliente cola o número de seguro social de um cliente em um ChatGPT público, esse dado entra em servidores de terceiros, potencialmente é incorporado em dados de treinamento futuro, e pode vazar indefinidamente.[^1_1]

## Multas, Conformidade e Tendências Futuras

### Valor e Severidade das Multas

O GDPR estabeleceu precedente de multas devastadoramente altas. A multa de €1,2 bilhão contra Meta em 2023 foi histórica. Contudo, em 2024, o total de multas de GDPR caiu 33% em relação a 2023, atingindo €1,2 bilhões para todo o ano. Isso não significa diminuição em enforcement, mas possível consolidação: multas maiores, menos frequentes, mas mais consequentes.[^1_12][^1_13]

O padrão emergente é também de "enforcement pessoal". Após o caso Clearview AI, a autoridade holandesa começou a investigar se pode responsabilizar pessoalmente os diretores da empresa por violações. Isso sinaliza mudança importante: não apenas corporações, mas executivos individuais podem ser pessoalmente culpados. Em 2025, espera-se mais "naming and shaming" – identificação pública de indivíduos responsáveis – como ferramenta de enforcement.[^1_12]

### Custos Além das Multas

As consequências financeiras vão muito além das multas. Um estudo 2025 de Baker Donelson sobre custos de violações de dados mostrou que shadow AI (sistemas de IA não monitorados, frequentemente usado por funcionários) agregou USD 670.000 ao custo médio de uma violação. Quando AI não gerenciada está envolvida, violações tipicamente expõem mais dados pessoais identificáveis (65% vs. baseline) e propriedade intelectual (40% vs. baseline), frequentemente armazenados em múltiplos ambientes que amplificam o dano.[^1_30]

Custódio cibercriminoso estimou custos globais de criminalidade cibernética em USD 10,5 trilhões para 2025, com brechas alimentadas por IA entre as mais rápido crescendo.[^1_1]

### Tendências de 2025 e Além

Várias tendências moldarão o enforcement e conformidade em 2025 e futuro:

**1. Regulação horizontal da IA**: Enquanto o GDPR é vertical (focado em proteção de dados), a UE AI Act é horizontal (focado em risco geral de IA). Ambas crescentemente se sobrepõem, exigindo que organizações naveguem dois frameworks regulatórios simultaneamente. Brasil provavelmente seguirá modelo similar, desenvolvendo legislação de IA complementar à LGPD.[^1_31][^1_6]

**2. Responsabilidade de terceiros**: Conforme IA prolifera em cadeias de suprimento, responsabilidade por violações está fluindo a montante e jusante da cadeia. Quando publicidades da Suécia usam Facebook Pixel sem consentimento apropriado, a Suécia multa não apenas Meta, mas os site owners que implementaram a ferramenta. Terceirizadores e provedores de serviços em nuvem são igualmente responsáveis por conformidade.[^1_32][^1_13]

**3. Pressão regulatória sobre modelos de linguagem generativa**: À medida que investigações iniciais (Itália contra OpenAI, Brasil contra ChatGPT, Canadá contra múltiplas plataformas) amadurecem, espera-se onda de enforcement contra provedores de LLM generativa. Questões de transparência, consentimento e acesso a direitos permanecerão prioritárias.

**4. Conformidade de IA para pequenas e médias empresas**: Enquanto grandes corporações foram alvos de multas, reguladores como ANPD estão claro sinalizando que nenhuma organização está acima da lei. Telekall Infoservice, pequena empresa de telecomunicações, recebeu primeira multa LGPD. Pequenos desenvolvedores de IA, freelancers que trenam modelos e startups precisarão demonstrar conformidade ou enfrentar sanções.

## Conclusão: O Caminho para Frente

As violações da LGPD e proteção de dados globais envolvendo inteligência artificial não são anomalias – são manifestações de um descompasso fundamental entre a velocidade da inovação tecnológica e a capacidade de reguladores de acompanhá-la. Empresas que constroem sistemas de IA estão operando frequentemente em zonas cinzentas regulatórias, e algumas evidentemente em violação clara de leis de proteção de dados.

A boa notícia é que reguladores globais – de Brasil a Europa a China – estão se mobilizando. A ANPD publicou orientações preliminares sobre IA. A UE implementou a AI Act. Multas recordes sinalizaram que conformidade não é opcional.

Para organizações que desenvolvem ou usam IA, a conformidade com LGPD, GDPR, CCPA, PIPL e outras leis requer:

- **Auditorias rigorosas de dados**: Mapear exatamente quais dados pessoais são coletados, processados e compartilhados em cada estágio do ciclo de vida de IA (treino, operação, refinamento).
- **Bases legais defensíveis**: Não confiar em "interesse legítimo" vago; documentar consentimento explícito ou excepção legal clara.
- **Transparência radical**: Divulgar claramente a usuários e titulares de dados como IA funciona, quais dados são utilizados, e como podem exercer direitos.
- **Testes de viés e discriminação**: Mesmo em tensão com GDPR, implementar testes robustos de viés, idealmente envolvendo dados real-worldmente representativos.
- **Redução de exposição**: Minimizar dados pessoais processados através de técnicas como federated learning, privacidade diferencial e anonimização.
- **Documentação**: Manter trilhas de auditoria completas de todas as decisões sobre tratamento de dados, para demonstração de conformidade em investigações.

O futuro da IA será definido não apenas por inovação técnica, mas por capacidade de inovar de forma responsável, respeitando direitos humanos fundamentais à privacidade. Reguladores como a ANPD estão sinalizando que essa capacidade é não-negociável.
<span style="display:none">[^1_100][^1_101][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

[^1_1]: https://www.protecto.ai/blog/ai-data-privacy-concerns-risk-breaches

[^1_2]: https://fpf.org/blog/brazils-anpd-preliminary-study-on-generative-ai-highlights-the-dual-nature-of-data-protection-law-balancing-rights-with-technological-innovation/

[^1_3]: https://www.compliancehub.wiki/breaches-and-fines-under-brazils-lei-geral-de-protecao-de-dados-lgpd-2/

[^1_4]: https://goadopt.io/en/blog/fines-in-LGPD/

[^1_5]: https://usercentrics.com/knowledge-hub/brazil-lgpd-general-data-protection-law-overview/

[^1_6]: https://iapp.org/news/a/what-brazil-s-anpd-expects-from-companies-using-generative-ai

[^1_7]: https://fpf.org/blog/how-data-protection-authorities-are-de-facto-regulating-generative-ai/

[^1_8]: https://www.medianama.com/2023/05/223-chatgpt-brazilian-data-protection-law-ai-regulation/

[^1_9]: https://pbcompliance.com.br/publicacao/lgpd-banimento-do-chatgpt-na-italia-e-os-reflexos-no-brasil/

[^1_10]: https://data-privacy-office.eu/fines-for-gdpr-violations-in-ai-systems-and-how-to-avoid-them/

[^1_11]: https://vinciworks.com/blog/the-biggest-data-protection-gdpr-and-ai-stories-of-2024/

[^1_12]: https://www.infosecurity-magazine.com/news/gdpr-fines-total-2024/

[^1_13]: https://www.adamigo.ai/blog/top-gdpr-fines-for-meta-ads-violations

[^1_14]: https://www.statista.com/statistics/1192794/meta-fines-from-eu-and-dpc/

[^1_15]: https://iapp.org/news/a/training-ai-on-personal-data-scraped-from-the-web

[^1_16]: https://consumerwatchdog.org/privacy/ca-attorney-general-and-leading-consumer-privacy-agency-urged-to-prevent-clear-and-present-danger-to-privacy-by-clearview-ai-facial-recognition-software/

[^1_17]: https://hstalks.com/doi/10.69554/XACT2373/

[^1_18]: https://ieeexplore.ieee.org/document/10084347/

[^1_19]: https://petsymposium.org/popets/2023/popets-2023-0072.pdf

[^1_20]: https://oag.ca.gov/privacy/ccpa

[^1_21]: https://www.clarip.com/data-privacy/california-privacy-law-facial-recognition/

[^1_22]: https://ipr.blogs.ie.edu/2025/01/27/how-do-the-european-unions-gdpr-and-chinas-pipl-regulate-cross-border-data-flows/

[^1_23]: https://www.china-briefing.com/news/pipl-vs-gdpr-key-differences-and-implications-for-compliance-in-china/

[^1_24]: https://rrijm.com/index.php/RRIJM/article/view/107

[^1_25]: https://www.minterellison.com/articles/ai-and-scraped-data-data-protection-implications

[^1_26]: https://iapp.org/news/a/training-ai-on-personal-data-scraped-from-the-web/

[^1_27]: https://data-privacy-office.eu/ai-bias-vs-data-privacy-can-the-eus-laws-find-balance/

[^1_28]: https://www.dataguard.com/blog/growing-data-privacy-concerns-ai/

[^1_29]: https://www.quinnemanuel.com/the-firm/publications/when-machines-discriminate-the-rise-of-ai-bias-lawsuits/

[^1_30]: https://www.bakerdonelson.com/webfiles/Publications/20250822_Cost-of-a-Data-Breach-Report-2025.pdf

[^1_31]: https://policyreview.info/pdf/policyreview-2024-3-1790.pdf

[^1_32]: https://secureprivacy.ai/blog/meta-consent-mode-explained-2025

[^1_33]: http://dergipark.org.tr/en/doi/10.30561/sinopusd.1353944

[^1_34]: https://ndujournal.ndu.edu.pk/site/article/view/229/164

[^1_35]: https://ieeexplore.ieee.org/document/10775891/

[^1_36]: https://belugyiszemlejournal.org/index.php/belugyiszemle/article/view/2055

[^1_37]: https://ejurnal.politeknikpratama.ac.id/index.php/jhpis/article/view/3837

[^1_38]: https://kuey.net/index.php/kuey/article/view/10320

[^1_39]: https://djhr.revistas.deusto.es/article/view/3200

[^1_40]: https://injurlens.bdproject.co.id/index.php/injurlens/article/view/104

[^1_41]: https://conflictandhealth.biomedcentral.com/articles/10.1186/s13031-024-00604-6

[^1_42]: https://economic-bulletin.com/index.php/journal/article/view/852

[^1_43]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10476881/

[^1_44]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/3C143E501E0824C8F9F0C40925965F43/S1537592723002827a.pdf/div-class-title-a-global-analysis-of-transgender-rights-introducing-the-trans-rights-indicator-project-trip-div.pdf

[^1_45]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10286185/

[^1_46]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9494011/

[^1_47]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5451102/

[^1_48]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9790938/

[^1_49]: https://onlinelibrary.wiley.com/doi/10.1002/jia2.26311

[^1_50]: https://esj.eastasouth-institute.com/index.php/eslhr/article/download/91/65

[^1_51]: https://www.lickslegal.com/post/more-sanctions-applied-by-the-brazilian-data-protection-authority-signal-that-violations-of-the-lgpd-will-not-be-tolerated

[^1_52]: https://www12.senado.leg.br/ril/edicoes/59/233/ril_v59_n233_p201.pdf

[^1_53]: https://thunderbit.com/blog/key-ai-data-privacy-stats

[^1_54]: https://wpcdn.idp.edu.br/idpsiteportal/2022/04/International_Dialogue-_on_LGPD_-Implementation_in_the_context_of_Global_DataProtection_English.pdf

[^1_55]: https://breached.company/real-world-examples-of-lgpd-fines-and-enforcement-actions-in-brazil/

[^1_56]: https://www.tandfonline.com/doi/pdf/10.1080/13600869.2024.2351671?needAccess=true

[^1_57]: https://periodicorease.pro.br/rease/article/download/17054/9549

[^1_58]: https://www.scielo.br/j/csp/a/mwFQB7k87vNkS4cHgBWmy4P/?format=pdf\&lang=en

[^1_59]: https://www.scielo.br/j/emquestao/a/w3xQNy4bnytwK6MxzgyKgsy/?format=pdf\&lang=pt

[^1_60]: http://www.scielo.br/pdf/aabc/v90n2/0001-3765-aabc-90-02-01279.pdf

[^1_61]: https://www.nucleodoconhecimento.com.br/wp-content/uploads/2021/04/Lei-Geral-De-Protecao-De-Dados-Pessoais-8211-LGPD.pdf

[^1_62]: https://periodicorease.pro.br/rease/article/download/16492/9106

[^1_63]: https://sol.sbc.org.br/journals/index.php/isys/article/download/1235/1784

[^1_64]: https://cedpo.eu/wp-content/uploads/generative-ai-the-data-protection-implications-16-10-2023.pdf

[^1_65]: https://www.tauilchequer.com.br/en/insights/publications/2024/02/anpd-applies-first-sanctions-of-2024

[^1_66]: https://seer.ucp.br/seer/index.php/LexHumana/article/view/3121

[^1_67]: https://iapp.org/news/a/lessons-from-brazilian-dpa-sanctions-to-date

[^1_68]: https://vestnik.ku.edu.kz/jour/article/view/2287

[^1_69]: https://www.mdpi.com/2227-9091/13/9/160

[^1_70]: https://janesthanalgcritcare.biomedcentral.com/articles/10.1186/s44158-025-00278-3

[^1_71]: https://fepbl.com/index.php/csitrj/article/view/2060

[^1_72]: https://biss.pensoft.net/article/136839/

[^1_73]: https://ieeexplore.ieee.org/document/11199026/

[^1_74]: https://www.semanticscholar.org/paper/9c435c32bf903734d7b485043ae66857a2300f66

[^1_75]: https://ieeexplore.ieee.org/document/9599471/

[^1_76]: https://linkinghub.elsevier.com/retrieve/pii/S0306437921001009

[^1_77]: http://arxiv.org/pdf/2409.13721.pdf

[^1_78]: https://www.tandfonline.com/doi/pdf/10.1080/13510347.2024.2353706?needAccess=true

[^1_79]: https://arxiv.org/pdf/2404.11476.pdf

[^1_80]: https://petsymposium.org/popets/2023/popets-2023-0088.pdf

[^1_81]: https://arxiv.org/pdf/1809.05762.pdf

[^1_82]: https://sciendo.com/pdf/10.2478/vjls-2022-0007

[^1_83]: https://www.palqee.com/blog/2021/what-to-know-chinese-pipl/

[^1_84]: https://www.cookieyes.com/blog/gdpr-fines/

[^1_85]: https://ijsra.net/node/7048

[^1_86]: https://c5k.com/12-6-68-article/HI240005

[^1_87]: https://gjeta.com/node/1788

[^1_88]: https://internationalpubls.com/index.php/pmj/article/view/4054

[^1_89]: https://ijsrcseit.com/CSEIT2390683

[^1_90]: https://www.ijfmr.com/research-paper.php?id=42672

[^1_91]: https://cjc.utpjournals.press/doi/10.3138/cjc.2022-0030

[^1_92]: https://wjarr.com/node/18774

[^1_93]: https://www.sciendo.com/article/10.2478/eustu-2024-0019

[^1_94]: http://arxiv.org/pdf/2403.10558.pdf

[^1_95]: https://arxiv.org/pdf/2502.10413.pdf

[^1_96]: https://arxiv.org/pdf/2304.00944.pdf

[^1_97]: https://arxiv.org/pdf/2412.15590.pdf

[^1_98]: http://arxiv.org/pdf/2410.03925.pdf

[^1_99]: http://arxiv.org/pdf/2112.07879.pdf

[^1_100]: https://arxiv.org/pdf/2205.09897.pdf

[^1_101]: https://www.isaca.org/resources/news-and-trends/isaca-now-blog/2025/facial-recognition-and-privacy-concerns-and-solutions-in-the-age-of-ai

