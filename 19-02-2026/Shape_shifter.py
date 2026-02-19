import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reproducibility
np.random.seed(42)

# Generate datasets
heights = np.random.normal(loc=170, scale=10, size=1000)          # Normal
incomes = np.random.exponential(scale=50000, size=1000)          # Right-skewed
scores = 100 - np.random.exponential(scale=10, size=1000)        # Left-skewed
scores = np.clip(scores, 0, 100)

# Create DataFrame
df = pd.DataFrame({
    'Heights': heights,
    'Incomes': incomes,
    'Scores': scores
})

# Plot Histogram + KDE
plt.figure(figsize=(15,5))

for i, col in enumerate(df.columns, 1):
    plt.subplot(1, 3, i)
    sns.histplot(df[col], kde=True)
    plt.title(col)

plt.tight_layout()
plt.show()

# Mean vs Median and Skewness identification
print("\nMean, Median & Skewness Type:\n")

for col in df.columns:
    mean = df[col].mean()
    median = df[col].median()
    
    if mean > median:
        skew = "Right Skewed"
    elif mean < median:
        skew = "Left Skewed"
    else:
        skew = "Normal Distribution"
        
    print(f"{col}: Mean = {mean:.2f}, Median = {median:.2f} → {skew}")
