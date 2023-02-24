from airflow.operators.bash import BashOperator
from airflow import DAG
from textwrap import dedent
import airflow
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from kafka import KafkaConsumer, KafkaProducer

#! Configuration Dags
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2015, 6, 1),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

#!scripts python
t1 = PythonOperator(
    task_id='elt_documento_pagar_spark',
    python_callable=processo_etl_spark
)
#! bash
templated_command = """
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7)}}"
        echo "{{ params.my_param }}"
    {% endfor %}
"""

t3 = BashOperator(
    task_id="templated",
    bash_command=templated_command,
    params={"my_param": "Parameter I passed in"},
    dag=dag,
)

#! Producer kafka
producer = KafkaProducer(
    bootstrap_servers=['127.0.0.1:9092'],
    value_serializer=json_serializer,
    partitioner=get_partition
)
producer.send("spark-transformed-text", text)
# <kafka.producer.future.FutureRecordMetadata at 0x7f6e3f2151c0>
producer.flush()
consumer = KafkaConsumer(
    "spark-transformed-text",
    bootstrap_servers='127.0.0.1:9092',
    auto_offset_reset='earliest',
    group_id='consumer-group-a'
)
print('<<<<<<<<<<<<<starting consumer>>>>>>>>>>>>>')
for msg in consumer:
    print('Text = {}'.format(json.loads(msg.value)))

#! Spark SubmitOperator conexao com o banco de dados mongodb
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

#! Consumer kafka and spark
dag = DAG('spark_job_dag', description='DAG to trigger pySpark job',
          schedule_interval='0 12 * * *',
          start_date=datetime(2020, 3, 20), catchup=False)

start_task = DummyOperator(task_id='start_task', dag=dag)

commands = """
    cd /Users/philips/Documents/Study_code/Spark/spark-samples;
    /usr/local/Cellar/apache-spark/3.3.0/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 fetch_data.py;
    """

fetch_data = BashOperator(
    task_id='spark-task',
    bash_command=commands,
    dag=dag)

start_task >> fetch_data

#! sequencia de tasks

with DAG(
    'tutorial',
    default_args={
        'depends_on_past': False,
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
        'queue': 'bash_queue',
        'pool': 'backfill',
        'priority_weight': 10,
        'end_date': datetime(2016, 1, 1),
        'wait_for_downstream': False,
        'sla': timedelta(hours=2),
        'execution_timeout': timedelta(seconds=300),
        'on_failure_callback': 'some_function',
        'on_success_callback': 'some_other_function',
        'on_retry_callback': 'another_function',
        'sla_miss_callback': 'yet_another_function',
        'trigger_rule': 'all_success'
    },

    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:

    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t2 = BashOperator(
        task_id='sleep',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=3,
    )
    t1.doc_md = dedent(
        """\
    #### Task Documentation
    You can document your task using the attributes `doc_md` (markdown),
    `doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets
    rendered in the UI's Task Instance Details page.
    ![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)

    """
    )

    dag.doc_md = __doc__ 
    dag.doc_md = """
    This is a documentation placed anywhere
    """  
    templated_command = dedent(
        """
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7)}}"
    {% endfor %}
    """
    )

    t3 = BashOperator(
        task_id='templated',
        depends_on_past=False,
        bash_command=templated_command,
    )

    t1 >> [t2, t3]


from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from datetime import datetime, timedelta

spark_master = "spark://spark:7077"
postgres_driver_jar = "/usr/local/spark/resources/jars/postgresql-9.4.1207.jar"

movies_file = "/usr/local/spark/resources/data/movies.csv"
ratings_file = "/usr/local/spark/resources/data/ratings.csv"
postgres_db = "jdbc:postgresql://postgres/test"
postgres_user = "test"
postgres_pwd = "postgres"

now = datetime.now()

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(now.year, now.month, now.day),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1)
}

dag = DAG(
        dag_id="spark-postgres", 
        description="This DAG is a sample of integration between Spark and DB. It reads CSV files, load them into a Postgres DB and then read them from the same Postgres DB.",
        default_args=default_args, 
        schedule_interval=timedelta(1)
    )

start = DummyOperator(task_id="start", dag=dag)

spark_job_load_postgres = SparkSubmitOperator(
    task_id="spark_job_load_postgres",
    application="/usr/local/spark/app/load-postgres.py",
    name="load-postgres",
    conn_id="spark_default",
    verbose=1,
    conf={"spark.master":spark_master},
    application_args=[movies_file,ratings_file,postgres_db,postgres_user,postgres_pwd],
    jars=postgres_driver_jar,
    driver_class_path=postgres_driver_jar,
    dag=dag)

spark_job_read_postgres = SparkSubmitOperator(
    task_id="spark_job_read_postgres",
    application="/usr/local/spark/app/read-postgres.py",
    name="read-postgres",
    conn_id="spark_default",
    verbose=1,
    conf={"spark.master":spark_master},
    application_args=[postgres_db,postgres_user,postgres_pwd],
    jars=postgres_driver_jar,
    driver_class_path=postgres_driver_jar,
    dag=dag)

end = DummyOperator(task_id="end", dag=dag)

start >> spark_job_load_postgres >> spark_job_read_postgres >> end