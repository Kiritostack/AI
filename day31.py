features = [
    [20, 30000, 1],
    [25, 50000, 3],
    [30, 80000, 6]
]
def get_high_salary(features):
    lis=[]
    
    for row in features:
        if(row[1]>=50000):
            lis.append(row[1])     
    return lis
print(get_high_salary(features))            
