import matplotlib.pyplot as plt

students = ['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 
            'Student6', 'Student7', 'Student8', 'Student9', 'Student10']
math_marks = [75, 85, 90, 80, 70, 65, 88, 92, 78, 84]  
science_marks = [70, 80, 85, 78, 65, 60, 90, 95, 80, 83]  

plt.scatter(math_marks, science_marks, color='b', label='Marks Comparison')


plt.xlabel('Mathematics Marks')
plt.ylabel('Science Marks')
plt.title('Scatter Plot of Mathematics vs Science Marks')


plt.legend()

plt.grid(True)

plt.show()
