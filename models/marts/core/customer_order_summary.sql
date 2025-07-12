{{ config(materialized='table') }}
SELECT
    c.customer_id,
    c.customer_name,
    c.c_mktsegment,
    o.total_orders,
    o.total_spent
FROM {{ ref('stg_customer') }} c
LEFT JOIN {{ ref('int_customer_orders') }} o
  ON c.customer_id = o.customer_id
