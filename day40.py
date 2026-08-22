predictions = [
    {"class": "cat", "confidence": 0.91},
    {"class": "dog", "confidence": 0.45},
    {"class": "cat", "confidence": 0.84},
    {"class": "car", "confidence": 0.98}
]
def count(predictions):
    coun=0
    for cou in predictions:
        coun=coun+1
    return coun
def filter_scores(predictions,threshold):
    return[ prediction
            for prediction in predictions
            if prediction.get("confidence",0) >=threshold
    ]
def classes(predictions,threshold):
    count={}
    for prediction in predictions:
        if prediction["confidence"]>threshold:
         count[prediction["class"]]=count.get(prediction["class"],0)+1
    return count  
def top_prediction(predictions):
        return max(prediction["confidence"] for prediction in predictions)      
def class_name(predictions):
    return max(predictions,key=lambda predictions:predictions["class"])
def rank_scores(predictions):
    return sorted(
        predictions,
        key= lambda predictions:predictions["confidence"],
        reverse=True)
def analyze_predictions(predictions, threshold):
    return{
        "Total":count(predictions),
        "valid":len(filter_scores(predictions,threshold)),
        "classes":
         classes(predictions,0.8)
        ,"top predictions":{
            "class":class_name(predictions),
            "confidence":top_prediction(predictions)
                            }
    }
print(analyze_predictions(predictions,0.8))