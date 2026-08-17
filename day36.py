predictions = [
    "cat",
    "dog",
    "cat",
    "bird",
    "dog",
    "cat",
    "bird"
]
count={}
for item in predictions:
    count[item]=count.get(item,0)+1

dic={item:count for item,count in count.items()}
print(dic)