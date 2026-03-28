# ================================
# Phase 0: Import Libraries
# ================================
import numpy as np
import pandas as pd
import time

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report

# ================================
# Phase 1: Data Architecture
# ================================

# Generate Dataset (1000 students, 20 features, imbalanced)
X, y = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=10,
    n_redundant=5,
    n_classes=2,
    weights=[0.9, 0.1],   # 90% placed, 10% unplaced
    random_state=42
)

# Train-Test Split (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Feature Scaling (Fit ONLY on training data)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ================================
# Phase 2: Baseline Model
# ================================

baseline_model = RandomForestClassifier(random_state=42)
baseline_model.fit(X_train_scaled, y_train)

y_pred = baseline_model.predict(X_test_scaled)

baseline_acc = accuracy_score(y_test, y_pred)
baseline_f1 = f1_score(y_test, y_pred)

print("=== Baseline Model ===")
print("Accuracy:", baseline_acc)
print("F1 Score:", baseline_f1)
print(classification_report(y_test, y_pred))


# ================================
# Phase 2: Grid Search (Accuracy)
# ================================

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

grid_acc = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

grid_acc.fit(X_train_scaled, y_train)

best_acc_model = grid_acc.best_estimator_

y_pred_acc = best_acc_model.predict(X_test_scaled)

print("\n=== Grid Search (Accuracy) ===")
print("Best Params:", grid_acc.best_params_)
print("Accuracy:", accuracy_score(y_test, y_pred_acc))
print("F1 Score:", f1_score(y_test, y_pred_acc))


# ================================
# Phase 2: Grid Search (F1 Score)
# ================================

grid_f1 = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='f1',
    n_jobs=-1
)

grid_f1.fit(X_train_scaled, y_train)

best_f1_model = grid_f1.best_estimator_

y_pred_f1 = best_f1_model.predict(X_test_scaled)

print("\n=== Grid Search (F1 Score) ===")
print("Best Params:", grid_f1.best_params_)
print("Accuracy:", accuracy_score(y_test, y_pred_f1))
print("F1 Score:", f1_score(y_test, y_pred_f1))


# ================================
# Phase 3: Efficiency Warfare
# ================================

# Measure Grid Search Time
start_time = time.time()

grid_full = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='f1',
    n_jobs=-1
)

grid_full.fit(X_train_scaled, y_train)

grid_time = time.time() - start_time

grid_best_f1 = f1_score(y_test, grid_full.best_estimator_.predict(X_test_scaled))


# ================================
# Randomized Search
# ================================

param_dist = {
    'n_estimators': np.arange(10, 500),
    'max_depth': [None] + list(np.arange(5, 30)),
    'min_samples_split': np.arange(2, 15)
}

start_time = time.time()

random_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    param_distributions=param_dist,
    n_iter=20,
    cv=5,
    scoring='f1',
    random_state=42,
    n_jobs=-1
)

random_search.fit(X_train_scaled, y_train)

random_time = time.time() - start_time

random_best_f1 = f1_score(y_test, random_search.best_estimator_.predict(X_test_scaled))


# ================================
# Comparison Table
# ================================

results = pd.DataFrame({
    "Method": ["GridSearchCV", "RandomizedSearchCV"],
    "Time Taken (sec)": [round(grid_time, 2), round(random_time, 2)],
    "Best F1 Score": [round(grid_best_f1, 4), round(random_best_f1, 4)]
})

print("\n=== Efficiency Comparison ===")
print(results)