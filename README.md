# Engenharia de dados

## Pipeline de dados

### Definição

![Alt text](images/Pipeline%20de%20dados.png)

> Pipeline moderna de dados

- Processamento de dados contínuo e extensível.
- A elasticidade e agilidade da nuvem.
- Recursos isolados e independentes para processamento de dados.
- Acesso democratizado a dados e gerenciamento de autoatendimento.
- Alta disponibilidade e recuperação de desastres

- Pipeline de dados e automação , agregação dos dados e movimentação dos mesmos
- Carrega dados brutos e transforma eles (ETL & ELT)

### Tecnologias e Conceitos Principais

- Existe diversas ferramentas de pipeline de dados (kinine ,pentaho ,camuda ,aws glue)
- terraform
- docker
- jenkins
- Microserviços
- cybersegurança
- Infraestrutura
- ci/cd
- dataops,mlops

> De onde vem os dados
> Fazer etapas em paralelo de tiverem um individualismo entre si

- componentes de um pipeline de dados
  - origem
    - nao extrair direto do banco da aplicaçao (banco segundario triggres)
    - origem e bom sempre ser do mesmo tipo (compatibilidade)
  - Processamento
    - stream
    - batch
    - Depende do que vc quer fazer
  - Destino
    - data lake
    - dw
    - data store
    - stream

### Ciclo de vida da engenhariade dados

![Alt text](images/Ciclo%20de%20vida.png)

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

> OBS:

- Arquitetura de dados e momentanea sempre muda conforme passa o tempo
- gestao de meta dados e questao de lgpd oque pode e nao pode fazer com os dados
- Orquestração e um gerenciamento de pipeline (airflow,docker,microserviços quando e muito grande)

### Processos por tras de tudo

- Arquitetura de dados
- Gestao de metados
- Orquestração
- Segurança
- CI/CD
- Dataops

## Arquitetura de Pipeline de dados

## Armazenamento distribuido

### Esse repositório contém estudos e projetos desenvolvidos durante cursos e bootcamps.

---

### [Digital Innovation One](https://web.digitalinnovation.one/track/cognizant-cloud-data-engineer?tab=path)

<u> Módulos: </u>

- **Fundamentos de Arquitetura de Sistemas**
- **Orquestração de contêiners com Docker**
- **Melhores práticas com Banco de Dados PostgreSQL**
- **Introdução ao MongoDB e Banco de Dados NoSQL**
- **Explorando o poder do NoSQL com Cassandra e HBase**
- **Fundamentos de ETL com Python**
- **Monitoramento de clusters Haddop de alto nível com HDFS e YARN**
- **Orquestrando ambientes de Big Data distribuídos com Zookeeper, Yarn e Sqoop**
- **Realizando consultas de maneira simples no ambiente complexo de Big Data com Hive e Impala**
- **Introdução a Engenharia de Dados na AWS**
- **Introdução a Engenharia de Dados na Azure**
- **Criando um Ecossistema Haddop totalmente Gerenciado com Google Cloud Dataproc**
- **Introdução à Mensageria na Nuvem com Kafka e Python**
- **Processando grandes conjuntos de dados de forma paralela e distribuída com Spark**
- **Criando Pipelines de Dados eficientes com Spark e Python**

---

### [How Bootcamp](https://learn.howedu.com.br/curso/engenharia-de-dados-cohort)

_Instrutores: André Sionek e Rhuan Lima_

<u> Módulos: </u>

- **Fundamentos de Ingestão de Dados**
- **SQL**
- **Capturando dados de uma API**
- **Capturando dados com crawlers**
- **Testes + Jenkins**
- **Introdução à AWS**
- **Integração contínua**
- **Data Lakes**
- **AWS Glue + Athena**
- **Redshift + Spectrum**
- **Apache Airflow**
- **Terraform e Cloudformation**
- **Conteúdos extras (Lambda, mensageria, spark)**
