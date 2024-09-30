import pandas as pd

# Define the movie data
movie = {
    "Movie Name": ["Titanic", "DeadPool", "Avatar", "No Way Home", "Avengers Endgame"],
    "Revenue": [2100000, 2900000, 1320000, 69000, 784900],
    "Budget": [200000, 500000, 200000, 100000, 300000],
    "Runtime": [454, 160, 678, 345, 890]  # Corrected the number of elements
}

# Create the DataFrame
df = pd.DataFrame(movie)

# Sort the DataFrame by Runtime in descending order
sorted_df = df.sort_values(by='Runtime', ascending=False)

# Print the sorted DataFrame
print(sorted_df)
