import pandas as pd
import sqlite3

conn = sqlite3.connect(
    "data/db/bluestock_mf.db"
)

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
    "data/processed/performance_clean.csv"
).to_sql(
    "performance",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database Created Successfully")
