from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer

# Load data (using breast cancer as a proxy for binary classification)
data = load_breast_cancer()
X, y = data.data, data.target

# Define the grid
param_grid = {
    'max_depth': [2, 4, 6, 8, 10],
    'criterion': ['gini', 'entropy']
}

# Initialize Grid Search
grid = GridSearchCV(
    estimator=DecisionTreeClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring='accuracy'
)

# Fit
grid.fit(X, y)

print(f"Best Parameters: {grid.best_params_}")
print(f"Best CV Accuracy: {grid.best_score_:.4f}")
