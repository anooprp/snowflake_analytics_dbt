from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
    'owner': 'anoop',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='dbt_cleanup',
    default_args=default_args,
    description='Run dbt clean to remove compiled files and modules',
    schedule=None,  # manual trigger only
    start_date=days_ago(1),
    catchup=False,
    tags=['dbt', 'cleanup'],
) as dag:

    DBT_DIR = "/usr/app"
    DBT_PROFILES_DIR = f"{DBT_DIR}/profiles"

    dbt_clean = BashOperator(
        task_id='dbt_clean',
        bash_command=(
            f'cd {DBT_DIR} && '
            f'dbt clean --profiles-dir {DBT_PROFILES_DIR}'
        ),
    )
