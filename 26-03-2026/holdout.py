# Does not work well with imbalanced dataset

import warnings
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Suppress warnings
warnings.filterwarnings("ignore")

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Logistic Regression as an example model
model = LogisticRegression()

# Holdout Cross-Validation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
holdout_accuracy = accuracy_score(y_test, y_pred)

print(f"Holdout Cross-Validation Accuracy: {holdout_accuracy}")