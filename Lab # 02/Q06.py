user = input("Enter a list :  ")
list1 = [int(x) for x in user.split()]


mul = 1
i=[0]

for i in list1:
    mul = mul * i
    i = i+1
    
print("the product of all the elements in the list is : ",mul)
