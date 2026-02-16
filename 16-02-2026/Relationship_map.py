import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dataset.csv")

# Scatter Plot: SquareFootage vs Price
plt.figure(figsize=(7,5))
sns.scatterplot(x='SquareFootage', y='Price', data=df)
plt.title("Square Footage vs Price")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.show()

# Boxplot: Category vs Price (Example: Location)
plt.figure(figsize=(7,5))
sns.boxplot(x='Location', y='Price', data=df)
plt.title("Location vs Price")
plt.xlabel("Location")
plt.ylabel("Price")
plt.show()
