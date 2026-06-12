-- Gold layer: user cohort and retention metrics.
-- Purpose:
--   Show whether users return after their first observed activity month.
--   This is useful for separating one-time browsing from repeat engagement.
--
-- Notes:
--   The public dataset contains user IDs and event dates, but it does not
--   include marketing consent, acquisition source, geography, or loyalty data.
--   Cohorts are therefore based on first observed activity in the dataset.

create or replace table gold_user_monthly_retention as
with user_first_activity as (
  select
    user_id,
    date_trunc('month', min(event_date)) as cohort_month
  from silver_clean_events
  where user_id is not null
  group by user_id
),
user_month_activity as (
  select
    user_id,
    date_trunc('month', event_date) as activity_month,
    count(distinct user_session) as active_sessions,
    count(distinct case when event_name = 'purchase' then user_session end) as purchase_sessions,
    sum(case when event_name = 'purchase' then coalesce(price, 0) else 0 end) as revenue
  from silver_clean_events
  where user_id is not null
  group by user_id, date_trunc('month', event_date)
),
cohort_activity as (
  select
    first_activity.cohort_month,
    month(activity.activity_month) - month(first_activity.cohort_month)
      + 12 * (year(activity.activity_month) - year(first_activity.cohort_month)) as months_since_cohort,
    activity.user_id,
    activity.active_sessions,
    activity.purchase_sessions,
    activity.revenue
  from user_month_activity activity
  join user_first_activity first_activity
    on activity.user_id = first_activity.user_id
),
cohort_sizes as (
  select
    cohort_month,
    count(distinct user_id) as cohort_users
  from user_first_activity
  group by cohort_month
)
select
  cohort_activity.cohort_month,
  cohort_activity.months_since_cohort,
  cohort_sizes.cohort_users,
  count(distinct cohort_activity.user_id) as active_users,
  count(distinct case when cohort_activity.purchase_sessions > 0 then cohort_activity.user_id end) as purchasing_users,
  sum(cohort_activity.active_sessions) as active_sessions,
  sum(cohort_activity.purchase_sessions) as purchase_sessions,
  sum(cohort_activity.revenue) as revenue,
  count(distinct cohort_activity.user_id) / nullif(cohort_sizes.cohort_users, 0) as retention_rate,
  count(distinct case when cohort_activity.purchase_sessions > 0 then cohort_activity.user_id end)
    / nullif(cohort_sizes.cohort_users, 0) as purchasing_user_rate
from cohort_activity
join cohort_sizes
  on cohort_activity.cohort_month = cohort_sizes.cohort_month
where cohort_activity.months_since_cohort >= 0
group by
  cohort_activity.cohort_month,
  cohort_activity.months_since_cohort,
  cohort_sizes.cohort_users
order by cohort_month, months_since_cohort;
