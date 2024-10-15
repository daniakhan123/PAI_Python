import numpy as np

random = np.random.randn(1000)

average = np.mean(random)
variance = np.var(random)
std_deviation = np.std(random)

with open("results.txt", "w") as f:
    f.write(f"Average: {average}\n")
    f.write(f"Variance: {variance}\n")
    f.write(f"Standard Deviation: {std_deviation}\n")

print("Results have been saved to 'results.txt'")
