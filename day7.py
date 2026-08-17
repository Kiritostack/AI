students={}
n=int(input("Enter the number of students:"))
for i in range(n):
    name=input("enter the name:")
    marks=int(input("enter the marks:"))
    students[name]=marks
print("\nStudents record")
with open("data.txt","w") as file:
    for name, marks in students.items():
        file.write(f"{name},{marks}\n")

print("data saved")

with open("data.txt","r") as file:
    for line in file:
        name, marks=line.strip().split(",")
        marks=int(marks)
        print(f"{name} ->{marks}")
 