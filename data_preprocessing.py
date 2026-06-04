import pandas as pd
import os

print("=" * 60)
print("DATA PREPROCESSING STARTED")
print("=" * 60)

# ==================================================
# LOAD DATASETS
# ==================================================

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")
category = pd.read_csv("data/raw/05_category_inflows.csv")
folios = pd.read_csv("data/raw/06_industry_folio_count.csv")
performance = pd.read_csv("data/raw/07_scheme_performance.csv")
transactions = pd.read_csv("data/raw/08_investor_transactions.csv")
holdings = pd.read_csv("data/raw/09_portfolio_holdings.csv")
benchmark = pd.read_csv("data/raw/10_benchmark_indices.csv")

print("\nAll datasets loaded successfully")

# ==================================================
# DATE CONVERSION
# ==================================================

nav_history["date"] = pd.to_datetime(nav_history["date"])

aum["date"] = pd.to_datetime(aum["date"])

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

benchmark["date"] = pd.to_datetime(
    benchmark["date"]
)

holdings["portfolio_date"] = pd.to_datetime(
    holdings["portfolio_date"]
)

print("\nDate columns converted")

# ==================================================
# HANDLE MISSING VALUES
# ==================================================

sip["yoy_growth_pct"] = sip["yoy_growth_pct"].fillna(0)

print("\nMissing values handled")

# ==================================================
# DATASETS DICTIONARY
# ==================================================

datasets = {
    "fund_master": fund_master,
    "nav_history": nav_history,
    "aum": aum,
    "sip": sip,
    "category": category,
    "folios": folios,
    "performance": performance,
    "transactions": transactions,
    "holdings": holdings,
    "benchmark": benchmark
}

# ==================================================
# MISSING VALUES REPORT
# ==================================================

print("\n" + "=" * 60)
print("MISSING VALUE REPORT")
print("=" * 60)

for name, df in datasets.items():
    print("\nDataset:", name)
    print(df.isnull().sum())

# ==================================================
# DUPLICATE REPORT
# ==================================================

print("\n" + "=" * 60)
print("DUPLICATE REPORT")
print("=" * 60)

for name, df in datasets.items():
    print(
        f"{name}: {df.duplicated().sum()} duplicates"
    )

# ==================================================
# DATASET SHAPES
# ==================================================

print("\n" + "=" * 60)
print("DATASET SHAPES")
print("=" * 60)

for name, df in datasets.items():
    print(
        f"{name}: {df.shape}"
    )

# ==================================================
# SAVE CLEANED FILES
# ==================================================

os.makedirs(
    "data/processed",
    exist_ok=True
)

fund_master.to_csv(
    "data/processed/fund_master_clean.csv",
    index=False
)

nav_history.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

aum.to_csv(
    "data/processed/aum_clean.csv",
    index=False
)

sip.to_csv(
    "data/processed/sip_clean.csv",
    index=False
)

category.to_csv(
    "data/processed/category_clean.csv",
    index=False
)

folios.to_csv(
    "data/processed/folios_clean.csv",
    index=False
)

performance.to_csv(
    "data/processed/performance_clean.csv",
    index=False
)

transactions.to_csv(
    "data/processed/transactions_clean.csv",
    index=False
)

holdings.to_csv(
    "data/processed/holdings_clean.csv",
    index=False
)

benchmark.to_csv(
    "data/processed/benchmark_clean.csv",
    index=False
)

print("\nAll cleaned files saved to data/processed")

# ==================================================
# SUMMARY
# ==================================================

print("\n" + "=" * 60)
print("PREPROCESSING COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nFiles created:")

print("fund_master_clean.csv")
print("nav_history_clean.csv")
print("aum_clean.csv")
print("sip_clean.csv")
print("category_clean.csv")
print("folios_clean.csv")
print("performance_clean.csv")
print("transactions_clean.csv")
print("holdings_clean.csv")
print("benchmark_clean.csv")
