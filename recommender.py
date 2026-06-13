import pandas as pd

performance = pd.read_csv("data/processed/performance_clean.csv")

risk = input("Enter Risk Appetite (Low/Moderate/High): ")

filtered = performance[
performance["risk_grade"].str.lower() == risk.lower()
]

recommendations = filtered.sort_values(
"sharpe_ratio",
ascending=False
).head(3)

print("\nTop 3 Recommended Funds\n")
print(
recommendations[
[
"scheme_name",
"fund_house",
"sharpe_ratio",
"return_3yr_pct"
]
]
)
