predictions = [
    {"class": "cat", "confidence": 0.91},
    {"class": "dog", "confidence": 0.76},
    {"class": "cat", "confidence": 0.84},
    {"class": "car", "confidence": 0.98},
    {"class": "dog", "confidence": 0.88}
]
classes=set(p['class'] for p in predictions)
pre={cls:sum(p['confidence']for p in predictions if p['class']==cls) / sum(1 for p in predictions if p['class']==cls)
     for cls in classes}
print(pre)