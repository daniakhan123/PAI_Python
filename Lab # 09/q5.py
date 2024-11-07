import matplotlib.pyplot as plt

genders = ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Male', 'Female']


male_count = genders.count('Male')
female_count = genders.count('Female')

gender_distribution = [male_count, female_count]
gender_labels = ['Male', 'Female']

plt.pie(gender_distribution, labels=gender_labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired(np.linspace(0, 1, len(gender_distribution))))
plt.title("Gender Distribution of Students")
plt.axis('equal')  
plt.show()
