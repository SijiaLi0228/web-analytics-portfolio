# Web Analytics Portfolio

This project demonstrates a small end-to-end analytics workflow for e-commerce web events.

It is designed around the type of workflow used in web/product analytics roles:

```text
raw web events -> cleaned validated events -> business-ready KPI tables -> dashboard insights
```

The project uses synthetic data only. It does not contain private business data, customer records, credentials, or production source code.

## Business Context

An e-commerce team wants to understand how visitors move through the digital shopping journey:

1. Product view
2. Add to cart
3. Begin checkout
4. Purchase

The goal is to identify funnel drop-off, compare performance across channels and devices, and create reliable KPI tables for dashboarding.

## Tools and Concepts

- Databricks SQL
- Medallion-style data modeling
- Bronze raw data
- Silver cleaned event data
- Gold business KPI tables
- Data quality checks
- Power BI dashboard design
- Web analytics concepts inspired by Matomo / Google Analytics event tracking

## Repository Structure

```text
data/
  raw_web_events_sample.csv
  products_sample.csv

sql/
  01_create_bronze_tables.sql
  02_create_silver_clean_events.sql
  03_create_gold_funnel_kpis.sql
  04_create_gold_product_performance.sql
  05_data_quality_checks.sql

docs/
  event_taxonomy.md
  dashboard_screenshots/

powerbi/
  dashboard_design.md
```

## Key Questions

- Which channels drive the most product views and purchases?
- Where does the funnel lose users?
- Is the drop-off different on mobile vs desktop?
- Which products have high views but low purchase conversion?
- Can the event data be trusted for reporting?

## Gold KPI Tables

### `gold_daily_funnel_kpis`

Daily funnel metrics by channel and device:

- sessions
- product view sessions
- add-to-cart sessions
- checkout sessions
- purchase sessions
- revenue
- view-to-cart rate
- cart-to-purchase rate
- session conversion rate

### `gold_product_performance`

Product-level performance:

- product views
- add-to-cart sessions
- purchase sessions
- revenue
- view-to-purchase rate

## Data Quality Checks

The project includes checks for:

- duplicate event IDs
- missing session IDs
- product events without product IDs
- purchase events without order IDs
- negative revenue
- invalid funnel ordering

## Dashboard Pages

The Power BI dashboard is designed with four pages:

1. Executive Overview
2. E-commerce Funnel
3. Product Performance
4. Channel and Device Analysis

See `powerbi/dashboard_design.md` for the dashboard layout.

## Interview Summary

This project demonstrates how I would approach a web analytics pipeline:

> I start by defining event taxonomy and business KPIs, validate raw event data, transform it into cleaned silver tables, and then create gold KPI tables that can support dashboards and stakeholder decisions.
