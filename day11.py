class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "Fail"

class School:
    def __init__(self):
        self.students=[]
    def add_std(self,Student):
        self.students.append(Student)           
    def show_std(self):
        print("Student record:\n")
        for s in self.students:
         print(f"{s.name} -> {s.marks}(grade{s.get_grade()})")
    def get_topper(self):
         if not self.students:
             print("Students not found")
         topper=max(self.students,key=lambda s:s.marks)
         print(f"Topper: {topper.name}->{topper.marks}({topper.get_grade()})")

school =School()

n=int(input("enter number of students:"))
for i in range(n):
    name=input("Enter the name:")
    marks=int(input("enter the marks:"))

    std=Student(name,marks)
    school.add_std(std)
school.show_std()
school.get_topper()     
