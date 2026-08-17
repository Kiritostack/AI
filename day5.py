def get_marks():
    marks=[]
    for i in range(1,6):
        m=int(input(f"Enter the marks{i}:"))
        marks.append(m)
    return marks
def summary(marks):
    total=sum(marks)
    average=sum(marks)/len(marks)
    highest=max(marks)
    minimum=min(marks)
    return total,average,highest,minimum
def grade(marks):
    pass_count=0
    for m in marks:
     if m>=90:
        pass_count=pass_count+1
        print("Grade A")
     elif m>=80:
        print("Grade B")
        pass_count=pass_count+1
     elif m>=60:
       print("Grade C")
       pass_count=pass_count+1
     elif m>=40:
        print("Grade E")
        pass_count=pass_count+1
     else:
      print("fail")
    print(f"pass count={pass_count}")

marks=get_marks()
total,average,highest,minimum=summary(marks)
print(f"highest={highest}")
print(f"average={average}")
print(f"minimum={minimum}")
print(f"total={total}")
grade(marks)