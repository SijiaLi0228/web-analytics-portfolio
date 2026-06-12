-- Gold layer: weekly KPI monitoring by category.
-- Purpose:
--   Create a recurring monitoring table that highlights categories where
--   conversion or revenue moves unusually compared with recent history.
--
-- This is not a causal model. It is an analyst monitoring layer that supports
-- better stakeholder review: what changed, where, and whether it needs action.

create or replace table gold_weekly_category_monitoring as
with weekly_kpis as (
  select
    date_trunc('week', event_date) as week_start,
    category_code,
    sum(sessions) as sessions,
    sum(view_sessions) as view_sessions,
    sum(cart_sessions) as cart_sessions,
    sum(remove_from_cart_sessions) as remove_from_cart_sessions,
    sum(purchase_sessions) as purchase_sessions,
    sum(revenue) as revenue,
    sum(cart_sessions) / nullif(sum(view_sessions), 0) as view_to_cart_rate,
    sum(purchase_sessions) / nullif(sum(cart_sessions), 0) as cart_to_purchase_rate,
    sum(purchase_sessions) / nullif(sum(sessions), 0) as session_conversion_rate
  from gold_daily_journey_kpis
  group by date_trunc('week', event_date), category_code
),
monitoring as (
  select
    *,
    avg(session_conversion_rate) over (
      partition by category_code
      order by week_start
      rows between 4 preceding and 1 preceding
    ) as previous_4w_conversion_avg,
    stddev_samp(session_conversion_rate) over (
      partition by category_code
      order by week_start
      rows between 4 preceding and 1 preceding
    ) as previous_4w_conversion_stddev,
    avg(revenue) over (
      partition by category_code
      order by week_start
      rows between 4 preceding and 1 preceding
    ) as previous_4w_revenue_avg
  from weekly_kpis
)
select
  week_start,
  category_code,
  sessions,
  view_sessions,
  cart_sessions,
  remove_from_cart_sessions,
  purchase_sessions,
  revenue,
  view_to_cart_rate,
  cart_to_purchase_rate,
  session_conversion_rate,
  previous_4w_conversion_avg,
  previous_4w_revenue_avg,
  (session_conversion_rate - previous_4w_conversion_avg)
    / nullif(previous_4w_conversion_stddev, 0) as conversion_z_score,
  case
    when previous_4w_conversion_avg is null then 'New / insufficient history'
    when (session_conversion_rate - previous_4w_conversion_avg)
      / nullif(previous_4w_conversion_stddev, 0) <= -2 then 'Conversion drop to investigate'
    when revenue < previous_4w_revenue_avg * 0.75 then 'Revenue drop to investigate'
    when session_conversion_rate > previous_4w_conversion_avg * 1.25 then 'Positive conversion movement'
    else 'Within expected range'
  end as monitoring_flag
from monitoring
order by week_start desc, category_code;
