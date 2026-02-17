import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Load dataset
df = pd.read_csv("LevelingDataset.csv")

# Select numeric columns only
numeric_df = df.select_dtypes(include='number')

# 1. Standardization (Mean = 0, Std = 1)
scaler_standard = StandardScaler()
standardized_data = scaler_standard.fit_transform(numeric_df)

df_standardized = pd.DataFrame(standardized_data, columns=numeric_df.columns)

# 2. Normalization (Range 0 to 1)
scaler_minmax = MinMaxScaler()
normalized_data = scaler_minmax.fit_transform(numeric_df)

df_normalized = pd.DataFrame(normalized_data, columns=numeric_df.columns)

# 3. Histogram Comparison (Before vs After Scaling)
feature = numeric_df.columns[0]  # Select first numeric column

plt.figure(figsize=(12, 4))

# Before Scaling
plt.subplot(1, 3, 1)
sns.histplot(numeric_df[feature], kde=True)
plt.title(f"Before Scaling - {feature}")

# After Standardization
plt.subplot(1, 3, 2)
sns.histplot(df_standardized[feature], kde=True)
plt.title(f"After Standardization - {feature}")

# After Normalization
plt.subplot(1, 3, 3)
sns.histplot(df_normalized[feature], kde=True)
plt.title(f"After Normalization - {feature}")

plt.tight_layout()
plt.show()
