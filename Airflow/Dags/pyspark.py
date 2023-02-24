
import airflow
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from pyspark.sql import SparkSession, functions


def processo_etl_spark():
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
    #! criação de dataframe com extração de dados 
    df = spark.read.format("jdbc") \
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
    # agrupamento de dados e agregação de valores
    group = df.select("CodigoTipoDocumento", "Vencimento", "Saldo") \
        .groupby(["CodigoTipoDocumento", "Vencimento"]).agg(functions.sum("Saldo").alias("Saldo"))
    #! carregamento de dados para dentro da base mongo
    group.write.format("com.mongodb.spark.sql.DefaultSource") \
        .mode("overwrite") \
        .option("database", "Financeiro") \
        .option("collection", "Fact_DocumentoPagar") \
        .save()
    termino = datetime.now()
    print(termino)
    print(termino - inicio)


default_args = {
    'owner': 'jozimar',
    'start_date': datetime(2020, 11, 18),
    'retries': 10,
    'retry_delay': timedelta(hours=1)
}
with airflow.DAG('dag_teste_spark_documento_vencido_v01',
                 default_args=default_args,
                 schedule_interval='0 1 * * *') as dag:
    task_elt_documento_pagar = PythonOperator(
        task_id='elt_documento_pagar_spark',
        python_callable=processo_etl_spark
    )
