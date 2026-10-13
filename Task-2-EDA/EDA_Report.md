# Exploratory Data Analysis (EDA) Report

## 1. Project Overview

For Task 2 of my SWYNEX Data Analytics Internship, I performed Exploratory Data Analysis (EDA) on the cleaned personal finance dataset using Python, Pandas, and Matplotlib.

The goal was to understand transaction patterns, calculate important statistics, identify unusual values, and present findings through charts.

## 2. Dataset Summary

- Total records: 15,000
- Total columns: 9
- Duplicate rows remaining: 0
- Transactions with recorded amounts: 14,438
- Missing amounts: 562
- Missing dates: 9,256

## 3. Important Statistics

- Mean transaction amount: 5,423,589.00
- Median transaction amount: 5,934.00
- Minimum recorded amount: -1,000
- Maximum recorded amount: 1,000,000,000
- 25th percentile: 2,857
- 75th percentile: 9,541

The large difference between the mean and median suggests that unusually large recorded amounts are affecting the average.

## 4. Key Insights

### Insight 1: Expenses are the most common transaction type

The dataset contains 12,760 expense transactions and 2,240 income transactions. Expenses account for approximately 85.1% of all records, while income accounts for 14.9%.

### Insight 2: Food is the most frequently recorded category

Food has 3,175 transactions, followed by Rent with 2,547 and Travel with 1,885. These are the three most frequently recorded categories in the dataset.

### Insight 3: Transaction amounts have extreme values

The minimum recorded amount is -1,000, while the maximum is 1,000,000,000. These values should be investigated to determine whether they represent valid transactions, refunds, or data-entry issues.

### Insight 4: The mean is much higher than the median

The mean amount is approximately 5.42 million, while the median is 5,934. This large difference suggests that unusually high amounts are pulling the average upward. Therefore, the median may better represent a typical transaction in this dataset.

### Insight 5: Many transaction dates are missing

There are 9,256 records with missing dates, representing approximately 61.7% of all records. This limits the reliability of date-based analysis, such as monthly spending trends.

### Insight 6: Some transaction amounts are missing

There are 562 records without a recorded amount, representing approximately 3.7% of all records. These records cannot be included in calculations that require a valid amount.

## 5. Charts Created

The following charts were generated using Matplotlib:

1. Transactions by Type
2. Top 10 Transaction Categories
3. Total Amount by Transaction Type
4. Transactions by Payment Method
5. Transactions by Location
6. Distribution of Transaction Amounts

## 6. Tools Used

- Python
- Pandas
- Matplotlib

## 7. Conclusion

The analysis shows that expenses are more common than income transactions, with Food, Rent, and Travel appearing most frequently. The dataset also contains missing dates, missing amounts, and extreme recorded values that need further investigation.

EDA helped summarize the data, identify patterns, and highlight potential data-quality concerns before creating an interactive dashboard.
