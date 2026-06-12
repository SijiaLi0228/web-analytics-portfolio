-- Gold layer: product friction scoring.
-- Purpose:
--   Prioritize products that attract attention but do not convert well.
--   This creates a review list for product, merchandising, pricing, content,
--   or tracking follow-up.
--
-- Interpretation:
--   A high friction score does not prove the root cause. It identifies products
--   where the gap between attention and purchase behavior deserves inspection.

create or replace table gold_product_friction_scores as
with product_base as (
  select
    product_id,
    category_code,
    brand,
    users,
    view_sessions,
    cart_sessions,
    remove_from_cart_sessions,
    purchase_sessions,
    revenue,
    avg_observed_price,
    cart_sessions / nullif(view_sessions, 0) as view_to_cart_rate,
    purchase_sessions / nullif(cart_sessions, 0) as cart_to_purchase_rate,
    purchase_sessions / nullif(view_sessions, 0) as view_to_purchase_rate,
    remove_from_cart_sessions / nullif(cart_sessions, 0) as remove_to_cart_rate
  from gold_product_performance
  where view_sessions >= 20
),
scored as (
  select
    *,
    percent_rank() over (order by view_sessions) as attention_percentile,
    1 - percent_rank() over (order by coalesce(view_to_cart_rate, 0)) as weak_view_to_cart_percentile,
    1 - percent_rank() over (order by coalesce(cart_to_purchase_rate, 0)) as weak_cart_to_purchase_percentile,
    percent_rank() over (order by coalesce(remove_to_cart_rate, 0)) as remove_pressure_percentile
  from product_base
)
select
  product_id,
  category_code,
  brand,
  users,
  view_sessions,
  cart_sessions,
  remove_from_cart_sessions,
  purchase_sessions,
  revenue,
  avg_observed_price,
  view_to_cart_rate,
  cart_to_purchase_rate,
  view_to_purchase_rate,
  remove_to_cart_rate,
  round(
    100 * (
      0.35 * attention_percentile
      + 0.25 * weak_view_to_cart_percentile
      + 0.25 * weak_cart_to_purchase_percentile
      + 0.15 * remove_pressure_percentile
    ),
    1
  ) as friction_score,
  case
    when coalesce(view_to_cart_rate, 0) < 0.05 then 'Product page relevance/content check'
    when coalesce(cart_to_purchase_rate, 0) < 0.20 then 'Checkout, delivery, price, or availability check'
    when coalesce(remove_to_cart_rate, 0) > 0.40 then 'Cart reconsideration or stock/price expectation check'
    else 'Monitor'
  end as suggested_investigation
from scored
order by friction_score desc, view_sessions desc;
