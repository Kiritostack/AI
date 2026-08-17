predictions = [
    {"class": "cat", "confidence": 0.91},
    {"class": "dog", "confidence": 0.76},
    {"class": "cat", "confidence": 0.84},
    {"class": "car", "confidence": 0.98},
    {"class": "dog", "confidence": 0.88}
]
totals = {}
counts = {}

for prediction in predictions:
    cls = prediction["class"]
    confidence = prediction["confidence"]

    totals[cls] = totals.get(cls, 0) + confidence
    counts[cls] = counts.get(cls, 0) + 1
averages = {
    cls: totals[cls] / counts[cls]
    for cls in totals
}
print(averages)