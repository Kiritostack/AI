from models.metrics import calculate_score
from models.validation import get_model_status

accuracy = calculate_score(96, 100)

print(accuracy)
print(get_model_status(accuracy))