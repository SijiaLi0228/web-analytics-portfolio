# Event Taxonomy

This event taxonomy defines the core e-commerce events used in the portfolio.

| Event name | Trigger | Required properties | Business question | QA rule |
|---|---|---|---|---|
| `view_item` | Product page loaded | `event_id`, `session_id`, `user_id`, `event_time`, `product_id`, `channel`, `device` | Which products receive attention? | `product_id` should not be null |
| `add_to_cart` | Add-to-cart button clicked | `event_id`, `session_id`, `user_id`, `event_time`, `product_id` | Which products move from interest to intent? | Should usually happen after `view_item` in the same session |
| `begin_checkout` | Checkout journey started | `event_id`, `session_id`, `user_id`, `event_time`, `product_id` | Where does checkout intent begin? | `session_id` should not be null |
| `purchase` | Order confirmed | `event_id`, `session_id`, `user_id`, `event_time`, `product_id`, `order_id`, `revenue` | What converts to sales? | `order_id` should be unique and revenue should be non-negative |

## Tracking Notes

The event names are inspired by common web analytics tools such as Matomo and Google Analytics. The goal is to keep event definitions consistent so downstream funnel metrics can be trusted.

## Segmentation Properties

Useful segmentation fields:

- channel
- device
- country
- product_id
- category
- session_id
- user_id
- event_date

## Data Quality Rules

- Every event must have `event_id`, `session_id`, and `event_time`.
- Product-related events should have `product_id`.
- Purchase events should have `order_id` and non-negative `revenue`.
- Duplicate `event_id` values should be investigated.
- Sudden changes in event volume should be checked against tracking releases or site changes.
