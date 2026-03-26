import warnings
from sklearn.datasets import load_iris
from sklearn.model_selection import LeaveOneOut
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Suppress warnings
warnings.filterwarnings("ignore")

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Logistic Regression as an example model
model = LogisticRegression()

# Leave-One-Out Cross-Validation
loo = LeaveOneOut()
loo_accuracies = []

for train_index, test_index in loo.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    loo_accuracies.append(accuracy)

print(f"Leave-One-Out Cross-Validation Accuracies: {loo_accuracies}")