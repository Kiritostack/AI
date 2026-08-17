data=["AI", "ML", "AI", "Python", "ML", "AI"]
def most_frequent(data):
    if not data:
        return{}

    count={}
    for item in data:
        count[item]=count.get(item,0)+1

    mostocur=None
    high=-1
    for item,count in count.items():
        if count>high:
            high=count
            mostocur=item   
    return mostocur

print(most_frequent(data))
             