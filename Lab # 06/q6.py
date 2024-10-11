import pandas as pd


df = pd.read_csv('world_alcohol.csv')

print(df.head())

filtered_df = df[(df['Year'] == 1987) | (df['Year'] == 1989)]
print(filtered_df)
