import random

trials = 1000
count_sum_7 = 0

for _ in range(trials):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    if dice1 + dice2 == 7:
        count_sum_7 += 1

experimental_probability = count_sum_7 / trials

print("Number of times sum = 7:", count_sum_7)
print("Experimental Probability:", experimental_probability)
