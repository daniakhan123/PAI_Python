
import pandas as pd


movie = {"Movie Name": ["Titanic", "DeadPool", "Avatar", "No Way Home", "Avengers Endgame"],
    "Revenue": [2100000, 2900000, 1320000, 69000, 784900],
    "Budget": [200000, 500000, 200000, 100000, 300000]}

df = pd.DataFrame(movie)
print_movies = df[(df["Revenue"] > 2000000) & (df["Budget"] < 1000000)]

print(print_movies)
