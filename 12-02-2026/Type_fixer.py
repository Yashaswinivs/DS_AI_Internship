import pandas as pd

# Sample dataset
data = {
    "Product": ["A", "B", "C"],
    "Price": ["$120", "$85", "$200"],
    "Date": ["2025-01-10", "2025-01-15", "2025-01-20"]
}

df = pd.DataFrame(data)

# 1. Check initial data types
print("Initial Data Types:\n", df.dtypes)

# 2. Remove '$' and convert Price column to float
df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)

# 3. Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Check updated data types
print("\nUpdated Data Types:\n", df.dtypes)

# Display final dataframe
print("\nCleaned DataFrame:\n", df)
