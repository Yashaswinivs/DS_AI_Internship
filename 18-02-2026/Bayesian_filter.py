# Given probabilities
P_spam = 0.10
P_ham = 0.90

P_free_given_spam = 0.90
P_free_given_ham = 0.05

# Total probability of "Free"
P_free = (P_free_given_spam * P_spam) + (P_free_given_ham * P_ham)

# Bayes' Theorem
P_spam_given_free = (P_free_given_spam * P_spam) / P_free

print("P(Free) =", P_free)
print("P(Spam | Free) =", P_spam_given_free)
