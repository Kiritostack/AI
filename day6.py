students={}
n=int(input("Enter the number of students"))
for i in range(n):
    name=input("Enter the name:")
    marks=int(input("Enter the marks:"))
    students[name]=marks
print("\nStudents record")
for name,marks in students.items():
    print(f"{name} ->{marks}")
print("\n topper")
topper=max(students,key=students.get)
print(f"Topper:{topper}({students[topper]})")
print("\nGrades:")
for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "E"
    else:
        grade = "Fail"

    print(f"{name} → Grade {grade}")

search=input("enter the name of the student")
if search in students:
    print(f"{search} scored {students[search]}")
else:
    print("not found")