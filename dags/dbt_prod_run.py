from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
    'owner': 'anoop',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=10),
}

with DAG(
    dag_id='dbt_pipeline_prod',
    default_args=default_args,
    description='DBT pipeline: run only test models with prod target',
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False,
    tags=['dbt', 'prod'],
) as dag:

    DBT_DIR = "/usr/app"
    DBT_PROFILES_DIR = f"{DBT_DIR}/profiles"
    DBT_TARGET = "prod"
    MODEL_SELECTOR = "sfa"

    dbt_deps = BashOperator(
        task_id='dbt_deps',
        bash_command=f'cd {DBT_DIR} && dbt deps --profiles-dir {DBT_PROFILES_DIR}',
    )

    dbt_run = BashOperator(
        task_id='dbt_run_test_models',
        bash_command=(
            f'cd {DBT_DIR} && '
            f'dbt run --profiles-dir {DBT_PROFILES_DIR} '
            f'--target {DBT_TARGET} --select {MODEL_SELECTOR}'
        ),
    )

    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command=(
            f'cd {DBT_DIR} && '
            f'dbt test --profiles-dir {DBT_PROFILES_DIR} '
            f'--target {DBT_TARGET} --select {MODEL_SELECTOR}'
        ),
    )

    dbt_docs_generate = BashOperator(
        task_id='dbt_docs_generate',
        bash_command=(
            f'cd {DBT_DIR} && '
            f'dbt docs generate --profiles-dir {DBT_PROFILES_DIR} '
            f'--target {DBT_TARGET}'
        ),
    )

    # Task flow
    dbt_deps >> dbt_run >> dbt_test >> dbt_docs_generate
