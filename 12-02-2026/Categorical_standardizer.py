import pandas as pd

# Sample dataset
data = {
    "Name": ["A", "B", "C", "D"],
    "Location": [" New York", "new york", "NEW YORK ", "New York"]
}

df = pd.DataFrame(data)

# View original unique values
print("Before cleaning:", df["Location"].unique())

# 1. Remove leading/trailing spaces
df["Location"] = df["Location"].str.strip()

# 2. Standardize casing (choose one)
df["Location"] = df["Location"].str.title()   # or use .str.lower()

# View cleaned unique values
print("\nAfter cleaning:", df["Location"].unique())

# Display final dataframe
print("\nCleaned DataFrame:\n", df)

