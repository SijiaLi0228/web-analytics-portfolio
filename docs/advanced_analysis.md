# Advanced Analysis Layer

This document explains the additional analysis modules that make the project closer to a realistic analyst workflow. The goal is to move beyond basic funnel charts and show how event data can support prioritization, monitoring, and stakeholder decisions.

## Why Add This Layer

A simple dashboard can show that conversion is low. A stronger analytics project should help answer follow-up questions:

- Is the drop-off concentrated in specific products or categories?
- Are users returning, or is the business mostly attracting one-time browsers?
- Did a weekly KPI move unusually compared with recent history?
- Can the tracking data be trusted enough to present the metric?
- Which issue should a product, marketing, or operations team investigate first?

## Advanced Outputs

| Output | SQL file | Business use |
|---|---|---|
| User cohort retention | [`06_create_gold_user_cohort_retention.sql`](../sql/06_create_gold_user_cohort_retention.sql) | Understand whether users return after first observed activity month |
| Product friction score | [`07_create_gold_product_friction_scores.sql`](../sql/07_create_gold_product_friction_scores.sql) | Prioritize products with high attention but weak conversion or high cart removal |
| Weekly KPI monitoring | [`08_create_gold_weekly_kpi_monitoring.sql`](../sql/08_create_gold_weekly_kpi_monitoring.sql) | Flag category-level conversion or revenue movement against recent history |
| Tracking quality scorecard | [`09_create_gold_tracking_quality_scorecard.sql`](../sql/09_create_gold_tracking_quality_scorecard.sql) | Summarize whether dashboard KPIs are ready for stakeholder interpretation |

## 1. User Cohort Retention

The retention layer groups users by their first observed activity month and checks whether they remain active in later months.

This adds depth because it moves the analysis from isolated sessions to user behavior over time.

Example stakeholder question:

> Are we attracting repeat users, or are most users only active once?

How I would use it:

- compare retention across cohorts
- separate active users from purchasing users
- identify whether product/category improvements affect returning behavior
- avoid overclaiming because the public dataset does not include acquisition channel or customer profile fields

## 2. Product Friction Score

The product friction score ranks products that receive attention but do not convert well. It combines:

- view volume percentile
- weak view-to-cart behavior
- weak cart-to-purchase behavior
- remove-from-cart pressure

This is not a causal model. It is a prioritization tool.

Example stakeholder question:

> Which products should merchandising or product teams inspect first?

Suggested follow-up checks:

- product page content and images
- price competitiveness
- stock or delivery expectations
- category placement and search discoverability
- tracking completeness

## 3. Weekly KPI Monitoring

The weekly monitoring layer compares each category's current conversion and revenue against its recent four-week history.

This makes the dashboard more operational because stakeholders can see whether a movement is likely normal variation or worth investigating.

Example stakeholder question:

> Did this category perform unusually this week, and should we act on it?

The output uses monitoring flags such as:

- `Conversion drop to investigate`
- `Revenue drop to investigate`
- `Positive conversion movement`
- `Within expected range`
- `New / insufficient history`

## 4. Tracking Quality Scorecard

The tracking quality scorecard turns raw QA checks into a dashboard-readiness view. It connects each issue to:

- severity
- issue rate
- business risk
- recommended action
- dashboard readiness

This is important because a tracking issue can look like a business issue. A stronger analyst should be able to explain the difference.

## How This Raises the Project Difficulty

The project now demonstrates:

- session-level funnel logic
- product-level prioritization scoring
- user cohort and retention modeling
- weekly KPI monitoring using rolling baselines
- data quality scorecarding
- dashboard interpretation with caveats and next actions

This is closer to how analytics work is actually used inside a company: not only to show charts, but to help teams decide where to investigate, what to trust, and what to monitor next.
