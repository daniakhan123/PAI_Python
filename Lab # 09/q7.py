import matplotlib.pyplot as plt

years = [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
sea_levels = [0, 3.2, 4.5, 6.0, 8.0, 9.5, 12.0, 14.5, 16.5, 18.0, 20.0]


plt.scatter(years, sea_levels, color='blue', label='Sea Level Rise')

plt.xlabel('Year')
plt.ylabel('Sea Level Rise (mm)')
plt.title('Sea Level Rise Over the Past 100 Years')


plt.grid(True)

plt.legend()


plt.show()
