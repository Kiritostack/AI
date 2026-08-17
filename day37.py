predictions = [
    {"class": "cat", "confidence": 0.91},
    {"class": "dog", "confidence": 0.76},
    {"class": "car", "confidence": 0.98},
    {"class": "bird", "confidence": 0.84}
]
print(sorted(predictions,key=lambda predictions:predictions["confidence"],reverse=True)[:2])