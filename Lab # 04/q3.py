class Student():

    def __init__(self , name , age):
        self.name = name
        self.age= age
        
    def print_biodata(self):
        print(self.name)
        print(self.age)
        
infor= Student("Dania" , 20)
infor.print_biodata()
    
