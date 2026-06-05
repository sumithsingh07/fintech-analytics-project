import pandas as pd
import numpy as np
import os
from scipy.stats import linregress
import matplotlib.pyplot as plt

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
# ==========================================================
# ALPHA BETA ANALYSIS
# ==========================================================

print("\nCalculating Alpha and Beta...")

nifty = benchmark[
    benchmark["index_name"].str.contains("NIFTY", case=False)
]

nifty100 = nifty.groupby("date")["close_value"].mean().reset_index()

nifty100["benchmark_return"] = (
    nifty100["close_value"].pct_change()
)

alpha_beta_results = []

for scheme in nav["amfi_code"].unique():

    df = nav[nav["amfi_code"] == scheme].copy()

    df = df.sort_values("date")

    df["fund_return"] = df["nav"].pct_change()

    merged = pd.merge(
        df,
        nifty100[["date", "benchmark_return"]],
        on="date",
        how="inner"
    )

    merged = merged.dropna()

    if len(merged) < 100:
        continue

    slope, intercept, r_value, p_value, std_err = linregress(
        merged["benchmark_return"],
        merged["fund_return"]
    )

    beta = slope

    alpha = intercept * 252 * 100

    tracking_error = (
        (merged["fund_return"]
         - merged["benchmark_return"]).std()
        * np.sqrt(252)
        * 100
    )

    alpha_beta_results.append([
        scheme,
        round(alpha, 2),
        round(beta, 2),
        round(tracking_error, 2)
    ])

alpha_beta = pd.DataFrame(
    alpha_beta_results,
    columns=[
        "amfi_code",
        "alpha_pct",
        "beta",
        "tracking_error_pct"
    ]
)

alpha_beta = alpha_beta.merge(
    perf[["amfi_code", "scheme_name"]],
    on="amfi_code",
    how="left"
)

alpha_beta.to_csv(
    "reports/alpha_beta.csv",
    index=False
)

alpha_beta[
    ["scheme_name", "tracking_error_pct"]
].to_csv(
    "reports/tracking_error.csv",
    index=False
)

print("alpha_beta.csv created")

# ==========================================================
# FUND SCORECARD
# ==========================================================

print("\nBuilding Fund Scorecard...")

scorecard = metrics.merge(
    alpha_beta[
        ["amfi_code", "alpha_pct"]
    ],
    on="amfi_code",
    how="left"
)

scorecard = scorecard.merge(
    perf[
        [
            "amfi_code",
            "return_3yr_pct",
            "expense_ratio_pct"
        ]
    ],
    on="amfi_code",
    how="left"
)

scorecard["return_rank"] = (
    scorecard["return_3yr_pct"]
    .rank(ascending=False)
)

scorecard["sharpe_rank"] = (
    scorecard["sharpe_ratio"]
    .rank(ascending=False)
)

scorecard["alpha_rank"] = (
    scorecard["alpha_pct"]
    .rank(ascending=False)
)

scorecard["expense_rank"] = (
    scorecard["expense_ratio_pct"]
    .rank(ascending=True)
)

scorecard["dd_rank"] = (
    scorecard["max_drawdown_pct"]
    .rank(ascending=False)
)

scorecard["score"] = (
    30 * (
        1 - scorecard["return_rank"]
        / scorecard["return_rank"].max()
    )
    +
    25 * (
        1 - scorecard["sharpe_rank"]
        / scorecard["sharpe_rank"].max()
    )
    +
    20 * (
        1 - scorecard["alpha_rank"]
        / scorecard["alpha_rank"].max()
    )
    +
    15 * (
        1 - scorecard["expense_rank"]
        / scorecard["expense_rank"].max()
    )
    +
    10 * (
        1 - scorecard["dd_rank"]
        / scorecard["dd_rank"].max()
    )
)

scorecard["score"] = scorecard["score"].round(2)

scorecard.sort_values(
    "score",
    ascending=False
).to_csv(
    "reports/fund_scorecard.csv",
    index=False
)

print("fund_scorecard.csv created")

# ==========================================================
# BENCHMARK COMPARISON
# ==========================================================

print("\nCreating Benchmark Chart...")

top5 = (
    scorecard
    .sort_values("score", ascending=False)
    .head(5)
)

plt.figure(figsize=(12, 6))

for scheme in top5["amfi_code"]:

    temp = nav[
        nav["amfi_code"] == scheme
    ].copy()

    temp = temp.sort_values("date")

    temp["growth"] = (
        temp["nav"]
        / temp["nav"].iloc[0]
    ) * 100

    name = top5[
        top5["amfi_code"] == scheme
    ]["scheme_name"].values[0]

    plt.plot(
        temp["date"],
        temp["growth"],
        label=name[:20]
    )

plt.title(
    "Top 5 Funds Benchmark Comparison"
)

plt.xlabel("Date")
plt.ylabel("Growth Index")

plt.legend()

plt.tight_layout()

plt.savefig(
    "reports/benchmark_comparison.png"
)

plt.close()

print("benchmark_comparison.png created")

print("\nRemaining Day 4 Tasks Completed")
print("\nDAY 4 COMPLETED")
