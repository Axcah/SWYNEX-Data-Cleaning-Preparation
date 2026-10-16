# Final Project: Personal Finance Insights Dashboard

## 1. Project Overview

This project analyzes a personal-finance transaction dataset to summarize transaction patterns, examine categories and payment methods, and highlight data-quality issues. The work combines data cleaning, exploratory data analysis (EDA), visualization, and an interactive Power BI dashboard.

**Objective:** Turn transaction records into clear, responsible insights while documenting missing and unusual values that could affect interpretation.

## 2. Problem Statement

A transaction dataset can contain missing dates or amounts, inconsistent labels, duplicate records, and unusually large values. These issues can make summaries and dashboards misleading if they are not checked first.

This project addresses the following questions:

- How many transaction records are classified as income and expense?
- Which categories occur most frequently?
- How are transactions distributed across payment methods and locations?
- What important data-quality limitations should viewers understand before using the results?
- How can these findings be communicated in a clear, interactive dashboard?

## 3. Dataset Information

The project uses the provided personal-finance transaction dataset, with **15,000 rows and 9 columns**.

| Column | Description |
|---|---|
| `transaction_id` | Transaction identifier |
| `user_id` | User identifier associated with the record |
| `date` | Recorded transaction date |
| `transaction_type` | Transaction type, such as Expense or Income |
| `category` | Transaction category, such as Food, Rent, Travel, or Salary |
| `amount` | Recorded transaction amount |
| `payment_mode` | Payment method recorded for the transaction |
| `location` | Location recorded for the transaction |
| `notes` | Additional notes associated with the record |

**Primary cleaned dataset:** [`cleaned_dataset.csv`](cleaned_dataset.csv)  
**Original dataset file:** [`budgetwise_finance_dataset.csv`](budgetwise_finance_dataset.csv)

## 4. Data Cleaning Process

The cleaning workflow was carried out in Python and saved through `clean_data.py`. The cleaned output was then used for EDA and dashboard development.

The workflow covered these checks and actions:

1. Inspected the dataset structure, column names, data types, and missing values.
2. Checked for duplicate rows and reviewed the cleaned output for remaining duplicates.
3. Converted transaction amounts to numeric values for analysis and checked for values that could not be parsed.
4. Parsed transaction dates where possible. Dates that could not be reliably recovered were left missing rather than replaced with invented dates.
5. Reviewed category, payment-method, and location labels for inconsistent values and empty entries.
6. Kept unusual amount values visible for investigation instead of automatically deleting them, because an unusual value is not necessarily an error.

### Data-quality status in the cleaned dataset

- Total rows: **15,000**
- Total columns: **9**
- Duplicate rows remaining: **0**
- Missing dates: **9,256**
- Missing amounts: **562**

Missing dates and amounts were not fabricated or automatically replaced with zero. They remain limitations for analyses that require those fields.

**Cleaning script:** [`clean_data.py`](clean_data.py)

## 5. Exploratory Data Analysis

EDA was performed using Python, Pandas, and Matplotlib. The analysis summarized transaction counts, category frequencies, amount statistics, and data-quality issues. Six charts were generated.

### Charts

1. [Transactions by Type](Task-2-EDA/01_transactions_by_type.png)
2. [Top Transaction Categories](Task-2-EDA/02_top_categories.png)
3. [Recorded Amount by Transaction Type](Task-2-EDA/03_amount_by_type.png)
4. [Transactions by Payment Method](Task-2-EDA/04_payment_methods.png)
5. [Transactions by Location](Task-2-EDA/05_locations.png)
6. [Distribution of Transaction Amounts](Task-2-EDA/06_amount_distribution.png)

**EDA script:** [`Task-2-EDA/eda_analysis.py`](Task-2-EDA/eda_analysis.py)  
**Detailed EDA report:** [`Task-2-EDA/EDA_Report.md`](Task-2-EDA/EDA_Report.md)

### Important amount statistics

| Statistic | Result |
|---|---:|
| Records with a recorded amount | 14,438 |
| Mean amount | 5,423,589.00 |
| Median amount | 5,934.00 |
| 25th percentile | 2,857 |
| 75th percentile | 9,541 |
| Minimum recorded amount | -1,000 |
| Maximum recorded amount | 1,000,000,000 |

The mean is much higher than the median, suggesting that extreme values heavily affect the average. The maximum amount of 1,000,000,000 and the minimum of -1,000 require validation before drawing conclusions from total amounts. A negative amount might represent a refund, reversal, or data-entry issue; the dataset alone does not confirm which explanation is correct.

## 6. Key Findings and Business Insights

### Finding 1: Expenses are the most common transaction type

The dataset contains **12,760 Expense records** and **2,240 Income records**. This is approximately **85.1% Expense** and **14.9% Income** by transaction count. These percentages describe record counts, not the value of money received or spent.

### Finding 2: Food, Rent, and Travel are the most frequent categories

- Food: **3,175** records
- Rent: **2,547** records
- Travel: **1,885** records

These are the three most frequently recorded categories. Frequency does not necessarily mean these categories have the highest valid monetary totals.

### Finding 3: Many dates are missing

**9,256 records (about 61.7%)** have no usable date. This limits reliable monthly or time-trend analysis, so a date-based trend should be treated cautiously or omitted until the dates can be verified.

### Finding 4: Some amounts are missing

**562 records (about 3.7%)** have missing amounts. Those records cannot contribute to amount-based calculations unless the missing values can be recovered from a trustworthy source.

### Finding 5: Extreme amounts require investigation

The maximum recorded amount is **1,000,000,000**, while the median is **5,934**. The large gap indicates that extreme values may distort average and total-amount comparisons. These values should be checked against source records before financial conclusions are drawn.

### Finding 6: Category labels may need business review

The cleaned dataset includes `Unknown` and `Misc` category labels. A business owner could review these records and decide whether they can be mapped consistently to existing categories; they should not be reassigned without evidence.

## 7. Power BI Dashboard

The interactive report was designed with a dark burgundy and red visual theme. It uses KPI cards, charts, a category table, and slicers to help a viewer explore the transaction data.

### Dashboard components

- KPI cards for total transactions, expense transactions, income transactions, missing dates, missing amounts, and median amount.
- A bar chart for transactions by category.
- A donut chart comparing Expense and Income transaction counts.
- Bar charts for payment method and location.
- A table showing the most frequent categories (or the top five expense categories when the Expense filter is applied).
- Slicers for transaction type, category, and payment method.
- A data-quality and key-insights note explaining major limitations.

### Dashboard files

Upload the Power BI file and screenshot to the `Task-3-Dashboard` folder before submitting this project:

- `Task-3-Dashboard/Task-3-Dashboard.pbix` — interactive Power BI report
- `Task-3-Dashboard/dashboard_screenshot.png` — screenshot of the finished report page

If your local files have different names, use the actual filenames consistently in this document and in GitHub.

## 8. Tools Used

- **Python** — data preparation and analysis
- **Pandas** — data manipulation and summary statistics
- **Matplotlib** — static EDA charts
- **Power Query** — data import and preparation in Power BI
- **Microsoft Power BI** — KPI cards, charts, slicers, and interactive dashboard
- **GitHub** — project versioning and sharing

## 9. Limitations and Next Steps

- Missing dates limit trustworthy time-based analysis.
- Missing amounts limit amount-based calculations.
- Extreme amount values should be validated against the source before totals or averages are used for decisions.
- Transaction counts must not be confused with amounts of money.
- `Unknown` and `Misc` categories may require review by someone who understands the original transactions.

Recommended next steps are to validate the unusual amounts, recover missing dates or amounts only from reliable source records, document any verified category mappings, and then refresh the dashboard.

## 10. Project Files

- [Task 1 cleaning script](clean_data.py)
- [Cleaned dataset](cleaned_dataset.csv)
- [Task 2 EDA folder](Task-2-EDA/)
- [EDA report](Task-2-EDA/EDA_Report.md)
- [Task 3 dashboard folder](Task-3-Dashboard/)

---

**Conclusion:** This project demonstrates a complete entry-level analytics workflow: data preparation, exploratory analysis, visualization, and dashboard development. It also documents data-quality limitations clearly so that the findings are not overstated.
