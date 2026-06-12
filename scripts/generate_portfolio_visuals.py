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


def svg_header(width, height):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="large-scale ecommerce clickstream analytics visual">
  <rect width="100%" height="100%" fill="{BG}"/>
  <style>
    .title{{font:700 30px Arial, sans-serif;fill:{TEXT}}}
    .subtitle{{font:400 14px Arial, sans-serif;fill:{MUTED}}}
    .h{{font:700 16px Arial, sans-serif;fill:{TEXT}}}
    .label{{font:400 13px Arial, sans-serif;fill:{MUTED}}}
    .value{{font:700 25px Arial, sans-serif;fill:{TEXT}}}
    .small{{font:400 12px Arial, sans-serif;fill:{MUTED}}}
    .xs{{font:400 10px Arial, sans-serif;fill:{MUTED}}}
    .white{{fill:#ffffff}}
    .pill{{font:700 11px Arial, sans-serif;fill:#ffffff}}
  </style>
"""


def write(path, content):
    (OUT / path).write_text(content)


def save_dashboard_overview_svg():
    cards = [
        ("Events", "285M", "public clickstream"),
        ("Sessions", "42.6M", "modeled from user_session"),
        ("Purchase CVR", "5.1%", "session-level KPI"),
        ("Revenue Index", "100", "normalized for demo"),
        ("QA Readiness", "Review", "2 high checks"),
        ("Advanced Tables", "4", "cohort + scoring + monitoring"),
    ]
    weekly_points = [(0, 38), (1, 42), (2, 41), (3, 44), (4, 37), (5, 49), (6, 46), (7, 52), (8, 48), (9, 54), (10, 50), (11, 57)]
    heatmap = [
        [100, 36, 24, 18, 14, 10],
        [100, 34, 22, 17, 13, 9],
        [100, 39, 27, 19, 15, 11],
        [100, 31, 20, 16, 12, 8],
    ]
    products = [
        (50, 165, 8, ACCENT_4),
        (92, 118, 11, ACCENT_3),
        (132, 82, 15, ACCENT),
        (176, 143, 9, ACCENT_4),
        (218, 65, 13, ACCENT_2),
        (266, 110, 10, ACCENT_3),
        (310, 42, 16, ACCENT_2),
        (356, 132, 12, ACCENT_4),
    ]
    lines = [svg_header(1280, 940)]
    lines += [
        f'  <rect x="0" y="0" width="1280" height="86" fill="#172b36"/>',
        '  <text x="38" y="42" class="title white">E-commerce Clickstream Analytics Workbench</text>',
        '  <text x="38" y="66" class="subtitle white" opacity="0.78">Journey KPIs, retention, product friction, weekly monitoring, and data quality readiness</text>',
        f'  <rect x="1040" y="26" width="92" height="30" rx="15" fill="{ACCENT}"/>',
        '  <text x="1086" y="46" text-anchor="middle" class="pill">GOLD LAYER</text>',
        f'  <rect x="1144" y="26" width="96" height="30" rx="15" fill="{ACCENT_2}"/>',
        '  <text x="1192" y="46" text-anchor="middle" class="pill">POWER BI</text>',
        f'  <rect x="32" y="116" width="180" height="762" rx="12" fill="#ffffff" stroke="{LINE}"/>',
        '  <text x="56" y="152" class="h">Report filters</text>',
        '  <text x="56" y="186" class="label">Date range</text>',
        f'  <rect x="56" y="198" width="116" height="28" rx="7" fill="#edf5fa" stroke="{LINE}"/>',
        '  <text x="68" y="217" class="small">Oct 2019 - Apr 2020</text>',
        '  <text x="56" y="260" class="label">Category</text>',
        '  <text x="72" y="292" class="small">electronics</text>',
        '  <text x="72" y="322" class="small">appliances</text>',
        '  <text x="72" y="352" class="small">computers</text>',
        '  <text x="56" y="410" class="label">Monitoring flags</text>',
        f'  <circle cx="64" cy="442" r="5" fill="{ACCENT_4}"/><text x="78" y="446" class="small">conversion drop</text>',
        f'  <circle cx="64" cy="472" r="5" fill="{ACCENT_3}"/><text x="78" y="476" class="small">revenue drop</text>',
        f'  <circle cx="64" cy="502" r="5" fill="{ACCENT_2}"/><text x="78" y="506" class="small">positive movement</text>',
        '  <text x="56" y="575" class="label">Data contract</text>',
        '  <text x="56" y="603" class="small">Required: session, user,</text>',
        '  <text x="56" y="621" class="small">event, product, price.</text>',
        '  <text x="56" y="663" class="label">Interpretation rule</text>',
        '  <text x="56" y="691" class="small">Do not explain a funnel</text>',
        '  <text x="56" y="709" class="small">drop before QA checks.</text>',
    ]
    for i, (title, value, sub) in enumerate(cards):
        x = 240 + (i % 3) * 330
        y = 116 + (i // 3) * 104
        lines += [
            f'  <rect x="{x}" y="{y}" width="300" height="82" rx="12" fill="#fff" stroke="{LINE}"/>',
            f'  <text x="{x + 18}" y="{y + 27}" class="label">{title}</text>',
            f'  <text x="{x + 18}" y="{y + 58}" class="value">{value}</text>',
            f'  <text x="{x + 128}" y="{y + 58}" class="small">{sub}</text>',
        ]

    lines += [
        f'  <rect x="240" y="342" width="500" height="244" rx="12" fill="#fff" stroke="{LINE}"/>',
        '  <text x="264" y="376" class="h">Weekly conversion monitor</text>',
        '  <text x="264" y="398" class="small">Current conversion vs recent movement by week</text>',
        f'  <line x1="278" y1="540" x2="704" y2="540" stroke="{LINE}"/>',
        f'  <line x1="278" y1="430" x2="278" y2="540" stroke="{LINE}"/>',
    ]
    point_path = []
    for idx, (_, value) in enumerate(weekly_points):
        x = 290 + idx * 35
        y = 552 - value * 2.0
        point_path.append(f"{x},{y}")
        lines += [
            f'  <circle cx="{x}" cy="{y}" r="4" fill="{ACCENT}"/>',
        ]
    lines.append(f'  <polyline points="{" ".join(point_path)}" fill="none" stroke="{ACCENT}" stroke-width="3"/>')
    lines += [
        f'  <rect x="585" y="426" width="132" height="42" rx="8" fill="#f8e6e2" stroke="{ACCENT_4}"/>',
        '  <text x="600" y="451" class="small">Drop flag: -2.1 z</text>',
    ]
    funnel = [("View", 100, ACCENT), ("Cart", 22, ACCENT_2), ("Remove", 9, ACCENT_3), ("Purchase", 6, ACCENT_4)]
    lines += [
        f'  <rect x="770" y="342" width="430" height="244" rx="12" fill="#fff" stroke="{LINE}"/>',
        '  <text x="794" y="376" class="h">Session-level funnel</text>',
        '  <text x="794" y="398" class="small">Built from flags, not raw click counts</text>',
    ]
    for idx, (label, pct, color) in enumerate(funnel):
        y = 426 + idx * 35
        width = pct * 2.6
        lines += [
            f'  <text x="794" y="{y + 17}" class="small">{label}</text>',
            f'  <rect x="876" y="{y}" width="{width}" height="22" rx="5" fill="{color}"/>',
            f'  <text x="{890 + width}" y="{y + 16}" class="xs">{pct}%</text>',
        ]
    lines += [
        f'  <rect x="240" y="616" width="300" height="230" rx="12" fill="#fff" stroke="{LINE}"/>',
        '  <text x="264" y="650" class="h">Cohort retention heatmap</text>',
        '  <text x="264" y="672" class="small">First observed activity month x cohort age</text>',
        f'  <rect x="570" y="616" width="300" height="230" rx="12" fill="#fff" stroke="{LINE}"/>',
        '  <text x="594" y="650" class="h">Product friction scatter</text>',
        '  <text x="594" y="672" class="small">Attention vs conversion risk</text>',
        f'  <rect x="900" y="616" width="300" height="230" rx="12" fill="#fff" stroke="{LINE}"/>',
        '  <text x="924" y="650" class="h">Tracking quality scorecard</text>',
        '  <text x="924" y="672" class="small">Metric readiness before publication</text>',
    ]
    colors = ["#e8f3ef", "#bfe4d3", "#7cc8ad", "#2f9e8f", "#1f5f8b"]
    for r, row in enumerate(heatmap):
        lines.append(f'  <text x="264" y="{714 + r * 30}" class="xs">cohort {r + 1}</text>')
        for c, value in enumerate(row):
            color = colors[0 if value < 15 else 1 if value < 25 else 2 if value < 40 else 3 if value < 80 else 4]
            lines += [
                f'  <rect x="{330 + c * 30}" y="{696 + r * 30}" width="24" height="24" rx="4" fill="{color}"/>',
                f'  <text x="{342 + c * 30}" y="{712 + r * 30}" text-anchor="middle" class="xs white">{value}</text>',
            ]
    lines += [
        f'  <line x1="612" y1="806" x2="828" y2="806" stroke="{LINE}"/>',
        f'  <line x1="612" y1="694" x2="612" y2="806" stroke="{LINE}"/>',
        '  <text x="620" y="824" class="xs">view sessions</text>',
        '  <text x="594" y="706" class="xs">CVR</text>',
    ]
    for x_offset, y_offset, radius, color in products:
        lines.append(f'  <circle cx="{594 + x_offset}" cy="{666 + y_offset}" r="{radius}" fill="{color}" opacity="0.82"/>')
    score_rows = [
        ("missing session", "critical", "publish caveat"),
        ("unknown event", "high", "validate"),
        ("negative price", "medium", "review rows"),
        ("purchase no cart", "medium", "sequence check"),
    ]
    for idx, (check, severity, action) in enumerate(score_rows):
        y = 704 + idx * 31
        color = ACCENT_4 if severity == "critical" else ACCENT_3 if severity == "high" else ACCENT
        lines += [
            f'  <circle cx="932" cy="{y - 4}" r="5" fill="{color}"/>',
            f'  <text x="946" y="{y}" class="xs">{check}</text>',
            f'  <text x="1042" y="{y}" class="xs">{action}</text>',
        ]
    lines += [
        f'  <rect x="240" y="878" width="960" height="34" rx="10" fill="#ffffff" stroke="{LINE}"/>',
        '  <text x="264" y="900" class="small">Analyst interpretation: use advanced tables to separate journey friction, product issues, repeat behavior, KPI movement, and tracking readiness before recommending action.</text>',
        "</svg>",
    ]
    write("dashboard_overview.svg", "\n".join(lines))


def save_pipeline_svg():
    labels = [
        ("Public Dataset", "285M events\\nuser/session/product"),
        ("Bronze", "raw clickstream\\nsource schema"),
        ("Silver", "event mapping\\nvalidated fields"),
        ("Core Gold", "journey KPIs\\nproduct performance"),
        ("Advanced Gold", "cohort retention\\nfriction monitoring"),
        ("Power BI", "stakeholder views\\nreadiness notes"),
    ]
    x_positions = [40, 230, 420, 610, 800, 990]
    lines = [svg_header(1180, 520)]
    lines += [
        '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1f5f8b"/></marker></defs>',
        '  <text x="40" y="50" class="title">Analytics Pipeline and Decision Layer</text>',
        '  <text x="40" y="76" class="subtitle">Large public clickstream data modeled into reusable KPI, prioritization, monitoring, and QA outputs</text>',
    ]
    for idx, (title, body) in enumerate(labels):
        x = x_positions[idx]
        body_lines = body.split("\\n")
        lines += [
            f'  <rect x="{x}" y="130" width="150" height="118" rx="12" fill="#fff" stroke="{LINE}"/>',
            f'  <text x="{x + 75}" y="170" text-anchor="middle" class="h">{title}</text>',
            f'  <text x="{x + 75}" y="202" text-anchor="middle" class="small">{body_lines[0]}</text>',
            f'  <text x="{x + 75}" y="222" text-anchor="middle" class="small">{body_lines[1]}</text>',
        ]
        if idx < len(labels) - 1:
            lines.append(f'  <path d="M{x + 156} 190 L{x + 184} 190" stroke="{ACCENT}" stroke-width="3" marker-end="url(#arrow)"/>')
    lines += [
        f'  <rect x="40" y="310" width="1100" height="140" rx="12" fill="#fff" stroke="{LINE}"/>',
        '  <text x="70" y="346" class="h">Advanced tables added</text>',
        f'  <rect x="70" y="372" width="225" height="42" rx="8" fill="#edf5fa"/><text x="86" y="398" class="small">gold_user_monthly_retention</text>',
        f'  <rect x="315" y="372" width="225" height="42" rx="8" fill="#eef4ef"/><text x="331" y="398" class="small">gold_product_friction_scores</text>',
        f'  <rect x="560" y="372" width="225" height="42" rx="8" fill="#f7ead2"/><text x="576" y="398" class="small">gold_weekly_category_monitoring</text>',
        f'  <rect x="805" y="372" width="250" height="42" rx="8" fill="#f8e6e2"/><text x="821" y="398" class="small">gold_tracking_quality_scorecard</text>',
        '  <text x="70" y="444" class="small">QA principle: do not interpret journey drop-off until session IDs, event types, product IDs, and purchase prices are validated.</text>',
        "</svg>",
    ]
    write("analytics_pipeline.svg", "\n".join(lines))


def save_funnel_svg():
    funnel = [("View sessions", 100, ACCENT), ("Cart sessions", 22, ACCENT_2), ("Remove-from-cart sessions", 9, ACCENT_3), ("Purchase sessions", 6, ACCENT_4)]
    lines = [svg_header(1080, 640)]
    lines += [
        '  <text x="40" y="50" class="title">Customer Journey Funnel</text>',
        '  <text x="40" y="76" class="subtitle">Session-level modeling with QA caveats and decision notes</text>',
        f'  <rect x="40" y="115" width="690" height="330" rx="12" fill="#fff" stroke="{LINE}"/>',
    ]
    for idx, (label, pct, color) in enumerate(funnel):
        y = 160 + idx * 62
        width = pct * 4.6
        lines += [
            f'  <text x="70" y="{y + 24}" class="label">{label}</text>',
            f'  <rect x="275" y="{y}" width="{width}" height="34" rx="6" fill="{color}"/>',
            f'  <text x="{290 + width}" y="{y + 23}" class="small">{pct}%</text>',
        ]
    lines += [
        f'  <rect x="760" y="115" width="280" height="330" rx="12" fill="#fff" stroke="{LINE}"/>',
        '  <text x="785" y="150" class="h">Diagnostic follow-up</text>',
        f'  <circle cx="794" cy="190" r="5" fill="{ACCENT}"/><text x="812" y="195" class="small">Validate event sequence</text>',
        f'  <circle cx="794" cy="228" r="5" fill="{ACCENT_2}"/><text x="812" y="233" class="small">Check product content</text>',
        f'  <circle cx="794" cy="266" r="5" fill="{ACCENT_3}"/><text x="812" y="271" class="small">Inspect price/availability</text>',
        f'  <circle cx="794" cy="304" r="5" fill="{ACCENT_4}"/><text x="812" y="309" class="small">Review checkout friction</text>',
        '  <text x="785" y="366" class="small">Interpretation is staged:</text>',
        '  <text x="785" y="388" class="small">tracking first, then product,</text>',
        '  <text x="785" y="410" class="small">then commercial action.</text>',
        f'  <rect x="40" y="485" width="1000" height="84" rx="12" fill="#fff" stroke="{LINE}"/>',
        '  <text x="70" y="520" class="h">Stakeholder note</text>',
        '  <text x="70" y="548" class="small">High views with weak cart or purchase movement should trigger category, pricing, availability, UX, and tracking checks before recommending action.</text>',
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
    lines = [svg_header(1100, 640)]
    lines += [
        '  <text x="40" y="50" class="title">Product Friction and Category Performance</text>',
        '  <text x="40" y="76" class="subtitle">Prioritizing products with high attention but weak purchase movement</text>',
        f'  <rect x="40" y="112" width="620" height="380" rx="12" fill="#fff" stroke="{LINE}"/>',
        '  <text x="70" y="146" class="h">Top friction candidates</text>',
        '  <text x="275" y="180" class="small">Revenue index</text>',
        '  <text x="540" y="180" class="small">CVR index</text>',
    ]
    for idx, (category, revenue, conversion) in enumerate(rows):
        y = 210 + idx * 52
        lines += [
            f'  <text x="70" y="{y + 17}" class="label">{category}</text>',
            f'  <rect x="275" y="{y}" width="{revenue * 2.0}" height="22" rx="4" fill="{ACCENT}"/>',
            f'  <text x="{284 + revenue * 2.0}" y="{y + 17}" class="small">{revenue}</text>',
            f'  <rect x="540" y="{y}" width="{conversion * 5.0}" height="22" rx="4" fill="{ACCENT_2}"/>',
            f'  <text x="{550 + conversion * 5.0}" y="{y + 17}" class="small">{conversion}</text>',
        ]
    lines += [
        f'  <rect x="700" y="112" width="350" height="380" rx="12" fill="#fff" stroke="{LINE}"/>',
        '  <text x="728" y="146" class="h">Friction score components</text>',
        f'  <rect x="730" y="188" width="180" height="24" rx="5" fill="{ACCENT}"/><text x="925" y="205" class="small">attention percentile</text>',
        f'  <rect x="730" y="236" width="130" height="24" rx="5" fill="{ACCENT_2}"/><text x="875" y="253" class="small">weak view-to-cart</text>',
        f'  <rect x="730" y="284" width="142" height="24" rx="5" fill="{ACCENT_3}"/><text x="887" y="301" class="small">weak cart-to-purchase</text>',
        f'  <rect x="730" y="332" width="86" height="24" rx="5" fill="{ACCENT_4}"/><text x="831" y="349" class="small">remove pressure</text>',
        '  <text x="728" y="410" class="small">Output is a review queue, not proof of cause.</text>',
        f'  <rect x="40" y="530" width="1010" height="64" rx="12" fill="#fff" stroke="{LINE}"/>',
        '  <text x="70" y="568" class="small">Analytical use: identify products with high browsing activity but weak purchase movement for product, pricing, content, availability, or tracking follow-up.</text>',
        "</svg>",
    ]
    write("product_performance.svg", "\n".join(lines))


if __name__ == "__main__":
    save_dashboard_overview_svg()
    save_pipeline_svg()
    save_funnel_svg()
    save_product_svg()
    print(f"wrote visuals to {OUT}")
