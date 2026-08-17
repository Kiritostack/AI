secret_number=7
for i in range(3):
    print(f"Your attempt no.{i+1}/3")
    try:
      guess=int(input("Enter your guess(1,10):"))
    except:
     print("INVALID INPUT")
     continue
    if guess==secret_number:
     print("You are right")
     break
    elif guess >secret_number:
      print("too high")
    else:
       print("too low")
else:
  print("you lost")       