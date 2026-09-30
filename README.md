# SWYNEX – Data Cleaning & Preparation

## Project Overview

This project focuses on cleaning and preparing a personal finance dataset for further analysis.

The dataset contains transaction information such as dates, transaction types, categories, amounts, payment modes, locations, and notes.

## Dataset

Source: Kaggle – BudgetWise Personal Finance Dataset

The original dataset contained:

- 15,900 rows
- 9 columns
- Missing values
- Duplicate records
- Inconsistent category values
- Inconsistent payment modes and locations
- Mixed currency symbols and formats in amount values
- Different date formats
- Incorrect data types

## Data Cleaning Performed

### 1. Duplicate Records
Removed duplicate rows from the dataset.

- Original duplicate rows: 900
- Remaining duplicate rows: 0

### 2. Category Standardization
Standardized inconsistent category names, spelling mistakes, and capitalization.

Examples:
- `Educaton` → `Education`
- `Fod` → `Food`
- `rent` → `Rent`
- `entertainment` → `Entertainment`

### 3. Payment Mode Standardization
Standardized inconsistent payment mode values.

Examples:
- `CARD`, `Crd` → `Card`
- `upi`, `UPi` → `UPI`
- `Csh`, `cash` → `Cash`
- `BankTransfer` → `Bank Transfer`

### 4. Location Standardization
Standardized city names, abbreviations, and capitalization.

Examples:
- `AHM` → `Ahmedabad`
- `LUC` → `Lucknow`
- `HYD` → `Hyderabad`
- `DEL` → `Delhi`

### 5. Amount Cleaning
Removed currency symbols and formatting characters and converted the amount column to a numeric data type.

Examples:
- `₹5070` → `5070`
- `Rs.828` → `828`
- `$9952` → `9952`

Missing amount values were kept as missing rather than inventing values.

### 6. Date Cleaning
Converted the date column into a consistent datetime format.

Missing date values were kept as missing.

### 7. Missing Values
Missing categorical and text values were replaced with `Unknown`.

Missing `amount` and `date` values were retained because their original values could not be reliably determined.

## Tools Used

- Python
- Pandas
- Visual Studio Code

## Before and After

| Metric | Before Cleaning | After Cleaning |
|---|---:|---:|
| Rows | 15,900 | 15,000 |
| Columns | 9 | 9 |
| Duplicate Rows | 900 | 0 |
| Amount Data Type | Object | Float |
| Date Data Type | Object | Datetime |

## Files

- `budgetwise_finance_dataset.csv` – Original raw dataset
- `cleaned_dataset.csv` – Cleaned dataset
- `clean_data.py` – Python cleaning script
- `README.md` – Project documentation

## How to Run

Install Pandas:

```bash
pip install pandas
```


Run the cleaning script:


```bash
python clean_data.py
```

The script generates:

`cleaned_dataset.csv`

## Result

The dataset was cleaned and standardized using Python and Pandas, making it ready for further analysis and visualization.