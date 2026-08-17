marks=[]
pass_count=0
for i in range(1,6):
    m=int(input("Enter the marks:"))
    marks.append(m)
total=sum(marks)
average=total/len(marks)
highest=max(marks)
minimum=min(marks)
print(f"highest={highest}")
print(f"average={average}")
print(f"minimum={minimum}")
print(f"total={total}")
for m in marks:
    if m>=40:
        pass_count=pass_count+1
        print("Grade E")
    elif m>60:
        print("Grade C")
    elif m>80:
       print("Grade B")
    elif m>90:
        print("Grade A")
    else:
      print("fail")
print(f"pass count={pass_count}")