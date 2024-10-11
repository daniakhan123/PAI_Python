import pandas as pd


df = pd.read_excel('employee.xlsx')

specified_year = int(input("Enter the year to filter employees: "))
filtered_employees = df[df['Year'] == specified_year]

print(filtered_employees)
