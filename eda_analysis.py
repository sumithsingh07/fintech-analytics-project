import pandas as pd
import matplotlib.pyplot as plt
import os
print("=" * 60)
print("EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 60)
# LOAD CLEANED DATASETS
fund_master = pd.read_csv("data/processed/fund_master_clean.csv")
nav = pd.read_csv("data/processed/nav_history_clean.csv")
aum = pd.read_csv("data/processed/aum_clean.csv")
sip = pd.read_csv("data/processed/sip_clean.csv")
category = pd.read_csv("data/processed/category_clean.csv")
folios = pd.read_csv("data/processed/folios_clean.csv")
performance = pd.read_csv("data/processed/performance_clean.csv")
transactions = pd.read_csv("data/processed/transactions_clean.csv")
holdings = pd.read_csv("data/processed/holdings_clean.csv")
benchmark = pd.read_csv("data/processed/benchmark_clean.csv")
# CREATE REPORTS FOLDER
os.makedirs("reports", exist_ok=True)
# TOP 10 FUNDS BY 5-YEAR RETURN
print("\n" + "=" * 60)
print("TOP 10 FUNDS BY 5-YEAR RETURN")
print("=" * 60)
top_returns = performance.sort_values(
    "return_5yr_pct",
    ascending=False
)
print(
    top_returns[
        ["scheme_name", "fund_house", "return_5yr_pct"]
    ].head(10)
)
# Save report
top_returns.to_csv(
    "reports/top_funds.csv",
    index=False
)
# FUND HOUSE AUM RANKING
print("\n" + "=" * 60)
print("FUND HOUSE AUM RANKING")
print("=" * 60)
aum["date"] = pd.to_datetime(aum["date"])
latest_aum = (
    aum.sort_values("date")
       .groupby("fund_house")
       .tail(1)
)
latest_aum = latest_aum.sort_values(
    "aum_crore",
    ascending=False
)
print(
    latest_aum[
        ["fund_house", "aum_crore"]
    ]
)
latest_aum.to_csv(
    "reports/aum_ranking.csv",
    index=False
)
# AUM Chart
plt.figure(figsize=(10, 5))
plt.bar(
    latest_aum["fund_house"],
    latest_aum["aum_crore"]
)
plt.xticks(rotation=45)
plt.title("Fund House AUM Ranking")
plt.ylabel("AUM (Crore)")
plt.tight_layout()
plt.savefig(
    "reports/aum_ranking.png"
)
plt.close()
# SIP INFLOW TREND
# ==================================================

print("\n" + "=" * 60)
print("SIP INFLOW SUMMARY")
print("=" * 60)

print(
    sip[
        [
            "month",
            "sip_inflow_crore"
        ]
    ].tail()
)

plt.figure(figsize=(12, 5))

plt.plot(
    sip["month"],
    sip["sip_inflow_crore"]
)

plt.xticks(rotation=45)

plt.title("Monthly SIP Inflows")
plt.ylabel("Crore")

plt.tight_layout()

plt.savefig(
    "reports/sip_trend.png"
)

plt.close()

# ==================================================
# CATEGORY INFLOWS
# ==================================================

print("\n" + "=" * 60)
print("CATEGORY INFLOWS")
print("=" * 60)

category_summary = (
    category.groupby("category")
    ["net_inflow_crore"]
    .sum()
    .sort_values(ascending=False)
)

print(category_summary)

category_summary.to_csv(
    "reports/category_summary.csv"
)

plt.figure(figsize=(10, 6))

category_summary.sort_values().plot(
    kind="barh"
)

plt.title("Category-wise Net Inflows")

plt.tight_layout()

plt.savefig(
    "reports/category_inflows.png"
)

plt.close()

# ==================================================
# INVESTOR DEMOGRAPHICS
# ==================================================

print("\n" + "=" * 60)
print("INVESTOR GENDER DISTRIBUTION")
print("=" * 60)

gender_count = (
    transactions["gender"]
    .value_counts()
)

print(gender_count)

gender_count.to_csv(
    "reports/gender_distribution.csv"
)

print("\n" + "=" * 60)
print("INVESTOR AGE GROUP DISTRIBUTION")
print("=" * 60)

age_count = (
    transactions["age_group"]
    .value_counts()
)

print(age_count)

age_count.to_csv(
    "reports/age_distribution.csv"
)

print("\n" + "=" * 60)
print("TOP 10 STATES")
print("=" * 60)

state_count = (
    transactions["state"]
    .value_counts()
    .head(10)
)

print(state_count)

state_count.to_csv(
    "reports/top_states.csv"
)

# ==================================================
# RISK VS RETURN
# ==================================================

print("\n" + "=" * 60)
print("TOP RISK-RETURN FUNDS")
print("=" * 60)

risk_return = performance[
    [
        "scheme_name",
        "return_3yr_pct",
        "std_dev_ann_pct"
    ]
]

print(
    risk_return.sort_values(
        "return_3yr_pct",
        ascending=False
    ).head(10)
)

plt.figure(figsize=(10, 6))

plt.scatter(
    performance["std_dev_ann_pct"],
    performance["return_3yr_pct"]
)

plt.xlabel("Risk (Std Dev)")
plt.ylabel("3-Year Return")

plt.title("Risk vs Return")

plt.tight_layout()

plt.savefig(
    "reports/risk_vs_return.png"
)

plt.close()

# ==================================================
# PORTFOLIO SECTOR ANALYSIS
# ==================================================

print("\n" + "=" * 60)
print("TOP SECTORS")
print("=" * 60)

sector_summary = (
    holdings.groupby("sector")
    ["weight_pct"]
    .sum()
    .sort_values(ascending=False)
)

print(sector_summary.head(10))

sector_summary.to_csv(
    "reports/sector_summary.csv"
)

# ==================================================
# BENCHMARK ANALYSIS
# ==================================================

benchmark["date"] = pd.to_datetime(
    benchmark["date"]
)

benchmark_summary = (
    benchmark.groupby("index_name")
    ["close_value"]
    .mean()
)

print("\n" + "=" * 60)
print("BENCHMARK AVERAGES")
print("=" * 60)

print(benchmark_summary)

benchmark_summary.to_csv(
    "reports/benchmark_summary.csv"
)

# ==================================================
# COMPLETION MESSAGE
# ==================================================

print("\n" + "=" * 60)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nGenerated Reports:")

print("top_funds.csv")
print("aum_ranking.csv")
print("gender_distribution.csv")
print("age_distribution.csv")
print("top_states.csv")
print("category_summary.csv")
print("sector_summary.csv")
print("benchmark_summary.csv")

print("\nGenerated Charts:")

print("aum_ranking.png")
print("sip_trend.png")
print("category_inflows.png")
print("risk_vs_return.png")
