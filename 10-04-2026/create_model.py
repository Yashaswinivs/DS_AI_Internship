from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pickle

# Dummy data (just for testing)
X = np.array([
    [0.5, 0.3, 0.1, 0.8],
    [0.6, 0.4, 0.2, 0.9],
    [0.4, 0.2, 0.1, 0.7],
    [0.7, 0.5, 0.3, 1.0]
])

y = np.array([0, 1, 0, 1])  # labels

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model saved as model.pkl")