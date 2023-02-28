# Engenharia de dados 🤖⚙️

Esse repositório contém estudos e projetos desenvolvidos durante cursos e bootcamps.

## Pipeline de dados

![Alt text](images/Pipeline%20de%20dados.png)

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

Tendo esse conceitos em mente fica muito mais facil definir todo entorno do projeto
