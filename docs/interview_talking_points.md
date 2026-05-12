# Interview Talking Points

## 30-Second Project Summary

This is a synthetic e-commerce web analytics project that simulates the workflow from raw web events to business-ready KPI tables. I defined core funnel events, cleaned and validated the event data, built gold tables for daily funnel and product performance, and designed a Power BI dashboard structure for stakeholder reporting.

## Why I Built It

I built this project to practice the type of workflow used in web and product analytics roles: turning tracking data into trusted business metrics. The focus is not only writing SQL, but also defining reliable events, checking data quality, and making the outputs usable for business teams.

## What the Pipeline Shows

```text
bronze_web_events_sample
  -> silver_clean_events
  -> gold_daily_funnel_kpis
  -> gold_product_performance
```

- Bronze: raw web event data
- Silver: cleaned and standardized event records
- Gold: KPI tables that can support dashboards and decisions

## Business Questions Answered

- Which channels and devices produce the strongest conversion?
- Where does the customer journey drop off?
- Which products receive attention but do not convert?
- Can the tracking data be trusted before making recommendations?

## Data Quality Mindset

Before interpreting funnel metrics, I check whether the data is reliable:

- duplicate event IDs
- missing session IDs
- missing product IDs on product events
- purchase events without order IDs
- negative revenue
- sessions with purchase but no add-to-cart event

This matters because a tracking issue can look like a business problem if the data is not validated first.

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
