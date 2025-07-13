from snowflake.snowpark import functions as F

def model(dbt, session):
    dbt.config(
        materialized="table",
        language="python"
    )

    df = dbt.ref("test_stg_orders")

    result = (
        df.group_by("customer_id")
          .agg(
              F.coalesce(F.count(df["order_id"]), F.lit(0)).alias("total_orders"),
              F.coalesce(F.sum(df["o_totalprice"]), F.lit(0)).alias("total_spent")
          )
    )

    return result
