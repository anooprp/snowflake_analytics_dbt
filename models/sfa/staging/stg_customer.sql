SELECT
    c_custkey      AS customer_id,
    c_name         AS customer_name,
    c_nationkey,
    c_mktsegment
FROM {{ ref('customer') }}
