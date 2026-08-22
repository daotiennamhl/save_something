import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

STOCK_CODES = ["gas", "gex", "hdb"]
OUTPUT_DIR = Path(__file__).resolve().parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


def parse_date(value):
    if value is None:
        return None
    return datetime.fromisoformat(str(value).replace("Z", "+00:00"))




def build_periods(stock_code):
    data_path = Path(__file__).resolve().parent / "json_file" / f"{stock_code}.json"
    with data_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    net_values = []
    for item in data:
        dt = parse_date(item["date"])
        if dt is None:
            continue
        net = float(item.get("buyForeignValue", 0.0)) - float(item.get("sellForeignValue", 0.0))
        net_values.append({
            "date": dt,
            "net": net,
            "symbol": item.get("symbol"),
        })

    def group_by_period(items, mode):
        grouped = defaultdict(float)
        labels = {}

        for item in items:
            dt = item["date"]
            if mode == "week":
                key = f"{dt.isocalendar()[0]}-W{dt.isocalendar()[1]:02d}"
                label = f"{dt.year}-W{dt.isocalendar()[1]:02d}"
            elif mode == "month":
                key = dt.strftime("%Y-%m")
                label = dt.strftime("%Y-%m")
            elif mode == "year":
                key = str(dt.year)
                label = str(dt.year)
            else:
                raise ValueError(f"Unsupported mode: {mode}")
            grouped[key] += item["net"]
            labels[key] = label

        ordered = []
        for key in sorted(grouped.keys()):
            ordered.append((labels[key], grouped[key]))
        return ordered

    return {
        "week": group_by_period(net_values, "week"),
        "month": group_by_period(net_values, "month"),
        "year": group_by_period(net_values, "year"),
    }


for stock_code in STOCK_CODES:
    print(f"\n=== Processing {stock_code.upper()} ===")
    periods = build_periods(stock_code)

    for mode, values in periods.items():
        labels = [v[0] for v in values]
        amounts = [v[1] for v in values]

        fig, ax = plt.subplots(figsize=(12, 6))
        bars = ax.bar(labels, amounts, color=["green" if v >= 0 else "red" for v in amounts])
        ax.axhline(0, color="black", linewidth=0.8)
        ax.set_title(f"Khối ngoại mua/bán ròng {stock_code.upper()} theo {mode}")
        ax.set_xlabel(mode.capitalize())
        ax.set_ylabel("Giá trị ròng (VND)")
        ax.grid(axis="y", linestyle="--", alpha=0.4)

        plt.xticks(rotation=45, ha="right")

        for bar, val in zip(bars, amounts):
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                height + (10_000_000 if height >= 0 else -10_000_000),
                f"{val:,.0f}",
                ha="center",
                va="bottom" if height >= 0 else "top",
                fontsize=8,
                color="black",
            )

        plt.tight_layout()
        file_name = OUTPUT_DIR / f"{stock_code.upper()}_foreign_flow_{mode}.png"
        plt.savefig(file_name, dpi=200)
        plt.close(fig)
        print(f"Saved: {file_name}")

print("Done.")
