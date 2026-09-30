import pandas as pd

# Load the dataset
df = pd.read_csv("budgetwise_finance_dataset.csv")


# 1. Remove duplicate records
df = df.drop_duplicates()



# 2. Standardize category values
category_map = {
    "Educaton": "Education",
    "education": "Education",
    "EDU": "Education",
    "Fod": "Food",
    "Foods": "Food",
    "FOOD": "Food",
    "Foodd": "Food",
    "food": "Food",
    "Utilties": "Utilities",
    "Utlities": "Utilities",
    "Utility": "Utilities",
    "utilities": "Utilities",
    "Rentt": "Rent",
    "Rnt": "Rent",
    "RENT": "Rent",
    "Travl": "Travel",
    "Traval": "Travel",
    "TRAVEL": "Travel",
    "HEALTH": "Health",
    "Helth": "Health",
    "Entertain": "Entertainment",
    "Entrtnmnt": "Entertainment",
    "Saving": "Savings",
    "SAVINGS": "Savings",
    "OTHERS": "Others",
    "others": "Others",
    "Other": "Others"
}
df["category"] = df["category"].replace(category_map)



# 3. Standardize payment modes
payment_map = {
    "card": "Card",
    "CARD": "Card",
    "Card": "Card",
    "Crd": "Card",
    "CRD": "Card",
    "upi": "UPI",
    "UPi": "UPI",
    "Upi": "UPI",
    "UPI": "UPI",
    "Csh": "Cash",
    "csh": "Cash",
    "cash": "Cash",
    "CASH": "Cash",
    "Cash": "Cash",
    "Bank Transfer": "Bank Transfer",
    "bank transfer": "Bank Transfer",
    "BankTransfer": "Bank Transfer",
    "Bank_Transfer": "Bank Transfer",
    "Bank Transfr": "Bank Transfer"
}

df["payment_mode"] = df["payment_mode"].replace(payment_map)



# 4. Standardize locations
location_map = {
    "Ahmedabad": "Ahmedabad",
    "AHMEDABAD": "Ahmedabad",
    "ahmedabad": "Ahmedabad",
    "AHM": "Ahmedabad",
    "Lucknow": "Lucknow",
    "lucknow": "Lucknow",
    "LUCKNOW": "Lucknow",
    "LUC": "Lucknow",
    "Hyderabad": "Hyderabad",
    "hyderabad": "Hyderabad",
    "HYDERABAD": "Hyderabad",
    "HYD": "Hyderabad",
    "Delhi": "Delhi",
    "DELHI": "Delhi",
    "delhi": "Delhi",
    "DEL": "Delhi",
    "Bangalore": "Bangalore",
    "BANGALORE": "Bangalore",
    "bangalore": "Bangalore",
    "BAN": "Bangalore",
    "Kolkata": "Kolkata",
    "KOLKATA": "Kolkata",
    "kolkata": "Kolkata",
    "KOL": "Kolkata",
    "Chennai": "Chennai",
    "CHENNAI": "Chennai",
    "chennai": "Chennai",
    "CHE": "Chennai",
    "Pune": "Pune",
    "PUNE": "Pune",
    "pune": "Pune",
    "PUN": "Pune",
    "Mumbai": "Mumbai",
    "MUMBAI": "Mumbai",
    "mumbai": "Mumbai",
    "MUM": "Mumbai",
    "Jaipur": "Jaipur",
    "JAIPUR": "Jaipur",
    "jaipur": "Jaipur",
    "JAI": "Jaipur"
}

df["location"] = df["location"].replace(location_map)



# 5. Clean amount values

df["amount"] = (
    df["amount"]
    .astype(str)
    .str.replace("₹", "", regex=False)
    .str.replace("Rs.", "", regex=False)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
)

df["amount"] = pd.to_numeric(df["amount"], errors="coerce")



# 6. Convert date to a consistent datetime format

df["date"] = pd.to_datetime(df["date"], errors="coerce", dayfirst=False)



# 7. Handle missing values

df["category"] = df["category"].fillna("Unknown")
df["payment_mode"]=df["payment_mode"].fillna("Unknown")
df["location"]=df["location"].fillna("Unknown")
df["notes"]=df["notes"].fillna("Unknown")



# 8. Save cleaned dataset

df.to_csv("cleaned_dataset.csv", index=False)

print("Cleaning completed successfully.")
print("Remaining duplicate rows:", df.duplicated().sum())
print("Final rows and columns:", df.shape)