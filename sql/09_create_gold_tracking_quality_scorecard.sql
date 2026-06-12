-- Gold layer: tracking quality scorecard.
-- Purpose:
--   Turn raw data quality checks into a stakeholder-readable scorecard.
--   This helps decide whether dashboard movement is ready for interpretation
--   or whether the tracking/data layer needs review first.

create or replace table gold_tracking_quality_scorecard as
with total_rows as (
  select count(*) as row_count
  from silver_clean_events
),
qa_checks as (
  select
    'missing_session_id' as check_name,
    'critical' as severity,
    count(*) as issue_rows,
    'Journey funnel cannot connect events into sessions' as business_risk,
    'Review tracking payload and exclude invalid rows from session KPIs' as recommended_action
  from silver_clean_events
  where user_session is null

  union all

  select
    'unknown_event_type' as check_name,
    'high' as severity,
    count(*) as issue_rows,
    'Event taxonomy is inconsistent, which can misstate KPI definitions' as business_risk,
    'Map expected source events and flag unexpected values for review' as recommended_action
  from silver_clean_events
  where event_name = 'unknown'

  union all

  select
    'missing_product_id_on_product_event' as check_name,
    'high' as severity,
    count(*) as issue_rows,
    'Product and category reporting may be incomplete' as business_risk,
    'Validate product payloads in tracking or source export' as recommended_action
  from silver_clean_events
  where event_name in ('view_item', 'add_to_cart', 'remove_from_cart', 'purchase')
    and product_id is null

  union all

  select
    'negative_price' as check_name,
    'medium' as severity,
    count(*) as issue_rows,
    'Revenue and average price metrics may be misleading' as business_risk,
    'Investigate source rows before using revenue metrics' as recommended_action
  from silver_clean_events
  where price < 0

  union all

  select
    'purchase_without_cart_event' as check_name,
    'medium' as severity,
    count(*) as issue_rows,
    'Could indicate missing cart tracking or a valid direct purchase path' as business_risk,
    'Compare by category/product and validate event sequence' as recommended_action
  from (
    select
      user_session,
      max(case when event_name = 'add_to_cart' then 1 else 0 end) as has_cart,
      max(case when event_name = 'purchase' then 1 else 0 end) as has_purchase
    from silver_clean_events
    group by user_session
  ) session_sequence
  where has_purchase = 1
    and has_cart = 0
)
select
  qa_checks.check_name,
  qa_checks.severity,
  qa_checks.issue_rows,
  total_rows.row_count as total_rows,
  qa_checks.issue_rows / nullif(total_rows.row_count, 0) as issue_rate,
  qa_checks.business_risk,
  qa_checks.recommended_action,
  case
    when qa_checks.severity = 'critical' and qa_checks.issue_rows > 0 then 'Do not publish affected KPI without caveat'
    when qa_checks.severity = 'high' and qa_checks.issue_rows > 0 then 'Publish only with validation note'
    when qa_checks.issue_rows > 0 then 'Monitor and explain limitation'
    else 'Passed'
  end as dashboard_readiness
from qa_checks
cross join total_rows
order by
  case qa_checks.severity
    when 'critical' then 1
    when 'high' then 2
    when 'medium' then 3
    else 4
  end,
  issue_rows desc;
