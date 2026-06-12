# Large-Scale E-commerce Clickstream Analytics Portfolio

An end-to-end web analytics portfolio project showing how product and customer journey events can be turned into trusted KPI tables, Power BI-ready reporting, and stakeholder-facing recommendations.

The project uses the public **eCommerce Behavior Data from Multi-Category Store** dataset: 285 million user events from a multi-category e-commerce store, covering October 2019 to April 2020.

```text
public clickstream dataset -> bronze raw events -> silver validated events -> gold journey/product KPI tables -> dashboard insight
```

The raw dataset is not stored in this repository because the public source file is large. This repository contains the source documentation, Databricks-style SQL model, data quality checks, dashboard design, visual examples, and case-study explanation.

## Project Snapshot

| Area | What this project shows |
|---|---|
| Business problem | Understand where users drop off between product view, cart, and purchase, and which categories/products need investigation first |
| Data | Public large-scale e-commerce clickstream data with users, sessions, event types, products, categories, brands, and prices |
| Analytics method | Bronze/silver/gold SQL modeling, session-level funnel logic, retention cohorts, product friction scoring, weekly KPI monitoring, and explicit data QA |
| Reporting output | Power BI-style dashboard design for journey, product, retention, category, anomaly-style monitoring, and QA readiness analysis |
| Communication output | A case study that turns technical outputs into business interpretation and next actions |
| Transparency | Public data is used so the method can be shared. Real business data from my e-commerce work is not exposed publicly. |

## Visual Outputs

![Dashboard overview](docs/dashboard_screenshots/dashboard_overview.svg)

![Analytics pipeline](docs/dashboard_screenshots/analytics_pipeline.svg)

## What This Project Demonstrates

- event taxonomy and tracking-plan thinking
- customer journey and funnel analysis
- product and category conversion analysis
- user cohort and retention analysis
- product friction scoring and investigation prioritization
- weekly KPI monitoring with rolling baselines
- tracking quality scorecarding
- Databricks-style SQL analytics workflows
- bronze, silver, and gold data modeling
- data QA, validation, and KPI definition
- Power BI dashboard planning
- stakeholder-facing interpretation and next-step recommendations

## Business Questions

- Where does the shopping journey lose users: product view, cart, or purchase?
- Which categories attract attention but fail to convert?
- Which products or brands generate revenue versus browsing only?
- Which KPI definitions are reliable enough for a recurring dashboard?
- What should be checked before treating a funnel drop-off as a business problem?
- Are users returning after their first observed activity month?
- Which products should be prioritized for content, pricing, availability, or tracking review?
- Did a category's weekly conversion or revenue movement look unusual compared with recent history?

## Project Entry Points

| Area | File | What it shows |
|---|---|---|
| Data source | [Source dataset](docs/source_dataset.md) | Why this public clickstream dataset was selected and how fields map to web analytics work |
| Project summary | [Project overview](docs/project_overview.md) | Scope, evidence, limitations, and next iteration |
| Walkthrough | [Project walkthrough](docs/project_walkthrough.md) | The project flow from business question to dashboard output |
| Business case | [Web funnel case study](docs/case_study_web_funnel.md) | End-to-end explanation of the journey analysis case |
| Advanced analysis | [Advanced analysis layer](docs/advanced_analysis.md) | Cohort retention, product friction scoring, weekly monitoring, and QA scorecard logic |
| Web tracking | [Matomo tracking plan](docs/matomo_tracking_plan.md) | How Matomo events can be defined, validated, and modeled |
| Event taxonomy | [Event taxonomy](docs/event_taxonomy.md) | Required events, properties, and validation rules |
| SQL KPI logic | [Journey KPI SQL](sql/03_create_gold_funnel_kpis.sql) | Session-level customer journey modeling by date and category |
| Product KPI logic | [Product performance SQL](sql/04_create_gold_product_performance.sql) | Product-level views, cart behavior, purchases, and revenue |
| Cohort retention | [User cohort SQL](sql/06_create_gold_user_cohort_retention.sql) | Monthly retention by first observed activity cohort |
| Product prioritization | [Product friction SQL](sql/07_create_gold_product_friction_scores.sql) | Ranking products with high attention but weak conversion |
| KPI monitoring | [Weekly monitoring SQL](sql/08_create_gold_weekly_kpi_monitoring.sql) | Category-level conversion/revenue monitoring against recent history |
| QA scorecard | [Tracking quality scorecard SQL](sql/09_create_gold_tracking_quality_scorecard.sql) | Dashboard readiness and tracking risk summary |
| Data quality | [Data QA explanation](docs/data_quality_checks.md) | Why each QA check matters and what it protects against |
| Data quality SQL | [Data quality SQL](sql/05_data_quality_checks.sql) | SQL checks before using dashboard results |
| Dashboard design | [Power BI dashboard design](powerbi/dashboard_design.md) | Power BI report structure, example visuals, and DAX measures |
| Visual generation | [Visual generation script](scripts/generate_portfolio_visuals.py) | Reproducible dashboard-style visuals for the portfolio |

## Gold KPI Tables

### `gold_daily_journey_kpis`

Daily journey metrics by product category:

- sessions
- users
- view sessions
- cart sessions
- remove-from-cart sessions
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

### `gold_user_monthly_retention`

User activity and purchasing retention by first observed activity month:

- cohort month
- months since cohort
- cohort users
- active users
- purchasing users
- retention rate
- purchasing user rate

### `gold_product_friction_scores`

Product review prioritization:

- view-to-cart rate
- cart-to-purchase rate
- remove-to-cart rate
- attention percentile
- friction score
- suggested investigation

### `gold_weekly_category_monitoring`

Weekly category monitoring:

- weekly sessions, purchases, revenue
- weekly conversion rates
- previous four-week baseline
- conversion z-score
- monitoring flag

### `gold_tracking_quality_scorecard`

Dashboard readiness and QA risk summary:

- QA check name
- severity
- issue rate
- business risk
- recommended action
- dashboard readiness

## How I Would Explain This Project

This project is not only about building charts. I would explain it as a full analytics workflow:

1. Start with the business question: which parts of the shopping journey deserve attention first?
2. Check whether the event data can be trusted before interpreting conversion.
3. Convert raw clickstream rows into session-level journey flags to avoid overcounting repeated events.
4. Build gold KPI tables that can be reused in Power BI and recurring reports.
5. Present insights as investigation priorities, not unsupported conclusions.

Example interpretation:

```text
If a category has high product views but weak add-to-cart or purchase rates, I would first validate tracking completeness, then investigate product content, price, availability, delivery expectations, and checkout friction.
```

## Dataset Fit and Limitations

This dataset is a strong fit for web analytics because it contains event-level behavior rather than only order summaries.

| Field type | Example fields | Analytical use |
|---|---|---|
| Customer journey | `user_id`, `user_session`, `event_time`, `event_type` | session behavior, repeat activity, funnel movement |
| Product behavior | `product_id`, `category_code`, `brand`, `price` | product attention, cart intent, purchase conversion |
| Commercial outcome | `event_type = purchase`, `price` | revenue and conversion analysis |

The dataset does not include traffic source, campaign, device, country, inventory status, or promotion fields. These are not invented in the analysis. They are documented as enrichment fields that would be added in a real business setup.

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
  06_create_gold_user_cohort_retention.sql
  07_create_gold_product_friction_scores.sql
  08_create_gold_weekly_kpi_monitoring.sql
  09_create_gold_tracking_quality_scorecard.sql

docs/
  source_dataset.md
  project_overview.md
  project_walkthrough.md
  case_study_web_funnel.md
  advanced_analysis.md
  data_quality_checks.md
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
8. Run `sql/06_create_gold_user_cohort_retention.sql` to create monthly cohort retention outputs.
9. Run `sql/07_create_gold_product_friction_scores.sql` to prioritize products for investigation.
10. Run `sql/08_create_gold_weekly_kpi_monitoring.sql` to create recurring weekly monitoring flags.
11. Run `sql/09_create_gold_tracking_quality_scorecard.sql` to summarize dashboard readiness risks.

## Current Version and Next Iteration

Current version:

- documented public dataset and field mapping
- SQL model for bronze, silver, and gold layers
- journey and product KPI logic
- cohort retention, product friction scoring, weekly monitoring, and QA scorecard SQL
- data QA explanation and SQL checks
- Power BI dashboard structure and visual examples
- public case-study narrative

Next iteration:

- run a larger monthly partition in Databricks
- export real query result screenshots from Databricks
- build the Power BI report directly from the gold tables
- add traffic source, device, and campaign fields if a suitable public dataset or export is available
- add automated weekly QA checks

## Summary

This project demonstrates an end-to-end web analytics workflow using a realistic public clickstream dataset: understand the event source, validate raw behavior data, build silver and gold analytical layers in SQL, and design Power BI views that connect customer journey behavior with product performance and practical business decisions.
