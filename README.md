# Large-Scale E-commerce Clickstream Analytics Portfolio

An end-to-end web analytics project showing how large-scale product and customer journey events can be modeled into trusted KPI tables and Power BI-ready insights.

The project is designed around the public **eCommerce Behavior Data from Multi-Category Store** dataset: 285 million user events from a multi-category e-commerce store, covering October 2019 to April 2020.

```text
public clickstream dataset -> bronze raw events -> silver validated events -> gold journey/product KPI tables -> Power BI insights
```

The repository does not store the raw dataset because the public source file is large. It contains the data source documentation, Databricks-style SQL model, quality checks, dashboard design, and visual examples.

## Visual Outputs

![Dashboard overview](docs/dashboard_screenshots/dashboard_overview.svg)

![Analytics pipeline](docs/dashboard_screenshots/analytics_pipeline.svg)

## Project Entry Points

| Area | File | What it shows |
|---|---|---|
| Data source | [Source dataset](docs/source_dataset.md) | Why this public clickstream dataset was selected and how fields map to web analytics work |
| Project summary | [Project overview](docs/project_overview.md) | Structure, scope, and analytical capabilities demonstrated |
| Web tracking | [Matomo tracking plan](docs/matomo_tracking_plan.md) | How Matomo events can be defined, validated, and modeled |
| Business case | [Web funnel case study](docs/case_study_web_funnel.md) | End-to-end explanation of the journey analysis case |
| SQL KPI logic | [Journey KPI SQL](sql/03_create_gold_funnel_kpis.sql) | Session-level customer journey modeling by date and category |
| Data quality | [Data quality SQL](sql/05_data_quality_checks.sql) | Checks before using dashboard results |
| Dashboard design | [Power BI dashboard design](powerbi/dashboard_design.md) | Power BI report structure, example visuals, and DAX measures |
| Visual generation | [Visual generation script](scripts/generate_portfolio_visuals.py) | Reproducible dashboard-style visuals for the portfolio |

## Why This Project

The goal is to show how I approach a web analytics problem at a realistic scale: define reliable events, validate raw clickstream data, model customer journey behavior into clean analytical tables, and prepare KPI outputs for dashboards and stakeholder decisions.

This project covers:

- large-scale web analytics
- customer journey and funnel analysis
- product and category conversion analysis
- Databricks / SQL analytics workflows
- Power BI reporting
- data QA, validation, and KPI definition
- stakeholder-facing insights

## Dataset Fit for Web Analyst Roles

This dataset is a good fit for web analyst roles because it contains event-level behavior rather than only order summaries.

| Field type | Example fields | Analytical use |
|---|---|---|
| Customer journey | `user_id`, `user_session`, `event_time`, `event_type` | session behavior, repeat activity, funnel movement |
| Product behavior | `product_id`, `category_code`, `brand`, `price` | product attention, cart intent, purchase conversion |
| Commercial outcome | `event_type = purchase`, `price` | revenue and conversion analysis |

The dataset does not include traffic source, campaign, device, or country. Those fields are therefore treated as optional enrichment fields rather than invented in the analysis.

## Business Questions

- Where does the shopping journey lose users: product view, cart, or purchase?
- Which categories attract attention but fail to convert?
- Which brands or product groups generate revenue versus browsing only?
- How does conversion differ across months or product categories?
- Can the raw event data be trusted before using it in Power BI?

## Gold KPI Tables

### `gold_daily_journey_kpis`

Daily journey metrics by product category:

- sessions
- users
- view sessions
- cart sessions
- purchase sessions
- revenue
- view-to-cart rate
- cart-to-purchase rate
- session conversion rate

### `gold_product_performance`

Product-level performance:

- product views
- cart sessions
- purchase sessions
- revenue
- average price
- view-to-purchase rate

## Repository Structure

```text
data/
  ecommerce_clickstream_sample.csv

sql/
  01_create_bronze_tables.sql
  02_create_silver_clean_events.sql
  03_create_gold_funnel_kpis.sql
  04_create_gold_product_performance.sql
  05_data_quality_checks.sql

docs/
  source_dataset.md
  project_overview.md
  project_walkthrough.md
  case_study_web_funnel.md
  event_taxonomy.md
  matomo_tracking_plan.md
  dashboard_screenshots/

powerbi/
  dashboard_design.md

scripts/
  generate_portfolio_visuals.py
```

## How to Run

1. Download the public dataset described in [docs/source_dataset.md](docs/source_dataset.md).
2. Upload a monthly partition or sample file to Databricks.
3. Run `sql/01_create_bronze_tables.sql` to create the bronze raw event table.
4. Run `sql/02_create_silver_clean_events.sql` to standardize and validate event fields.
5. Run `sql/03_create_gold_funnel_kpis.sql` to create daily journey KPIs.
6. Run `sql/04_create_gold_product_performance.sql` to create product-level KPIs.
7. Run `sql/05_data_quality_checks.sql` to inspect tracking and data quality issues.

## Summary

This project demonstrates an end-to-end web analytics workflow using a realistic public clickstream dataset: understand the event source, validate raw behavior data, build silver and gold analytical layers in SQL, and design Power BI views that connect customer journey behavior with product performance.
