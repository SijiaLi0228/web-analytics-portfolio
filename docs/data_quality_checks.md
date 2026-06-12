# Data Quality Checks

This document explains the data quality layer behind the web analytics portfolio. The SQL implementation is in [`sql/05_data_quality_checks.sql`](../sql/05_data_quality_checks.sql).

## Why This Matters

Funnel analysis can be misleading when tracking data is incomplete. A low conversion rate may reflect a real customer journey issue, but it may also come from missing session IDs, broken event names, duplicated events, or missing product information.

The purpose of this QA step is to separate tracking quality from business performance before sharing dashboard conclusions.

## QA Checks

| Check | Business risk if ignored | What I would do next |
|---|---|---|
| Missing session IDs | Funnel steps cannot be connected into journeys | Review tracking setup and exclude invalid rows from journey KPIs |
| Unknown event types | Event taxonomy is inconsistent, making metrics unreliable | Map expected events and flag unexpected values for review |
| Missing product IDs on product events | Product and category performance may be undercounted | Validate product payloads in tracking or source export |
| Negative prices | Revenue and average price metrics become misleading | Remove or investigate rows before dashboarding |
| Duplicate generated event IDs | Events may be overcounted | Deduplicate or inspect ingestion logic |
| Purchases with no prior cart event | Could indicate missing cart tracking or a valid direct purchase path | Compare by category/product and validate tracking sequence |

## QA Logic

The checks are designed around the question:

```text
Can the data support a business decision, or do we need to fix/understand tracking first?
```

The SQL file checks the cleaned silver table before results are used in gold KPI tables or dashboards.

## How I Would Communicate QA Results

I would not present the dashboard as final if the QA checks reveal material issues. Instead, I would separate the message into two layers:

1. Data quality finding: what is missing, duplicated, or inconsistent.
2. Business finding: what appears to be true after known tracking limitations are accounted for.

Example:

```text
Category A has a low cart-to-purchase rate, but 18% of its purchase sessions have no recorded cart event. I would validate cart-event tracking before concluding that checkout friction is the main issue.
```

This makes the analysis more trustworthy and gives stakeholders a clearer next action.
