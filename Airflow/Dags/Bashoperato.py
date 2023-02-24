import airflow
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'jozimar',
    'start_date': datetime(2020, 11, 18),
    'retries': 10,
    'retry_delay': timedelta(hours=1)
}
with airflow.DAG('dag_teste_spark_documento_vencido_v2',
                 default_args=default_args,
                 schedule_interval='0 1 * * *') as dag:
    task_elt_documento_pagar = BashOperator(
        task_id='elt_documento_pagar_spark',
        bash_command="python ./dags/sparkjob.py",
    )
