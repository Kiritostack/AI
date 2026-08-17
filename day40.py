scores = [
    {"name": "Model-A", "score": 0.91},
    {"name": "Model-B", "score": 0.72},
    {"name": "Model-C", "score": 0.96},
    {"name": "Model-D", "score": 0.84}
]
def filter_scores(scores,threshold):
    return[ scor
            for scor in scores
            if scor.get("score",0) >=threshold
    ]
def rank_scores(scores):
    return sorted(
        scores,
        key= lambda scores:scores["score"],
        reverse=True)
filtered=filter_scores(scores,0.8)
print(rank_scores(filtered))
        