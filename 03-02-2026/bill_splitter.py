# Take inputs
total_bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))

# Calculate share
share = total_bill / people

# Output
print("Total Bill:", total_bill)
print("Each person pays:", share)

# Bonus (type checking)
print(type(total_bill))
print(type(people))
print(type(share))
