import airflow
from datetime import datetime, timedelta
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

default_args = {
    'owner': 'jozimar',
    'start_date': datetime(2020, 11, 18),
    'retries': 10,
    'retry_delay': timedelta(hours=1)
}
with airflow.DAG('dag_teste_spark_documento_vencido_v3', default_args=default_args, schedule_interval='0 1 * * *') as dag:
    task_elt_documento_pagar = SparkSubmitOperator(
        task_id='elt_documento_pagar_spark',
        conn_id='spark',
        application="./dags/sparkjob.py",
        # caso precise enviar dados da dag para o job airflow utilize esta propriedade
        application_args=[
            "{{ds}}", "sqlserver://127.0.0.1:1433;databaseName=Teste"],
        total_executor_cores=3,
        executor_memory="30g",
        conf={
            "spark.mongodb.input.uri": "mongodb://127.0.0.1:27017/Financeiro",
            "spark.mongodb.output.uri": "mongodb://127.0.0.1:27017/Financeiro",
            "spark.network.timeout": 10000000,
            "spark.executor.heartbeatInterval": 10000000,
            "spark.storage.blockManagerSlaveTimeoutMs": 10000000,
            "spark.driver.maxResultSize": "20g"
        },
        packages="org.mongodb.spark:mongo-spark-connector_2.12:3.0.0,com.microsoft.sqlserver:mssql-jdbc:8.4.1.jre8"
    )
