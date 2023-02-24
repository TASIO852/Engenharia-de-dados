from datetime import datetime
from airflow.models import DAG, Variable
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from bots.PythonHelper import get_result

default_args = {
    'owner': 'Remediate',
    'start_date': datetime(2021, 7, 7),
    'depends_on_past': False,
}

with DAG(
        dag_id='PythonDemo',
        default_args=default_args,
        schedule_interval=None,
        tags=['Demo1']) as dag:

    start_remediation = PythonOperator(
        task_id='start_remediation',
        provide_context=True,
        python_callable=get_result
    )

    end_remediation = DummyOperator(
        task_id='end_remediation',
        trigger_rule="one_success"
    )

    start_remediation >> end_remediation