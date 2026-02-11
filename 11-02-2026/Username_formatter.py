import pandas as pd

# Create the Series
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

# Clean the data: strip spaces and convert to lowercase
cleaned = usernames.str.strip().str.lower()

# Check which names contain the letter 'a'
contains_a = cleaned.str.contains('a')

print("Original Series:\n", usernames)
print("\nCleaned Series:\n", cleaned)
print("\nContains letter 'a':\n", contains_a)
