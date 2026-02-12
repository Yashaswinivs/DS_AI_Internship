import pandas as pd

# Create the Series with missing values
grades = pd.Series([85, None, 92, 45, None, 78, 55])


# Identify missing values
missing = grades.isnull()

# Fill missing values with 0
filled_grades = grades.fillna(0)

# Apply boolean mask to filter scores > 60
filtered_scores = filled_grades[filled_grades > 60]

print("Original Series:\n", grades)
print("\nMissing Values (True = Missing):\n", missing)
print("\nSeries after filling missing values:\n", filled_grades)
print("\nScores greater than 60:\n", filtered_scores)
