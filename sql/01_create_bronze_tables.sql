-- Databricks SQL
-- Bronze layer for the public eCommerce Behavior Data from Multi-Category Store dataset.
-- The raw dataset is large, so this repository documents the schema and provides
-- SQL that can be run after uploading a monthly partition or sample file to Databricks.

create or replace table bronze_ecommerce_events (
  event_time timestamp,
  event_type string,
  product_id bigint,
  category_id bigint,
  category_code string,
  brand string,
  price double,
  user_id bigint,
  user_session string
);

-- Example loading pattern after uploading a CSV file to a Databricks volume.
-- Replace the path with the location of the downloaded public dataset file.
--
-- copy into bronze_ecommerce_events
-- from '/Volumes/main/default/ecommerce_clickstream/ecommerce-behavior.csv'
-- fileformat = csv
-- format_options ('header' = 'true', 'inferSchema' = 'false');

-- Lightweight review sample. This is only for checking that the downstream SQL
-- can be read and executed without downloading the full source file.

create or replace table bronze_ecommerce_events_sample as
select * from values
  (timestamp('2019-10-01 00:00:01'), 'view',             100001, 2053013555631882655, 'electronics.smartphone', 'samsung',  329.90, 501001, 's001'),
  (timestamp('2019-10-01 00:01:20'), 'cart',             100001, 2053013555631882655, 'electronics.smartphone', 'samsung',  329.90, 501001, 's001'),
  (timestamp('2019-10-01 00:04:05'), 'purchase',         100001, 2053013555631882655, 'electronics.smartphone', 'samsung',  329.90, 501001, 's001'),
  (timestamp('2019-10-01 00:12:10'), 'view',             100002, 2053013555631882655, 'electronics.smartphone', 'apple',    949.00, 501002, 's002'),
  (timestamp('2019-10-01 00:14:18'), 'view',             100003, 2053013565983425517, 'electronics.audio',      'sony',     119.00, 501003, 's003'),
  (timestamp('2019-10-01 00:16:23'), 'cart',             100003, 2053013565983425517, 'electronics.audio',      'sony',     119.00, 501003, 's003'),
  (timestamp('2019-10-01 00:18:07'), 'remove_from_cart', 100003, 2053013565983425517, 'electronics.audio',      'sony',     119.00, 501003, 's003'),
  (timestamp('2019-10-02 09:20:10'), 'view',             100004, 2053013553375346967, 'appliances.kitchen',     'bosch',    499.00, 501004, 's004'),
  (timestamp('2019-10-02 09:24:45'), 'cart',             100004, 2053013553375346967, 'appliances.kitchen',     'bosch',    499.00, 501004, 's004'),
  (timestamp('2019-10-03 11:10:02'), 'view',             100005, 2053013558920217191, 'computers.notebook',     'lenovo',   799.00, 501005, 's005'),
  (timestamp('2019-10-03 11:18:30'), 'purchase',         100005, 2053013558920217191, 'computers.notebook',     'lenovo',   799.00, 501005, 's005')
as t(event_time, event_type, product_id, category_id, category_code, brand, price, user_id, user_session);
