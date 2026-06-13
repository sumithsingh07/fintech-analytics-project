import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Loading data...")

nav = pd.read_csv("data/processed/nav_history_clean.csv")

nav["date"] = pd.to_datetime(nav["date"])
nav = nav.sort_values(["amfi_code", "date"])

nav["daily_return"] = nav.groupby("amfi_code")["nav"].pct_change()

# VaR and CVaR

results = []

for fund in nav["amfi_code"].unique():
        returns = nav.loc[
        nav["amfi_code"] == fund,
        "daily_return"
        ].dropna()


if len(returns) > 0:
    var95 = np.percentile(returns, 5)
    cvar95 = returns[returns <= var95].mean()

    results.append([
        fund,
        var95,
        cvar95
    ])


var_df = pd.DataFrame(
results,
columns=["amfi_code", "VaR_95", "CVaR_95"]
)

var_df.to_csv(
"reports/var_cvar_report.csv",
index=False
)

print("var_cvar_report.csv created")

# Rolling Sharpe Ratio

top_funds = nav["amfi_code"].unique()[:5]

plt.figure(figsize=(12, 6))

for fund in top_funds:
    temp = nav[nav["amfi_code"] == fund].copy()


rolling_sharpe = (
    temp["daily_return"].rolling(90).mean()
    /
    temp["daily_return"].rolling(90).std()
) * np.sqrt(252)

plt.plot(
    temp["date"],
    rolling_sharpe,
    label=str(fund)
)


plt.title("Rolling 90-Day Sharpe Ratio")
plt.legend()

plt.savefig("reports/rolling_sharpe_chart.png")
plt.close()

print("rolling_sharpe_chart.png created")
print("DAY 6 COMPLETE")
