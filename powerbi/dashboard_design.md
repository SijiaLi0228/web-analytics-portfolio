# Power BI Dashboard Design

This dashboard can be built from the gold KPI tables produced by the Databricks SQL scripts.

The design goal is to support stakeholder conversations, not only display charts. Each page is tied to a business question and a follow-up action.

## Data Sources

Recommended model tables:

- `gold_daily_funnel_kpis`
- `gold_product_performance`
- `products_sample`

Suggested relationships:

```text
gold_product_performance.product_id -> products_sample.product_id
```

For the daily funnel page, `gold_daily_funnel_kpis` can be used directly because it is already aggregated by date, channel, and device.

## Page 1: Executive Overview

Purpose: give stakeholders a quick view of web and sales performance.

Business question:

> Are traffic, conversion, and revenue moving in the right direction?

Recommended visuals:

- KPI card: sessions
- KPI card: purchase sessions
- KPI card: revenue
- KPI card: session conversion rate
- Line chart: revenue by date
- Bar chart: sessions by channel
- Bar chart: conversion rate by device
- Table or matrix: channel, sessions, revenue, conversion rate

Recommended filters:

- date
- channel
- device
- country

Stakeholder talking point:

```text
I would use this page to start the meeting with the overall performance picture, then move into funnel or product pages only when a KPI needs explanation.
```

## Page 2: E-commerce Funnel

Purpose: identify where users drop off.

Business question:

> Which funnel step creates the biggest loss of user intent?

Recommended visuals:

- Funnel chart:
  - product view sessions
  - add-to-cart sessions
  - checkout sessions
  - purchase sessions
- Bar chart: view-to-cart rate by channel
- Bar chart: cart-to-purchase rate by device
- Table: daily funnel KPIs

Key insight template:

```text
Mobile traffic has lower cart-to-purchase conversion than desktop. The next step is to inspect mobile checkout UX, payment flow, and whether mobile checkout events are tracked correctly.
```

## Page 3: Product Performance

Purpose: understand product-level conversion and revenue.

Business question:

> Which products attract interest but fail to convert?

Recommended visuals:

- Table: product name, views, add-to-cart, purchases, revenue, view-to-purchase rate
- Bar chart: revenue by product
- Scatter plot: view sessions vs purchase sessions
- Conditional formatting: low conversion / high views

Key insight template:

```text
Some products receive high views but low purchase conversion, which may indicate pricing, product content, availability, or checkout friction.
```

## Page 4: Channel and Device Analysis

Purpose: compare traffic quality across channels and devices.

Business question:

> Which traffic sources produce useful demand rather than only volume?

Recommended visuals:

- Matrix: channel x device with sessions, revenue, conversion
- Bar chart: revenue by channel
- Bar chart: conversion rate by device
- Map or bar chart: sessions by country

Key insight template:

```text
Paid mobile traffic drives sessions but has weaker conversion, suggesting a need to review campaign targeting and mobile landing page relevance.
```

## Measures to Create in Power BI

Example DAX measures:

```text
Total Sessions = SUM(gold_daily_funnel_kpis[sessions])
Total Revenue = SUM(gold_daily_funnel_kpis[revenue])
Purchase Sessions = SUM(gold_daily_funnel_kpis[purchase_sessions])
Session Conversion Rate = DIVIDE([Purchase Sessions], [Total Sessions])
Product View Sessions = SUM(gold_daily_funnel_kpis[product_view_sessions])
Add To Cart Sessions = SUM(gold_daily_funnel_kpis[add_to_cart_sessions])
View To Cart Rate = DIVIDE([Add To Cart Sessions], [Product View Sessions])
Cart To Purchase Rate = DIVIDE([Purchase Sessions], [Add To Cart Sessions])
Revenue Per Session = DIVIDE([Total Revenue], [Total Sessions])
```

## Dashboard QA Checklist

Before sharing the dashboard, I would check:

- metric definitions match the SQL gold tables
- filters do not create misleading totals
- revenue formatting is clear
- conversion rates are displayed as percentages
- product and channel names are readable
- no chart relies on raw event-level rows when a gold table should be used
- dashboard insights are tied to a suggested next action

## Portfolio Screenshot Checklist

After building the report, add screenshots to a `docs/dashboard_screenshots/` folder:

- executive overview
- funnel dashboard
- product performance page
- channel/device analysis page
- Databricks query result for `gold_daily_funnel_kpis`
- Databricks query result for `gold_product_performance`

## Interview Talking Point

A concise way to explain the dashboard design:

```text
I would not design the dashboard as a collection of charts. I would structure it around stakeholder questions: first overall performance, then funnel drop-off, then product-level performance, then channel and device differences. This makes the dashboard easier to use in recurring business meetings.
```
