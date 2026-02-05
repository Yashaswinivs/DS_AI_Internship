# Dictionary with at least three contacts
contacts = {
    "Alice": "9876543210",
    "Bob": "9123456780",
    "Charlie": "9988776655"
}
# Add a new contact
contacts["Diana"] = "9012345678"
# Update an existing contact's phone number
contacts["Bob"] = "9000000000"
# Safe access using .get()
existing_contact = contacts.get("Alice", "Contact not found")
missing_contact = contacts.get("Eve", "Contact not found")
# Display safe lookup results
print("Safe Lookup Results:")
print("Alice:", existing_contact)
print("Eve:", missing_contact)
print("\nContact List:")
# Iterate and print all contacts
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
