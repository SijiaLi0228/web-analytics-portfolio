-- Duplicate event IDs
select event_id, count(*) as row_count
from bronze_web_events_sample
group by event_id
having count(*) > 1;

-- Missing product IDs on product-related events
select *
from silver_clean_events
where event_name in ('view_item', 'add_to_cart', 'begin_checkout', 'purchase')
  and product_id is null;

-- Purchase events without order ID
select *
from silver_clean_events
where event_name = 'purchase'
  and order_id is null;

-- Negative revenue
select *
from silver_clean_events
where revenue < 0;

-- Event order check: sessions with purchase but no add_to_cart
with session_flags as (
  select
    session_id,
    max(case when event_name = 'add_to_cart' then 1 else 0 end) as has_add_to_cart,
    max(case when event_name = 'purchase' then 1 else 0 end) as has_purchase
  from silver_clean_events
  group by session_id
)
select *
from session_flags
where has_purchase = 1
  and has_add_to_cart = 0;
