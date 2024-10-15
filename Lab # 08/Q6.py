import numpy as np
mat1 = np.random.randint(1 , 10 , size = (5 , 3))
print(mat1)
print()
mat2 = np.random.randint(1 , 10 , size = (3 , 2))
print(mat2)
print()
mat_mul = np.dot(mat1 , mat2)
print(mat_mul)
