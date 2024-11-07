
import matplotlib.pyplot as plt
import numpy as np

students = ["student1", "student2", "student3", "student4", "student5", "student6", 
            "student7", "student8", "student9", "student10", "student11", "student12", 
            "student13", "student14", "student15", "student16", "student17", "student18", 
            "student19", "student20"]

heights = [160, 155, 170, 165, 180, 175, 168, 162, 155, 173,160, 159, 167, 174, 180, 169, 166, 160, 158, 172]

plt.figure(figsize=(10, 6))
bar_colors = np.random.rand(len(students))
plt.bar(students, heights, color=plt.cm.jet(bar_colors))
plt.xlabel("Students")
plt.ylabel("Height (cm)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 8))
plt.pie(heights, labels=students, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired(np.linspace(0, 1, len(heights))))
plt.title('Student Height Distribution')
plt.axis('equal')
plt.show()
