from sklearn.model_selection import RandomizedSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer
from scipy.stats import randint

# Load data
data = load_breast_cancer()
X, y = data.data, data.target

# Define distributions
param_dist = {
    'max_depth': randint(2, 20),
    'min_samples_split': randint(2, 20),
    'criterion': ['gini', 'entropy']
}

# Initialize Random Search
random_search = RandomizedSearchCV(
    estimator=DecisionTreeClassifier(random_state=42),
    param_distributions=param_dist,
    n_iter=15, # Only test 15 random combinations
    cv=5,
    scoring='accuracy',
    random_state=42
)

# Fit
random_search.fit(X, y)

print(f"Best Parameters: {random_search.best_params_}")
print(f"Best CV Accuracy: {random_search.best_score_:.4f}")