import numpy as np
import pandas as pd

# Sample dataset (you can replace this with pd.read_csv("dataset.csv"))
np.random.seed(42)
data = np.random.normal(loc=50, scale=10, size=1000)

df = pd.DataFrame({'Values': data})

# Step 1: Calculate Mean and Standard Deviation
mean = df['Values'].mean()
std = df['Values'].std()

# Step 2: Calculate Z-score
df['z_score'] = (df['Values'] - mean) / std

# Step 3: Identify Outliers
outliers = df[np.abs(df['z_score']) > 3]

# Print results
print(f"Mean (μ): {mean:.2f}")
print(f"Standard Deviation (σ): {std:.2f}")
print("\nOutliers (|Z| > 3):")
print(outliers)
