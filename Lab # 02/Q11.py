students = {'Dania': [85, 90, 78],'Emaan': [92, 88, 79],'Zunaira': [70, 80, 85]}

def add_grade(name, grade):
        students[name].append(grade)
        print("Added grade", grade, "to", name + "'s list.")


def calculate_avg(name2):
        grades = students[name2]
        if len(grades) > 0:
            average = sum(grades) / len(grades)
            print("The average grade for",name2, "is:", round(average, 2))
        else:
            print(name2, "has no grades.")


def add_std(name3):
        students[name3] = []
        print("Added new student:", name3)


def remove_std(name4):
        del students[name]
        print("Removed student:", name4)

        
name = input("Emter students name whose grade you want to add : ")
grade = input ("Enter the Grade of that student : ")
add_grade(name, grade)   
name2 = input("Enter students name whose Averge you want to calculate : ")   
calculate_avg(name2)
name3 = input("Enter New students Name : ")       
add_std(name3)    
name4 = input("Emter students name who you want to remove :  ")         
remove_std(name4)    
