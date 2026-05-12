# Matomo Tracking Plan

This document shows how I would plan, validate, and use Matomo web tracking for an e-commerce analytics project.

The same methodology can also be adapted to Google Analytics, server-side logs, or exported web event data.

## 1. Tracking Objective

The tracking setup should help answer these business questions:

- How many users view products, add items to cart, start checkout, and purchase?
- Which channels and devices produce the strongest conversion?
- Which products receive attention but do not convert?
- Are tracking events complete and reliable enough for reporting?
- Which parts of the journey should stakeholders investigate first?

## 2. Core Events

| Journey step | Event category | Event action | Event name example | Required properties |
|---|---|---|---|---|
| Product page viewed | Ecommerce | View Item | `view_item` | `product_id`, `category`, `price`, `session_id` |
| Add to cart | Ecommerce | Add To Cart | `add_to_cart` | `product_id`, `quantity`, `session_id` |
| Checkout started | Ecommerce | Begin Checkout | `begin_checkout` | `product_id`, `cart_value`, `session_id` |
| Purchase completed | Ecommerce | Purchase | `purchase` | `order_id`, `revenue`, `product_id`, `session_id` |
| Search used | Site Search | Search | `site_search` | `search_term`, `results_count`, `session_id` |
| Promotion clicked | Promotion | Click | `promotion_click` | `campaign`, `placement`, `session_id` |

## 3. Recommended Dimensions

Useful dimensions for segmentation:

- channel
- campaign
- device
- country
- product category
- product ID
- new vs returning visitor
- checkout step
- promotion name

## 4. Tracking QA Checklist

Before using the data in a dashboard, I would validate:

- Events fire once per intended user action.
- Required event properties are populated.
- Product IDs match the product catalog.
- Purchase revenue is non-negative and matches order data.
- Order IDs are unique.
- Mobile and desktop events follow the same naming rules.
- Event volume does not suddenly drop after website releases.
- Consent settings and privacy requirements are respected.

## 5. Data Pipeline Use

Matomo events can be exported and modeled into analytical layers:

```text
Matomo event export
  -> raw event table
  -> cleaned event table
  -> funnel KPI table
  -> Power BI dashboard
```

The SQL files in this repository demonstrate the modeling step after event data has been collected.

## 6. Reporting Output

The final dashboard should show:

- total sessions
- product view sessions
- add-to-cart sessions
- checkout sessions
- purchase sessions
- conversion rate
- revenue
- channel and device performance
- product-level conversion
- data quality warnings

## 7. Stakeholder Questions

For stakeholder meetings, I would use the tracking data to answer:

- Is the issue traffic quality, product interest, checkout friction, or tracking quality?
- Which segment should we investigate first?
- What should be tested next?
- Which KPI should be monitored weekly?

## 8. Design Rationale

The dashboard should not start from chart types. It should start from agreed journey events, required properties, and validation rules. This prevents stakeholders from making decisions based on broken or incomplete tracking.
