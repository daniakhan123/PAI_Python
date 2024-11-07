import matplotlib.pyplot as plt

ages = [22, 24, 25, 19, 30, 35, 28, 27, 31, 34, 18, 20, 36, 32, 29, 33, 40, 41, 25, 26]


age_groups = ['18-25', '26-30', '31-35', '36 and above']

group_18_25 = len([age for age in ages if 18 <= age <= 25])
group_26_30 = len([age for age in ages if 26 <= age <= 30])
group_31_35 = len([age for age in ages if 31 <= age <= 35])
group_36_above = len([age for age in ages if age >= 36])


age_distribution = [group_18_25, group_26_30, group_31_35, group_36_above]

plt.pie(age_distribution, labels=age_groups, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired(np.linspace(0, 1, len(age_distribution))))
plt.title("Distribution of Student Ages")
plt.axis('equal')
plt.show()
