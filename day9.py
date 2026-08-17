import random
attempt=3
secret=random.randint(1,10)
print("guess the number")
while attempt>0:
    try:
       num=int(input("Guess the number between 1 to 10:"))
    except ValueError:
        print("Invalid format")
        continue
    if secret==num:
        print("you won")
        break
    elif secret>num:
        print("too low")
    elif secret<num:
        print("too high")
    attempt-=1     
    print(f"attempts:{attempt}")    
else:
    print("you lost")    

