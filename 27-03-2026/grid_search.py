from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
X, y = data.data, data.target

param_grid = {'max_depth': [2, 5, 10]}

# Tune for Accuracy
grid_acc = GridSearchCV(DecisionTreeClassifier(), param_grid, scoring='accuracy', cv=3)
grid_acc.fit(X, y)

# Tune for F1
grid_f1 = GridSearchCV(DecisionTreeClassifier(), param_grid, scoring='f1', cv=3)
grid_f1.fit(X, y)

print(f"Best Depth (Accuracy): {grid_acc.best_params_['max_depth']}")
print(f"Best Depth (F1):       {grid_f1.best_params_['max_depth']}")