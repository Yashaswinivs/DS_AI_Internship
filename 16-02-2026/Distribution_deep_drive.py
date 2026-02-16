import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

# Load dataset
df = pd.read_csv("dataset.csv")

# 1. Histogram + KDE for Price
plt.figure(figsize=(7,5))
sns.histplot(df['Price'], kde=True)
plt.title("Distribution of Price")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

# 2. Skewness and Kurtosis
price_skew = skew(df['Price'])
price_kurt = kurtosis(df['Price'])

print("Skewness of Price:", price_skew)
print("Kurtosis of Price:", price_kurt)

# 3. Count Plot for Categorical Column (Location / City)
plt.figure(figsize=(7,5))
sns.countplot(x='Location', data=df)
plt.title("Count Plot of Location")
plt.xlabel("Location")
plt.ylabel("Count")
plt.show()
