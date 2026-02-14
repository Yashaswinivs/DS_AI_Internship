import matplotlib.pyplot as plt

# ---------- Subplot 1: Bar Chart ----------
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")

# ---------- Subplot 2: Line Plot ----------
months = [1, 2, 3, 4, 5]
revenue = [200, 350, 300, 500, 650]

plt.subplot(1, 2, 2)
plt.plot(months, revenue, marker='o')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display plots
plt.show()
