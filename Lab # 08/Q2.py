import numpy as np

arr = np.arange(1, 19 , 2)
arr = arr.reshape(3,3)
print(arr)

for x in arr:
    for y in x:
        print(y )
        
        
