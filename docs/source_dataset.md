# Source Dataset

## Selected Dataset

**eCommerce Behavior Data from Multi-Category Store**

- Public mirror: <https://huggingface.co/datasets/kevykibbz/ecommerce-behavior-data-from-multi-category-store_oct-nov_2019>
- Original dataset family: public e-commerce behavior data from a multi-category online store
- Scale: 285 million user events
- Time frame: October 2019 to April 2020
- Granularity: one row per product-related user event

## Why This Dataset Fits the Role

This project is intended for web analytics and product insights roles. The dataset is useful because it is not only an order table. It captures customer behavior before purchase.

| Role question | Dataset support |
|---|---|
| How do users move through the shopping journey? | `event_type`, `user_session`, `event_time` |
| Which products attract attention? | `product_id`, `category_code`, `brand`, `view` events |
| Which products convert? | `cart` and `purchase` events |
| Which categories create drop-off? | category-level funnel and conversion KPIs |
| Can reporting tables be trusted? | missing session, invalid price, event ordering, and duplicate checks |

## Source Fields

Expected source schema:

| Field | Description |
|---|---|
| `event_time` | Timestamp of the event |
| `event_type` | User action, such as `view`, `cart`, `remove_from_cart`, `purchase` |
| `product_id` | Product identifier |
| `category_id` | Numeric category identifier |
| `category_code` | Category path/code when available |
| `brand` | Product brand |
| `price` | Product price at event time |
| `user_id` | User identifier |
| `user_session` | Session identifier |

## Analytical Scope

This dataset supports:

- product view to cart analysis
- cart to purchase conversion
- category-level drop-off
- product-level revenue and conversion
- repeat user/session behavior
- price and brand analysis
- data quality checks before dashboarding

It does not include marketing channel, campaign, device, or country. If those fields are needed, they should come from a separate tracking source such as Matomo, GA4 export, ad platform data, or server-side enrichment.

## How This Maps to Matomo

The source dataset uses `event_type` values such as `view`, `cart`, and `purchase`. For dashboarding and stakeholder communication, this project normalizes them into web analytics event names:

| Source `event_type` | Normalized event name | Journey step |
|---|---|---|
| `view` | `view_item` | Product discovery |
| `cart` | `add_to_cart` | Shopping intent |
| `remove_from_cart` | `remove_from_cart` | Cart friction or reconsideration |
| `purchase` | `purchase` | Conversion |

This mirrors how a Matomo or GA-style tracking plan would define consistent event names and properties before data is modeled for reporting.
