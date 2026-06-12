# Project Overview

This document summarizes the structure and analytical purpose of the large-scale e-commerce clickstream analytics project.

## Project Scope

The project models a common digital commerce analytics workflow:

```text
public clickstream dataset -> raw events -> validated events -> gold KPI tables -> dashboard-ready reporting
```

The selected dataset contains 285 million product-related user events from a multi-category e-commerce store. The repository keeps only a lightweight review sample and SQL model; the raw source file should be downloaded separately because of its size.

## What the Project Demonstrates

- Public dataset selection and field mapping
- Event taxonomy design
- Matomo and GA-compatible tracking planning
- SQL-based KPI modeling
- Bronze, silver, and gold analytics layers
- Customer journey and conversion analysis
- Product and category performance analysis
- User cohort and retention analysis
- Product friction scoring for investigation prioritization
- Weekly KPI monitoring with recent-history baselines
- Tracking quality scorecarding
- Data QA and validation
- Power BI dashboard planning
- Stakeholder-facing explanation of business questions, limitations, and next actions

## Key Files

| Area | File | What it shows |
|---|---|---|
| Data source | [Source dataset](source_dataset.md) | Dataset scale, fields, and role fit |
| Project overview | [README](../README.md) | End-to-end workflow and business context |
| Tracking requirements | [Event taxonomy](event_taxonomy.md) | Event definitions, properties, and QA rules |
| Web tracking plan | [Matomo tracking plan](matomo_tracking_plan.md) | How tracking can be defined and validated |
| Advanced analysis | [Advanced analysis layer](advanced_analysis.md) | Cohort, friction scoring, KPI monitoring, and QA scorecard modules |
| SQL modeling | [Journey KPI SQL](../sql/03_create_gold_funnel_kpis.sql) | Journey KPI logic by date and category |
| Product analytics | [Product performance SQL](../sql/04_create_gold_product_performance.sql) | Product-level conversion and revenue logic |
| Retention analytics | [Cohort retention SQL](../sql/06_create_gold_user_cohort_retention.sql) | User cohort retention by first observed activity month |
| Product prioritization | [Product friction SQL](../sql/07_create_gold_product_friction_scores.sql) | Scoring products with attention but weak conversion |
| KPI monitoring | [Weekly monitoring SQL](../sql/08_create_gold_weekly_kpi_monitoring.sql) | Weekly category movement against recent baseline |
| QA readiness | [Tracking quality scorecard SQL](../sql/09_create_gold_tracking_quality_scorecard.sql) | Tracking risk summary for dashboard interpretation |
| Data quality | [Data QA explanation](data_quality_checks.md) | Why each QA check matters before interpreting dashboard results |
| Data quality SQL | [Data quality SQL](../sql/05_data_quality_checks.sql) | SQL checks before using dashboard results |
| Dashboard design | [Power BI dashboard design](../powerbi/dashboard_design.md) | Report structure and measure examples |

## Analytical Capabilities Shown

| Capability | Evidence in this project |
|---|---|
| Web analytics | Event taxonomy, journey KPIs, Matomo tracking plan |
| SQL analytics | Bronze, silver, and gold SQL scripts |
| Dashboard preparation | Power BI page design and DAX measure examples |
| Product and customer journey analysis | Category, product, session, and conversion questions |
| Advanced prioritization | Product friction scoring and weekly KPI monitoring flags |
| Retention thinking | Cohort-level active and purchasing user retention |
| Data quality | Explicit QA checks before interpreting performance |
| Stakeholder communication | Clear KPI definitions and dashboard question framing |

## Project Status

The project contains a realistic public-data design, Databricks-style SQL scripts, documentation, and portfolio visuals. It now includes both core reporting tables and deeper analysis modules for retention, prioritization, monitoring, and data quality readiness.

This is a public portfolio version, so it deliberately avoids confidential business data. The purpose is to show the method clearly: define events, validate raw data, model reusable KPI tables, and design dashboard outputs around stakeholder questions.

Next improvements:

- run a larger monthly partition in Databricks
- export real Databricks query result screenshots
- build a Power BI report directly from the gold tables
- add campaign, device, traffic source, and customer segment fields if a suitable public source becomes available
