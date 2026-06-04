import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

print("=" * 60)
print("EDA ANALYSIS STARTED")
print("=" * 60)

# ==================================================
# CREATE REPORTS FOLDER
# ==================================================

os.makedirs("reports", exist_ok=True)

# ==================================================
# LOAD DATA
# ==================================================

fund_master = pd.read_csv(
    "data/processed/fund_master_clean.csv"
)

nav = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

aum = pd.read_csv(
    "data/processed/aum_clean.csv"
)

sip = pd.read_csv(
    "data/processed/sip_clean.csv"
)

category = pd.read_csv(
    "data/processed/category_clean.csv"
)

folios = pd.read_csv(
    "data/processed/folios_clean.csv"
)

performance = pd.read_csv(
    "data/processed/performance_clean.csv"
)

transactions = pd.read_csv(
    "data/processed/transactions_clean.csv"
)

holdings = pd.read_csv(
    "data/processed/holdings_clean.csv"
)

benchmark = pd.read_csv(
    "data/processed/benchmark_clean.csv"
)

# ==================================================
# DATE CONVERSION
# ==================================================

nav["date"] = pd.to_datetime(nav["date"])

aum["date"] = pd.to_datetime(aum["date"])

benchmark["date"] = pd.to_datetime(
    benchmark["date"]
)

# ==================================================
# 1. NAV TREND ANALYSIS
# ==================================================

print("Creating NAV Trend Chart...")

merged = nav.merge(
    fund_master[
        ["amfi_code", "scheme_name"]
    ],
    on="amfi_code"
)

fig = px.line(
    merged,
    x="date",
    y="nav",
    color="scheme_name",
    title="NAV Trend of All Schemes"
)

fig.write_html(
    "reports/nav_trend_all_funds.html"
)

# ==================================================
# 2. AUM RANKING
# ==================================================

print("Creating AUM Ranking...")

aum_rank = aum.groupby(
    "fund_house"
)["aum_crore"].mean().sort_values(
    ascending=False
)

plt.figure(figsize=(10, 5))

sns.barplot(
    x=aum_rank.values,
    y=aum_rank.index
)

plt.title("Average AUM by Fund House")

plt.tight_layout()

plt.savefig(
    "reports/aum_ranking.png"
)

plt.close()

aum_rank.to_csv(
    "reports/aum_ranking.csv"
)

# ==================================================
# 3. SIP TREND
# ==================================================

print("Creating SIP Trend...")

plt.figure(figsize=(12, 5))

plt.plot(
    sip["month"],
    sip["sip_inflow_crore"]
)

plt.xticks(rotation=45)

plt.title("Monthly SIP Inflow Trend")

plt.tight_layout()

plt.savefig(
    "reports/sip_trend.png"
)

plt.close()

# ==================================================
# 4. CATEGORY INFLOWS
# ==================================================

print("Creating Category Heatmap...")

pivot = category.pivot(
    index="category",
    columns="month",
    values="net_inflow_crore"
)

plt.figure(figsize=(14, 6))

sns.heatmap(
    pivot,
    cmap="YlGnBu"
)

plt.title(
    "Category Inflow Heatmap"
)

plt.tight_layout()

plt.savefig(
    "reports/category_inflows.png"
)

plt.close()

# ==================================================
# 5. AGE DISTRIBUTION
# ==================================================

print("Creating Age Distribution...")

age = transactions[
    "age_group"
].value_counts()

plt.figure(figsize=(6, 6))

plt.pie(
    age,
    labels=age.index,
    autopct="%1.1f%%"
)

plt.title(
    "Age Group Distribution"
)

plt.savefig(
    "reports/age_distribution.png"
)

plt.close()

age.to_csv(
    "reports/age_distribution.csv"
)

# ==================================================
# 6. GENDER DISTRIBUTION
# ==================================================

print("Creating Gender Distribution...")

gender = transactions[
    "gender"
].value_counts()

plt.figure(figsize=(6, 6))

plt.pie(
    gender,
    labels=gender.index,
    autopct="%1.1f%%"
)

plt.title(
    "Gender Distribution"
)

plt.savefig(
    "reports/gender_distribution.png"
)

plt.close()

gender.to_csv(
    "reports/gender_distribution.csv"
)

# ==================================================
# 7. TOP STATES
# ==================================================

print("Creating State Analysis...")

top_states = transactions.groupby(
    "state"
)["amount_inr"].sum().sort_values(
    ascending=False
)

top_states.to_csv(
    "reports/top_states.csv"
)

plt.figure(figsize=(10, 6))

top_states.head(10).plot(
    kind="barh"
)

plt.title(
    "Top States by Investment"
)

plt.tight_layout()

plt.savefig(
    "reports/top_states.png"
)

plt.close()

# ==================================================
# 8. T30 vs B30
# ==================================================

city = transactions[
    "city_tier"
].value_counts()

plt.figure(figsize=(6, 6))

plt.pie(
    city,
    labels=city.index,
    autopct="%1.1f%%"
)

plt.title(
    "T30 vs B30 Distribution"
)

plt.savefig(
    "reports/city_tier_distribution.png"
)

plt.close()

# ==================================================
# 9. FOLIO GROWTH
# ==================================================

print("Creating Folio Growth...")

plt.figure(figsize=(12, 5))

plt.plot(
    folios["month"],
    folios["total_folios_crore"]
)

plt.xticks(rotation=45)

plt.title(
    "Industry Folio Growth"
)

plt.tight_layout()

plt.savefig(
    "reports/folio_growth.png"
)

plt.close()

# ==================================================
# 10. TOP FUNDS
# ==================================================

top_funds = performance.sort_values(
    "return_5yr_pct",
    ascending=False
)

top_funds.to_csv(
    "reports/top_funds.csv",
    index=False
)

# ==================================================
# 11. RISK VS RETURN
# ==================================================

print("Creating Risk vs Return...")

plt.figure(figsize=(10, 6))

plt.scatter(
    performance["std_dev_ann_pct"],
    performance["return_5yr_pct"]
)

plt.xlabel("Risk")

plt.ylabel("Return")

plt.title(
    "Risk vs Return"
)

plt.savefig(
    "reports/risk_vs_return.png"
)

plt.close()

# ==================================================
# 12. CORRELATION MATRIX
# ==================================================

print("Creating Correlation Matrix...")

pivot_nav = nav.pivot_table(
    index="date",
    columns="amfi_code",
    values="nav"
)

returns = pivot_nav.pct_change()

corr = returns.corr()

plt.figure(figsize=(12, 8))

sns.heatmap(
    corr,
    cmap="coolwarm"
)

plt.title(
    "NAV Return Correlation Matrix"
)

plt.tight_layout()

plt.savefig(
    "reports/correlation_matrix.png"
)

plt.close()

# ==================================================
# 13. SECTOR ALLOCATION
# ==================================================

print("Creating Sector Analysis...")

sector = holdings.groupby(
    "sector"
)["weight_pct"].sum()

sector.to_csv(
    "reports/sector_summary.csv"
)

plt.figure(figsize=(8, 8))

plt.pie(
    sector,
    labels=sector.index,
    autopct="%1.1f%%"
)

centre = plt.Circle(
    (0, 0),
    0.60,
    fc="white"
)

fig = plt.gcf()

fig.gca().add_artist(
    centre
)

plt.title(
    "Sector Allocation"
)

plt.savefig(
    "reports/sector_donut.png"
)

plt.close()

# ==================================================
# 14. BENCHMARK SUMMARY
# ==================================================

benchmark_summary = benchmark.groupby(
    "index_name"
)["close_value"].agg(
    ["min", "max", "mean"]
)

benchmark_summary.to_csv(
    "reports/benchmark_summary.csv"
)

# ==================================================
# 15. CATEGORY SUMMARY
# ==================================================

category_summary = category.groupby(
    "category"
)["net_inflow_crore"].sum()

category_summary.to_csv(
    "reports/category_summary.csv"
)

print("=" * 60)
print("EDA ANALYSIS COMPLETED")
print("=" * 60)

print("\nFiles generated in reports folder:")
print("""
nav_trend_all_funds.html
aum_ranking.png
aum_ranking.csv
sip_trend.png
category_inflows.png
age_distribution.png
gender_distribution.png
top_states.csv
top_states.png
city_tier_distribution.png
folio_growth.png
top_funds.csv
risk_vs_return.png
correlation_matrix.png
sector_donut.png
sector_summary.csv
benchmark_summary.csv
category_summary.csv
""")
