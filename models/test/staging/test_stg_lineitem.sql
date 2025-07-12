SELECT
    l_orderkey     AS order_id,
    l_quantity,
    l_extendedprice,
    l_discount,
    l_shipdate
FROM {{ ref('test_lineitem') }}
