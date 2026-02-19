import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Reproducibility
np.random.seed(42)

# Step 1: Create heavily skewed dataset (Income-like data)
data = np.random.exponential(scale=50000, size=100000)

# Step 2: Repeated sampling
sample_means = []

for _ in range(1000):
    sample = np.random.choice(data, size=30, replace=False)
    sample_means.append(sample.mean())

# Step 3: Plot histogram of sample means
plt.figure(figsize=(8,5))
sns.histplot(sample_means, kde=True)
plt.title("Central Limit Theorem: Distribution of Sample Means")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()
