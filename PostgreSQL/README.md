# **PostgresSQL**

PostgreSQL é um sistema gerenciador de banco de dados objeto-relacional baseado no POSTGRES, Versão 4.2, desenvolvido na Universidade da Califórnia no Departamento de Ciências da Computação em Berkeley, o qual foi pioneiro em muitos conceitos que vieram a estar disponíveis em alguns bancos de dados comerciais mais tarde.

> Algumas características modernas do PostgreSQL:

- Consultas complexas;
- Chaves estrangeiras (foreign keys);
- Gatilhos (triggers);
- Visões (views);
- Integridade transacional.

[Introduçao a postgres](https://www.youtube.com/watch?v=Z_SPrzlT4Fc)

[Documentação](https://www.postgresql.org/docs/)

# **Para que serve ?**

O PostgreSQL é uma ferramenta que atua como sistema de gerenciamento de bancos de dados relacionados. Seu foco é permitir implementação da linguagem SQL em estruturas, garantindo um trabalho com os padrões desse tipo de ordenação dos dados.

# **Como funciona ?**

Ele consiste em um processo de servidor que lê e grava os arquivos de banco de dados reais, e um conjunto de programas cliente que se comunicam com o servidor. O mais comumente utilizado é o comando psql, que permite ao usuário executar consultas SQL e visualizar os seus resultados.

# **Qual e a Arquitetura ?**

![arquitetura](Images/Postgres%20docker.png)

# **Como instalar ?**

Ele ja vem por padrão quando e configurado as demais Ferramentas mas para obter os recursos de forma completa iremos usar a imagem oficial dele onde tem tudo especificado de como se deve fazer a instalação e uso da imagem

[Docker hub](https://hub.docker.com/_/postgres/)

[Instalação no docker](https://www.youtube.com/watch?v=JbFHbVAp-VM)

# **Como funciona dentro do container ?**

Nesse caso basta você digitar a mesma senha que definiu no comando docker run. Pronto, com isso agora você terá acesso ao banco do Docker assim como se estivesse acessando qualquer outra instância do Postgres

[Detalhes](https://brunolorencolopes.gitlab.io/blog/pt-br/docker/RODANDO_O_POSTGRES_EM_DOCKER.html)

# **Como usar ?**

Depende do que vc quer trabalhar e oque vc fez no processo de transformações isso vai definir o seu resultado no banco de dados e no tableau

[Fazendo conexao local](https://hevodata.com/learn/spark-postgresql/)

[Ambiente docker (recomendado)](https://omahony.id.au/tech/2021/01/28/spark-postgres-jupyter.html)

# **Uso do Python ?**

- [Psycopg2](https://pypi.org/project/psycopg2/)
