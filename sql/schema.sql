create database mutual_funds;
use mutual_funds;
CREATE TABLE fund_master (
    amfi_code INTEGER PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    plan TEXT
);
CREATE TABLE nav_history (
    amfi_code INTEGER,
    date DATE,
    nav REAL
);
CREATE TABLE performance (
    amfi_code INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    sharpe_ratio REAL,
    beta REAL
);