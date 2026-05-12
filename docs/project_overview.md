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
- Data QA and validation
- Power BI dashboard planning

## Key Files

| Area | File | What it shows |
|---|---|---|
| Data source | [Source dataset](source_dataset.md) | Dataset scale, fields, and role fit |
| Project overview | [README](../README.md) | End-to-end workflow and business context |
| Tracking requirements | [Event taxonomy](event_taxonomy.md) | Event definitions, properties, and QA rules |
| Web tracking plan | [Matomo tracking plan](matomo_tracking_plan.md) | How tracking can be defined and validated |
| SQL modeling | [Journey KPI SQL](../sql/03_create_gold_funnel_kpis.sql) | Journey KPI logic by date and category |
| Product analytics | [Product performance SQL](../sql/04_create_gold_product_performance.sql) | Product-level conversion and revenue logic |
| Data quality | [Data quality SQL](../sql/05_data_quality_checks.sql) | Checks before using dashboard results |
| Dashboard design | [Power BI dashboard design](../powerbi/dashboard_design.md) | Report structure and measure examples |

## Analytical Capabilities Shown

| Capability | Evidence in this project |
|---|---|
| Web analytics | Event taxonomy, journey KPIs, Matomo tracking plan |
| SQL analytics | Bronze, silver, and gold SQL scripts |
| Dashboard preparation | Power BI page design and DAX measure examples |
| Product and customer journey analysis | Category, product, session, and conversion questions |
| Data quality | Explicit QA checks before interpreting performance |
| Stakeholder communication | Clear KPI definitions and dashboard question framing |

## Project Status

The project contains a realistic public-data design, Databricks-style SQL scripts, documentation, and portfolio visuals. The next improvement is running the full monthly dataset in Databricks and exporting real query result screenshots.
