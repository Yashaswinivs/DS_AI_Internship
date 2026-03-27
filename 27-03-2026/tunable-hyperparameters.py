from sklearn.tree import DecisionTreeClassifier

# Initialize a default model
model = DecisionTreeClassifier()

# Get all tunable hyperparameters
params = model.get_params()

print("Tunable Hyperparameters for DecisionTreeClassifier:")
for key, value in params.items():
    print(f"{key:20} : {value}")

print("\nKey hyperparameters for complexity:")
print("- max_depth (Tree depth)")
print("- min_samples_split (Minimum samples to split)")