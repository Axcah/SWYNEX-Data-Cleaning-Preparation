

import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the cleaned dataset
df = pd.read_csv("cleaned_dataset.csv")

# Make sure amount is numeric
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

# 2. Basic information
print("Dataset size:", df.shape)
print("Duplicate rows:", df.duplicated().sum())

print("\nMissing values:")
print(df.isnull().sum())

# 3. Statistics about transaction amounts
print("\nAmount statistics:")
print(df["amount"].describe())

# 4. Count transactions by type
print("\nTransactions by type:")
print(df["transaction_type"].value_counts())

# 5. Count transactions by category
print("\nTransactions by category:")
print(df["category"].value_counts())

# 6. Compare amounts by transaction type
print("\nTotal amount by transaction type:")
print(df.groupby("transaction_type")["amount"].sum())

# 7. Chart: transaction types
df["transaction_type"].value_counts().plot(kind="bar")
plt.title("Transactions by Type")
plt.xlabel("Transaction Type")
plt.ylabel("Number of Transactions")
plt.tight_layout()
plt.savefig("01_transactions_by_type.png")
plt.close()

# 8. Chart: top 10 categories
df["category"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Transaction Categories")
plt.xlabel("Category")
plt.ylabel("Number of Transactions")
plt.tight_layout()
plt.savefig("02_top_categories.png")
plt.close()

# 9. Chart: amount by transaction type
df.groupby("transaction_type")["amount"].sum().plot(kind="bar")
plt.title("Total Amount by Transaction Type")
plt.xlabel("Transaction Type")
plt.ylabel("Total Recorded Amount")
plt.tight_layout()
plt.savefig("03_amount_by_type.png")
plt.close()

# 10. Chart: payment methods
df["payment_mode"].value_counts().plot(kind="bar")
plt.title("Transactions by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Transactions")
plt.tight_layout()
plt.savefig("04_payment_methods.png")
plt.close()

# 11. Chart: locations
df["location"].value_counts().plot(kind="bar")
plt.title("Transactions by Location")
plt.xlabel("Location")
plt.ylabel("Number of Transactions")
plt.tight_layout()
plt.savefig("05_locations.png")
plt.close()

# 12. Chart: distribution of amounts
df["amount"].dropna().plot(kind="hist", bins=30)
plt.title("Distribution of Transaction Amounts")
plt.xlabel("Amount")
plt.ylabel("Number of Transactions")
plt.tight_layout()
plt.savefig("06_amount_distribution.png")
plt.close()

print("\nEDA completed successfully.")
print("Six charts have been saved.")




