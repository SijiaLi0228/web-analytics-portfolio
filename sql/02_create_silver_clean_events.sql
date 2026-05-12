-- Silver layer: clean and standardize public clickstream events.
-- For full-data runs, replace bronze_ecommerce_events_sample with bronze_ecommerce_events.

create or replace table silver_clean_events as
select
  sha2(concat_ws('|',
    cast(event_time as string),
    coalesce(cast(user_id as string), ''),
    coalesce(user_session, ''),
    coalesce(cast(product_id as string), ''),
    coalesce(event_type, '')
  ), 256) as event_id,
  event_time,
  date(event_time) as event_date,
  date_trunc('month', event_time) as event_month,
  lower(trim(event_type)) as source_event_type,
  case lower(trim(event_type))
    when 'view' then 'view_item'
    when 'cart' then 'add_to_cart'
    when 'remove_from_cart' then 'remove_from_cart'
    when 'purchase' then 'purchase'
    else 'unknown'
  end as event_name,
  cast(product_id as string) as product_id,
  cast(category_id as string) as category_id,
  lower(nullif(trim(category_code), '')) as category_code,
  lower(nullif(trim(brand), '')) as brand,
  cast(price as double) as price,
  cast(user_id as string) as user_id,
  user_session
from bronze_ecommerce_events_sample
where event_time is not null
  and user_id is not null
  and user_session is not null;
