-- Gold layer: product-level performance metrics.

create or replace table gold_product_performance as
select
  product_id,
  coalesce(category_code, 'unknown') as category_code,
  coalesce(brand, 'unknown') as brand,
  count(*) as event_rows,
  count(distinct user_id) as users,
  count(distinct case when event_name = 'view_item' then user_session end) as view_sessions,
  count(distinct case when event_name = 'add_to_cart' then user_session end) as cart_sessions,
  count(distinct case when event_name = 'remove_from_cart' then user_session end) as remove_from_cart_sessions,
  count(distinct case when event_name = 'purchase' then user_session end) as purchase_sessions,
  sum(case when event_name = 'purchase' then coalesce(price, 0) else 0 end) as revenue,
  avg(price) as avg_observed_price,
  count(distinct case when event_name = 'purchase' then user_session end)
    / nullif(count(distinct case when event_name = 'view_item' then user_session end), 0) as view_to_purchase_rate
from silver_clean_events
where product_id is not null
group by product_id, coalesce(category_code, 'unknown'), coalesce(brand, 'unknown')
order by revenue desc;
