class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def grade(self):
        if self.marks>=90:
            return "A"
        elif self.marks>=60:
            return "B"
        elif self.marks>=40:
            return "C"
        else:
            return "Fail"

    def display(self):
        print(f"{self.name} passed with {self.marks},Grade = {self.grade()}")

students =[]
n=int(input("enter the number of students,you want:"))
for i in range(n):
 name=input("Enter the name")
 marks=int(input("enter the marks"))
 s=student(name,marks)
 students.append(s)



print("print the records")

for s in students:
    s.display()




