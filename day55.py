import json

data = {"model": "Claude", "accuracy": 0.92}

text = json.dumps(data)
result = json.loads(text)

print(result["model"])
print(type(text))