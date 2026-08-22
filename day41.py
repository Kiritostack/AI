def top_prediction(predictions):
    if not predictions:
        return None
    # Finds the full dictionary with the highest confidence
    return max(predictions, key=lambda p: p["confidence"])

# Example dataset
sample_predictions = [
    {"label": "cat", "confidence": 0.45},
    {"label": "dog", "confidence": 0.89},
    {"label": "bird", "confidence": 0.12}
]

# Get the result
best_prediction = top_prediction(sample_predictions)

# Print the result and its object class
print("Result:", best_prediction)
print("Class of result:", type(best_prediction))
