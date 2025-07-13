{% test row_count(model, min_rows) %}

    with row_count as (
        select count(*) as num_rows from {{ model }}
    )

    select *
    from row_count
    where num_rows < {{ min_rows }}

{% endtest %}