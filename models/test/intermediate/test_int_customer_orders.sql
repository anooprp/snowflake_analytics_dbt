SELECT
    customer_id,
    COALESCE(COUNT(order_id), 0) AS total_orders,
    coalesce(sum(o_totalprice), 0) as total_spent
FROM {{ ref('test_stg_orders') }}
GROUP BY customer_id
