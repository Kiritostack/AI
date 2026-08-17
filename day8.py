student={}
try:
    n=int(input("Enter number of students:"))
except ValueError:
    print("invalid input")
    n=0
    
for i in range(n):
    name=input("Enter the name of the student:")
    
    try:
        marks=int(input("Enter the marks:"))
        if marks<0 or marks>100:
         print("enter marks between 0 to 100:")
         break
    except ValueError:
        print("Invalid input")

    student[name]=marks

try:
    with open("daa.txt","w") as file:
        for name,marks in student.items():
            file.write(f"{name},{marks}\n")
    print("data saved")

except Exception as e:
    print("Error in saving the file",e)


print("read data\n")
  
try:
    with open("daa.txt","r") as file:
        for line in file:
            name,marks=line.strip().split(",")
            marks=int(marks)
            print(f"{name}->{marks}")  
except FileNotFoundError:
    print("file is not found")




