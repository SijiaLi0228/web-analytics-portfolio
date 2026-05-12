from pathlib import Path

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


def header(width, height):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="large-scale ecommerce clickstream analytics visual">
  <rect width="100%" height="100%" fill="{BG}"/>
  <style>
    .title{{font:700 28px Arial, sans-serif;fill:{TEXT}}}
    .subtitle{{font:400 14px Arial, sans-serif;fill:{MUTED}}}
    .h{{font:700 16px Arial, sans-serif;fill:{TEXT}}}
    .label{{font:400 13px Arial, sans-serif;fill:{MUTED}}}
    .value{{font:700 24px Arial, sans-serif;fill:{TEXT}}}
    .small{{font:400 12px Arial, sans-serif;fill:{MUTED}}}
  </style>
'''


def write(name, lines):
    (OUT / name).write_text("\n".join(lines) + "\n")


def dashboard_overview():
    cards = [
        ("Dataset Scale", "285M", "public clickstream events"),
        ("Time Range", "7 months", "Oct 2019 - Apr 2020"),
        ("Granularity", "event-level", "user + session + product"),
        ("Journey Events", "4 types", "view, cart, remove, purchase"),
        ("Gold Tables", "2 core", "journey + product KPIs"),
    ]
    lines = [header(900, 1030)]
    lines += [
        '  <text x="40" y="50" class="title">Large-Scale E-commerce Clickstream Dashboard</text>',
        '  <text x="40" y="76" class="subtitle">Public dataset workflow: raw events -&gt; silver validated events -&gt; gold KPI tables -&gt; Power BI insights</text>',
    ]
    for i, (title, value, sub) in enumerate(cards):
        x = 40 + (i % 3) * 275
        y = 105 + (i // 3) * 118
        lines += [
            f'  <rect x="{x}" y="{y}" width="250" height="96" rx="10" fill="#fff" stroke="{LINE}"/>',
            f'  <text x="{x + 18}" y="{y + 28}" class="label">{title}</text>',
            f'  <text x="{x + 18}" y="{y + 61}" class="value">{value}</text>',
            f'  <text x="{x + 18}" y="{y + 84}" class="small">{sub}</text>',
        ]

    lines += [
        f'  <rect x="40" y="345" width="820" height="270" rx="10" fill="#fff" stroke="{LINE}"/>',
        '  <text x="64" y="380" class="h">Customer Journey Funnel</text>',
        '  <text x="64" y="402" class="small">Illustrative rates after SQL aggregation by session</text>',
    ]
    for label, pct, color, y in [
        ("Product view", 100, ACCENT, 438),
        ("Add to cart", 18, ACCENT_2, 483),
        ("Remove cart", 7, ACCENT_3, 528),
        ("Purchase", 5, ACCENT_4, 573),
    ]:
        width = pct * 4.2
        lines += [
            f'  <text x="64" y="{y + 17}" class="label">{label}</text>',
            f'  <rect x="245" y="{y}" width="{width:g}" height="24" rx="4" fill="{color}"/>',
            f'  <text x="{260 + width:g}" y="{y + 17}" class="small">{pct}%</text>',
        ]

    lines += [
        f'  <rect x="40" y="655" width="820" height="295" rx="10" fill="#fff" stroke="{LINE}"/>',
        '  <text x="64" y="690" class="h">Revenue Index by Category</text>',
        '  <text x="64" y="712" class="small">Designed for category-level stakeholder review</text>',
    ]
    for i, (category, value) in enumerate([("electronics", 100), ("appliances", 74), ("computers", 63), ("accessories", 42), ("unknown", 27)]):
        x = 120 + i * 145
        height = value * 1.35
        y = 905 - height
        lines += [
            f'  <rect x="{x}" y="{y:g}" width="58" height="{height:g}" rx="5" fill="{ACCENT}"/>',
            f'  <text x="{x + 29}" y="930" text-anchor="middle" class="small">{category}</text>',
            f'  <text x="{x + 29}" y="{y - 8:g}" text-anchor="middle" class="small">{value}</text>',
        ]
    lines += [
        '  <text x="40" y="995" class="small">Interpretation: separate product discovery, cart intent, purchase conversion, and data quality before making recommendations.</text>',
        '</svg>',
    ]
    write("dashboard_overview.svg", lines)


def analytics_pipeline():
    labels = [
        ("Public Dataset", "285M events", "user/session/product"),
        ("Bronze", "raw clickstream", "source schema"),
        ("Silver", "event mapping", "QA fields"),
        ("Gold", "journey KPIs", "product performance"),
        ("Power BI", "stakeholder views", "DAX measures"),
    ]
    lines = [header(940, 360)]
    lines += [
        '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1f5f8b"/></marker></defs>',
        '  <text x="40" y="50" class="title">Analytics Pipeline</text>',
        '  <text x="40" y="76" class="subtitle">Large public clickstream data modeled into dashboard-ready KPI tables</text>',
    ]
    for i, (title, line1, line2) in enumerate(labels):
        x = 40 + i * 180
        lines += [
            f'  <rect x="{x}" y="135" width="142" height="110" rx="10" fill="#fff" stroke="{LINE}"/>',
            f'  <text x="{x + 71}" y="176" text-anchor="middle" class="h">{title}</text>',
            f'  <text x="{x + 71}" y="205" text-anchor="middle" class="small">{line1}</text>',
            f'  <text x="{x + 71}" y="224" text-anchor="middle" class="small">{line2}</text>',
        ]
        if i < 4:
            lines.append(f'  <path d="M{x + 148} 190 L{x + 172} 190" stroke="{ACCENT}" stroke-width="3" marker-end="url(#arrow)"/>')
    lines += ['  <text x="40" y="315" class="small">QA principle: do not interpret journey drop-off until session IDs, event types, product IDs, and purchase prices are validated.</text>', '</svg>']
    write("analytics_pipeline.svg", lines)


def funnel_analysis():
    lines = [header(960, 500)]
    lines += [
        '  <text x="40" y="50" class="title">Customer Journey Funnel</text>',
        '  <text x="40" y="76" class="subtitle">Session-level modeling for large-scale product behavior events</text>',
    ]
    for label, pct, color, y in [
        ("View sessions", 100, ACCENT, 125),
        ("Cart sessions", 18, ACCENT_2, 195),
        ("Remove-from-cart sessions", 7, ACCENT_3, 265),
        ("Purchase sessions", 5, ACCENT_4, 335),
    ]:
        width = pct * 4.2
        lines += [
            f'  <text x="50" y="{y + 23}" class="label">{label}</text>',
            f'  <rect x="270" y="{y}" width="{width:g}" height="34" rx="5" fill="{color}"/>',
            f'  <text x="{285 + width:g}" y="{y + 23}" class="small">{pct}%</text>',
        ]
    lines += ['  <text x="40" y="430" class="small">Example use: high product views with weak cart or purchase movement should trigger category, pricing, availability, and tracking checks.</text>', '</svg>']
    write("funnel_analysis.svg", lines)


def product_performance():
    rows = [("electronics.smartphone", 100, 22), ("computers.notebook", 82, 15), ("appliances.kitchen", 74, 12), ("electronics.audio", 55, 9), ("accessories", 38, 4)]
    lines = [header(920, 520)]
    lines += [
        '  <text x="40" y="50" class="title">Product and Category Performance</text>',
        '  <text x="40" y="76" class="subtitle">Comparing attention, purchase movement, and revenue concentration</text>',
        f'  <rect x="40" y="110" width="840" height="330" rx="10" fill="#fff" stroke="{LINE}"/>',
        '  <text x="245" y="138" class="small">Revenue index</text>',
        '  <text x="610" y="138" class="small">View-to-purchase index</text>',
    ]
    for i, (category, revenue, conversion) in enumerate(rows):
        y = 165 + i * 55
        lines += [
            f'  <text x="65" y="{y + 17}" class="label">{category}</text>',
            f'  <rect x="245" y="{y}" width="{revenue * 2.4:g}" height="22" rx="4" fill="{ACCENT}"/>',
            f'  <text x="{255 + revenue * 2.4:g}" y="{y + 17}" class="small">{revenue}</text>',
            f'  <rect x="610" y="{y}" width="{conversion * 7.0:g}" height="22" rx="4" fill="{ACCENT_2}"/>',
            f'  <text x="{620 + conversion * 7.0:g}" y="{y + 17}" class="small">{conversion}</text>',
        ]
    lines += ['  <text x="40" y="480" class="small">Analytical use: identify categories with high browsing activity but weak purchase movement for product, pricing, content, or availability follow-up.</text>', '</svg>']
    write("product_performance.svg", lines)


if __name__ == "__main__":
    dashboard_overview()
    analytics_pipeline()
    funnel_analysis()
    product_performance()
    print(f"wrote visuals to {OUT}")
