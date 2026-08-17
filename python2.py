number=[]
for i in range(5):
    num = int(input("Enter number:"))
    number.append(num)

    maximum=max(number)
    minimum=min(number)
    average=sum(number)/len(number)
    print("Numbers:",number)
    print("Maximum",maximum)
    print("Minimum",minimum)
    print("Average",average)
