from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "dashboard_screenshots"
OUT.mkdir(parents=True, exist_ok=True)

events = pd.read_csv(ROOT / "data" / "raw_web_events_sample.csv", parse_dates=["event_time"])
products = pd.read_csv(ROOT / "data" / "products_sample.csv")
events["event_date"] = events["event_time"].dt.date
events["revenue"] = events["revenue"].fillna(0)

session_flags = (
    events.groupby(["event_date", "channel", "device", "session_id"], as_index=False)
    .agg(
        viewed_product=("event_name", lambda s: int((s == "view_item").any())),
        added_to_cart=("event_name", lambda s: int((s == "add_to_cart").any())),
        began_checkout=("event_name", lambda s: int((s == "begin_checkout").any())),
        purchased=("event_name", lambda s: int((s == "purchase").any())),
        revenue=("revenue", "sum"),
    )
)

product_perf = (
    events.merge(products, on="product_id", how="left")
    .groupby(["product_id", "product_name"], as_index=False)
    .agg(
        view_sessions=("session_id", lambda s: s[events.loc[s.index, "event_name"].eq("view_item")].nunique()),
        add_to_cart_sessions=("session_id", lambda s: s[events.loc[s.index, "event_name"].eq("add_to_cart")].nunique()),
        purchase_sessions=("session_id", lambda s: s[events.loc[s.index, "event_name"].eq("purchase")].nunique()),
        revenue=("revenue", "sum"),
    )
)
product_perf["view_to_purchase_rate"] = product_perf["purchase_sessions"] / product_perf["view_sessions"]

total_sessions = session_flags["session_id"].nunique()
product_views = session_flags["viewed_product"].sum()
adds = session_flags["added_to_cart"].sum()
checkouts = session_flags["began_checkout"].sum()
purchases = session_flags["purchased"].sum()
revenue = session_flags["revenue"].sum()
conversion = purchases / total_sessions

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "axes.edgecolor": "#d9dee7",
        "axes.labelcolor": "#5f6b7a",
        "xtick.color": "#5f6b7a",
        "ytick.color": "#5f6b7a",
        "text.color": "#1f2937",
        "figure.facecolor": "#f7f8fb",
        "axes.facecolor": "#ffffff",
    }
)

ACCENT = "#1f5f8b"
ACCENT_2 = "#2f9e8f"
ACCENT_3 = "#e6a23c"
MUTED = "#5f6b7a"
LINE = "#d9dee7"


def add_card(fig, xy, width, height, title, value, sub=""):
    ax = fig.add_axes([xy[0], xy[1], width, height])
    ax.axis("off")
    box = FancyBboxPatch(
        (0, 0),
        1,
        1,
        boxstyle="round,pad=0.018,rounding_size=0.04",
        linewidth=1,
        edgecolor=LINE,
        facecolor="#ffffff",
    )
    ax.add_patch(box)
    ax.text(0.06, 0.68, title, fontsize=10, color=MUTED, weight="bold", va="center")
    ax.text(0.06, 0.34, value, fontsize=20, color="#1f2937", weight="bold", va="center")
    if sub:
        ax.text(0.06, 0.14, sub, fontsize=8.5, color=MUTED, va="center")
    return ax


def save_dashboard_overview():
    fig = plt.figure(figsize=(16, 9), dpi=160)
    fig.text(0.04, 0.94, "E-commerce Web Analytics Dashboard", fontsize=22, weight="bold")
    fig.text(
        0.04,
        0.905,
        "Sample output from public-safe event data: tracking events -> gold KPI tables -> stakeholder-ready reporting",
        fontsize=10.5,
        color=MUTED,
    )

    add_card(fig, (0.04, 0.765), 0.16, 0.105, "Sessions", f"{total_sessions:,}", "distinct session_id")
    add_card(fig, (0.22, 0.765), 0.16, 0.105, "Purchases", f"{purchases:,}", f"{conversion:.1%} conversion")
    add_card(fig, (0.40, 0.765), 0.16, 0.105, "Revenue", f"DKK {revenue:,.0f}", "purchase events")
    add_card(fig, (0.58, 0.765), 0.16, 0.105, "View -> Cart", f"{adds / product_views:.1%}", "session level")
    add_card(fig, (0.76, 0.765), 0.16, 0.105, "Cart -> Purchase", f"{purchases / adds:.1%}", "session level")

    ax_funnel = fig.add_axes([0.04, 0.42, 0.40, 0.27])
    steps = ["Product view", "Add to cart", "Checkout", "Purchase"]
    vals = [product_views, adds, checkouts, purchases]
    colors = [ACCENT, ACCENT_2, ACCENT_3, "#c95f4f"]
    ax_funnel.barh(steps[::-1], vals[::-1], color=colors[::-1])
    ax_funnel.set_title("Funnel by Session", loc="left", fontsize=13, weight="bold")
    ax_funnel.set_xlabel("Sessions")
    ax_funnel.grid(axis="x", color="#edf0f4", linewidth=0.8)
    for i, value in enumerate(vals[::-1]):
        ax_funnel.text(value + 0.08, i, f"{value}", va="center", fontsize=10)
    ax_funnel.spines[["top", "right", "left"]].set_visible(False)

    ax_channel = fig.add_axes([0.52, 0.42, 0.40, 0.27])
    channel = session_flags.groupby("channel", as_index=False).agg(sessions=("session_id", "nunique"), revenue=("revenue", "sum"))
    channel = channel.sort_values("revenue", ascending=False)
    ax_channel.bar(channel["channel"], channel["revenue"], color=ACCENT)
    ax_channel.set_title("Revenue by Channel", loc="left", fontsize=13, weight="bold")
    ax_channel.set_ylabel("DKK")
    ax_channel.grid(axis="y", color="#edf0f4", linewidth=0.8)
    for i, value in enumerate(channel["revenue"]):
        ax_channel.text(i, value + 20, f"{value:.0f}", ha="center", fontsize=9)
    ax_channel.spines[["top", "right"]].set_visible(False)

    ax_product = fig.add_axes([0.04, 0.10, 0.88, 0.22])
    product_sorted = product_perf.sort_values("revenue", ascending=False)
    ax_product.bar(product_sorted["product_name"], product_sorted["view_sessions"], label="View", color="#9fc4d7")
    ax_product.bar(product_sorted["product_name"], product_sorted["purchase_sessions"], label="Purchase", color=ACCENT)
    ax_product.set_title("Product Attention vs Purchase Sessions", loc="left", fontsize=13, weight="bold")
    ax_product.set_ylabel("Sessions")
    ax_product.legend(frameon=False, ncol=2, loc="upper right")
    ax_product.grid(axis="y", color="#edf0f4", linewidth=0.8)
    ax_product.spines[["top", "right"]].set_visible(False)
    plt.savefig(OUT / "dashboard_overview.png", bbox_inches="tight")
    plt.close(fig)


def save_funnel_analysis():
    fig, ax = plt.subplots(figsize=(11, 6), dpi=160)
    fig.text(0.06, 0.94, "Funnel Analysis", fontsize=20, weight="bold")
    fig.text(0.06, 0.895, "Session-level flags reduce overcounting from repeated events.", fontsize=10.5, color=MUTED)

    steps = ["Product view", "Add to cart", "Checkout", "Purchase"]
    vals = [product_views, adds, checkouts, purchases]
    y = range(len(steps))
    ax.barh(list(y), vals, color=[ACCENT, ACCENT_2, ACCENT_3, "#c95f4f"])
    ax.set_yticks(list(y), steps)
    ax.invert_yaxis()
    ax.set_xlabel("Sessions")
    ax.grid(axis="x", color="#edf0f4")
    ax.spines[["top", "right", "left"]].set_visible(False)
    for idx, value in enumerate(vals):
        rate = value / vals[0] if vals[0] else 0
        ax.text(value + 0.08, idx, f"{value} sessions ({rate:.0%} of views)", va="center", fontsize=10)

    ax.text(
        0.02,
        -0.22,
        "Interpretation example: if checkout sessions are low relative to add-to-cart sessions, validate checkout event coverage before treating it as UX friction.",
        transform=ax.transAxes,
        fontsize=10,
        color=MUTED,
    )
    plt.tight_layout(rect=[0.04, 0.08, 0.98, 0.86])
    plt.savefig(OUT / "funnel_analysis.png", bbox_inches="tight")
    plt.close(fig)


def save_product_performance():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), dpi=160)
    fig.suptitle("Product Performance", fontsize=20, weight="bold", x=0.06, ha="left")

    product_sorted = product_perf.sort_values("revenue", ascending=True)
    axes[0].barh(product_sorted["product_name"], product_sorted["revenue"], color=ACCENT)
    axes[0].set_title("Revenue by Product", loc="left", fontsize=13, weight="bold")
    axes[0].set_xlabel("DKK")
    axes[0].grid(axis="x", color="#edf0f4")
    axes[0].spines[["top", "right", "left"]].set_visible(False)

    rate_sorted = product_perf.sort_values("view_to_purchase_rate", ascending=True)
    axes[1].barh(rate_sorted["product_name"], rate_sorted["view_to_purchase_rate"], color=ACCENT_2)
    axes[1].set_title("View-to-Purchase Rate", loc="left", fontsize=13, weight="bold")
    axes[1].set_xlabel("Rate")
    axes[1].set_xlim(0, 0.7)
    axes[1].grid(axis="x", color="#edf0f4")
    axes[1].spines[["top", "right", "left"]].set_visible(False)
    axes[1].xaxis.set_major_formatter(lambda x, pos: f"{x:.0%}")

    for ax in axes:
        ax.tick_params(axis="y", length=0)

    fig.text(
        0.06,
        0.03,
        "Analytical use: identify products with high attention but weak purchase conversion for content, pricing, availability, or checkout follow-up.",
        fontsize=10,
        color=MUTED,
    )
    plt.tight_layout(rect=[0.04, 0.08, 0.98, 0.9])
    plt.savefig(OUT / "product_performance.png", bbox_inches="tight")
    plt.close(fig)


def save_pipeline():
    fig, ax = plt.subplots(figsize=(14, 4.8), dpi=160)
    ax.axis("off")
    fig.text(0.04, 0.9, "Analytics Pipeline", fontsize=20, weight="bold")
    fig.text(0.04, 0.84, "Production-style flow demonstrated with public-safe sample data", fontsize=10.5, color=MUTED)

    labels = [
        ("Tracking Plan", "event taxonomy\nrequired properties\nQA rules"),
        ("Raw Events", "web events\nsessions\nproducts"),
        ("Silver Clean Events", "standardized fields\nvalidated IDs\nevent dates"),
        ("Gold KPI Tables", "funnel KPIs\nproduct performance\nchannel/device"),
        ("Power BI", "dashboard pages\nDAX measures\nstakeholder view"),
    ]
    xs = [0.04, 0.235, 0.43, 0.625, 0.82]
    for i, (title, body) in enumerate(labels):
        rect = FancyBboxPatch(
            (xs[i], 0.32),
            0.145,
            0.36,
            boxstyle="round,pad=0.018,rounding_size=0.025",
            linewidth=1.2,
            edgecolor=LINE,
            facecolor="#ffffff",
            transform=ax.transAxes,
        )
        ax.add_patch(rect)
        ax.text(xs[i] + 0.0725, 0.59, title, ha="center", va="center", fontsize=11, weight="bold", transform=ax.transAxes)
        ax.text(xs[i] + 0.0725, 0.45, body, ha="center", va="center", fontsize=9, color=MUTED, transform=ax.transAxes)
        if i < len(labels) - 1:
            ax.annotate(
                "",
                xy=(xs[i + 1] - 0.015, 0.5),
                xytext=(xs[i] + 0.16, 0.5),
                xycoords=ax.transAxes,
                arrowprops=dict(arrowstyle="->", color=ACCENT, lw=2),
            )

    ax.text(
        0.04,
        0.12,
        "QA principle: validate tracking and data completeness before interpreting funnel movement as a business issue.",
        fontsize=10,
        color=MUTED,
        transform=ax.transAxes,
    )
    plt.savefig(OUT / "analytics_pipeline.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    save_dashboard_overview()
    save_funnel_analysis()
    save_product_performance()
    save_pipeline()
    print(f"wrote images to {OUT}")
