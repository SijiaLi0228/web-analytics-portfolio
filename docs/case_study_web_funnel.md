# Case Study: E-commerce Web Funnel Analytics

## 1. Business Scenario

An e-commerce team wants to understand how users move from product discovery to purchase. Traffic comes from several channels and devices, but the team needs a reliable view of where users drop off and which product areas deserve attention.

The main business question is:

> Which parts of the digital shopping journey should be investigated first to improve conversion and revenue?

## 2. Analytical Objective

The objective is to create a clean, reusable analytics layer that can support dashboard reporting and stakeholder decisions.

The analysis focuses on:

- product view volume
- add-to-cart behavior
- checkout behavior
- purchase conversion
- revenue
- channel and device differences
- product-level conversion patterns
- tracking data quality

## 3. Data Model

The project follows a simple medallion-style structure:

```text
bronze_web_events_sample
  -> silver_clean_events
  -> gold_daily_funnel_kpis
  -> gold_product_performance
```

### Bronze

Raw web event data. This layer keeps the original event-level records.

### Silver

Cleaned and standardized event data. This layer prepares event dates, event names, product IDs, session IDs, channels, devices, and revenue fields for analysis.

### Gold

Business-ready KPI tables. These tables are easier to use in Power BI or recurring stakeholder reports.

## 4. KPI Definitions

| KPI | Definition | Why it matters |
|---|---|---|
| Sessions | Distinct sessions by date, channel, and device | Measures traffic volume |
| Product view sessions | Sessions with at least one `view_item` event | Measures product discovery |
| Add-to-cart sessions | Sessions with at least one `add_to_cart` event | Measures shopping intent |
| Checkout sessions | Sessions with at least one `begin_checkout` event | Measures checkout intent |
| Purchase sessions | Sessions with at least one `purchase` event | Measures conversion |
| View-to-cart rate | Add-to-cart sessions / product view sessions | Shows product page effectiveness |
| Cart-to-purchase rate | Purchase sessions / add-to-cart sessions | Shows checkout and purchase friction |
| Session conversion rate | Purchase sessions / total sessions | Overall conversion quality |
| Revenue | Sum of purchase revenue | Commercial outcome |

## 5. SQL Logic

The main funnel table is built at session level first, then aggregated by date, channel, and device.

This prevents overcounting when a user triggers the same event multiple times in one session.

Example logic used in `sql/03_create_gold_funnel_kpis.sql`:

```sql
max(case when event_name = 'view_item' then 1 else 0 end) as viewed_product,
max(case when event_name = 'add_to_cart' then 1 else 0 end) as added_to_cart,
max(case when event_name = 'begin_checkout' then 1 else 0 end) as began_checkout,
max(case when event_name = 'purchase' then 1 else 0 end) as purchased
```

## 6. Data Quality Checks

Before interpreting funnel results, the tracking data should be validated.

The project includes checks for:

- duplicate event IDs
- missing session IDs
- missing product IDs on product-related events
- purchase events without order IDs
- negative revenue
- sessions with purchases but no add-to-cart event

This matters because a tracking problem can look like a business performance issue if the data is not validated first.

## 7. Dashboard Design

The Power BI design has four pages:

1. Executive Overview
2. E-commerce Funnel
3. Product Performance
4. Channel and Device Analysis

The dashboard is designed to support both high-level management review and deeper analyst investigation.

## 8. Example Stakeholder Interpretation

If mobile traffic has high product views but lower cart-to-purchase conversion, the interpretation should not stop at "mobile users are less valuable."

The next checks would include:

- whether mobile events are tracked correctly
- whether checkout events are missing on mobile
- whether payment or delivery steps differ by device
- whether mobile traffic comes from a lower-intent channel
- whether product content or loading speed affects mobile users

This approach separates tracking quality, user experience, and commercial performance.

## 9. Project Explanation

This project demonstrates the analytics workflow behind web and product reporting: define event requirements, clean raw events, validate tracking quality, build gold KPI tables in SQL, and design a Power BI dashboard around stakeholder questions.

The goal is not just to calculate metrics. The goal is to make sure the metrics are trustworthy and actionable.

## 10. Next Improvements

The next improvements would be:

- connect Matomo or GA event exports
- add promotion and campaign fields
- add screenshot evidence from Databricks query results
- build the Power BI report from the gold tables
- add automated weekly data quality checks
