filename = input("Enter the filename to open (e.g., config.txt): ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile Content:")
        print(content)

except FileNotFoundError:
    print("Oops! That file doesn't exist yet ")
