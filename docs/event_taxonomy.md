# Event Taxonomy

This event taxonomy defines the core e-commerce events used in the portfolio.

The goal is to make funnel reporting reliable by agreeing on event names, triggers, required properties, and quality rules before building dashboards.

## Core Funnel Events

| Event name | Trigger | Required properties | Business question | QA rule |
|---|---|---|---|---|
| `view_item` | Product page loaded | `event_id`, `session_id`, `user_id`, `event_time`, `product_id`, `channel`, `device` | Which products receive attention? | `product_id` should not be null |
| `add_to_cart` | Add-to-cart button clicked | `event_id`, `session_id`, `user_id`, `event_time`, `product_id`, `quantity` | Which products move from interest to intent? | Should usually happen after `view_item` in the same session |
| `begin_checkout` | Checkout journey started | `event_id`, `session_id`, `user_id`, `event_time`, `product_id`, `cart_value` | Where does checkout intent begin? | `session_id` should not be null |
| `purchase` | Order confirmed | `event_id`, `session_id`, `user_id`, `event_time`, `product_id`, `order_id`, `revenue` | What converts to sales? | `order_id` should be unique and revenue should be non-negative |

## Supporting Events

| Event name | Trigger | Useful properties | Why it matters |
|---|---|---|---|
| `site_search` | Search form submitted | `search_term`, `results_count`, `session_id` | Helps identify demand and search friction |
| `promotion_click` | Promotion or banner clicked | `campaign`, `placement`, `session_id` | Connects campaign exposure to behavior |
| `filter_used` | Product filter applied | `filter_type`, `filter_value`, `session_id` | Helps explain product discovery behavior |
| `checkout_error` | Checkout error shown | `error_type`, `checkout_step`, `session_id` | Helps diagnose checkout drop-off |

## Tracking Notes

The event names are inspired by common web analytics tools such as Matomo and Google Analytics. The goal is to keep event definitions consistent so downstream funnel metrics can be trusted.

## Segmentation Properties

Useful segmentation fields:

- channel
- campaign
- device
- country
- product_id
- category
- session_id
- user_id
- event_date
- new vs returning visitor
- promotion name

## Acceptance Criteria

Before using the events in reporting, I would check:

- each event has a clear business purpose
- event names follow one naming convention
- required properties are populated
- product IDs match the product catalog
- purchase revenue matches order data
- mobile and desktop tracking follow the same rules
- consent and privacy requirements are respected

## Data Quality Rules

- Every event must have `event_id`, `session_id`, and `event_time`.
- Product-related events should have `product_id`.
- Purchase events should have `order_id` and non-negative `revenue`.
- Duplicate `event_id` values should be investigated.
- Sudden changes in event volume should be checked against tracking releases or site changes.
- Sessions with purchase but no checkout or add-to-cart event should be reviewed before drawing business conclusions.

## Stakeholder Questions Supported

This taxonomy supports questions such as:

- Which products generate interest but do not convert?
- Which channel or device has the weakest funnel step?
- Is a conversion issue caused by user behavior, tracking quality, or checkout friction?
- Which events should be monitored weekly?
