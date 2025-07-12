{{ config(materialized='table') }}
SELECT
    c.customer_id,
    SUM(l.net_revenue) AS total_revenue
FROM {{ ref('test_stg_customer') }} c
JOIN {{ ref('test_stg_orders') }} o ON c.customer_id = o.customer_id
JOIN {{ ref('test_int_orders_lineitems') }} l ON o.order_id = l.order_id
GROUP BY c.customer_id
