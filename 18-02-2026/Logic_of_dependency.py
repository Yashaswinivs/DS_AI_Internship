# Independent Events 

# Probability of Heads on a coin
P_heads = 1 / 2

# Probability of rolling 6 on a die
P_six = 1 / 6

# Independent probability formula
P_heads_and_six = P_heads * P_six

print("Independent Events:")
print("P(Heads AND 6) =", P_heads_and_six)

# Dependent Events 

# Marbles: 5 Red, 5 Blue
total_marbles = 10
red_marbles = 5

# First red
P_first_red = red_marbles / total_marbles

# After one red is removed
red_remaining = red_marbles - 1
total_remaining = total_marbles - 1
