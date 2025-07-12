SELECT
    customer_id,
    COUNT(order_id) AS total_orders,
    coalesce(sum(o_totalprice), 0) as total_spent
FROM {{ ref('stg_orders') }}
GROUP BY customer_id
