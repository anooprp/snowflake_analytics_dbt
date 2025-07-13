from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'anoop',
    'start_date': datetime(2025, 7, 10),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='snowflake_table_cleanup',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=['cleanup', 'snowflake'],
) as dag:

    # print_conn_env = BashOperator(
    #     task_id='print_snowflake_conn',
    #     bash_command='echo "SNOWFLAKE_CONN: $AIRFLOW_CONN_SNOWFLAKE_CLEANUP"'
    # )

    truncate_prod_orders = SQLExecuteQueryOperator(
        task_id='truncate_prod_orders',
        conn_id='snowflake_cleanup',
        sql='TRUNCATE TABLE core.customer_order_summary;',
        hook_params={
            "account": "wf35605.europe-west3.gcp",
            "warehouse": "COMPUTE_WH",
            "database": "DBT_ANALYTICS",
            "schema": "CORE",
            "role": "ACCOUNTADMIN",
        }
    )

    truncate_prod_customers = SQLExecuteQueryOperator(
        task_id='truncate_prod_customers',
        conn_id='snowflake_cleanup',
        sql='TRUNCATE TABLE core.revenue_per_customer;',
            hook_params={
                "account": "wf35605.europe-west3.gcp",
                "warehouse": "COMPUTE_WH",
                "database": "DBT_ANALYTICS",
                "schema": "CORE",
                "role": "ACCOUNTADMIN",
            }
    )

    truncate_dev_orders = SQLExecuteQueryOperator(
        task_id='truncate_dev_orders',
        conn_id='snowflake_dev_cleanup',
        sql='TRUNCATE TABLE core.test_customer_order_summary;',
        hook_params={
            "account": "iv50318.europe-west3.gcp",
            "warehouse": "COMPUTE_WH",
            "database": "TEST_DB",
            "schema": "CORE",
            "role": "ACCOUNTADMIN",
        }
    )

    truncate_dev_customers = SQLExecuteQueryOperator(
        task_id='truncate_dev_customers',
        conn_id='snowflake_dev_cleanup',
        sql='TRUNCATE TABLE core.test_revenue_per_customer;',
            hook_params={
                "account": "iv50318.europe-west3.gcp",
                "warehouse": "COMPUTE_WH",
                "database": "TEST_DB",
                "schema": "CORE",
                "role": "ACCOUNTADMIN",
            }
    )

    truncate_prod_orders >> truncate_prod_customers
    truncate_dev_orders >> truncate_dev_customers
