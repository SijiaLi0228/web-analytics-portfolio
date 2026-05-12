# Project Walkthrough

This document explains the project from business question to analytics output.

## 1. Project Summary

This is a synthetic e-commerce web analytics project that simulates the workflow from web tracking to business reporting.

The project defines core funnel events, cleans and validates event data, builds gold tables for daily funnel and product performance, and designs a Power BI dashboard structure for recurring reporting.

## 2. Why This Project Exists

The purpose is to practice a realistic analytics workflow: turning tracking data into trusted business metrics.

The focus is not only writing SQL. It is also about defining reliable events, checking data quality, creating clear KPI definitions, and making outputs usable for business teams.

## 3. Data Pipeline

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
- Dashboard: reporting layout for business review

## 4. Business Questions

The project is designed to answer questions such as:

- Which channels and devices produce the strongest conversion?
- Where does the customer journey drop off?
- Which products receive attention but do not convert?
- Can the tracking data be trusted before making recommendations?
- Which KPI should be monitored weekly?

## 5. Data Quality Approach

Before interpreting funnel metrics, the project checks whether the data is reliable:

- duplicate event IDs
- missing session IDs
- missing product IDs on product events
- purchase events without order IDs
- negative revenue
- sessions with purchase but no add-to-cart event

This matters because a tracking issue can look like a business problem if the data is not validated first.

## 6. SQL Modeling Approach

The funnel logic is built at session level first.

Instead of counting every event row directly, the model first flags whether a session had each key journey step: product view, add to cart, checkout, and purchase. Then those session-level flags are aggregated by date, channel, and device.

This avoids overcounting users who trigger the same event multiple times in one session.

## 7. Dashboard Approach

The dashboard is structured around business questions:

1. Executive Overview: Are traffic, conversion, and revenue moving in the right direction?
2. E-commerce Funnel: Where do users drop off?
3. Product Performance: Which products attract interest but fail to convert?
4. Channel and Device Analysis: Which traffic sources produce useful demand?

## 8. Matomo Tracking Logic

The tracking plan starts by defining the key journey events and required properties, then validating that events fire correctly before using them in dashboards.

The important point is not only installing a tag. The tracking logic needs to support reliable business questions.

## 9. Databricks / SQL Practice

The project uses Databricks-style SQL workflows to create tables, clean raw events, build gold KPI tables, and prepare outputs for reporting.

The focus is analytics engineering at a practical analyst level: producing tables that are understandable, reusable, and dashboard-ready.

## 10. Future Extensions

If this were extended further, the next additions would be:

- Matomo or GA event exports
- campaign and paid media fields
- customer segment fields
- promotion and discount data
- Power BI screenshots or a published dashboard
- automated data quality checks
- weekly KPI monitoring and alerts
