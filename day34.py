def frequency_count(data):
    counts = {}
    for item in data:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


data = ["Python", "AI", "Python", "ML", "AI", "Python"]


result = frequency_count(data)
print(result)