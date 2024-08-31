list1  = input("Enter list : ")
list2 = [int(x) for x in list1.split()]


print(list2)

mul = 1

for i in range(0 , len(list2)):
    mul = mul * i

print("product of all elements in the list is : " , mul)

    
    
    
    
