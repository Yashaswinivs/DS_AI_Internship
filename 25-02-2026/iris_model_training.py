# Step 1: Import required libraries




# Step 2: Load dataset
df = pd.read_csv("iris.csv")
print("Dataset Loaded Successfully\n")
print(df.head())

# Step 3: Feature & Target separation
X = df.drop("species", axis=1)
y = df["species"]

# Step 4: Encode target labels
encoder = LabelEncoder()
y = encoder.fit_transform(y)


# Step 5: Train-Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# Step 6: Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 7: Model Training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 8: Prediction
y_pred = model.predict(X_test)

# Step 9: Evaluation
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", accuracy)

print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=encoder.classes_))

# Step 10: Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

# -------- GRAPH 1: Confusion Matrix Heatmap --------
plt.figure()
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=encoder.classes_,
            yticklabels=encoder.classes_)
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix Heatmap")
plt.show()

# -------- GRAPH 2: Feature Importance --------
importances = model.feature_importances_
features = X.columns

plt.figure()
plt.bar(features, importances)
plt.xlabel("Features")
plt.ylabel("Importance Score")
plt.title("Feature Importance Graph")
plt.show()

# -------- GRAPH 3: Actual vs Predicted --------
plt.figure()
plt.plot(y_test, label="Actual", marker='o')
plt.plot(y_pred, label="Predicted", marker='x')
plt.legend()
plt.title("Actual vs Predicted Output")
plt.xlabel("Sample Index")
plt.ylabel("Class")
plt.show()