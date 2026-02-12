import pandas as pd

# Create the Series
products = pd.Series([700, 150, 300], index=['Laptop', 'Mouse', 'Keyboard'])

# Access price of Laptop using label-based indexing
laptop_price = products['Laptop']

# Slice first two products using positional indexing
first_two = products.iloc[:2]

print("Full Series:\n", products)
print("\nPrice of Laptop:", laptop_price)
print("\nFirst two products:\n", first_two)

