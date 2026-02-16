import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dataset.csv")

# 1. Correlation Matrix
corr = df.corr(numeric_only=True)

# 2. Heatmap Visualization
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.show()

# 3. Identify highly correlated variables (> 0.8)
high_corr = corr[(corr > 0.8) & (corr < 1.0)]
print("Highly correlated variable pairs (correlation > 0.8):")
print(high_corr)

# 4. Boxplot to detect outliers in main numerical column (Price)
plt.figure(figsize=(6,4))
sns.boxplot(y=df['Price'])
plt.title("Boxplot of Price (Outlier Detection)")
plt.ylabel("Price")
plt.show()
