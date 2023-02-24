import sys
from pyspark import SparkConf, SparkContext
import datetime
from pyspark.sql import SparkSession, functions

spark = SparkSession \
    .builder \
    .appName("Extração Documentos a Pagar") \
    .config("spark.jars.packages",
            "org.mongodb.spark:mongo-spark-connector_2.12:3.0.0,com.microsoft.sqlserver:mssql-jdbc:8.4.1.jre8") \
    .config("spark.mongodb.input.uri", "mongodb://127.0.0.1:27017/Financeiro") \
    .config("spark.mongodb.output.uri", "mongodb://127.0.0.1:27017/Financeiro") \
    .config("spark.driver.maxResultSize", "8g") \
    .config("spark.network.timeout", 10000000) \
    .config("spark.executor.heartbeatInterval", 10000000) \
    .config("spark.storage.blockManagerSlaveTimeoutMs", 10000000) \
    .config("spark.executor.memory", "10g") \
    .master("spark://192.168.0.1:7077") \
    .getOrCreate()

inicio = datetime.now()
print(inicio)

jdbcDF = spark.read.format("jdbc") \
    .option("url", "jdbc:sqlserver://127.0.0.1:1433;databaseName=Teste") \
    .option("user", 'Teste') \
    .option("password", 'teste') \
    .option("numPartitions", 100) \
    .option("partitionColumn", "Id") \
    .option("lowerBound", 1) \
    .option("upperBound", 488777675) \
    .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
    .option("dbtable", "(select Id, DataVencimento AS Vencimento, TipoCod AS CodigoTipoDocumento, cast(recsld as FLOAT) AS Saldo from DocumentoPagar \
     where TipoCod in ('200','17') and RecPag = 'A') T") \
    .load()

group = jdbcDF.select("CodigoTipoDocumento", "Vencimento", "Saldo") \
    .groupby(["CodigoTipoDocumento", "Vencimento"]).agg(functions.sum("Saldo").alias("Saldo"))
group.write.format("com.mongodb.spark.sql.DefaultSource") \
    .mode("overwrite") \
    .option("database", "Financeiro") \
    .option("collection", "Fact_DocumentoPagar") \
    .save()
termino = datetime.now()
print(termino)
print(termino - inicio)

# As configurações são recebidas pelo comando spark-submit executado no SparkSubmitOperator
spark = SparkSession(SparkContext(conf=SparkConf()).getOrCreate())
# argumento recebidos da dag - data execução
data_base = datetime.strptime(sys.argv[1], '%Y-%m-%d')
inicio = datetime.now()
print(inicio)

# extrair dados do sql server
df = spark.read.format("jdbc") \
    .option("url", "jdbc:{}".format(sys.argv[2])) \
    .option("user", 'Teste') \
    .option("password", 'teste') \
    .option("numPartitions", 100) \
    .option("partitionColumn", "Id") \
    .option("lowerBound", 1) \
    .option("upperBound", 488777675) \
    .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
    .option("dbtable", "(select Id, DataVencimento AS Vencimento, TipoCod AS CodigoTipoDocumento, cast(recsld as FLOAT) AS Saldo from DocumentoPagar \
     where TipoCod in ('200','17') and RecPag = 'A') T") \
    .load()
# agrupar
group = df.select("CodigoTipoDocumento", "Vencimento", "Saldo") \
    .groupby(["CodigoTipoDocumento", "Vencimento"]).agg(functions.sum("Saldo").alias("Saldo"))

# salvar dados no mongo
group.write.format("com.mongodb.spark.sql.DefaultSource") \
    .mode("overwrite") \
    .option("database", "Financeiro") \
    .option("collection", "Fact_DocumentoPagar") \
    .save()
termino = datetime.now()
print(termino)
print(termino - inicio)
