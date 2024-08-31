def employee(name, sal=None):
    if sal is None:
        sal = 10000

    NewSalary= sal - (sal * 0.02)
    
    print("Employee Name:", name)
    print("Employee Salary after Deduction of 2% tax:", NewSalary)
    return

name = input("Employee name: ")
salary = input("Salary (leave blank for default): ")


if salary != " ":
    sal = float(salary)
else:
    sal = None

employee(name, sal)
