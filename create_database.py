import pandas as pd
import sqlite3

conn = sqlite3.connect(
    "data/db/bluestock_mf.db"
)

# Load cleaned files

pd.read_csv(
    "data/processed/fund_master_clean.csv"
).to_sql(
    "fund_master",
    conn,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/nav_history_clean.csv"
).to_sql(
    "nav_history",
    conn,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/aum_clean.csv"
).to_sql(
    "aum",
    conn,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/sip_clean.csv"
).to_sql(
    "sip",
    conn,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/category_clean.csv"
).to_sql(
    "category_inflows",
    conn,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/folios_clean.csv"
).to_sql(
    "folios",
    conn,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/performance_clean.csv"
).to_sql(
    "performance",
    conn,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/transactions_clean.csv"
).to_sql(
    "transactions",
    conn,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/holdings_clean.csv"
).to_sql(
    "holdings",
    conn,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/benchmark_clean.csv"
).to_sql(
    "benchmark",
    conn,
    if_exists="replace",
    index=False
)

print("Database Created Successfully")

conn.close()
