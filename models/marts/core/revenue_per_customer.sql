{{ config(materialized='table') }}
SELECT
    c.customer_id,
    SUM(l.net_revenue) AS total_revenue
FROM {{ ref('stg_customer') }} c
JOIN {{ ref('stg_orders') }} o ON c.customer_id = o.customer_id
JOIN {{ ref('int_orders_lineitems') }} l ON o.order_id = l.order_id
GROUP BY c.customer_id
