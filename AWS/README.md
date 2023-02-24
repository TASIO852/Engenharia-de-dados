# Amazon Web Services

- Nessa parte vamos explica as principais ferramentas existentes na AWS para os **engenheiro de dados** e vamos indicar suas **funcionalidades** e oque cada uma faz em um sistema sempre vamos colocar de modo que gere um **Datalake** no processo de ferramentas.

- Para informações mais detalhadas podemos acessar a [Documentation](https://docs.aws.amazon.com/index.html)

- As ferramentas que vamos estudar vao ser so relacionadas a engenharia de dados e Big Data iremos seguir esse site de formação de datalakes [Site da aws](https://aws.amazon.com/pt/big-data/datalakes-and-analytics/)

> Dicas e Ideias

- Interessante criar um usuario e grupo para cada serviço utilizado
- usar os serviços de forma separada em termos de config
- cada serviço complementa o outro
- cada serviço tem sua evolução
  - EC2 >> EMR
  - S3 >> RDS

# Bucket S3!

[Docs](https://docs.aws.amazon.com/s3/?icmpid=docs_homepage_featuredsvcs)
[Preço](https://aws.amazon.com/pt/s3/pricing/)

- O Amazon Simple Storage Service (Amazon S3) é um serviço de armazenamento de objetos que oferece escalabilidade líder do setor, disponibilidade de dados, segurança e performance.
- Clientes de todos os tamanhos e setores podem usar o Amazon S3 para armazenar e proteger qualquer volume de dados para uma variedade de casos de uso, como data lakes e análises de big data.
- O Amazon S3 fornece recursos de gerenciamento para que você possa otimizar, organizar e configurar o acesso aos seus dados para atender aos seus requisitos específicos de negócios, organizacionais e de compatibilidade.

- armazena objetos (csv,excel,imagem)
- arquivos nao públicos tem que colocar a permissão e fazer uma politica de permissão com json
- a politica de permissão e como se fosse um yml so que json
- a origem dos arquivos pode vim de outro serviço da aws
- e igual o git hub so que pago
- os custos do projeto vai depender de como vc vai armazenar e qual ea sua nescidade

# IAM

[Docs](https://docs.aws.amazon.com/iam/index.html)

- O AWS Identity and Access Management (IAM) é um serviço da web que ajuda você a controlar com segurança o acesso aos recursos da AWS.
- Você usa o IAM para controlar quem está autenticado (conectado) e autorizado (tem permissões) para usar recursos.

- faz o gerenciamento de acesos e recursos dos serviços ofertados na aws
- sempre quando for usar a ferramenta pegar todas as senha e credenciais pq depois nao da pra recuperar
- nao cobra nada

# EC2

- Basicamente e uma 'VM' que se passa por 'Servidor' (so que semm interface) que vc pode configurar da forma que quiser e sincronizar com outras 'VM'

- O Amazon Elastic Compute Cloud (Amazon EC2) fornece capacidade de computação escalável na nuvem Amazon Web Services (AWS).
- O uso do Amazon EC2 elimina a necessidade de investir em hardware antecipadamente, para que você possa desenvolver e implantar aplicativos com mais rapidez.
- Você pode usar o Amazon EC2 para iniciar quantos servidores virtuais precisar, configurar a segurança e a rede e gerenciar o armazenamento.
- O Amazon EC2 permite que você aumente ou diminua a escala para lidar com mudanças nos requisitos ou picos de popularidade, reduzindo sua necessidade de prever o tráfego.

[Docs](https://docs.aws.amazon.com/ec2/index.html)

[Preço](https://aws.amazon.com/pt/ec2/pricing/on-demand/)

# EMR

- Amazon EMR é uma plataforma de cluster gerenciada que simplifica a execução de frameworks de Big Data
- processar e analisar grandes volumes de dados. Usando essas estruturas e projetos de código aberto relacionados
- O Amazon EMR também permite transformar e mover grandes volumes de dados para e da AWS Armazenamentos de dados e bancos de dados, como o Amazon Simple Storage Service (Amazon S3) e o Amazon DynamoDB.

# RDS

O Amazon Relational Database Service (Amazon RDS) é um serviço da Web que facilita a configuração, a operação e escalabilidade de um banco de dados relacional na Nuvem AWS. Ele fornece capacidade econômica e redimensionável para um banco de dados relacional padrão do setor e gerencia tarefas comuns de administração de banco de dados.

# Route 53

- O Amazon Route 53 é um web service de Domain Name System (DNS) altamente disponível e dimensionável.
- Você pode usar o Route 53 para executar três funções principais em qualquer combinação:

1. Registrar nomes de domínio
2. Rotear tráfego de Internet para os recursos do seu domínio
3. Verificar a integridade de seus recursos

# Amazon Redshift

- A primeira etapa para criar um data warehouse é executar um conjunto de nós, chamado cluster do Amazon Redshift.
- Depois de provisionar o seu cluster, você pode fazer upload do seu conjunto de dados e executar consultas de análise de dados.
- Independentemente do tamanho do conjunto de dados, o Amazon Redshift oferece performance de consulta rápida usando as mesmas ferramentas baseadas em SQL e aplicações de business intelligence que você usa hoje.

# Glue

- O AWS Glue é um serviço de integração de dados com tecnologia sem servidor que facilita aos usuários de análise a descoberta, preparação, transferência e integração de dados de várias fontes.
- Você pode usá-lo para análise, machine learning e desenvolvimento de aplicações.
- Também inclui outras ferramentas de produtividade e operações de dados para criação, execução de trabalhos e implementação de fluxos de trabalho de negócios.
- Com o AWS Glue, você pode detectar e se conectar a mais de 70 fontes de dados diversas e gerenciar seus dados em um catálogo de dados centralizado.
- Você pode criar, executar e monitorar visualmente pipelines de extração, transformação e carregamento (ETL) para carregar dados em seus data lakes

## AWS Glue Studio

- O AWS Glue Studio é uma interface gráfica que facilita a criação, a execução e o monitoramento de trabalhos de integração de dados no AWS Glue.
- Você pode compor visualmente fluxos de trabalho de transformação de dados e executá-los perfeitamente no mecanismo de ETL com tecnologia sem servidor baseado no Apache Spark do AWS Glue.
- Com o AWS Glue Studio, você pode criar e gerenciar trabalhos que coletam, transformam e limpam dados. Use também o AWS Glue Studio para solucionar problemas e editar scripts de trabalho.

Os principais recursos do aws glue :

- Descobrir e organizar dados
- Transformar, preparar e limpar dados para análise
- Criar e monitorar pipelines de dado

# Lambda function

[Preço](https://aws.amazon.com/pt/lambda/pricing/)
[Docs](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)

# CloudWhat (EventBridge)

- Basicamente sao automaçoes que rodam o seu codigo do lambda de acordo com oque vc configura deixando tudo automatico e como se fosse o job que e configurado em batch do pentaho
- Pode ser configurado para ser usado em qualquer ferramenta da amazon

# Athena

# Kinesis

# SageMaker
