# Recruiter Quick Scan

This page is written for hiring managers and recruiters who want to understand the portfolio quickly.

## What This Project Demonstrates

This project shows a compact analytics workflow for an e-commerce web journey:

```text
tracking plan -> raw events -> cleaned events -> gold KPI tables -> Power BI dashboard design
```

The data is synthetic, but the structure mirrors work commonly done in web analytics, product analytics, and commercial analytics roles.

## Best Files to Review First

| Area | File | What it shows |
|---|---|---|
| Project overview | `README.md` | End-to-end workflow and business context |
| Tracking thinking | `docs/event_taxonomy.md` | Event definitions, properties, and QA rules |
| Matomo/GA thinking | `docs/matomo_tracking_plan.md` | How I would plan and validate web tracking |
| SQL modeling | `sql/03_create_gold_funnel_kpis.sql` | Funnel KPI logic by channel and device |
| Product analytics | `sql/04_create_gold_product_performance.sql` | Product-level conversion and revenue logic |
| Data quality | `sql/05_data_quality_checks.sql` | Checks before trusting dashboard results |
| Dashboard design | `powerbi/dashboard_design.md` | Power BI page design and measures |
| Interview summary | `docs/interview_talking_points.md` | How I would explain the project in an interview |

## Skills Shown

- SQL analytics and KPI modeling
- Web event taxonomy and tracking validation
- Funnel and conversion analysis
- Product performance analysis
- Data quality checks
- Dashboard design for Power BI
- Business translation from data tables to stakeholder questions

## Role Fit

| Role requirement | Evidence in this portfolio |
|---|---|
| Web analytics | Event taxonomy, funnel KPIs, Matomo-style tracking plan |
| SQL / Databricks | Bronze, silver, and gold SQL scripts |
| Power BI | Dashboard page plan and DAX measure examples |
| Stakeholder reporting | Business questions, KPI definitions, and dashboard layout |
| Commercial mindset | Channel, device, product, conversion, and revenue analysis |
| Data quality mindset | Explicit QA checks before interpreting performance |

## What I Can Discuss in an Interview

I can walk through how I would:

1. Define tracking requirements with stakeholders.
2. Translate business questions into measurable web events.
3. Validate raw tracking data before dashboarding.
4. Build reliable KPI tables for funnel and product reporting.
5. Use dashboard outputs to recommend follow-up analysis.

## Current Status

The project contains working sample data and SQL logic. The next planned improvement is adding dashboard screenshots from Databricks or Power BI after the visual report is built.
