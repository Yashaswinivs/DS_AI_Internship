import numpy as np

# Create a 5x3 array of random integers between 50 and 100
scores = np.random.randint(50, 101, size=(5, 3))

# Calculate column-wise mean (mean of each subject)
mean_scores = scores.mean(axis=0)

# Subtract mean using broadcasting
centered_scores = scores - mean_scores

print("Original Scores:\n", scores)
print("\nMean of Each Subject:\n", mean_scores)
print("\nCentered (Normalized) Scores:\n", centered_scores)
