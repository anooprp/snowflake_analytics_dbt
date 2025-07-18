SELECT
    order_id,
    SUM(l_extendedprice * (1 - l_discount)) AS net_revenue
FROM {{ ref('stg_lineitem') }}
GROUP BY order_id
