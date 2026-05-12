-- Gold layer: daily customer journey KPIs by category.
-- The source dataset does not include traffic source or device, so this table
-- focuses on product/category journey behavior rather than channel attribution.

create or replace table gold_daily_journey_kpis as
with session_category_flags as (
  select
    event_date,
    category_code,
    user_session,
    max(user_id) as user_id,
    max(case when event_name = 'view_item' then 1 else 0 end) as viewed_product,
    max(case when event_name = 'add_to_cart' then 1 else 0 end) as added_to_cart,
    max(case when event_name = 'remove_from_cart' then 1 else 0 end) as removed_from_cart,
    max(case when event_name = 'purchase' then 1 else 0 end) as purchased,
    sum(case when event_name = 'purchase' then coalesce(price, 0) else 0 end) as revenue
  from silver_clean_events
  where event_name in ('view_item', 'add_to_cart', 'remove_from_cart', 'purchase')
  group by event_date, category_code, user_session
)
select
  event_date,
  coalesce(category_code, 'unknown') as category_code,
  count(distinct user_session) as sessions,
  count(distinct user_id) as users,
  sum(viewed_product) as view_sessions,
  sum(added_to_cart) as cart_sessions,
  sum(removed_from_cart) as remove_from_cart_sessions,
  sum(purchased) as purchase_sessions,
  sum(revenue) as revenue,
  sum(added_to_cart) / nullif(sum(viewed_product), 0) as view_to_cart_rate,
  sum(purchased) / nullif(sum(added_to_cart), 0) as cart_to_purchase_rate,
  sum(purchased) / nullif(count(distinct user_session), 0) as session_conversion_rate
from session_category_flags
group by event_date, coalesce(category_code, 'unknown')
order by event_date, category_code;
