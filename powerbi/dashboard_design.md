# Power BI Dashboard Design

This dashboard can be built from the gold KPI tables produced by the Databricks SQL scripts.

## Page 1: Executive Overview

Purpose: give stakeholders a quick view of web and sales performance.

Recommended visuals:

- KPI card: sessions
- KPI card: purchase sessions
- KPI card: revenue
- KPI card: session conversion rate
- Line chart: revenue by date
- Bar chart: sessions by channel
- Bar chart: conversion rate by device

Recommended filters:

- date
- channel
- device
- country

## Page 2: E-commerce Funnel

Purpose: identify where users drop off.

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
Mobile traffic has lower cart-to-purchase conversion than desktop. The next step is to inspect mobile checkout UX and payment flow.
```

## Page 3: Product Performance

Purpose: understand product-level conversion and revenue.

Recommended visuals:

- Table: product name, views, add-to-cart, purchases, revenue, view-to-purchase rate
- Bar chart: revenue by product
- Scatter plot: view sessions vs purchase sessions

Key insight template:

```text
Some products receive high views but low purchase conversion, which may indicate pricing, product content, availability, or checkout friction.
```

## Page 4: Channel and Device Analysis

Purpose: compare traffic quality across channels and devices.

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
```

## Portfolio Screenshot Checklist

Add screenshots to `docs/dashboard_screenshots/`:

- executive overview
- funnel dashboard
- product performance page
- channel/device analysis page
