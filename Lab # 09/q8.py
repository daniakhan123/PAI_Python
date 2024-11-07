import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
y2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

plt.plot(x, y1, label="y1 = Prime Numbers", color='pink', marker='o')
plt.plot(x, y2, label="y2 = Squares", color='gray', marker='o')
plt.title("Two Lines on One Graph")
plt.xlabel("Amazing X-axis")
plt.ylabel("Incredible Y-axis")
plt.legend(loc='lower right')
plt.show()
