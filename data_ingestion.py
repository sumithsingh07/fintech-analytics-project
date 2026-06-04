
'''import pandas as pd
import os
folder = "data/raw"
for file in os.listdir(folder):
    if file.endswith(".csv"):
        df = pd.read_csv(
            os.path.join(folder,file)
        )
        print("\n"+"="*50)
        print("FILE:",file)
        print("Shape:")
        print(df.shape)
        print("\nDtypes:")
        print(df.dtypes)
        print("\nHead:")
        print(df.head())'''
import pandas as pd
import os
folder = "data/raw"
for file in os.listdir(folder):
    if file.endswith(".csv"):
        print("\n" + "="*50)
        print("FILE:", file)
        df = pd.read_csv(
            os.path.join(folder, file)
        )
        print("Shape:")
        print(df.shape)
        print("\nColumns:")
        print(df.columns.tolist())
        path = os.path.join(folder, file)
        df = pd.read_csv(path)
        print("\n" + "="*60)
        print("FILE:", file)
        print("Shape:", df.shape)
        print("\nDtypes:")
        print(df.dtypes)
        print("\nMissing Values:")
        print(df.isnull().sum())
        print("\nDuplicate Rows:")
        print(df.duplicated().sum())
        print("\nHead:")
        print(df.head())
# ==========================================
# FUND MASTER EXPLORATION
# ==========================================
# Load fund master separately

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

nav_history = pd.read_csv(
    "data/raw/02_nav_history.csv"
)
print("\nFUND HOUSES")
print(fund_master["fund_house"].unique())

print("\nCATEGORIES")
print(fund_master["category"].unique())

print("\nSUB CATEGORIES")
print(fund_master["sub_category"].unique())

print("\nRISK CATEGORIES")
print(fund_master["risk_category"].unique())
# ==========================================
# AMFI CODE VALIDATION
# ==========================================

master_codes = set(
    fund_master["amfi_code"]
)

nav_codes = set(
    nav_history["amfi_code"]
)

missing_codes = master_codes - nav_codes

print("\nAMFI VALIDATION")
print("Missing Codes:")
print(missing_codes)

print("Count:")
print(len(missing_codes))
# ==========================================
# DATA QUALITY SUMMARY
# ==========================================

print("\nDATA QUALITY SUMMARY")
print("Total Schemes:", len(fund_master))
print("Total NAV Records:", len(nav_history))
print("Missing AMFI Codes:", len(missing_codes))
