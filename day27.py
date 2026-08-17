text = "AI ML AI Python ML AI"

words = text.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(words)
print(set(words))
print(frequency)