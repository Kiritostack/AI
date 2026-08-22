sample_predictions = [
    {"label": "cat", "confidence": 0.45},
    {"label": "dog", "confidence": 0.89},
    {"label": "bird", "confidence": 0.12}
]
def filter_predictions(predictions, threshold):
    return [
        prediction
        for prediction in predictions
        if prediction.get("confidence", 0) >= threshold
    ]


def count_classes(predictions):
    counts = {}

    for prediction in predictions:
        cls = prediction["label"]
        counts[cls] = counts.get(cls, 0) + 1

    return counts


def top_prediction(predictions):
    if not predictions:
        return None

    return max(
        predictions,
        key=lambda prediction: prediction["confidence"]
    )


def analyze_predictions(predictions, threshold):

    valid = filter_predictions(predictions, threshold)

    return {
        "total": len(predictions),
        "valid": len(valid),
        "classes": count_classes(valid),
        "top_prediction": top_prediction(valid)
        
    }
print(analyze_predictions(sample_predictions,0.8))