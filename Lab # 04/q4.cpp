class Employee():
    def __init__(self):
        self.name = ""
        self.sal = 0
        self.tax_per = 2
        
    def get_data(self):
        self.name = input("Enter Employee name: ")
        self.sal = int(input("Enter Employee Salaray : "))
        self.tax_per = int(input("Enter Tax Percentage : "))
    def Salary_after_tax(self):
        tax = 2/100
        self.sal= self.sal - self.sal*(self.tax_per/100)
        print("Salary after tax : ",self.sal)
            
    def update_tax_percentage(self):
        
        tax_update = int(input("Enter Updated Percentage of Tax "))
        self.sal = self.sal - self.sal*(tax_update/100)
        print("Salary after tax update: ",self.sal)

        
    
ep = Employee()
ep.get_data()
ep.Salary_after_tax()
ep.update_tax_percentage()
