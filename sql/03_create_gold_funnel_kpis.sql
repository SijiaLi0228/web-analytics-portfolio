-- Create daily funnel KPIs by channel and device.

create or replace table gold_daily_funnel_kpis as
with session_flags as (
  select
    event_date,
    channel,
    device,
    session_id,
    max(case when event_name = 'view_item' then 1 else 0 end) as viewed_product,
    max(case when event_name = 'add_to_cart' then 1 else 0 end) as added_to_cart,
    max(case when event_name = 'begin_checkout' then 1 else 0 end) as began_checkout,
    max(case when event_name = 'purchase' then 1 else 0 end) as purchased,
    sum(coalesce(revenue, 0)) as revenue
  from silver_clean_events
  group by event_date, channel, device, session_id
)
select
  event_date,
  channel,
  device,
  count(distinct session_id) as sessions,
  sum(viewed_product) as product_view_sessions,
  sum(added_to_cart) as add_to_cart_sessions,
  sum(began_checkout) as checkout_sessions,
  sum(purchased) as purchase_sessions,
  sum(revenue) as revenue,
  sum(added_to_cart) / nullif(sum(viewed_product), 0) as view_to_cart_rate,
  sum(purchased) / nullif(sum(added_to_cart), 0) as cart_to_purchase_rate,
  sum(purchased) / nullif(count(distinct session_id), 0) as session_conversion_rate
from session_flags
group by event_date, channel, device
order by event_date, channel, device;
