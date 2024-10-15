import numpy as np

data_type = [('name', 'S20'), ('class', int), ('height', float)]

students = [
    ('Dania', 10, 5.9),
    ('Tanisha', 9, 5.2),
    ('Zunaira', 10, 6.0),
    ('Emaan', 9, 5.8),
    ('Murtaza', 9, 5.7),
    ('Muneeb', 10, 5.8)
]

std = np.array(students, dtype=data_type)#structured array

sorted = np.sort(std, order=['class', 'height'])

print("Sorted Students by class and then height:")
for student in sorted:
    print(student)

