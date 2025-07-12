SELECT
    o_orderkey     AS order_id,
    o_custkey      AS customer_id,
    o_orderstatus,
    o_totalprice,
    o_orderdate
FROM {{ ref('orders') }}
