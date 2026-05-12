-- Data quality checks for public e-commerce clickstream events.

-- Missing session IDs
select count(*) as missing_session_rows
from bronze_ecommerce_events_sample
where user_session is null;

-- Unknown event types after normalization
select source_event_type, count(*) as rows
from silver_clean_events
where event_name = 'unknown'
group by source_event_type
order by rows desc;

-- Missing product IDs on product-related events
select event_name, count(*) as rows
from silver_clean_events
where event_name in ('view_item', 'add_to_cart', 'remove_from_cart', 'purchase')
  and product_id is null
group by event_name;

-- Negative prices
select *
from silver_clean_events
where price < 0;

-- Duplicate generated event IDs
select event_id, count(*) as row_count
from silver_clean_events
group by event_id
having count(*) > 1;

-- Sessions with purchase but no earlier cart event.
-- This is not automatically wrong, but it should be reviewed because source
-- tracking may miss intermediate steps.
with session_flags as (
  select
    user_session,
    max(case when event_name = 'view_item' then 1 else 0 end) as has_view,
    max(case when event_name = 'add_to_cart' then 1 else 0 end) as has_cart,
    max(case when event_name = 'purchase' then 1 else 0 end) as has_purchase
  from silver_clean_events
  group by user_session
)
select *
from session_flags
where has_purchase = 1
  and has_cart = 0;
