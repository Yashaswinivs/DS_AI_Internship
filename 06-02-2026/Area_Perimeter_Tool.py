# Define the function ( create a function that takes length and width, calculates:
# Area = length × width
# Perimeter = 2 × (length + width)and then returns both values)
# Take user input and Call the function and print the result
def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area, perimeter = calc_rectangle(length, width)
print(f"Area: {area}, Perimeter: {perimeter}")
