# Fundamentos de engenharia de dados

## Pipeline de dados

- Pipeline de dados e automação , agregação dos dados e movimentação dos mesmos
- Carrega dados brutos e transforma eles (ETL & ELT)
- Existe diversas ferramentas de pipeline de dados (kinine ,pentaho ,camuda ,aws glue)
- Estudar terraform docker jenkins
- Microserviços
- cybersegurança
- Infraestrutura
- ci/cd
- dataops,mlops

Ideia : fazer linguagem de programaçao para lidar com configuraçoes de cybersegurança (tipo terraform)

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

### Definição

![Alt text](images/Pipeline%20de%20dados.png)

> Pipeline moderna de dados

- Processamento de dados contínuo e extensível.
- A elasticidade e agilidade da nuvem.
- Recursos isolados e independentes para processamento de dados.
- Acesso democratizado a dados e gerenciamento de autoatendimento.
- Alta disponibilidade e recuperação de desastres

### Principais ferramentas da area de engenharia de dados

Real time
armazenamento cloud
transformaçao

### ciclo de vida da engenhariade dados

- Fonte de dado
  - conectores especificos para cada fonte de dados
- Ingestao de dados
  - em um db separado
- Transformaçao e enriquecimento
- Carga e uso dos dados
  - dashboard
  - produto
- Armazenamento
  - data store
  - sistema intermediario de armazenamento

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```
