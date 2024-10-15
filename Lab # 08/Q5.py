import numpy as np

mat1 = np.random.choice([2 , 5, 9, 10], size=(4 , 4))
print(mat1)
print()
mat2 = np.eye(4 ,4)
print(mat2)
print()
mat_mul = np.dot(mat1 , mat2)
print("after multiplication : ")
print(mat_mul)
mat3 = np.array([[1 , 3, 5 ,7],
                 [9, 11, 13, 15 ],
                 [17, 19, 21, 23],
                 [25, 27 , 29, 31]])

add_mat = mat_mul + mat3
print("after addition : ")
print(add_mat)

