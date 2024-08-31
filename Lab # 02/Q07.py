temp = [34,45,32,49,26,47,28,39,34,19,24,56,17,43,27,21,13,18,15,29,53,42,31,14,9,33,11,35,20,45]

sum = 0 
for i in temp:
    sum = sum + i

avg = sum / 30
print("The Average Temperature of the Month is : " , avg)

maxtemp = temp[0]
for i in temp:
    if(i>maxtemp):
        maxtemp = i
    
print("The maximum temperature is : ",maxtemp)

mintemp = temp[0]
for i in temp:
    if(i<mintemp):
        mintemp = i

print("The maximum temperature is : ",mintemp)

        
ascending = sorted(temp)
print("Temperatures in Ascending Order:", ascending)
        
print("Before removing : ",temp)
removeDay = 24
temp.pop(removeDay)
print("After removing : ",temp)

