import matplotlib.pyplot as plt

flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint", "Cookies & Cream"]
scoops_sold = [500, 350, 250, 150, 100]

plt.pie(scoops_sold, labels=flavors, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired(np.linspace(0, 1, len(scoops_sold))))
plt.title("Distribution of Ice Cream Sales")
plt.axis('equal')
plt.show()
