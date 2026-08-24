from collections import defaultdict

count = defaultdict(int)

models = ["GPT", "Claude", "GPT"]

for model in models:
    count[model] += 1

print(count["GPT"])
print(count["Claude"])