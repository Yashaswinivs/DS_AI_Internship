# list with duplicate user IDs
raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
# the list into a set to remove duplicates
unique_users = set(raw_logs)
# Print the unique user IDs
print("Unique Users:", unique_users)
# Check if a specific ID exists in the set
print("Is ID05 present?", "ID05" in unique_users)
# Print the count of original list and unique set
print("Total log entries:", len(raw_logs))
print("Unique users count:", len(unique_users))
