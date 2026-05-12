# Event Taxonomy

This event taxonomy defines how the public clickstream source events are interpreted for web analytics reporting.

The dataset contains product-level behavior. The taxonomy normalizes raw source events into journey steps that can support funnel, product, and category analysis.

## Core Journey Events

| Source event | Normalized event name | Trigger | Required properties | Business question | QA rule |
|---|---|---|---|---|---|
| `view` | `view_item` | Product was viewed | `event_time`, `product_id`, `user_id`, `user_session` | Which products receive attention? | `product_id` and `user_session` should not be null |
| `cart` | `add_to_cart` | Product was added to cart | `event_time`, `product_id`, `user_id`, `user_session` | Which products move from interest to intent? | Should usually happen after a product view in the same session |
| `remove_from_cart` | `remove_from_cart` | Product was removed from cart | `event_time`, `product_id`, `user_id`, `user_session` | Where might cart friction appear? | Should usually follow a cart event |
| `purchase` | `purchase` | Product was purchased | `event_time`, `product_id`, `user_id`, `user_session`, `price` | What converts to revenue? | Price should be non-negative |

## Optional Matomo / GA Events Not Present in Source

The selected public dataset does not include every event a company would normally track. In a production Matomo setup, I would also define:

| Event name | Why it would matter |
|---|---|
| `site_search` | Search demand and search-result quality |
| `promotion_click` | Campaign and placement engagement |
| `begin_checkout` | Checkout intent before purchase |
| `checkout_error` | Checkout friction and technical issues |
| `lead_form_submit` | Lead generation performance |

These are listed as production tracking extensions, not as fields invented in the public dataset.

## Segmentation Properties

Available in the selected dataset:

- product_id
- category_id
- category_code
- brand
- price
- user_id
- user_session
- event_date
- event_month

Optional enrichment fields for a real company setup:

- channel
- campaign
- device
- country
- new vs returning visitor
- promotion name

## Data Quality Rules

- Every event should have `event_time`, `event_type`, `user_id`, and `user_session`.
- Product-related events should have `product_id`.
- Purchase events should have non-negative `price`.
- Unknown event types should be reviewed before modeling.
- Sudden changes in event volume should be checked against tracking releases or site changes.
- Sessions with purchases but no earlier cart or view event should be treated carefully before drawing business conclusions.

## Stakeholder Questions Supported

This taxonomy supports questions such as:

- Which products generate interest but do not convert?
- Which category has the weakest journey step?
- Is a conversion issue caused by user behavior, tracking quality, or product/checkout friction?
- Which event should be monitored weekly?
