# Project Walkthrough

This document explains the project from business question to analytics output.

## 1. Project Summary

This is an e-commerce web analytics project based on a public large-scale clickstream dataset. The dataset contains product-level user events such as product views, cart actions, remove-from-cart actions, and purchases.

The project cleans and validates raw event data, builds gold tables for customer journey and product performance, and designs a Power BI dashboard structure for recurring reporting.

## 2. Why This Project Exists

The purpose is to practice a realistic analytics workflow: turning product-level customer behavior data into trusted business metrics.

The focus is not only writing SQL. It is also about understanding the source data, defining reliable events, checking data quality, creating clear KPI definitions, and making outputs usable for business teams.

This is a public portfolio project, so it uses public data that can be shared openly. My real e-commerce work involves private product, order, customer, web, and operational data, so this repository is designed to demonstrate the method without exposing confidential business information.

## 3. Data Pipeline

```text
public clickstream dataset
  -> bronze_ecommerce_events
  -> silver_clean_events
  -> gold_daily_journey_kpis
  -> gold_product_performance
  -> Power BI dashboard design
```

- Source dataset: public multi-category e-commerce behavior data
- Bronze: raw event data
- Silver: cleaned and standardized event records
- Gold: KPI tables that can support dashboards and decisions
- Dashboard: reporting layout for business review

## 4. Business Questions

The project is designed to answer questions such as:

- Where does the customer journey drop off?
- Which categories and brands produce stronger conversion?
- Which products receive attention but do not convert?
- Can the event data be trusted before making recommendations?
- Which KPI should be monitored weekly?

## 5. Data Quality Approach

Before interpreting funnel metrics, the project checks whether the data is reliable:

- missing session IDs
- unknown event types
- missing product IDs on product events
- negative prices
- duplicate generated event IDs
- sessions with purchase but no cart event

This matters because a tracking issue can look like a business problem if the data is not validated first.

## 6. SQL Modeling Approach

The journey logic is built at session-category level first.

Instead of counting every event row directly, the model first flags whether a session had each key journey step: product view, add to cart, remove from cart, and purchase. Then those session-level flags are aggregated by date and category.

This avoids overcounting users who trigger the same event multiple times in one session.

## 7. Dashboard Approach

The dashboard is structured around business questions:

1. Executive Overview: Are events, users, sessions, conversion, and revenue moving in the right direction?
2. Customer Journey Funnel: Where do users drop off?
3. Product Performance: Which products attract interest but fail to convert?
4. Category and Brand Analysis: Which product groups create revenue versus browsing activity?

## 8. Matomo Tracking Logic

The public dataset is not a Matomo export, but the modeling logic mirrors how a Matomo setup should be planned:

- define agreed event names
- define required properties
- validate event completeness
- model raw events into business KPIs
- present only trusted metrics in dashboards

## 9. Databricks / SQL Practice

The project uses Databricks-style SQL workflows to create tables, clean raw events, build gold KPI tables, and prepare outputs for reporting.

The focus is analytics engineering at a practical analyst level: producing tables that are understandable, reusable, and dashboard-ready.

## 10. Future Extensions

If this were extended further, the next additions would be:

- run the full monthly source file in Databricks
- add Matomo or GA event exports for channel, campaign, device, and country fields
- add customer segment fields
- add product availability and promotion data
- export real Databricks query screenshots
- build the Power BI report from the gold tables
- automate weekly data quality checks

## 11. Interview Narrative

If I had one minute to explain the project, I would say:

```text
I wanted to show the full path from raw digital behavior data to a business-ready analytics output. I selected a public e-commerce clickstream dataset because it has realistic web events: views, cart actions, removals, and purchases. I designed the pipeline as bronze, silver, and gold layers, cleaned and standardized the events, then built session-level KPI tables so repeated clicks would not inflate the funnel. Before interpreting performance, I added data quality checks because tracking issues can look like business issues. The final output is a Power BI dashboard design and case study that helps a stakeholder decide which category, product group, or tracking issue to investigate first.
```
