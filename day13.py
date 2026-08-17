import numpy as np
marks=[]
n=int(input("Enter the no of students:"))
for i in range(n):
    m=int(input(f"enter the marks{i+1}:"))
    marks.append(m)

marks_arr=np.array(marks)

print("data Analysis")
print("mean:",np.mean(marks_arr))
print("Highest:",np.max(marks_arr))    