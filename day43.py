predictions = [
    {"class": "cat", "confidence": 0.91},
    {"class": "dog", "confidence": 0.75},
    {"class": "car", "confidence": 1.2},
    {"class": "bird"},
    {"class": "person", "confidence": 0.88}
]
def validate_predictions(predictions):
    valid=0
    invaild=0
    for prediction in predictions:
      if "confidence" not in prediction:
        invaild+=1
        continue
      val=prediction["confidence"]
      try:
        num=float(val)
        if 0.0 <= num <= 1.0:
         valid+=1
        else:
         invaild+=1   
      except(ValueError,TypeError):
        invaild+=1
      
    return {"valid":valid,"invaild":invaild}
print(validate_predictions(predictions))