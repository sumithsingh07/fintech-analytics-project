\# Bluestock Mutual Fund Data Dictionary



\## 01\_fund\_master.csv



| Column             | Type    | Description                |

| ------------------ | ------- | -------------------------- |

| amfi\_code          | Integer | Unique AMFI scheme code    |

| fund\_house         | Text    | Mutual fund company        |

| scheme\_name        | Text    | Name of scheme             |

| category           | Text    | Fund category              |

| sub\_category       | Text    | Fund sub-category          |

| plan               | Text    | Direct/Regular plan        |

| launch\_date        | Date    | Launch date                |

| benchmark          | Text    | Benchmark index            |

| expense\_ratio\_pct  | Float   | Expense ratio (%)          |

| exit\_load\_pct      | Float   | Exit load (%)              |

| min\_sip\_amount     | Integer | Minimum SIP amount         |

| min\_lumpsum\_amount | Integer | Minimum lumpsum investment |

| fund\_manager       | Text    | Fund manager name          |

| risk\_category      | Text    | Risk classification        |

| sebi\_category\_code | Text    | SEBI category code         |



\## 02\_nav\_history.csv



| Column    | Type    | Description     |

| --------- | ------- | --------------- |

| amfi\_code | Integer | Scheme code     |

| date      | Date    | NAV date        |

| nav       | Float   | Net Asset Value |



\## 03\_aum\_by\_fund\_house.csv



| Column         | Type    | Description       |

| -------------- | ------- | ----------------- |

| date           | Date    | Reporting date    |

| fund\_house     | Text    | Fund house        |

| aum\_lakh\_crore | Float   | AUM in lakh crore |

| aum\_crore      | Integer | AUM in crore      |

| num\_schemes    | Integer | Number of schemes |



\## 04\_monthly\_sip\_inflows.csv



| Column                    | Type    | Description           |

| ------------------------- | ------- | --------------------- |

| month                     | Text    | Month                 |

| sip\_inflow\_crore          | Integer | SIP inflow amount     |

| active\_sip\_accounts\_crore | Float   | Active SIP accounts   |

| new\_sip\_accounts\_lakh     | Float   | New SIP accounts      |

| sip\_aum\_lakh\_crore        | Float   | SIP AUM               |

| yoy\_growth\_pct            | Float   | YoY growth percentage |



\## 05\_category\_inflows.csv



| Column           | Type  | Description   |

| ---------------- | ----- | ------------- |

| month            | Text  | Month         |

| category         | Text  | Fund category |

| net\_inflow\_crore | Float | Net inflow    |



\## 06\_industry\_folio\_count.csv



| Column              | Type  | Description   |

| ------------------- | ----- | ------------- |

| month               | Text  | Month         |

| total\_folios\_crore  | Float | Total folios  |

| equity\_folios\_crore | Float | Equity folios |

| debt\_folios\_crore   | Float | Debt folios   |

| hybrid\_folios\_crore | Float | Hybrid folios |

| others\_folios\_crore | Float | Other folios  |



\## 07\_scheme\_performance.csv



| Column           | Type    | Description      |

| ---------------- | ------- | ---------------- |

| amfi\_code        | Integer | Scheme code      |

| return\_1yr\_pct   | Float   | 1-Year Return    |

| return\_3yr\_pct   | Float   | 3-Year Return    |

| return\_5yr\_pct   | Float   | 5-Year Return    |

| alpha            | Float   | Alpha            |

| beta             | Float   | Beta             |

| sharpe\_ratio     | Float   | Sharpe Ratio     |

| sortino\_ratio    | Float   | Sortino Ratio    |

| max\_drawdown\_pct | Float   | Maximum Drawdown |



\## 08\_investor\_transactions.csv



| Column           | Type    | Description             |

| ---------------- | ------- | ----------------------- |

| investor\_id      | Text    | Investor ID             |

| transaction\_date | Date    | Transaction date        |

| transaction\_type | Text    | SIP/Lumpsum/Redemption  |

| amount\_inr       | Integer | Transaction amount      |

| state            | Text    | Investor state          |

| city             | Text    | Investor city           |

| age\_group        | Text    | Investor age group      |

| gender           | Text    | Investor gender         |

| payment\_mode     | Text    | Payment method          |

| kyc\_status       | Text    | KYC verification status |



\## 09\_portfolio\_holdings.csv



| Column            | Type    | Description         |

| ----------------- | ------- | ------------------- |

| amfi\_code         | Integer | Scheme code         |

| stock\_symbol      | Text    | Stock ticker        |

| stock\_name        | Text    | Company name        |

| sector            | Text    | Sector              |

| weight\_pct        | Float   | Portfolio weight    |

| market\_value\_cr   | Float   | Market value        |

| current\_price\_inr | Float   | Current stock price |



\## 10\_benchmark\_indices.csv



| Column      | Type  | Description         |

| ----------- | ----- | ------------------- |

| date        | Date  | Trading date        |

| index\_name  | Text  | Benchmark index     |

| close\_value | Float | Closing index value |



