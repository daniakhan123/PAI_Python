user = input("Enter list : ")
list1 = user.split()

for i in range(len(list1)):
    list1[i] = int(list1[i])
    
num = int(input("Enter number : "))

i = 0
while i < len(list1):
    if list1[i] < num:
        del list1[i]  
    else:
        i += 1
        
print(list1)
