
phy = int(input("Enter marks for Physics: "))
chem = int(input("Enter marks for Chemistry: "))
math = int(input("Enter marks for Maths: "))

marks = {
    "Physics": phy,
    "Chemistry": chem,
    "Maths": math
}

total= phy+ chem + math
average = total / 3

highest= max(marks, key=marks.get)

print("Average Marks:", average)
print("Subject with the Highest Marks:", highest)
