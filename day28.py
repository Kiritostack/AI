text = "AI AI ML Python AI ML"

words = text.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)
print(frequency["AI"])
print(frequency.get("Java", 0))
