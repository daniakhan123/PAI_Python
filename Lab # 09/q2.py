
import matplotlib.pyplot as plt

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
populations = [8175133, 3792621, 2695598, 2129784, 1445632]

plt.barh(cities, populations, color='skyblue')
plt.xlabel("Population")
plt.ylabel("Cities")
plt.title("Population of Cities")
plt.show()
