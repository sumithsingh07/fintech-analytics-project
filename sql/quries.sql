use mutual_funds;
-- Top 10 funds by 3 year return
SELECT
    scheme_name,
    return_3yr_pct
FROM performance
ORDER BY return_3yr_pct DESC
LIMIT 10;
-- Average NAV
SELECT
    amfi_code,
    AVG(nav) AS avg_nav
FROM nav_history
GROUP BY amfi_code;
-- Fund count by category
SELECT
    category,
    COUNT(*) AS total_funds
FROM fund_master
GROUP BY category;