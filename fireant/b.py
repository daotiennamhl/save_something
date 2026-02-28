import json
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

INPUT_FILE = "msn.json"
OUTPUT_IMAGE = "daily_net_and_price.png"

def parse_number(x):
    if x is None:
        return 0.0
    if isinstance(x, (int, float)):
        return float(x)
    try:
        s = str(x).replace(",", "").replace(" ", "").replace("VND", "")
        return float(s)
    except:
        return 0.0

def parse_date(s):
    if not s:
        return None
    for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%d/%m/%Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(s, fmt)
        except:
            continue
    try:
        return datetime.fromisoformat(s)
    except:
        return None

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def extract_rows(records):
    rows = []
    for rec in records:
        date_str = rec.get("date") or rec.get("tradeDate") or rec.get("day")
        date = parse_date(date_str)
        if not date:
            continue
        buy = parse_number(rec.get("buyForeignValue") or rec.get("foreignBuyValue") or rec.get("buyValue"))
        sell = parse_number(rec.get("sellForeignValue") or rec.get("foreignSellValue") or rec.get("sellValue"))
        close = parse_number(rec.get("closePrice") or rec.get("priceClose") or rec.get("close") or rec.get("close_price"))
        net = buy - sell
        rows.append((date, net, close))
    rows.sort(key=lambda x: x[0])
    return rows

def plot_combined(rows, outpath):
    dates = [r[0] for r in rows]
    nets = [r[1] for r in rows]
    closes = [r[2] for r in rows]

    fig, ax1 = plt.subplots(figsize=(14,7))

    # Bar chart for net purchases
    colors = ["#2ca02c" if v >= 0 else "#d62728" for v in nets]
    ax1.bar(dates, nets, color=colors, width=0.8, label="Net Purchases (buy - sell)")
    ax1.set_ylabel("Net Purchases (value)", color="#2f4f4f")
    ax1.tick_params(axis="y", labelcolor="#2f4f4f")

    # Zero line
    ax1.axhline(0, color="black", linewidth=0.8)

    # Secondary axis for close price
    ax2 = ax1.twinx()
    ax2.plot(dates, closes, color="#1f77b4", marker="o", linewidth=1.5, label="Close Price")
    ax2.set_ylabel("Close Price", color="#1f77b4")
    ax2.tick_params(axis="y", labelcolor="#1f77b4")

    # Formatting x-axis
    ax1.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax1.xaxis.set_major_formatter(mdates.ConciseDateFormatter(mdates.AutoDateLocator()))
    plt.xticks(rotation=45, ha="right")

    # Legends
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left")

    # Annotate top 3 absolute net days
    abs_nets = [abs(v) for v in nets]
    if len(nets) > 0:
        top_idx = sorted(range(len(nets)), key=lambda i: abs_nets[i], reverse=True)[:3]
        for i in top_idx:
            y = nets[i]
            ax1.annotate(f"{y:,.0f}", xy=(dates[i], y),
                         xytext=(0, 6 if y >= 0 else -12),
                         textcoords="offset points", ha="center", fontsize=8, color="black")

    plt.title("Daily Net Foreign Purchases and Close Price of VIX")
    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    plt.close()
    print(f"Saved chart to {outpath}")

def main():
    records = load_json(INPUT_FILE)
    rows = extract_rows(records)
    if not rows:
        print("No valid records found. Check JSON keys and date formats.")
        return
    plot_combined(rows, OUTPUT_IMAGE)

if __name__ == "__main__":
    main()
