# Project Overview

This document summarizes the structure and analytical purpose of the e-commerce web analytics project.

## Project Scope

The project models a common digital commerce analytics workflow:

```text
tracking plan -> raw events -> cleaned events -> gold KPI tables -> dashboard-ready reporting
```

The repository uses public-safe sample data so the methodology can be reviewed without exposing private business data.

## What the Project Demonstrates

- Event taxonomy design
- Matomo and GA-compatible tracking planning
- SQL-based KPI modeling
- Bronze, silver, and gold analytics layers
- Funnel and conversion analysis
- Product performance analysis
- Data QA and validation
- Power BI dashboard planning

## Key Files

| Area | File | What it shows |
|---|---|---|
| Project overview | [README](../README.md) | End-to-end workflow and business context |
| Tracking requirements | [Event taxonomy](event_taxonomy.md) | Event definitions, properties, and QA rules |
| Web tracking plan | [Matomo tracking plan](matomo_tracking_plan.md) | How tracking can be defined and validated |
| SQL modeling | [Funnel KPI SQL](../sql/03_create_gold_funnel_kpis.sql) | Funnel KPI logic by channel and device |
| Product analytics | [Product performance SQL](../sql/04_create_gold_product_performance.sql) | Product-level conversion and revenue logic |
| Data quality | [Data quality SQL](../sql/05_data_quality_checks.sql) | Checks before using dashboard results |
| Dashboard design | [Power BI dashboard design](../powerbi/dashboard_design.md) | Report structure and measure examples |
| Project explanation | [Project walkthrough](project_walkthrough.md) | How the project can be explained end to end |

## Analytical Capabilities Shown

| Capability | Evidence in this project |
|---|---|
| Web analytics | Event taxonomy, funnel KPIs, Matomo tracking plan |
| SQL analytics | Bronze, silver, and gold SQL scripts |
| Dashboard preparation | Power BI page design and DAX measure examples |
| Marketing and product analysis | Channel, device, product, and conversion questions |
| Data quality | Explicit QA checks before interpreting performance |
| Stakeholder communication | Clear KPI definitions and dashboard question framing |

## Project Status

The project contains working sample data, SQL scripts, and documentation for the analytical workflow. The next improvement is adding screenshots from Databricks query results and a Power BI dashboard built from the gold tables.
