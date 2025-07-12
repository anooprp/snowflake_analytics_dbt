{{ config(materialized='table') }}
SELECT
    c.customer_id,
    c.customer_name,
    c.c_mktsegment,
    COALESCE(o.total_orders, 0) AS total_orders,
    COALESCE(o.total_spent, 0) AS total_spent
FROM {{ ref('test_stg_customer') }} c
LEFT JOIN {{ ref('test_int_customer_orders') }} o
  ON c.customer_id = o.customer_id
