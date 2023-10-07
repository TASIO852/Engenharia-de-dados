# Engenharia de dados 🤖⚙️

A engenharia de dados é um campo da ciência da computação e engenharia que se concentra na concepção e construção de sistemas e infraestruturas para coletar, armazenar, processar e analisar dados em grande escala. Enquanto a análise de dados se concentra em extrair insights dos dados, a engenharia de dados se concentra em tornar os dados acessíveis, confiáveis e utilizáveis. Eis algumas áreas-chave da engenharia de dados:

1. **Infraestrutura de dados**: Desenvolver e manter a arquitetura (como bancos de dados, grandes armazenamentos de dados e plataformas de processamento em grande escala como Hadoop e Spark) para armazenar e processar dados.

2. **ETL (Extract, Transform, Load)**: Processos e ferramentas utilizadas para extrair dados de fontes, transformá-los em um formato utilizável e carregá-los em um armazenamento de dados.

3. **Bancos de dados**: Desenho, construção e manutenção de bancos de dados relacionais e não-relacionais para garantir o acesso rápido e seguro aos dados.

4. **Streaming de dados**: Trabalhando com dados em tempo real, muitas vezes provenientes de fontes como sensores, logs de aplicativos ou redes sociais.

5. **Governança e qualidade de dados**: Estabelecer políticas e ferramentas para assegurar que os dados estejam precisos, confiáveis, limpos e protegidos.

6. **Otimização de desempenho**: Garantindo que os sistemas de dados operem de maneira eficiente, escalável e confiável.

A engenharia de dados desempenha um papel fundamental na facilitação das operações de ciência de dados, machine learning e analytics, pois cria as "estradas" e "pontes" que levam os dados às pessoas e sistemas que os utilizam.

Os engenheiros de dados frequentemente trabalham em conjunto com cientistas de dados, analistas e outros stakeholders para garantir que os dados estejam disponíveis e em formatos adequados para análise e modelagem.

## Pipeline de Dados

### Pipeline Moderna de Dados

- **Processamento Contínuo**: Capacidade de processar dados de maneira ininterrupta e adaptável às necessidades em mudança.
- **Elasticidade na Nuvem**: Aproveitando a escalabilidade e flexibilidade das soluções baseadas em nuvem para adaptar-se à demanda.
- **Isolamento de Recursos**: Garantindo que os recursos para processamento de dados operem de forma independente e sem interferências.
- **Democratização do Acesso**: Permitindo um acesso amplo e controlado aos dados e facilitando o gerenciamento pelo usuário.
- **Resiliência**: Garantindo alta disponibilidade e robustos mecanismos de recuperação de desastres.
- **Automação e Agregação**: Facilitando a integração, movimentação e consolidação de dados de diversas fontes.
- **Transformação de Dados**: Capaz de lidar com dados brutos, processando-os através de ETL (Extração, Transformação, Carga) & ELT (Extração, Carga, Transformação).

### Pipeline ETL

- **Flexibilidade**: O pipeline ETL pode ser configurado de múltiplas formas, dependendo das necessidades específicas.
- **Modalidades de Processamento**: Pode operar em lotes (batch) ou em tempo real (streaming).
- **Fatores Decisivos**: A estruturação do pipeline é influenciada por:
  - Volume de dados.
  - Natureza ou tipo de dados.
  - Infraestrutura e localização de armazenamento dos dados.

### Pipeline de Machine Learning

- **Dependências**: O sucesso de um pipeline de Machine Learning está atrelado aos processos de extração e transformação de dados.
- **Produto Final**: Representa a culminação de todo o esforço em engenharia de dados, preparando os dados para modelagem e análise.

### Pipeline CI/CD

- **Foco em Versionamento**: Este pipeline concentra-se na integração contínua e entrega contínua (CI/CD), garantindo que as versões de código sejam gerenciadas e implementadas de forma eficaz.

## Principais Tecnologias e Conceitos sobre Dados

### Conceitos

- **CI/CD**: Refere-se à Integração Contínua e Entrega Contínua, práticas que promovem a frequente integração de código e sua entrega automatizada.
- **DataOps**: Metodologia que aplica práticas ágeis, de desenvolvimento e operações, ao gerenciamento de dados, visando melhorar a qualidade e a velocidade da análise de dados.
- **MLOps**: Combinação de Machine Learning com operações de desenvolvimento, visando facilitar a produção e manutenção de modelos de ML em produção.
- **Microserviços**: Arquitetura que estrutura uma aplicação como uma coleção de serviços autônomos, leves e interconectados.
- **Cybersegurança**: Práticas, tecnologias e processos projetados para proteger sistemas, redes e dados de ataques digitais.
- **Infraestrutura**: Componentes físicos e organizacionais necessários para o funcionamento de um ambiente ou sistema.

### Tecnologias

- **Terraform**: Ferramenta de código aberto para criar, alterar e melhorar infraestrutura de forma segura e previsível.
- **Docker**: Plataforma que permite criar, testar e implementar aplicações dentro de contêineres.
- **Delta Lake**: Armazenamento de camada para datasets massivos, trazendo ACID transactions para Apache Spark e Big Data workloads.
- **Python**: Linguagem de programação versátil, amplamente usada em análise de dados e machine learning.
- **Apache Spark**: Motor de análise unificado para processamento de dados em larga escala.
- **Databricks**: Plataforma baseada em nuvem para análise de dados e AI utilizando Apache Spark.
- **Apache Beam**: Modelo de programação para definir e executar pipelines de processamento de dados.
- **Apache Airflow**: Plataforma para programar e monitorar fluxos de trabalho.
- **Apache Kafka**: Plataforma de streaming de eventos em tempo real, usada para construir pipelines de dados e aplicativos de streaming.

**Observação**: Existem muitas ferramentas de pipeline de dados open-source, acessíveis e fáceis de aprender, adequadas para projetos menores.

**Exemplos**: Kibana, Pentaho, Camunda.

## Ciclo de Vida dos Projetos de Engenharia de Dados

![Alt text](Images/Readme/Ciclo%20de%20vida.png)

- **Fonte de Dados**
  - Utilização de conectores específicos, adaptados para cada fonte de dados, garantindo a integridade e fidelidade na coleta.
  
- **Ingestão de Dados**
  - Armazenamento inicial em um banco de dados separado, preparando os dados para processamento e análise.

- **Transformação e Enriquecimento**
  - Limpeza, tratamento e transformação de dados usando ferramentas como Pandas.
  - Processamento em larga escala com Apache Spark, permitindo manipulação de grandes volumes.

- **Carga e Uso dos Dados**
  - Armazenamento intermediário, como Postgres ou MongoDB, para servir como ponte entre a transformação e a análise.
  - Criação de data marts, que são subconjuntos de data warehouses, otimizados para atender áreas ou funções específicas da organização.

- **Armazenamento**
  - Implementação de estratégias de armazenamento diferenciadas para cada etapa do ciclo, variando entre cache, memória e disco.

- **Analytics, Machine Learning, IA, Relatórios e Dashboards**
  - Desenvolvimento de relatórios detalhados para insights.
  - Previsão e modelagem para atingir metas.
  - Construção de dashboards interativos.
  - Criação de produtos baseados em dados, alavancados por Machine Learning e Inteligência Artificial.

![Alt text](<Images/Readme/Hierarquia das nessecesidades.png>)

### Observações

- **Arquitetura de Dados**: É dinâmica e evolui com o tempo, adaptando-se às mudanças nas necessidades e tecnologias.
- **Gestão de Metadados e LGPD**: Crucial para a conformidade com regulamentos sobre o que pode e não pode ser feito com os dados.
- **Orquestração**: Trata-se do gerenciamento e automação de workflows. Ferramentas como Airflow e Docker são essenciais, e a estrutura de microserviços é adotada para projetos de grande escala.

### Processos Fundamentais

- **Arquitetura de Dados**: Estruturação e organização dos dados.
- **Gestão de Metadados**: Administração e categorização das informações que descrevem os dados.
- **Orquestração**: Automatização e gerenciamento de processos e workflows.
- **Segurança**: Proteção de dados contra ameaças e vazamentos.
- **CI/CD**: Integração e entrega contínua para atualizações e implementações ágeis.
- **DataOps**: Metodologias ágeis aplicadas à engenharia de dados, focadas na colaboração e eficiência.

## Arquitetura de Dados: Um Guia Estruturado

A arquitetura de dados é o alicerce de qualquer projeto relacionado à análise e processamento de dados. Abaixo, descrevemos os conceitos-chave para construir uma arquitetura robusta e escalável.

### Conceitos Fundamentais

Antes de embarcar na jornada da arquitetura de dados, considere:

- **Visão do Projeto**: Compreenda a finalidade e os objetivos do projeto.
- **Requisitos de Negócio**: Identifique as necessidades e expectativas da empresa.
- **Tipo de Pipeline**: Determine se o processo será em batch ou streaming.
- **Volume de Dados**: Estime o tamanho e escala dos dados.
- **Extração e Processamento**: Planeje como os dados serão adquiridos e processados.
- **Integração Contínua/Entrega Contínua (CI/CD) e Infraestrutura como Código (IAC)**: Estabeleça processos automáticos para desenvolvimento e implantação.
- **Orçamento**: Avalie o custo financeiro do projeto.

### Etapas-chave

Uma visão detalhada do projeto envolve:

1. **Regras de Negócio**: Defina as regras que guiarão a manipulação dos dados.
2. **Infraestrutura**: Escolha entre Cloud ou On-premise para ingestão e transformação dos dados.
3. **Dados e Volume**: Identifique a natureza e magnitude dos dados.
4. **Pipeline**: Selecione e configure o tipo de pipeline (Batch, Streaming ou Ambos).
5. **Armazenamento**: Determine onde os dados serão armazenados.
6. **Conectividade**: Estabeleça as ligações entre as fases do pipeline.
7. **Custo**: Analise o orçamento geral.

### Redução de Custos

A arquitetura é frequentemente influenciada pelo orçamento. Ferramentas open-source podem ser uma opção eficiente em termos de custo:

- Databricks
- Snowflake
- Delta tables
- Jenkins
- MindDB

Considere, ao avaliar custos:

- Volume dos dados.
- Transformação necessária.
- Esforço do desenvolvedor para otimização.

### Oportunidades de Melhoria

Melhorar constantemente é fundamental. Antes de implementar mudanças:

- Avalie o **custo** da mudança.
- Estime o **esforço** necessário.
- Identifique o **problema** que a mudança resolve.

Técnicas recomendadas incluem:

- Diagramação
- Documentação
- Pesquisa e defesa da ideia
- Análise de caso de uso, tanto individualmente quanto de forma holística.

### Dicas Práticas

- **Machine Learning**: Considere containerizar modelos usando Docker ou ECS AWS, com IAC via Terraform ou AWS Fargate.
- **Pipeline de CI/CD**: Utilize uma plataforma centralizada, como o **Azure DevOps**. Embora seja um serviço pago, oferece um conjunto abrangente de ferramentas.

## Armazenamento e Processamento Distribuído

A forma como os dados são armazenados desempenha um papel crucial na determinação da eficiência de ingestão, processamento e carregamento. Cada etapa do ciclo de vida dos dados possui considerações distintas de armazenamento e formato.

### Tipos de Armazenamento

Ao escolher um método de armazenamento, considere:

- **Volume de Dados**: Qual é a quantidade total de dados?
- **Custo**: Qual é o orçamento para o armazenamento?
- **Padrões de Acesso**: Como os dados são acessados e com que frequência?
- **Tipo de Dados**: Qual é a natureza dos dados - estruturado, semi-estruturado ou não estruturado?
- **Método de Ingestão**: Os dados são ingeridos em lote ou em tempo real?
- **Durabilidade e Retenção**: Por quanto tempo os dados precisam ser armazenados?

Com essas considerações, podemos adaptar estratégias conforme as necessidades do projeto evoluem.

### SQL vs. NoSQL vs. Baseado em Arquivos

A decisão entre modelos de armazenamento depende das necessidades do projeto:

- **SQL**:
  - Armazenamento tabular e relacional.
  - Dados estruturados.
  - Sistemas de Gestão de Bancos de Dados (SGBDs) tradicionais: Postgres, MySQL, Oracle.
- **NoSQL**:
  - Flexibilidade de formatos, como JSON e XML.
  - Alta performance e escalabilidade.
  - Exemplos: MongoDB, Cassandra, AWS DynamoDB.
- **Baseado em Arquivos**:
  - Ideal para variedade e eficiência.
  - Exemplos: Parquet, Delta, CSV.
  - Usado frequentemente em soluções temporárias ou versionadas, como os estágios **Bronze, Silver e Gold** no Delta.

### Armazenamento Colunar vs. Linha

A estrutura de armazenamento influencia diretamente a performance:

- **Linha**:
  - Semelhante a planilhas, como Excel.
  - **Vantagens**: Adequado para grandes volumes de dados.
  - **Desvantagens**: Menor performance e flexibilidade.
  
- **Colunar**:
  - Armazenamento orientado a colunas, otimizado para leituras rápidas.
  - Comum em dados oriundos de sistemas web em formato JSON.
  - **Vantagens**: Alta performance em consultas.
  - **Desvantagens**: Menor capacidade de armazenamento.

### Formatos de Arquivo

A escolha do formato de arquivo depende do ecossistema e da arquitetura do projeto:

- **CSV**: Texto simples e delimitado, amplamente utilizado.
- **Parquet**: Colunar, eficiente para leitura e compactação.
- **Delta**: Suporta ACID, útil para versionamento.
- **JSON**: Semi-estruturado, comum em APIs e sistemas web.
- **Orc**: Colunar, otimizado para grandes volumes de dados.
- **Avro**: Binário, com esquema, bom para dados em movimento.

Lembre-se de que a decisão sobre formatos e modelos de armazenamento deve se alinhar à arquitetura geral, seja ela na nuvem ou on-premise.

## Sistemas Distribuídos e Clusters

Antes de nos aprofundarmos em sistemas distribuídos, é fundamental entender o potencial e as limitações de uma única máquina. Uma máquina individual pode executar tarefas básicas, como armazenamento e processamento, além de rodar scripts e diversos serviços. No entanto, há um limite físico para o que ela pode realizar. Com essa limitação em mente, surgiu o conceito de cluster de processamento distribuído: um agrupamento de máquinas que operam conjuntamente como um único sistema. Esta união visa distribuir a carga de trabalho, tornando as operações mais eficientes e rápidas.

### Hierarquia dos Sistemas Distribuídos

**Sistema Local**:

- Sistema operacional **LINUX**
  - EXT4 (principal sistema de arquivos do Linux)

**Sistema Distribuído**:

- Ambiente em rede
- 3 máquinas:
  - Sistema operacional **LINUX**
    - Software para armazenamento distribuído
    - Software para processamento distribuído
      - EXT4 (como sistema de armazenamento local)

> ![Imagem representativa do sistema distribuído](Images/Readme/Sistema%20distribuido.png)

> ![Imagem sobre sistemas de arquivos locais](Images/Readme/SIstemasArq.png)

> ![Imagem sobre sistemas de arquivos distribuídos](Images/Readme/SIstemArqusss.png)

### Sistemas de Processamento Distribuído

- **Sistemas Tradicionais**:
  > ![Visualizar](Images/Readme/SistemaPro.png)

- **Sistemas em Cloud e Atuais**:
  > ![Visualizar](Images/Readme/CloudProcess.png)

### Vantagens dos Sistemas Distribuídos

- **Escalabilidade**: Capacidade de expansão flexível.
  - Vertical: Adição ou melhoria do hardware interno (e.g., novo processador).
  - Horizontal: Acréscimo de novas máquinas ao sistema.
  
- **Confiabilidade**: Em caso de falha em uma máquina, as outras compensam a deficiência.

- **Desempenho**: Processamento paralelo proporcionado por várias máquinas reduz o tempo de execução.

- **Flexibilidade**: Os sistemas distribuídos são versáteis e podem ser usados para diversas funções, desde big data até outras necessidades empresariais.

### Desafios dos Sistemas Distribuídos

- **Complexidade**: Requer um planejamento cuidadoso de hardware e software.

- **Sobrecarga de Comunicação**: O risco de congestionamento da rede pode aumentar a latência.

- **Riscos de Segurança**: Se uma máquina for comprometida, outras podem ser afetadas, ameaçando a integridade dos dados.

- **Custo Elevado**: A instalação e manutenção exigem investimento em equipamentos robustos e especialistas qualificados.

**Ilustração de um Cluster**:
> ![Visualizar Cluster](Images/Readme/cluster-overview.png)

---

Esta reformulação oferece uma estrutura mais clara e informações detalhadas sobre sistemas distribuídos e clusters.

## Armazenamento de Dados: Data Lake, Data Warehouse, e Além

Ao buscar soluções de armazenamento e tratamento de dados, é essencial entender certos `CONCEITOS` fundamentais. Eles desempenham papéis específicos no universo de dados. Vamos detalhá-los:

- **Data Warehouse**:
  - **Definição**: Um banco de dados projetado principalmente para consultas analíticas, permitindo o processamento rápido e inteligente de grandes volumes de dados.
  - **Características**:
    - Frequentemente associado a bancos de dados transacionais.
    - Comumente o destino final de dados processados.
    - Otimizado para consultas analíticas.
    - Integra dados de múltiplas fontes.
    - Suporta ferramentas de BI (Business Intelligence).
    - Armazena dados históricos.

- **Data Lake**:
  - **Definição**: Um repositório que armazena grandes volumes de dados em seu formato natural, geralmente no início do pipeline de dados.
  - **Características**:
    - Governança de dados é crucial para evitar o caos ("data swamp").
    - Capaz de armazenar diversos tipos de dados, estruturados ou não.
    - Projetado para processamento e consulta performática.
    - Flexível e altamente escalável (ex.: Cluster).

- **Data Lakehouse**:
  - **Definição**: Uma combinação de Data Lake e Data Warehouse, oferendo o melhor de ambos em uma única plataforma.
  - **Características**:
    - Armazenamento flexível, suportando vários tipos de dados.
    - Implementado de forma unificada com ferramentas estratégicas.
    - Requer consideração cuidadosa devido à sua complexidade e custos.

- **Data Store**:
  - **Definição**: Repositório para armazenamento e gerenciamento de dados.
  - **Categorias**:
    - Banco de dados relacionais.
    - Banco de dados não-relacionais.
    - Sistemas de arquivos, como HDFS, Amazon S3, parquet e NTFS.
    - Motores de busca textual (full-text search engine).
    - Filas de mensagens.
    - Armazenamento em memória (in-memory data store).
    - Armazenamento key-value.

- **Data Hub**:
  - **Definição**: Uma solução que integra vários conceitos e métodos de armazenamento, otimizando práticas e reutilizando infraestruturas existentes.
    - ![Alt text](Images/Readme/Datahub.png)

- **Data Mesh**:
  - **Definição**: Uma abordagem que considera a infraestrutura de dados como plataforma. Por exemplo, Databricks, que opera como um data lakehouse em um ambiente SaaS.
    - ![Alt text](Images/Readme/DataMesh.png)

Ao escolher uma solução, é essencial alinhar os conceitos à estratégia de negócios, otimizando os investimentos e garantindo a eficiência no tratamento dos dados.

## Modelagem de Dados

A modelagem de dados é fundamental para a organização e otimização do armazenamento e acesso a informações. Esse processo envolve projetar e construir estruturas lógicas para representar as relações e formas de armazenamento de dados, geralmente por meio de diagramas e definições de tabelas. Antes de utilizar os dados, é imprescindível uma modelagem adequada para garantir a eficácia das operações.

### Modelagem Relacional

- Baseia-se na criação de entidades e na definição de suas relações através de tabelas e campos.
- Exemplo: "Clientes" e "Produtos" são entidades que podem ter uma relação entre si.
- É frequentemente aplicada em Sistemas Gerenciadores de Bancos de Dados (SGBDs) relacionais e sistemas transacionais, focando na organização eficiente do armazenamento.

### Modelagem Dimensional

- Amplamente usada em sistemas de Business Intelligence (BI) e Data Warehouses (DW) para analisar dados em uma perspectiva multidimensional.
- Normalmente, os sistemas relacionais atuam como fonte de dados para essa modelagem.
- Centra-se em:
  - **Medidas**: Valores numéricos como receita, preço e quantidade.
  - **Dimensões**: Contextualizam as medidas, como nome do produto ou cliente.
- Os dados, frequentemente, são agregados de maneira escalável, facilitando cálculos e análises.
- Principal objetivo é a análise profunda de dados, auxiliando na criação de dashboards e relatórios.

### Modelagem de Datalakes

- Abordagem para armazenar vastos volumes de dados, independentemente de sua origem ou tipo.
- Comumente associado a conceitos como clusters de processamento, armazenamento e pipelines de dados.

### Modelo Conceitual

- Foca na área de negócios, destacando entidades ou fatos centrais para a modelagem.

### Modelo Lógico

- Tradução detalhada do modelo conceitual, preparando o terreno para o técnico de TI que construirá o modelo.

### Modelo Físico

- Representa a efetiva implementação, sendo articulado em linguagens de programação, como SQL ou Python.

### Definindo Granularidade

- Refere-se à precisão com que os dados são representados.
- A granularidade pode ser:
  - **Alta**: Dados subdivididos em detalhes minuciosos.
  - **Baixa**: Dados mais agregados e generalizados.
- É crucial na modelagem de dados pois influencia o armazenamento, recuperação e análise.
- Uma granularidade bem definida é a chave para balancear precisão analítica com eficiência de armazenamento e processamento. Por exemplo, em um DW, é necessário analisar vendas por dia ou por hora? A resposta determinará a granularidade adequada.

![Alt text](Images/Readme/Modelagem%20de%20dados.png)

## Qualidade de Dados, Rastreabilidade de Dados e Observabilidade de Dados

### Qualidade de Dados (Data Quality)

- A qualidade de dados refere-se à capacidade dos dados serem confiáveis, precisos e úteis para os usuários finais. Uma boa qualidade implica em dados que apresentam:
  - **Precisão**: Acurácia em representar a realidade.
  - **Exatidão**: Conformidade com o valor real ou padrão.
  - **Consistência**: Uniformidade ao longo do tempo.
  - **Relevância**: Pertinência ao propósito.
  - **Cobertura**: Abrangência completa do escopo.
  - **Atualização**: Dados recentes e atualizados.
- Para assegurar esta qualidade, são empregadas técnicas avançadas, como mineração de dados e estatística, para identificar e mitigar potenciais erros, como informações erradas ou medições equivocadas.
- Posteriormente, os dados passam por limpeza, removendo entradas duplicadas ou nulas, normalizando-os a padrões pertinentes e validando junto aos stakeholders de negócio.

### Rastreabilidade de Dados (Data Lineage)

- Esse conceito está ligado à capacidade de rastrear a trajetória dos dados em todo seu ciclo de vida. Isso permite:
  - Identificar e corrigir erros em diferentes etapas do processamento.
  - Oferecer transparência e confiança, ao possibilitar que os usuários compreendam a origem e a evolução dos dados.
    - Exemplo: A abordagem da "Arquitetura Medallion".
  - Facilitar auditorias, proporcionando uma visão holística da documentação e das atividades do projeto.
  - Potencializar a eficiência dos processos de negócio e análises, abrindo caminho para otimizações.

### Observabilidade de Dados (Data Observability)

- A observabilidade é o olhar atento sobre o comportamento dos dados dentro dos sistemas, atuando como uma ferramenta de monitoramento em tempo real.
  ![Alt text](Images/Readme/Observ.png)
  
- É crucial entender o estado e comportamento dos dados no sistema, pois isso permite antecipar problemas, realizar diagnósticos e implementar correções de maneira eficaz.
- Uma estratégia efetiva para alcançar isso é a gestão de metadados, que proporciona uma visão completa do estado dos dados.

**Os 5 Pilares da Observabilidade de Dados**:
![Alt text](Images/Readme/PilarObserv.png)

Estes três conceitos - qualidade, rastreabilidade e observabilidade - são essenciais para assegurar que os dados sejam não apenas confiáveis, mas também transparentes, monitoráveis e otimizados para aplicações de negócios.

## DevOps na Engenharia de Dados

### O que é DevOps?

- **Definição**: DevOps é uma cultura e conjunto de práticas que busca integrar equipes de desenvolvimento e operações de TI para produzir software com mais eficiência e qualidade.
  
- **Características principais**:
  - Automação de infraestrutura e implantação de software.
  - Monitoramento e análise métrica de performance.
  - Testes e feedbacks contínuos.

### Valor do DevOps na Engenharia de Dados

- **Automação de Infraestrutura**: Criação de ambientes de forma previsível via código.
- **Controle de Versão**: Código e dados gerenciados de forma colaborativa.
- **Integração Contínua**: Detecção precoce de erros e conflitos.
- **Entrega Contínua**: Implementações rápidas e seguras.
- **Monitoramento**: Assegura qualidade e desempenho de sistemas.
- **Automação de Processamento de Dados**: Redução de latências.
- **Testes Automatizados**: Garantia de qualidade e detecção precoce de falhas.

### Infraestrutura como Código (IaC) na Engenharia de Dados

- **Consistência**: Infraestrutura uniforme em todos os ambientes.
- **Eficiência**: Rápida configuração e gestão de componentes.
- **Flexibilidade**: Ajustes rápidos conforme necessidades.
- **Controle de Versão**: Mudanças gerenciadas como código.

### Integração Contínua/Entrega Contínua (CI/CD)

- **Gerenciamento de Código**: Versionamento evita conflitos.
- **Teste Automatizado**: Verifica integridade de soluções de dados.
- **Pipeline de Dados**: Processamento, armazenamento e entrega automatizados.
- **Configuração via IaC**: Ambientes preparados rapidamente.
- **Monitoramento**: Identificação de falhas e desempenho.
- **Entrega Contínua**: Implementações seguras e ágeis.

### Containers e Orquestração

- **Portabilidade**: Migrar entre ambientes com facilidade.
- **Escalabilidade**: Ajuste de recursos conforme demanda.
- **Resiliência**: Disponibilidade contínua, mesmo após falhas.
- **Eficiência**: Uso otimizado de hardware.
- **Flexibilidade**: Atualizações modulares.
- **Desenvolvimento com Containers**: Ambientes de teste eficientes e consistentes.
- **Orquestração**: Gestão otimizada de clusters de bancos de dados.

### Soluções em Cloud para Engenharia de Dados

- **Escalabilidade**: Recursos ajustáveis conforme necessidade.
- **Redução de Custos**: Pagamento conforme uso.
- **Acesso Universal**: Recursos acessíveis de qualquer local.
- **Manutenção Simplificada**: Provedores gerenciam infraestrutura.

Comparando com soluções locais:

- **Controle Total**: Maior segurança e personalização.
- **Latência de Rede**: Soluções locais podem oferecer latências mais baixas.
- **Investimento Inicial**: Exige mais recursos iniciais, mas duráveis.

---

Uma ferramenta legal de aprender eo docker aqui tem um link para melhor explicação Docker/README.md

## Segurança e Integridade dos Dados

No cenário atual, onde a informação é um ativo vital para as empresas, é crucial implementar medidas de segurança robustas para proteger os dados. Neste contexto, garantir um ambiente de alta disponibilidade não é apenas uma opção, mas uma necessidade.

Neste curso, você será capacitado para montar um ambiente seguro e de alta disponibilidade de dados de forma eficaz e profissional. As principais competências que você adquirirá incluem:

1. **Desenvolvimento de Sistemas de Segurança**: Compreenderá os mecanismos essenciais para criar sistemas que protejam os dados de ameaças internas e externas.

2. **Controle de Acesso Avançado**: Aprenderá a estabelecer protocolos rigorosos de controle de acesso, garantindo que apenas indivíduos autorizados tenham acesso a informações confidenciais.

3. **Criptografia e Proteção de Dados**: Dominará técnicas avançadas de encriptação para assegurar que os dados armazenados ou transmitidos sejam inacessíveis a indivíduos não autorizados.

4. **Sistemas de Auditoria**: Estabelecerá procedimentos de auditoria para monitorar e rastrear todas as atividades relacionadas aos dados, facilitando a identificação e correção de qualquer comportamento suspeito ou atividade não autorizada.

5. **Configuração de Alta Disponibilidade**: Aprenderá a configurar sistemas em cluster, garantindo que os dados estejam sempre acessíveis, mesmo em situações de falha de hardware ou software.

6. **Testes de Invasão e Avaliação de Vulnerabilidades**: Será capaz de simular ataques ao ambiente de dados para identificar falhas e vulnerabilidades, garantindo que o sistema esteja sempre um passo à frente das ameaças.

Ao final deste curso, você terá um conhecimento abrangente sobre as melhores práticas de segurança de dados, preparando-o para enfrentar os desafios do mundo digital atual e garantir que as informações de sua organização estejam sempre protegidas e acessíveis.

Para mais conteudos vc pode acessar a pasta **SRC** obrigado por ler ate aqui 🫡🫡
