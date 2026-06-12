# Power BI Dashboard Design

This dashboard is designed from the gold KPI tables produced by the Databricks SQL scripts for a large-scale public e-commerce clickstream dataset.

The design goal is to support stakeholder conversations about customer journey behavior, product/category performance, user retention, weekly monitoring, and tracking quality. The selected dataset does not contain traffic source or device fields, so channel attribution should not be shown unless those fields are added from another source.

## Example Dashboard Output

The visuals below show the intended reporting output for the large-scale clickstream project.

![Dashboard overview](../docs/dashboard_screenshots/dashboard_overview.svg)

![Funnel analysis](../docs/dashboard_screenshots/funnel_analysis.svg)

![Product performance](../docs/dashboard_screenshots/product_performance.svg)

## Data Sources

Recommended model tables:

- `gold_daily_journey_kpis`
- `gold_product_performance`
- `gold_user_monthly_retention`
- `gold_product_friction_scores`
- `gold_weekly_category_monitoring`
- `gold_tracking_quality_scorecard`
- `silver_clean_events`

Suggested relationships:

```text
gold_product_performance.product_id -> product dimension, if a separate product dimension is available
gold_daily_journey_kpis.category_code -> category dimension, if available
```

## Page 1: Executive Overview

Purpose: give stakeholders a quick view of event volume, journey movement, conversion, and revenue.

Business question:

> Are users moving from product discovery to cart and purchase, and which categories explain the performance?

Recommended visuals:

- KPI card: total events
- KPI card: sessions
- KPI card: users
- KPI card: purchase sessions
- KPI card: revenue
- Line chart: sessions and purchase sessions by date
- Bar chart: revenue by category
- Table: category, sessions, cart sessions, purchase sessions, revenue, conversion

Recommended filters:

- date
- event type
- category
- brand
- price range

## Page 2: Customer Journey Funnel

Purpose: identify where users drop off.

Business question:

> Which journey step creates the biggest loss of user intent?

Recommended visuals:

- Funnel chart:
  - view sessions
  - cart sessions
  - purchase sessions
- Bar chart: view-to-cart rate by category
- Bar chart: cart-to-purchase rate by category
- Table: daily journey KPIs

Example interpretation:

```text
If a category has high view volume but weak cart or purchase conversion, the next step is to inspect product relevance, pricing, availability, product page content, and tracking completeness.
```

## Page 3: Product Performance

Purpose: understand product-level attention, intent, and revenue.

Business question:

> Which products attract interest but fail to convert?

Recommended visuals:

- Table: product ID, category, brand, views, cart sessions, purchase sessions, revenue, view-to-purchase rate
- Bar chart: revenue by product/category
- Scatter plot: view sessions vs purchase sessions
- Conditional formatting: high view / low purchase products

Example interpretation:

```text
High views with low purchase conversion may indicate pricing, product content, availability, shipping expectations, or checkout friction.
```

## Page 4: Product Friction Review

Purpose: prioritize products that deserve investigation.

Business question:

> Which products have high attention but weak conversion or high remove-from-cart pressure?

Recommended visuals:

- Table: product ID, category, brand, views, cart sessions, purchases, remove-to-cart rate, friction score, suggested investigation
- Scatter plot: view sessions vs view-to-purchase rate
- Bar chart: top 20 products by friction score
- Slicer: category and brand

Example interpretation:

```text
A high friction score is not a conclusion. It tells the team where to inspect product content, pricing, stock, delivery expectations, or tracking quality first.
```

## Page 5: Cohort Retention

Purpose: understand whether users return after first observed activity.

Business question:

> Are users coming back, or is activity mostly one-time browsing?

Recommended visuals:

- Heatmap: cohort month x months since cohort, colored by retention rate
- Line chart: active users by cohort age
- KPI card: month-1 retention
- KPI card: purchasing user rate

## Page 6: Weekly KPI Monitoring

Purpose: identify unusual category movement for recurring business review.

Business question:

> Which category moved unusually compared with recent history?

Recommended visuals:

- Table: week, category, sessions, revenue, conversion, previous 4-week baseline, monitoring flag
- Line chart: conversion rate vs previous 4-week average
- Bar chart: revenue movement by category
- Filter: monitoring flag

## Page 7: Tracking Quality Scorecard

Purpose: decide whether dashboard metrics are ready to publish or need caveats.

Business question:

> Are tracking and data quality good enough to interpret the dashboard?

Recommended visuals:

- Table: check name, severity, issue rows, issue rate, business risk, recommended action, dashboard readiness
- KPI card: critical issues
- KPI card: high-severity issues
- Status indicator: dashboard readiness

## Page 8: Category and Brand Analysis

Purpose: compare product groups and identify where business teams should investigate.

Business question:

> Which categories and brands create revenue, and which only create browsing activity?

Recommended visuals:

- Matrix: category x brand with sessions, revenue, conversion
- Bar chart: revenue by category
- Bar chart: view-to-purchase rate by brand
- Table: top products by revenue and top products by under-conversion

## Measures to Create in Power BI

Example DAX measures:

```text
Total Sessions = SUM(gold_daily_journey_kpis[sessions])
Total Users = SUM(gold_daily_journey_kpis[users])
View Sessions = SUM(gold_daily_journey_kpis[view_sessions])
Cart Sessions = SUM(gold_daily_journey_kpis[cart_sessions])
Purchase Sessions = SUM(gold_daily_journey_kpis[purchase_sessions])
Total Revenue = SUM(gold_daily_journey_kpis[revenue])
View To Cart Rate = DIVIDE([Cart Sessions], [View Sessions])
Cart To Purchase Rate = DIVIDE([Purchase Sessions], [Cart Sessions])
Session Conversion Rate = DIVIDE([Purchase Sessions], [Total Sessions])
Revenue Per Purchase Session = DIVIDE([Total Revenue], [Purchase Sessions])
Average Friction Score = AVERAGE(gold_product_friction_scores[friction_score])
Month 1 Retention = CALCULATE(AVERAGE(gold_user_monthly_retention[retention_rate]), gold_user_monthly_retention[months_since_cohort] = 1)
Critical QA Issues = CALCULATE(COUNTROWS(gold_tracking_quality_scorecard), gold_tracking_quality_scorecard[severity] = "critical", gold_tracking_quality_scorecard[issue_rows] > 0)
```

## Dashboard QA Checklist

Before sharing the dashboard, I would check:

- metric definitions match the SQL gold tables
- filters do not create misleading totals
- purchase revenue uses only purchase events
- conversion rates are displayed as percentages
- category and brand labels are readable
- no chart relies on raw event-level rows when a gold table should be used
- dashboard insights are tied to a suggested next action
- friction-score outputs are explained as prioritization, not causal proof
- retention analysis is described as first-observed activity retention, not true customer acquisition retention
- monitoring flags are reviewed with business context before escalation

## Design Rationale

The dashboard is structured around stakeholder questions rather than chart types: first overall performance, then journey drop-off, then product-level performance, then category and brand differences.

The important analytics habit is to validate event coverage and KPI definitions before presenting funnel movement as a business issue.
