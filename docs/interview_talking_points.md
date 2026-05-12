# Interview Talking Points

## 30-Second Project Summary

This is a synthetic e-commerce web analytics project that simulates the workflow from web tracking to business reporting. I define core funnel events, clean and validate the event data, build gold tables for daily funnel and product performance, and design a Power BI dashboard structure for stakeholder reporting.

## Why I Built It

I built this project to practice the type of workflow used in web, product, and commercial analytics roles: turning tracking data into trusted business metrics.

The focus is not only writing SQL. It is also about defining reliable events, checking data quality, creating clear KPI definitions, and making outputs usable for business teams.

## What the Pipeline Shows

```text
Matomo-style tracking plan
  -> bronze_web_events_sample
  -> silver_clean_events
  -> gold_daily_funnel_kpis
  -> gold_product_performance
  -> Power BI dashboard design
```

- Tracking plan: defines events, required properties, and QA expectations
- Bronze: raw web event data
- Silver: cleaned and standardized event records
- Gold: KPI tables that can support dashboards and decisions
- Dashboard: reporting layout for stakeholder meetings

## Business Questions Answered

- Which channels and devices produce the strongest conversion?
- Where does the customer journey drop off?
- Which products receive attention but do not convert?
- Can the tracking data be trusted before making recommendations?
- Which KPI should be monitored weekly?

## Data Quality Mindset

Before interpreting funnel metrics, I check whether the data is reliable:

- duplicate event IDs
- missing session IDs
- missing product IDs on product events
- purchase events without order IDs
- negative revenue
- sessions with purchase but no add-to-cart event

This matters because a tracking issue can look like a business problem if the data is not validated first.

## How I Would Explain the SQL

I would explain that the funnel logic is built at session level first.

Instead of counting every event row directly, I first flag whether a session had each key journey step: product view, add to cart, checkout, and purchase. Then I aggregate those session-level flags by date, channel, and device.

This avoids overcounting users who trigger the same event multiple times in one session.

## How I Would Explain the Dashboard

I would structure the dashboard around stakeholder questions:

1. Executive Overview: Are traffic, conversion, and revenue moving in the right direction?
2. E-commerce Funnel: Where do users drop off?
3. Product Performance: Which products attract interest but fail to convert?
4. Channel and Device Analysis: Which traffic sources produce useful demand?

## If Asked About Matomo

I would say:

> I have practiced Matomo tracking setup and would approach it by first defining the key journey events and required properties, then validating that events fire correctly before using them in dashboards. For me, the important part is not only installing a tag, but making sure the tracking logic supports reliable business questions.

## If Asked About Databricks

I would say:

> My current Databricks practice focuses on the analytics workflow: creating tables, cleaning raw events, building gold KPI tables, and preparing outputs for reporting. I am not positioning myself as a data engineer, but I can work with SQL-based analytics tables and understand the bronze, silver, and gold structure.

## If Asked About Power BI

I would say:

> I would connect the gold KPI tables to Power BI, define measures such as conversion rate and revenue per session, and design pages around stakeholder decisions rather than only chart types.

## How I Would Extend It

If this were a real production project, I would add:

- Matomo or GA event exports
- campaign and paid media fields
- customer segment fields
- promotion and discount data
- Power BI screenshots or a published dashboard
- automated data quality checks
- weekly KPI monitoring and alerts

## Relevance to Analyst Roles

This project is relevant to roles involving:

- web analytics
- product analytics
- e-commerce analytics
- SQL/Databricks workflows
- Power BI reporting
- stakeholder-facing KPI design
- marketing and funnel performance analysis
