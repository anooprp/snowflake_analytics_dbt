from snowflake.snowpark import functions as F

def model(dbt, session):
    dbt.config(
        materialized="table",
        language="python"
    )

    # Correct: Use dbt.ref to get string table name
    df = dbt.ref("test_stg_lineitem", database="TEST_DB", schema="STG")

    result = (
        df.group_by("order_id")
        .agg(
            F.sum(df["l_extendedprice"] * (1 - df["l_discount"])).alias("net_revenue")
        )
    )

    return result