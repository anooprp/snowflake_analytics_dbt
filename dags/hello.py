from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

with DAG(
    dag_id='hello_log_test',
    schedule_interval=timedelta(days=1),  # corrected key from `schedule` to `schedule_interval`
    start_date=datetime(2021, 1, 1),
    catchup=False,
) as dag:
    hello = BashOperator(
        task_id='say_hello',
        bash_command='echo "Hello from Airflow!"'
    )

    world = BashOperator(
        task_id='say_world',
        bash_command='echo "World from Airflow!"'
    )

    # Define execution order
    hello >> world
