-- Create product-level performance metrics.

create or replace table gold_product_performance as
select
  e.product_id,
  p.product_name,
  p.category,
  count(distinct case when e.event_name = 'view_item' then e.session_id end) as view_sessions,
  count(distinct case when e.event_name = 'add_to_cart' then e.session_id end) as add_to_cart_sessions,
  count(distinct case when e.event_name = 'purchase' then e.session_id end) as purchase_sessions,
  sum(coalesce(e.revenue, 0)) as revenue,
  count(distinct case when e.event_name = 'purchase' then e.session_id end)
    / nullif(count(distinct case when e.event_name = 'view_item' then e.session_id end), 0) as view_to_purchase_rate
from silver_clean_events e
left join bronze_products_sample p
  on e.product_id = p.product_id
group by e.product_id, p.product_name, p.category
order by revenue desc;
