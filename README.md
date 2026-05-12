# Web Analytics Portfolio

A compact end-to-end analytics portfolio project for e-commerce web events.

This project demonstrates the workflow commonly used in web, product, and commercial analytics roles:

```text
raw web events -> cleaned validated events -> business-ready KPI tables -> dashboard insights
```

The project uses synthetic data only. It does not contain private business data, customer records, credentials, or production source code.

## Why This Project

The goal is to show how I would approach a real web analytics problem: define reliable events, validate raw tracking data, model it into clean analytical tables, and prepare KPI outputs for dashboards and stakeholder decisions.

This is especially relevant to roles involving:

- web analytics
- product analytics
- e-commerce funnel analysis
- Databricks / SQL analytics workflows
- Power BI reporting
- data quality and KPI definition

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
  interview_talking_points.md
  dashboard_screenshots/

powerbi/
  dashboard_design.md
```

## How to Run

1. Open Databricks SQL Editor or a SQL notebook.
2. Run `sql/01_create_bronze_tables.sql` to create sample bronze tables.
3. Run `sql/02_create_silver_clean_events.sql` to create cleaned event data.
4. Run `sql/03_create_gold_funnel_kpis.sql` to create daily funnel KPIs.
5. Run `sql/04_create_gold_product_performance.sql` to create product-level KPIs.
6. Run `sql/05_data_quality_checks.sql` to inspect data quality issues.

The SQL scripts are designed to be readable and interview-friendly. The first script includes an inline sample-data setup so the project can be reviewed without external systems.

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

See `powerbi/dashboard_design.md` for the dashboard layout and DAX measure examples.

## Interview Summary

This project demonstrates how I would approach a web analytics pipeline:

> I start by defining event taxonomy and business KPIs, validate raw event data, transform it into cleaned silver tables, and then create gold KPI tables that can support dashboards and stakeholder decisions.
