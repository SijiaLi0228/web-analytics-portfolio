# Case Study: E-commerce Clickstream Journey Analytics

## Executive Summary

This case study shows how I would turn raw e-commerce event data into a business-ready funnel and product performance analysis.

The central question is not simply "what is the conversion rate?" The useful question is:

> Which journey step, product group, or tracking issue should a business team investigate first?

The output is a set of SQL-modeled gold tables, a dashboard structure, and a stakeholder interpretation framework. The project uses a public clickstream dataset so the method can be shared openly, while the same workflow reflects the type of thinking I use in real e-commerce data work.

## 1. Business Scenario

An e-commerce team wants to understand how users move from product discovery to purchase across a large product catalog. The available data contains product-level user events from a public multi-category store dataset.

The main business question is:

> Which product categories or product groups should be investigated first to improve conversion and revenue?

## 2. Analytical Objective

The objective is to create a clean, reusable analytics layer that can support dashboard reporting and stakeholder decisions. The output should help a product, marketing, or commercial team decide what to inspect next.

The analysis focuses on:

- product view volume
- cart behavior
- remove-from-cart behavior
- purchase conversion
- revenue
- category and brand differences
- product-level conversion patterns
- tracking data quality

## 3. Stakeholder Framing

Before building the SQL tables, I would align the work around stakeholder questions:

| Stakeholder question | Analytical response |
|---|---|
| Are customers moving through the journey as expected? | Build view, cart, remove-from-cart, and purchase session KPIs |
| Which categories need attention first? | Compare view-to-cart, cart-to-purchase, conversion, and revenue by category |
| Is this a tracking problem or a business problem? | Run QA checks before interpreting drop-off |
| What should we do next? | Translate metrics into investigation priorities, not unsupported conclusions |

## 4. Data Model

The project follows a medallion-style structure:

```text
bronze_ecommerce_events
  -> silver_clean_events
  -> gold_daily_journey_kpis
  -> gold_product_performance
```

### Bronze

Raw clickstream data from the public source. This layer keeps the original event-level records.

### Silver

Cleaned and standardized event data. This layer maps source `event_type` values into normalized event names such as `view_item`, `add_to_cart`, `remove_from_cart`, and `purchase`.

### Gold

Business-ready KPI tables. These tables are easier to use in Power BI or recurring stakeholder reports.

## 5. KPI Definitions

| KPI | Definition | Why it matters |
|---|---|---|
| Sessions | Distinct `user_session` values | Measures journey volume |
| Users | Distinct `user_id` values | Measures customer reach |
| View sessions | Sessions with at least one `view_item` event | Measures product discovery |
| Cart sessions | Sessions with at least one `add_to_cart` event | Measures shopping intent |
| Remove-from-cart sessions | Sessions with at least one `remove_from_cart` event | Signals cart reconsideration or friction |
| Purchase sessions | Sessions with at least one `purchase` event | Measures conversion |
| View-to-cart rate | Cart sessions / view sessions | Shows product interest quality |
| Cart-to-purchase rate | Purchase sessions / cart sessions | Shows purchase friction |
| Session conversion rate | Purchase sessions / total sessions | Overall conversion quality |
| Revenue | Sum of purchase prices | Commercial outcome |

## 6. SQL Logic

The main journey table is built at session-category level first, then aggregated by date and category.

This prevents overcounting when a user triggers the same event multiple times in one session.

Example logic used in `sql/03_create_gold_funnel_kpis.sql`:

```sql
max(case when event_name = 'view_item' then 1 else 0 end) as viewed_product,
max(case when event_name = 'add_to_cart' then 1 else 0 end) as added_to_cart,
max(case when event_name = 'remove_from_cart' then 1 else 0 end) as removed_from_cart,
max(case when event_name = 'purchase' then 1 else 0 end) as purchased
```

## 7. Data Quality Checks

Before interpreting journey results, the tracking data should be validated.

The project includes checks for:

- missing session IDs
- unknown event types
- missing product IDs on product-related events
- negative prices
- duplicate generated event IDs
- sessions with purchases but no cart event

This matters because a tracking problem can look like a business performance issue if the data is not validated first.

## 8. Dashboard Design

The Power BI design has four pages:

1. Executive Overview
2. Customer Journey Funnel
3. Product Performance
4. Category and Brand Analysis

The dashboard is designed to support both high-level management review and deeper analyst investigation.

## 9. Decision Outputs

The analysis should lead to a prioritized action list. For example:

| Pattern in dashboard | First interpretation | Next action |
|---|---|---|
| High views, weak add-to-cart | Product interest exists, but product relevance or page content may be weak | Review product page content, pricing, availability, and search/category placement |
| Strong cart activity, weak purchase | Intent exists, but checkout or delivery expectations may create friction | Inspect checkout flow, delivery cost, payment, and stock availability |
| Purchases without recorded cart events | Possible missing tracking or alternative purchase path | Validate event sequence before reporting conversion as final |
| High revenue from few products | Concentrated commercial dependency | Monitor product availability and category exposure |

## 10. Example Stakeholder Interpretation

If a category has high product views but weak cart or purchase conversion, the interpretation should not stop at "users do not like this category."

The next checks would include:

- whether product IDs and category labels are complete
- whether cart or purchase events are tracked consistently
- whether prices, product content, availability, or delivery expectations explain the drop-off
- whether the pattern is category-specific or product-specific
- whether repeat users behave differently from single-session users

This approach separates tracking quality, user behavior, product experience, and commercial performance.

## 11. Project Explanation

This project demonstrates the analytics workflow behind web and product reporting: understand the event source, clean raw clickstream events, validate tracking quality, build gold KPI tables in SQL, and design a Power BI dashboard around stakeholder questions.

The goal is not just to calculate metrics. The goal is to make sure the metrics are trustworthy and actionable.
