{% test test_revenue_customer_relationship(model) %}
select customer_id
from {{ ref('revenue_per_customer') }}
where customer_id not in (
    select customer_id from {{ ref('customer_order_summary') }}
)
{% endtest %}