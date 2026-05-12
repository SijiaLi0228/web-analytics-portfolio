from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "dashboard_screenshots"
OUT.mkdir(parents=True, exist_ok=True)

ACCENT = "#1f5f8b"
ACCENT_2 = "#2f9e8f"
ACCENT_3 = "#e6a23c"
ACCENT_4 = "#c95f4f"
MUTED = "#5f6b7a"
LINE = "#d9dee7"
BG = "#f7f8fb"
TEXT = "#1f2937"


def svg_header(width, height):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="large-scale ecommerce clickstream analytics visual">
  <rect width="100%" height="100%" fill="{BG}"/>
  <style>
    .title{{font:700 28px Arial, sans-serif;fill:{TEXT}}}
    .subtitle{{font:400 14px Arial, sans-serif;fill:{MUTED}}}
    .h{{font:700 16px Arial, sans-serif;fill:{TEXT}}}
    .label{{font:400 13px Arial, sans-serif;fill:{MUTED}}}
    .value{{font:700 24px Arial, sans-serif;fill:{TEXT}}}
    .small{{font:400 12px Arial, sans-serif;fill:{MUTED}}}
  </style>
"""


def write(path, content):
    (OUT / path).write_text(content)


def save_dashboard_overview_svg():
    cards = [
        ("Dataset Scale", "285M", "public clickstream events"),
        ("Time Range", "7 months", "Oct 2019 - Apr 2020"),
        ("Granularity", "event-level", "user + session + product"),
        ("Journey Events", "4 types", "view, cart, remove, purchase"),
        ("Gold Tables", "2 core", "journey + product KPIs"),
    ]
    category_revenue = [
        ("electronics", 100),
        ("appliances", 74),
        ("computers", 63),
        ("accessories", 42),
        ("unknown", 27),
    ]
    lines = [svg_header(980, 660)]
    lines += [
        '  <text x="40" y="50" class="title">Large-Scale E-commerce Clickstream Dashboard</text>',
        '  <text x="40" y="76" class="subtitle">Public dataset workflow: raw events -> silver validated events -> gold KPI tables -> Power BI insights</text>',
    ]
    for i, (title, value, sub) in enumerate(cards):
        x = 40 + i * 184
        lines += [
            f'  <rect x="{x}" y="105" width="164" height="100" rx="10" fill="#fff" stroke="{LINE}"/>',
            f'  <text x="{x + 16}" y="133" class="label">{title}</text>',
            f'  <text x="{x + 16}" y="167" class="value">{value}</text>',
            f'  <text x="{x + 16}" y="191" class="small">{sub}</text>',
        ]

    funnel = [("Product view", 100, ACCENT), ("Add to cart", 18, ACCENT_2), ("Remove cart", 7, ACCENT_3), ("Purchase", 5, ACCENT_4)]
    lines += [
        f'  <rect x="40" y="245" width="420" height="300" rx="10" fill="#fff" stroke="{LINE}"/>',
        '  <text x="64" y="280" class="h">Customer Journey Funnel</text>',
        '  <text x="64" y="302" class="small">Illustrative rates after SQL aggregation by session</text>',
    ]
    for idx, (label, pct, color) in enumerate(funnel):
        y = 340 + idx * 46
        width = pct * 3
        lines += [
            f'  <text x="64" y="{y + 17}" class="label">{label}</text>',
            f'  <rect x="185" y="{y}" width="{width}" height="24" rx="4" fill="{color}"/>',
            f'  <text x="{195 + width}" y="{y + 17}" class="small">{pct}%</text>',
        ]

    lines += [
        f'  <rect x="500" y="245" width="440" height="300" rx="10" fill="#fff" stroke="{LINE}"/>',
        '  <text x="524" y="280" class="h">Revenue Index by Category</text>',
        '  <text x="524" y="302" class="small">Designed for category-level stakeholder review</text>',
    ]
    for i, (category, value) in enumerate(category_revenue):
        x = 540 + i * 74
        height = value * 1.65
        y = 500 - height
        lines += [
            f'  <rect x="{x}" y="{y}" width="42" height="{height}" rx="4" fill="{ACCENT}"/>',
            f'  <text x="{x + 21}" y="520" text-anchor="middle" class="small">{category}</text>',
            f'  <text x="{x + 21}" y="{y - 8}" text-anchor="middle" class="small">{value}</text>',
        ]
    lines += [
        '  <text x="40" y="605" class="small">Interpretation: the analyst separates product discovery, cart intent, purchase conversion, and data quality before making recommendations.</text>',
        "</svg>",
    ]
    write("dashboard_overview.svg", "\n".join(lines))


def save_pipeline_svg():
    labels = [
        ("Public Dataset", "285M events\nuser/session/product"),
        ("Bronze", "raw clickstream\nsource schema"),
        ("Silver", "event mapping\nQA fields"),
        ("Gold", "journey KPIs\nproduct performance"),
        ("Power BI", "stakeholder views\nDAX measures"),
    ]
    x_positions = [40, 220, 400, 580, 760]
    lines = [svg_header(940, 360)]
    lines += [
        '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1f5f8b"/></marker></defs>',
        '  <text x="40" y="50" class="title">Analytics Pipeline</text>',
        '  <text x="40" y="76" class="subtitle">Large public clickstream data modeled into dashboard-ready KPI tables</text>',
    ]
    for idx, (title, body) in enumerate(labels):
        x = x_positions[idx]
        body_lines = body.split("\n")
        lines += [
            f'  <rect x="{x}" y="135" width="142" height="110" rx="10" fill="#fff" stroke="{LINE}"/>',
            f'  <text x="{x + 71}" y="176" text-anchor="middle" class="h">{title}</text>',
            f'  <text x="{x + 71}" y="205" text-anchor="middle" class="small">{body_lines[0]}</text>',
            f'  <text x="{x + 71}" y="224" text-anchor="middle" class="small">{body_lines[1]}</text>',
        ]
        if idx < len(labels) - 1:
            lines.append(f'  <path d="M{x + 148} 190 L{x + 172} 190" stroke="{ACCENT}" stroke-width="3" marker-end="url(#arrow)"/>')
    lines += [
        '  <text x="40" y="315" class="small">QA principle: do not interpret journey drop-off until session IDs, event types, product IDs, and purchase prices are validated.</text>',
        "</svg>",
    ]
    write("analytics_pipeline.svg", "\n".join(lines))


def save_funnel_svg():
    funnel = [("View sessions", 100, ACCENT), ("Cart sessions", 18, ACCENT_2), ("Remove-from-cart sessions", 7, ACCENT_3), ("Purchase sessions", 5, ACCENT_4)]
    lines = [svg_header(900, 480)]
    lines += [
        '  <text x="40" y="50" class="title">Customer Journey Funnel</text>',
        '  <text x="40" y="76" class="subtitle">Session-level modeling for large-scale product behavior events</text>',
    ]
    for idx, (label, pct, color) in enumerate(funnel):
        y = 125 + idx * 70
        width = pct * 5.8
        lines += [
            f'  <text x="50" y="{y + 23}" class="label">{label}</text>',
            f'  <rect x="240" y="{y}" width="{width}" height="34" rx="5" fill="{color}"/>',
            f'  <text x="{255 + width}" y="{y + 23}" class="small">{pct}% of product-view sessions</text>',
        ]
    lines += [
        '  <text x="40" y="425" class="small">Example use: high product views with weak cart or purchase movement should trigger category, pricing, availability, and tracking checks.</text>',
        "</svg>",
    ]
    write("funnel_analysis.svg", "\n".join(lines))


def save_product_svg():
    rows = [
        ("electronics.smartphone", 100, 22),
        ("computers.notebook", 82, 15),
        ("appliances.kitchen", 74, 12),
        ("electronics.audio", 55, 9),
        ("accessories", 38, 4),
    ]
    lines = [svg_header(920, 520)]
    lines += [
        '  <text x="40" y="50" class="title">Product and Category Performance</text>',
        '  <text x="40" y="76" class="subtitle">Comparing attention, purchase movement, and revenue concentration</text>',
        f'  <rect x="40" y="110" width="840" height="330" rx="10" fill="#fff" stroke="{LINE}"/>',
        '  <text x="245" y="138" class="small">Revenue index</text>',
        '  <text x="610" y="138" class="small">View-to-purchase index</text>',
    ]
    for idx, (category, revenue, conversion) in enumerate(rows):
        y = 165 + idx * 55
        lines += [
            f'  <text x="65" y="{y + 17}" class="label">{category}</text>',
            f'  <rect x="245" y="{y}" width="{revenue * 2.4}" height="22" rx="4" fill="{ACCENT}"/>',
            f'  <text x="{255 + revenue * 2.4}" y="{y + 17}" class="small">{revenue}</text>',
            f'  <rect x="610" y="{y}" width="{conversion * 7.0}" height="22" rx="4" fill="{ACCENT_2}"/>',
            f'  <text x="{620 + conversion * 7.0}" y="{y + 17}" class="small">{conversion}</text>',
        ]
    lines += [
        '  <text x="40" y="480" class="small">Analytical use: identify categories with high browsing activity but weak purchase movement for product, pricing, content, or availability follow-up.</text>',
        "</svg>",
    ]
    write("product_performance.svg", "\n".join(lines))


def save_png_placeholders():
    plt.rcParams.update({"font.family": "DejaVu Sans", "figure.facecolor": BG, "axes.facecolor": "#ffffff"})
    fig, ax = plt.subplots(figsize=(12, 6), dpi=160)
    ax.axis("off")
    box = FancyBboxPatch((0.03, 0.12), 0.94, 0.72, boxstyle="round,pad=0.02,rounding_size=0.02", linewidth=1, edgecolor=LINE, facecolor="#ffffff")
    ax.add_patch(box)
    ax.text(0.08, 0.70, "Large-Scale E-commerce Clickstream Portfolio", fontsize=20, weight="bold", color=TEXT)
    ax.text(0.08, 0.58, "285M public user events -> Databricks SQL -> Power BI-ready insights", fontsize=12, color=MUTED)
    ax.text(0.08, 0.45, "Core analysis: customer journey, product conversion, category performance, and data QA.", fontsize=12, color=MUTED)
    plt.savefig(OUT / "dashboard_overview.png", bbox_inches="tight")
    plt.savefig(OUT / "analytics_pipeline.png", bbox_inches="tight")
    plt.savefig(OUT / "funnel_analysis.png", bbox_inches="tight")
    plt.savefig(OUT / "product_performance.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    save_dashboard_overview_svg()
    save_pipeline_svg()
    save_funnel_svg()
    save_product_svg()
    save_png_placeholders()
    print(f"wrote visuals to {OUT}")
