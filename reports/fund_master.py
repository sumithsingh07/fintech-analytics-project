fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

print("Fund Houses")
print(fund_master["fund_house"].unique())

print("Categories")
print(fund_master["category"].unique())

print("Sub Categories")
print(fund_master["sub_category"].unique())

print("Risk Categories")
print(fund_master["risk_category"].unique())
