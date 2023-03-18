# Engenharia de dados 🤖⚙️

Esse repositório contém estudos e projetos desenvolvidos durante cursos e bootcamps.

## Pipeline de dados

![Alt text](Images/Readme/Pipeline%20de%20dados.png)

> Pipeline moderna de dados

- Processamento de dados contínuo e extensível.
- A elasticidade e agilidade da nuvem.
- Recursos isolados e independentes para processamento de dados.
- Acesso democratizado a dados e gerenciamento de autoatendimento.
- Alta disponibilidade e recuperação de desastres

- Pipeline de dados e automação , agregação dos dados e movimentação dos mesmos
- Carrega dados brutos e transforma eles (ETL & ELT)

> Pipeline ETL

- Um pipeline etl pode ser feita de diversas maneiras diferentes depende do seu caso de uso
- Podem ser feitas em batch ou em streaming
- Um dos fatores mais importante de decisao de como fazer esse pipeline sao :
  - Volume de dados
  - tipo de dados
  - Local de armazenamento dos dados

> Pipeline Machine learn

- Um pipeline de Machine learn dependen exclusivamente dos pipelines de:
  - Extração
  - Transformação
- O pipeline de ML e um produto final de toda a engenharia de dados

> Pipeline CI/CD

- Esse pipeline e voltado para versionamento de codigo

## Principais Tecnologias e Conceitos

> Conceitos

- ci/cd
- dataops
- mlops
- Microserviços
- cybersegurança
- Infraestrutura

> Tecnologias

- terraform
- docker
- Delta Lake
- Python
- Apache spark
- Databricks
- Apache Beam
- Apache Airflow
- Apache Kafka

[Mais informações](Data\Src\17-BibliografiaCap02.pdf)

OBS : Existe diversas ferramentas de pipeline de dados open-sourse e de facil acesso e aprendizado que poden ser usadas para pequenos trabalhos

EX: kinine ,pentaho ,camuda

## Ciclo de vida da engenhariade dados

![Alt text](Images/Readme/Ciclo%20de%20vida.png)

- Fonte de dados
  - conectores especificos para cada fonte de dados
- Ingestao de dados
  - em um db separado
- Transformaçao e enriquecimento
  - tratamento com pandas
  - Ultilização do spark
- Carga e uso dos dados
  - sistema intermediario de armazenamento (postgres ou mongo)
  - Formação de data marts
- Armazenamento
  - Armazenamento intermediario para cada etapa acima
  - Cache
  - Memoria
  - Disco
- Analytics, Machine Learning, IA, Relatórios e Dashboards
  - relatorios
  - previsao de metas
  - dashboard
  - produto

![Alt text](Images/Readme/Hierarquia%20das%20nessecesidades.png)

> OBS:

- Arquitetura de dados e momentanea sempre muda conforme passa o tempo
- gestao de meta dados e questao de lgpd oque pode e nao pode fazer com os dados
- Orquestração e um gerenciamento de pipeline (airflow,docker,microserviços quando e muito grande)

> Processos por tras de tudo

- Arquitetura de dados
- Gestao de metados
- Orquestração
- Segurança
- CI/CD
- Dataops

## Arquitetura de dados

Antes de fazer uma arquitetura de dados e importante ter em mente conceitos bem definidos como :

- Visao geral do projeto
- Compreensão dos requisitos de negocio
- Qual tipo de pipeline se encaixa no processo (Batch ou Streamin)
- Volume de dados
- Como vai ser a extração e processamento dos dados
- Processo de CI/CD e IAC
- Custo do projeto

Tendo esse conceitos em mente fica muito mais facil definir todo entorno do projeto e colocar as boas praticas em ação

> visão geral por etapas

Tendo a visão geral do projeto sabendo dos principais topicos :

1.Regra de negocio
2.Estrutura para ingestão e trannformação dos dados (Infraestrutura Cloud ou On-premise)
3.Estrutura dos proprios dados e volume de dados
4.Escolha do tipo de pipeline e montagem da mesma sendo (Bath,stream ou ambos)
5.Local de armazenamento
6.Conexão entre as etapas de cada pipeline
7.Custo de todo projeto

> Custo de todo projeto

Geralmente toda a arquitetura gira em torno da problematica que vc esta enfrentando e dos custos que isso vai gerar para empresa com isso vc pode trabalhar e organizar sua arquitetura em torno disso pensando nisso e importante criar algumas soluçoes que nao estao pre-desenvolvidas como as soluçoes em cloud muitas das vezes sao usadas ferramentas open source para isso que nao geram custos muito elevados e resolve o problema muito melhor que as soluçoes nas grandes clouds (AWS,GCP e AZURE) alguns exemplos sao :

- Databricks
- Snowflake
- Delta tables
- jenkis
- MindDB

E muitos outros sao usados para diminuir os custos de um ou mais pipelines de dados

Alguns pontos sao levados em conta para poder medir o custo dos pipelines :

- Volume de dados
- Transformação desses dados
- Esforço do desenvolvedor para otmizar os dados

![Alt text](Images/Readme/Custos.png)

> Oportunidade de melhoria

Uma arquitetura de dados sempre pode ser melhorada assim como seus pipelines individualmente com tecnicas ou eventualidades que vao surgindo ao longo dos processo e tem que ser alterado o modo com que as coisa sao feitas acresentando ou retirando algumas atividades ou tecnologias como eo caso de uma migração podemos colocar algumas tecnicas a serem seguidas com algumas perguntas antes de fazer essas alteraçoes para a melhoria do projeto:

- Quanto isso vai custar ?
- Qual vai ser o esforço para mudar ?
- Qual a problematica que isso resolve ?

Podemos colocar em foco de tecnicas:

- Diagramação
- Documentação
- Defesa e pesquisa da ideia a ser emplementado
- Estudo do caso de uso individual (Pipeline e ferramenta) e de forma geral do projeto

> Dica:

- Em relação a o pipeline machine learn e interesante colocar em um container para os modelos soluçoes como docker ou ECS AWS usando a IAC terraform ou AWS Fargate
- O pipeline de CI/CD e interresante colocar em uma plataforma centraliada com todos os atributos uma plataforma boa eo **AZURE devops** Apesar de ser pago e uma das plataformas mais completas

## Armazenamento e Processamento distribuido

O armazenamento de dados e muito importante pois a forma que vc lida com isso pode definir varias partes do seu processo como a forma de ingestao, processamento e a carga. Os dados tem um ciclo de vida para cada etapa eo seu armazenamento e formato sao muito relevantes para cada parte.

> Definindo tipo de armazenamento

Na hora de definir e importante que tenha alguns conceitos definidos:

- Volume de dados
- Custo do armazenamento
- Quantidade de acessos
- Padroes de acesso
- Tipo de dados
- Tipo de ingestão
- Frequencia dos dados e periodos de armazenamento

Com esses conceitos a seguir podemos definir estrategias para que seja feita de forma consistente. Isso pode mudar conforme o tempo eas aplicaçoes vao evoluindo

> SQL X NOSQL X Baseado em arquivos

Para a escolha do modelo vc deve saber quais sao os padroes de acessos adotados no projeto ea nessesidade de seu usuaria em acessar esses dados e em qual formato seria o melhor para isso temos algumas opçoes:

- `SQL`: Formato tradicional de armazenamento tabular e um dos formatos mais atigos e è ultilizados ate hoje
  - Sao dados estruturado 1:1
  - Uso de SGBDs
    - Ex: Postgres, MySQL, Oracle
- `NOSQL`: Permite o armazenamento em diferentes formatos como XML e JSON para armazenamento rapido e presiso
  - Foi criado na era de bigdata
  - Sao sistemas orientados a performace
  - Depende do contexto para usar (Pipeline em stream e uma boa oportunidade para usar)
  - Ex: MongoDB, Cassandra e AWS DynamoDB
- `Baseado em arquivos`: Sao arquivos com muita variedade e performaticos de arquivo como :
  - Ex: Parquet,delta e csv
  - Interresanto colocar esse tipo de armazenamento para soluçoes intermediarias onde se tem que colocar varias versoes do mesmo dado
    - EX: no formato delta temos a forma de **Bronze, silver e gold**

> Colunar ou linha

Esse modelo de armazenamento e importante para definir as tecnologias usadas para os pipelines e a performace como um todo

- Formato em linha ex :
  ![Alt text](Images/Readme/Formato_LInha.png)
- Formato tradicional e de facil compreendimento apenas lembre como e o EXCEL
- `Vantagens` : Volume de dados altisimo
- `Desvantagens` : Pouco performatico , Pouca variedade para conseguir armazenar

- Formato em coluna ex:
  ![Alt text](Images/Readme/Dados_colunar.png)
- Pode ser fazer uma busca desses dados pelo inices ja que buscando apenas um se retorna todos que sao referentes a ele
- Cada indice dentro dele tem dados de "Chave-valor" para a associação entre dimensao e metrica de cada um
- Esse tipo de dado e muito comun vindo de sistemas web em formato JSON
- `Vantagens`: Muito performatico pela sua forma de consulta principalmente
  - Os bancos noSLQ usam como base esse modelo
- `Desvantagen`: Pouco volume para armazenamento

> Tipos de arquivo e dados

A escolha dos tipos de arquivo vai depender do sistema e da arquitetura de engenharia de dados que foi escolhida para o projeto se vai ser nunvem ou on-premise. isso tambem vai influenciar no formato temporario de dados em cada etapa do pipeline e bons arquivos para isso sao :

- Csv
- Parquet
- Delta
- Json
- Orc
- Avro

## Sistema Distribuido Clusters

Para começarmos temos que definir o poder de uma maquina sozinha que conseque fazer tarefas basicas como armazenamento e processamento podendo executar scripts e outros serviços e essa mesma maquina tem um limite fisico do que ela pode fazer. Tendo isso em vista nasceu como soluçao o uso de varias maquinas ao mesmo tempo os chamados cluster de processamento distribuido que trabalham juntos como um unico sistema para fazer as tarefas distribuindo as cargar de trabalho e deixando as tarefas mais eficientes e reduzindo seu tempo.

> Hierarquia dos Sistemas distribuidos

Sistema Local

- Sistemas operacional **LINUX**
  - EXT4(Sistema de armazenamento do linux)

Sistema Distribuido

- Ambiente de rede
- 3 maquinas
  - Sistemas operacional **LINUX**
    - Software de armazenamento distribuido
    - Software de processamento distribuido
      - EXT4(Sistema de armazenamento local do linux)

![Alt text](Images/Readme/Sistema%20distribuido.png)

> Sistemas de arquivos locais

![Alt text](Images/Readme/SIstemasArq.png)

> Sistemas de arquivos Distribuido

![Alt text](Images/Readme/SIstemArqusss.png)

> Sistema de processamento distribuido

- Sistemas Tradicionais
  ![Alt text](Images/Readme/SistemaPro.png)

- Sistemas em cloud e mais novos
  ![Alt text](Images/Readme/CloudProcess.png)

> Vantagens

- `Escalabilidade` : podemos colocar quantas maquinas nos quisermos
  - Vertical : Aumenta o hardware (colocar um processador novo)
  - Horizontal : Aumenta o numero de maquinas
- `Confiabilidade` : Se uma maquina der problema as outras vao dar conta
- `Desempenho`: Tarefas sao feitas em paralelo com varias maquinas e por isso o tempo e diminuido
- `Flexibilidade`: Os sistemsa distribuidos sao adaptaveis com diversas funçoes nao so para bigdata ele serve podendo atender a diversos propositos dentro da empresa

> Desvantagens

- `Complexidade`: E muito mais dificil preparar o hardware e software com uma arquitetura moderna do que apenas uma maquina
- `Sobrecarga de comunicação `: Pode ocorre uma sobre carga de rede e uma latencia muito grande aumentando o tempo de resposta entre as maquinas e o usuario
- `Riscos de segurança`: Se uma maquina for raqueada todas sao afetadas podendo perder todas elas e os proprio dados
- `Custo elevado`: Configurar e mater um sistema dessa complexidade demanda de proficionais e maquinas extremamente potentes e isso nao e de graça

**Exemplo de cluster**

![Alt text](Images/Readme/cluster-overview.png)

## Data lake, Data Warehause, Data Store etc...

Alguns `CONCEITOS` sao muito importantes na hora de escolher seu armazenamento e metodologia para isso vamos definir esse conceitos abaixo citando alguns exemplos:

- `Data Warehause`: E um tipo de banco de dado projetado para consultas com alto volume de dados para analises rapidas e inteligentes
  - Normalmente vem junto com banco de dados transasionais
  - E usado sempre no final do processo para os dados serem armazenados e usados
  - Desempenho de consulta analitica
  - Integração de dados de varias fontes
  - Suporte a BI
  - Armazenamento de dados historicos
- `Data Lake`: No data lake primeiro e feito o armazenamento dos dados para depois fazer o tratamento dos mesmos ele pode estar no meio do processo de pipeline
  - O paradgma de governancia de dados e muito forte nesse cenario para nao se transformar em um pantano de dados
  - Pode ser armazenar qualquer tipo de dados no data lake diferentemente do DW
  - Foi projetado para processar e consultar de forma performatica qualquer tipo de dado
  - Tem bastante flexibilidade para suas atividades
  - Bastante escalabilidade para armazenamento (Cluster)
- `Data lakehause`: E uma plataforma moderna de armazenamento baseada no data lake e data warehause podendo armazenar a qualquer tipo de dado implementado como um sistema unificado pelas ferramentas de forma estrategica pela sua complexidade e custos elevados
- `Data Store`: Repositorio para armazenamento e gerenciamento de dados dividido em 7 categorias:
  - Banco de dados relacionais
  - Banco de dados nao relacionais
  - Sistemas de arquivos
    - HDFS
    - Amazon S3
    - parquet
    - NTFS (Rede local)
  - full-text search engine
  - fila de mensagens
  - in-memory data store
  - Armazenamento key-value
- `Data Hub`: A mecanica do datahub e ultilizar todas as maneiras e conceitos apresentados anteriormente usando as melhores praticas e reaproveitando tudo oque ja esta feito
  ![Alt text](Images/Readme/Datahub.png)
- `Data Mesh`: Infraestrutura de dados como plataforma um exemplo bem claro disso eo databricks que aborta esse proposito como datalakehause em um ambiente SAAS
  ![Alt text](Images/Readme/DataMesh.png)

## Modelagem de dados

Modelagem de dados eo processo de projetar e criar modelos e estruturas logicas que representam como os dados sao relacionados e armazenados.Com a criação de diagramas e definiçoes de tabelas.A modelagem de dados sempre vem primeiro que qualquer ação antes da ultilizaçao dos dados.

> Modelagem Relacional

- E uma modelagem que se baseia em entidades e na relação entre elas com tabelas e campos
- EX: clientes e produtos sao duas entidades e tem um relação entre elas
- E amplamente ultilizado em sistemas transasionais e em bancos relacionais (SGBDs) focando principalmente na forma como os dados sao armazenados

> Modelagem Dimensional

- E uma tecnica ultilizada amplamente em sistemas de BI e DW que facilita a analise dos dados de forma multidimensional
- Geralmente o sistema relacional e tratado como data source pelo modelo dimensional
- Tem como base os fatos relacionados a aqueles dados sendo eles:
  - Medidas: Que sao valores numericos como receita,preço de produto e quantidade de produtos
  - Dimensoes: Que sao nomes ou contextos desses valores como nome do produto ou nome do cliente
- Geralmente esses dados vem de forma agregada e escalavel especificas para fazer calculos em cima desses dados
- Com foco em analise dos dados e geração de dashboards e relatorios

> Modelagem de datalakes

- E uma abordagem para construçao de sistemas de armazenamento de dados voltado para grandes volumes de dados de qualquer tipo e origem
- Normalmente vem sempre atrelado a conceitos como cluster de processamento/armazenamento e pipeline de dados

![Alt text](Images/Readme/Modelagem%20de%20dados.png)

Modelo conceitual

- E um modelo voltado mais para a area de negocios tendo so as entidades ou fatos que vao participar da modelagem e motagem dos dados

Modelo logico

- E um modelo que ea a traduçao do anterior sendo mais detalhado e voltado para o proficioal de TI que vai atuar na montagem do modelo em questao

Modelo fisico

- E o modelo propriamente dito e escrito em linguagem de programação como SQL ou mesmo Python

> Definindo granularidade

- Granularidade é o nível de detalhe ou precisão com que os dados são representados em um modelo de dados.
- A granularidade dos dados pode ser alta, quando os dados são divididos em muitas entidades e atributos pequenos, ou baixa, quando os dados são agregados em poucas entidades e atributos maiores
- A granularidade é uma característica importante a ser considerada na modelagem de dados, pois afeta a capacidade de armazenar, recuperar e analisar dados.
- Uma granularidade alta permite uma maior flexibilidade e precisão na análise dos dados, mas pode exigir mais armazenamento e processamento. Por outro lado, uma granularidade baixa pode resultar em dados agregados e menos precisos, mas pode ser mais fácil de armazenar e processar. Portanto, é importante equilibrar a granularidade dos dados com as necessidades de negócioe técnicas para garantir uma boa modelagem de dados
- Por exemplo: Considerando um DW, os relatórios devem permitir análisede vendas por diaou por hora? A resposta a essa pergunta ajuda a definir o nível de granularidade necessário na modelagem.

## Data Quality, Data Lineage e Data Observability

> Data Quality

- Data Quality nada mais e que a medida da qualidade dos dados medindo principalmente o quanto eles sao confiaveis para o usuario final sendo colocado em foco que os dados sejam :
  - Presisao
  - Exatidao
  - Consistencia
  - Relevancia
  - Cobertura
  - Atualização
- O valor da qualidade de dados sao aplicada tecnicas como mineração de dados e estatistica para potenciais erros serem mitigados como escrita errado ou mediçoes erradas
- Logo apos e feito um trabalho de limpeza dos dados tiramdo nulos duplicatas colocando em padroes relevantes e validando os mesmo com a area de negocio

> Data Lineage

- Ajuda a ganrantir a qualidade de dados rastreando o fluxo dos mesmo para corrigir erros em diferentes pontos do processo
- Fornece tbm transparencia e confiança aos dados permitindo aos usuarios compreender a origem e evoluçao dos mesmos
  - Ex: Arquitetura medalion
- Facilitar auditoria dos processos de dados fornecendo uma visao completa da documentação e atividades exercidas no projeto em questao
- Melhora da eficiencia do negocio e anlises possibilitando e aumentando o numero de otimizações

> Data Observability

- A observabilidade dos dados esta muito ligada ao sistema com que esses dados estao integrados e fazendo os seus processos como uma forma de monitorar tudo oque e feito
  ![Alt text](Images/Readme/Observ.png)

- Sendo assim e importante entender o estado de comportamento dos dados no sistema para conseguir resolver problemas e corrigir erros
- Uma maneira muito boa de fazer isso e pela gestão de metadados

Os 5 pilares da Observability dos dados
![Alt text](Images/Readme/PilarObserv.png)

## DevOps para engenharia de dados

> Oque e devops ?

- DevOps é uma cultura e conjunto de práticas que tem como objetivo integrar as equipes de desenvolvimento de software e operações de TI (tecnologia da informação) para criar e entregar software de forma mais eficiente e com maior qualidade

- As práticas DevOps incluem automação de processos de infraestrutura e deployment (implantação) de software, monitoramento e análise de métricas de performance e estabilidade, testes automatizados e contínuos, e implementação de feedbacks contínuos e iterações no processo de desenvolvimento

> Oque essa pratica agrega para engenharia de dados ?

- `Automação de infraestrutura`: a infraestrutura de dados podeser gerenciada por código, permitindo a criação de ambientes de desenvolvimento, teste e produção de maneira consistente e previsível.
- `Controle de versão`: todo o código e artefatos de dados podemser armazenados em um sistema de controle de versão, permitindo o controle de mudanças e a colaboração entre as equipes de desenvolvimento e operações.
- `Integração contínua (CI)`: o código podeser integrado e testado continuamente, permitindo a identificação precoce de erros e problemas de compatibilidade.
- ` Entrega contínua (CD)`: as mudanças no código e na infraestrutura podemser entregues rapidamente e com segurança para a produção, usando pipelines automatizados de deploy.
- `Monitoramento`: os dados e os sistemas de infraestrutura podemser monitorados constantemente para garantir a qualidade, a estabilidade e a performance. A análise de métricas e logs podeser usada para identificar problemas e oportunidades de melhoria.
- `Automação de processamento de dados`: o processamento de dados podeser automatizado, permitindo que novos dados sejam processados assim que estiverem disponíveis, minimizando o tempo de latência.
- `Testes automatizados`: testes automatizados podemser usados para garantir a qualidade dos dados e do código, permitindo a identificação precoce de erros e problemas.

> Como IAC pode ajudar o engenheiro de dados

A IaC é frequentemente usada em conjunto com outras práticas de DevOps, como integração contínua, entrega contínua e automação de testes, permitindo a criação de processos automatizados e consistentes para o desenvolvimento e a implantação de aplicativos e serviços.

- `Consistência`: A infraestrutura pode ser criada e configurada de maneira consistente em todos os ambientes, incluindo desenvolvimento, teste e produção.
- `Eficiência`: A IaC permite que a infraestrutura seja gerenciada de forma mais rápida e eficiente, reduzindo o tempo e o esforço necessários para configurar servidores e outros componentes de infraestrutura.
- `Flexibilidade`: As configurações de infraestrutura podem ser facilmente alteradas e atualizadas com base nas necessidades do aplicativo ou serviço.
- `Controle de versão`: Todas as alterações na infraestrutura são controladas e gerenciadas como mudanças no código,o que permite o controle de versão, o rastreamento e a colaboração de equipe.

> CI/CD

- `Gerenciamento de código fonte`: É importante usar um sistema de controle de versão, como o Git, para gerenciar o código-fonte do projeto de dados. Isso permite que vários Engenheiros e Arquitetos de Dados trabalhem no mesmo projeto, e o versionamento de código ajuda a evitar conflitos e problemas de integração.
- `Teste automatizado`: Automação detestes para garantir que as alterações no código não interrompam o funcionamento de soluções de dados já existentes. Isso pode incluir testes unitários, testes de integração e testes de carga para verificar a escalabilidade da solução de dados.
- `Pipeline de dados`: Automação do processo de desenvolvimento e implantação de soluções de dados criando um pipeline de dados. Isso inclui o processamento, armazenamento e entrega de dados. Cada etapa do pipeline deve ser testada e validada antes de ser implementada em produção.
- `Configuração de infraestrutura como código`: Usando ferramentas como Terraform ou CloudFormation, você pode automatizar a configuração da infraestrutura necessária para implementar umasolução de dados. Isso permite que você configure rapidamente um ambiente de teste e produção para implementar e testar soluções de dados.
- `Monitoramento e alertas`: Configuração deum sistema de monitoramento e alertas para ospipelines de dados. Isso ajudará a identificar problemas de desempenho ou erros no pipeline e permitirá que a equipe de operações de dados responda rapidamente.
- `Entrega contínua`: Configuração de um processo de entrega contínua que permita a implantação automatizada da solução de dados em um ambiente de produção. Isso ajudará a garantir que a solução de dados seja entregue rapidamente e com segurança.

> Container e Orquestração

- `Portabilidade`: Os containers podem ser facilmente movidos entre ambientes de desenvolvimento, teste e produção, permitindo que as aplicações sejam implantadas de forma rápida e consistente em diferentes ambientes.
- `Escalabilidade`: A orquestração de containers permite que as aplicações sejam escaladas rapidamente para atender às demandas de tráfego.
- `Resiliência`: Os containers podem ser reiniciados automaticamente em caso de falha ou erro, garantindo que as aplicações estejam sempre disponíveis.
- `Eficiência`: A utilização de containers permite que os recursos de hardware sejam compartilhados entre várias aplicações, reduzindo o desperdício de recursos e aumentando a eficiência.
- `Flexibilidade`: Os containers permitem que as aplicações sejam empacotadas de forma modular, o que facilita a manutenção e atualização de diferentes componentes do aplicativo.
- `Desenvolvimento e teste de soluções de dados`: Os containers podem ser usados para criar ambientes de desenvolvimento e teste para soluções de dados. Isso pode incluir a criação de clusters de bancos de dados, ambientes de processamento de dados e outras infraestruturas de dados. Os containers podem ser criados rapidamente e facilmente, o que permite aos Engenheiros de Dadoscriar e testar soluções de dados de maneira mais eficiente, exatamente como ensinamos na Formação Engenheiro de Dados.
- `Implantação de soluções de dados`: Os containers podem ser usados para implantar soluções de dados em ambientes de produção. Os containers permitem que as soluções de dados sejam empacotadas e implantadas de forma consistente em diferentes ambientes, incluindo ambientes de nuvem e on-premises(local).
- `Orquestração de clusters de bancos de dados`: Os containers podem ser usados para orquestrar clusters de bancos de dados, permitindo que os bancos de dados sejam dimensionados rapidamente e gerenciados de maneira eficiente. Ferramentas de orquestração de containers, como o Kubernetes, podem ser usadas para gerenciar clusters de bancos de dados e permitir que eles sejam dimensionados horizontalmente em resposta a aumentos de demanda.
- `Processamento de dados distribuídos`: Os containers podem ser usados para criar ambientes de processamento de dados distribuídos. Isso pode incluir a implantação de clusters Apache Hadoop ou Apache Spark em containers. Isso permite que os processos de processamento de dados sejam escalados horizontalmente e gerenciados de maneira mais eficiente, exatamente como ensinamos na Formação Engenheiro de Dados.
- `Automação de processos de dados`: Os containers podem ser usados para automatizar processos de dados. Isso pode incluir a criação de pipelines de dados em containers, permitindo que os dados sejam processados de maneira eficiente e consistente, exatamente como ensinamos na Formação Arquitetode Dados.

> Soluçoes em Cloud

Cloud Computing é uma abordagem que permite que os recursos de computação, armazenamento e rede sejam alugados sob demanda em provedores de nuvem, como Amazon Web Services (AWS), Microsoft Azure ou Google Cloud Platform. Essa abordagem oferece várias vantagens para a Engenharia de Dados:

- `Escalabilidade`: A nuvem permite escalar recursos de computação e armazenamento com base nas necessidades do projeto, permitindo que os recursos sejam aumentados ou diminuídos conforme necessário.
- `Redução de custos`: A nuvem permite que as empresas paguem apenas pelos recursos que usam, sem a necessidade de investir em infraestrutura local. Isso pode ser especialmente vantajoso para projetos que exigem recursos de computação e armazenamento intensivos.
- ` Facilidade  de  acesso`: A nuvem permite que as equipes acessem os recursos de Engenharia de Dados de qualquer lugar, desde que tenham acesso à Internet.
- ` Manutenção  simplificada`: Os provedores de nuvem geralmente gerenciam a manutenção e atualização dos recursos de infraestrutura, liberando as equipes de TI para se concentrarem em outras áreas de trabalho.Por outro lado, uma solução local de Engenharia de Dados oferece outras vantagens, incluindo:
  - `Controle  total`: Uma solução local oferece às empresas controle totalsobre sua infraestrutura de dados, incluindo segurança, privacidade e conformidade.
  - `Latência de rede`: Em alguns casos, a latência de rede pode ser um problema para projetos de Engenharia de Dados em nuvem, especialmente para projetos que exigem grandes volumes de dados e latências baixas.
  - `Investimento inicial`: O uso de uma solução local de Engenharia de Dados pode exigir um grande investimento inicial em hardware, software e licenças, mas que pode ser usado por diversos anos em muitos diferentes projetos.

## Segurança dos dados

A implementar segurança e montar um ambiente de alta disponibilidade de dados de forma eficiente e profissional. Aprenderá a criar sistemas de segurança e controle de acesso, habilitando encriptação e ativando sistemas de auditoria, além de configurar alta disponibilidade no acesso aos dados em cluster, bem como, aprenderá como realizar testes de invasão e roubo de dados, objetivando identificar falhas e vulnerabilidades no ambiente de dados.
