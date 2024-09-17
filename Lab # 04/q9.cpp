class student:
    def __init__(self , id , name):
        self.id = id
        self.name = name
        
    def printInfo(self):
        print(f"ID : {self.id}")
        print(f"Name : {self.name}")
        
class marks(student):
    def __init__(self ,id , name ,  marks_algo=0 , marks_dataScience=0 , makrs_cal=0):
        super().__init__(id , name)
    
        self.marks_algo = marks_algo
        self.marks_dataScience = marks_dataScience
        self.marks_cal = makrs_cal
        
    def obtainMarks(self):
        self.marks_dataScience = int(input("Enter marks of Data Sceince : "))
        self.marks_algo = int(input("Enter marks of Algorithm : "))
        self.marks_cal = int(input("Enter marks of Calculus : "))
        
        
    def displayMarks(self):
        print("Data Sceince Marks : ",self.marks_dataScience)
        print("Algorithm Marks : ",self.marks_algo)
        print("Calculus Marks : ",self.marks_cal)
        
class result(marks):
    def __init__(self , id , name):
        super().__init__(id , name)
        self.total = 0
        self.avg = 0

    def total_marks_avg_marks(self):
        self.total = self.marks_algo + self.marks_dataScience + self.marks_cal
        print(f"Total Marks  : {self.total}")
        self.avg = self.total/3
        print(f"Average  : {self.avg}")

        
    
my_result = result(230072 ,"Dania")
my_result.printInfo()
my_result.obtainMarks()
my_result.displayMarks()
my_result.total_marks_avg_marks()
        
        
        
