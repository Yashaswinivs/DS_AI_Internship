import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Sample dataset
data = {
    "Transmission": ["Automatic", "Manual", "Automatic", "Manual", "Automatic"],
    "Color": ["Red", "Blue", "Green", "Blue", "Red"]
}

df = pd.DataFrame(data)
print("Original Dataset:\n", df)

# 1. Label Encoding (Binary / Ordinal)
le = LabelEncoder()
df["Transmission_encoded"] = le.fit_transform(df["Transmission"])

# 2. One-Hot Encoding (Nominal)
# drop_first=True avoids Dummy Variable Trap
df_encoded = pd.get_dummies(df, columns=["Color"], drop_first=True)

print("\nEncoded Dataset:\n", df_encoded)
