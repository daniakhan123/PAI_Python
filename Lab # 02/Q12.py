keys = []
values = []

num = int(input("Enter the number of elements you want to add to the lists: "))


print("Enter elements for list 1 :")
for i in range(num):
    element = input("Enter element  for list 1: ")
    keys.append(element)

print("Enter elements for list 2 :")
for i in range(num):
    element2 = input("Enter element for list 2: ")
    values.append(element2)

dict = {}
for i in range(num):
    dict[keys[i]] = values[i]

print(dict)
