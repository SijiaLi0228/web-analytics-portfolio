-- Create a cleaned event table.

create or replace table silver_clean_events as
select
  event_id,
  session_id,
  user_id,
  event_time,
  date(event_time) as event_date,
  lower(trim(channel)) as channel,
  lower(trim(device)) as device,
  upper(trim(country)) as country,
  lower(trim(event_name)) as event_name,
  product_id,
  order_id,
  cast(revenue as double) as revenue
from bronze_web_events_sample
where event_id is not null
  and session_id is not null
  and event_time is not null;
