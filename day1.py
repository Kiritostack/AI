name =input("Enter your name:")
age=int(input("Enter your age:"))
height=float(input("enter your height:"))

print(f"\nHello {name},you are {age} years old!")
print(f"Your Height is {height:.2f} feet")
if (age<0):
    print("INVAILD AGE")
if(age>=18):
    print("you are an adult")
else:
    print("you are an minor")
