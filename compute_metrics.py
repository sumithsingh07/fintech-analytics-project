import pandas as pd
import numpy as np
import os

print("=" * 60)
print("PERFORMANCE ANALYTICS STARTED")
print("=" * 60)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

nav = pd.read_csv("data/processed/nav_history_clean.csv")
perf = pd.read_csv("data/processed/performance_clean.csv")
benchmark = pd.read_csv("data/processed/benchmark_clean.csv")

nav["date"] = pd.to_datetime(nav["date"])
benchmark["date"] = pd.to_datetime(benchmark["date"])

results = []

# --------------------------------------------------
# CALCULATE METRICS
# --------------------------------------------------

for scheme in nav["amfi_code"].unique():

    df = nav[nav["amfi_code"] == scheme].copy()
    df = df.sort_values("date")

    if len(df) < 252:
        continue

    # Daily Returns
    df["daily_return"] = df["nav"].pct_change()

    returns = df["daily_return"].dropna()

    if len(returns) == 0:
        continue

    # CAGR
    start_nav = df["nav"].iloc[0]
    end_nav = df["nav"].iloc[-1]

    years = (df["date"].max() - df["date"].min()).days / 365

    cagr = ((end_nav / start_nav) ** (1 / years) - 1) * 100

    # Annual Return
    annual_return = returns.mean() * 252 * 100

    # Volatility
    volatility = returns.std() * np.sqrt(252) * 100

    # Sharpe Ratio
    risk_free = 0.06

    sharpe = (
        (returns.mean() * 252 - risk_free)
        / (returns.std() * np.sqrt(252))
    )

    # Sortino Ratio
    downside = returns[returns < 0]

    if len(downside) > 0:
        downside_std = downside.std() * np.sqrt(252)

        sortino = (
            (returns.mean() * 252 - risk_free)
            / downside_std
        )
    else:
        sortino = np.nan

    # Max Drawdown
    cumulative = (1 + returns).cumprod()

    running_max = cumulative.cummax()

    drawdown = (
        cumulative - running_max
    ) / running_max

    max_drawdown = drawdown.min() * 100

    # Value at Risk (95%)
    var95 = np.percentile(returns, 5) * 100

    results.append([
        scheme,
        round(cagr, 2),
        round(annual_return, 2),
        round(volatility, 2),
        round(sharpe, 2),
        round(sortino, 2),
        round(max_drawdown, 2),
        round(var95, 2)
    ])

# --------------------------------------------------
# CREATE METRICS DATAFRAME
# --------------------------------------------------

metrics = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "cagr_pct",
        "annual_return_pct",
        "volatility_pct",
        "sharpe_ratio",
        "sortino_ratio",
        "max_drawdown_pct",
        "var95_pct"
    ]
)

# --------------------------------------------------
# MERGE FUND NAMES
# --------------------------------------------------

metrics = metrics.merge(
    perf[["amfi_code", "scheme_name"]],
    on="amfi_code",
    how="left"
)

# --------------------------------------------------
# SAVE REPORTS
# --------------------------------------------------

os.makedirs("reports", exist_ok=True)

metrics.to_csv(
    "reports/performance_metrics.csv",
    index=False
)

# Top Sharpe Funds

metrics.sort_values(
    "sharpe_ratio",
    ascending=False
).to_csv(
    "reports/sharpe_ranking.csv",
    index=False
)

# VaR Report

metrics[
    ["scheme_name", "var95_pct"]
].to_csv(
    "reports/var_report.csv",
    index=False
)

print("\nPerformance Metrics Created")

print("\nTop 10 Sharpe Ratio Funds:\n")

print(
    metrics.sort_values(
        "sharpe_ratio",
        ascending=False
    )[[
        "scheme_name",
        "sharpe_ratio"
    ]].head(10)
)

print("\nFiles Saved:")

print("performance_metrics.csv")
print("sharpe_ranking.csv")
print("var_report.csv")

print("\nDAY 4 COMPLETED")
