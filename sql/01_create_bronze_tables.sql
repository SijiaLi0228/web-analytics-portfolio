-- Databricks SQL
-- Create bronze tables from synthetic CSV files after uploading them to Databricks.
-- If using the UI, upload the CSV files first and create tables with the same names.

create or replace table bronze_web_events (
  event_id string,
  session_id string,
  user_id string,
  event_time timestamp,
  channel string,
  device string,
  country string,
  event_name string,
  product_id string,
  order_id string,
  revenue double
);

create or replace table bronze_products (
  product_id string,
  product_name string,
  category string,
  list_price double
);

-- Alternative quick-start: create sample rows directly in Databricks.

create or replace table bronze_web_events_sample as
select * from values
  ('e001', 's001', 'u001', timestamp('2026-05-01 09:00:00'), 'organic', 'desktop', 'DK', 'view_item', 'p001', null, null),
  ('e002', 's001', 'u001', timestamp('2026-05-01 09:02:00'), 'organic', 'desktop', 'DK', 'add_to_cart', 'p001', null, null),
  ('e003', 's001', 'u001', timestamp('2026-05-01 09:04:00'), 'organic', 'desktop', 'DK', 'begin_checkout', 'p001', null, null),
  ('e004', 's001', 'u001', timestamp('2026-05-01 09:07:00'), 'organic', 'desktop', 'DK', 'purchase', 'p001', 'o001', 299.00),
  ('e005', 's002', 'u002', timestamp('2026-05-01 10:00:00'), 'paid', 'mobile', 'DK', 'view_item', 'p002', null, null),
  ('e006', 's002', 'u002', timestamp('2026-05-01 10:03:00'), 'paid', 'mobile', 'DK', 'add_to_cart', 'p002', null, null),
  ('e007', 's003', 'u003', timestamp('2026-05-01 11:00:00'), 'direct', 'mobile', 'SE', 'view_item', 'p003', null, null),
  ('e008', 's004', 'u004', timestamp('2026-05-02 12:00:00'), 'organic', 'desktop', 'DK', 'view_item', 'p001', null, null),
  ('e009', 's004', 'u004', timestamp('2026-05-02 12:03:00'), 'organic', 'desktop', 'DK', 'add_to_cart', 'p001', null, null),
  ('e010', 's005', 'u005', timestamp('2026-05-02 13:00:00'), 'paid', 'desktop', 'NO', 'view_item', 'p004', null, null),
  ('e011', 's005', 'u005', timestamp('2026-05-02 13:06:00'), 'paid', 'desktop', 'NO', 'begin_checkout', 'p004', null, null),
  ('e012', 's006', 'u006', timestamp('2026-05-02 14:00:00'), 'referral', 'mobile', 'DK', 'view_item', 'p002', null, null),
  ('e013', 's006', 'u006', timestamp('2026-05-02 14:04:00'), 'referral', 'mobile', 'DK', 'add_to_cart', 'p002', null, null),
  ('e014', 's006', 'u006', timestamp('2026-05-02 14:08:00'), 'referral', 'mobile', 'DK', 'begin_checkout', 'p002', null, null),
  ('e015', 's006', 'u006', timestamp('2026-05-02 14:12:00'), 'referral', 'mobile', 'DK', 'purchase', 'p002', 'o002', 499.00),
  ('e016', 's007', 'u007', timestamp('2026-05-03 09:30:00'), 'organic', 'mobile', 'DK', 'view_item', 'p003', null, null),
  ('e017', 's007', 'u007', timestamp('2026-05-03 09:34:00'), 'organic', 'mobile', 'DK', 'add_to_cart', 'p003', null, null),
  ('e018', 's008', 'u008', timestamp('2026-05-03 10:15:00'), 'paid', 'mobile', 'DK', 'view_item', 'p001', null, null),
  ('e019', 's009', 'u009', timestamp('2026-05-03 10:45:00'), 'email', 'desktop', 'DE', 'view_item', 'p004', null, null),
  ('e020', 's009', 'u009', timestamp('2026-05-03 10:48:00'), 'email', 'desktop', 'DE', 'add_to_cart', 'p004', null, null),
  ('e021', 's009', 'u009', timestamp('2026-05-03 10:55:00'), 'email', 'desktop', 'DE', 'purchase', 'p004', 'o003', 599.00)
as t(event_id, session_id, user_id, event_time, channel, device, country, event_name, product_id, order_id, revenue);

create or replace table bronze_products_sample as
select * from values
  ('p001', 'Starter Kit', 'Education', 299.00),
  ('p002', 'Advanced Kit', 'Education', 499.00),
  ('p003', 'Accessory Pack', 'Education', 199.00),
  ('p004', 'Classroom Bundle', 'Education', 599.00)
as t(product_id, product_name, category, list_price);
