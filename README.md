# Fundamentos de engenharia de dados

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

![Alt text](Images/Ciclo%20de%20vida.png)

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
