
friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
# common interests using intersection
shared_interests = friend_a & friend_b
# all unique interests using union
all_interests = friend_a | friend_b
# interests unique to friend_a using difference
unique_to_a = friend_a - friend_b
# Print the results
print("Shared Interests:", shared_interests)
print("All Interests:", all_interests)
print("Interests unique to Friend A:", unique_to_a)
