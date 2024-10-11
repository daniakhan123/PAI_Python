import pandas as pd

products_df = pd.read_csv('products.csv')
orders_df = pd.read_csv('orders.csv')

print("First 5 rows of products_df:")
print(products_df.head())
print("\nLast 10 rows of products_df:")
print(products_df.tail(10))

print("\nFirst 5 rows of orders_df:")
print(orders_df.head())
print("\nLast 10 rows of orders_df:")
print(orders_df.tail(10))

merged_df = pd.merge(orders_df, products_df, on='ProductID')


merged_df['Revenue'] = merged_df['Quantity'] * merged_df['Price']

total_rev = merged_df['Revenue'].sum()
print(f"\nTotal Revenue: {total_rev}")

sale = merged_df.groupby('ProductName')['Quantity'].sum().reset_index()

best_selling = sale.sort_values(by='Quantity', ascending=False).head(5)
print("\nTop 5 Best-Selling Products:")
print(best_selling)

low_selling = sale.sort_values(by='Quantity', ascending=True).head(5)
print("\nTop 5 Low-Selling Products:")
print(low_selling)

top_5_merged = pd.merge(best_selling, products_df, on='ProductName')
common= top_5_merged['Category'].mode()[0]
print(f"\nMost Common Category among Top 5 Best-Selling Products: {common}")


avg = products_df.groupby('Category')['Price'].mean().reset_index()
print("\nAverage Price of Products in Each Category:")
print(avg)

merged_df['Order Date'] = pd.to_datetime(merged_df['Order Date'], format='%m-%d-%Y')


merged_df['Day'] = merged_df['Order Date'].dt.day
merged_df['Month'] = merged_df['Order Date'].dt.month
merged_df['Year'] = merged_df['Order Date'].dt.year


day_revenue = merged_df.groupby('Day')['Revenue'].sum().idxmax()
month_revenue = merged_df.groupby('Month')['Revenue'].sum().idxmax()
year_revenue = merged_df.groupby('Year')['Revenue'].sum().idxmax()

print(f"\nDay with highest total revenue: {day_revenue}")
print(f"Month with highest total revenue: {month_revenue}")
print(f"Year with highest total revenue: {year_revenue}")

monthly_revenue = merged_df.groupby('Month')['Revenue'].sum().reset_index()
monthly_revenue.columns = ['Month', 'Total Revenue']
print("\nTotal Revenue for Each Month:")
print(monthly_revenue)

print("\nChecking for null values in products_df:")
print(products_df.isnull().sum())

print("\nChecking for null values in orders_df:")
print(orders_df.isnull().sum())


