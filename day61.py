class AIModel:
    def __init__(self, name: str, accuracy: float):
        self.name = name
        self._accuracy = accuracy

    def update_accuracy(self, accuracy: float) -> None:
        if 0 <= accuracy <= 1:
            self._accuracy = accuracy
        else:
            raise ValueError("Invalid accuracy")

    def get_accuracy(self) -> float:
        return self._accuracy
    def increase_accuracy(self, amount: float) -> None:
        if amount<0:
            raise ValueError
        new_accuracy=min(self._accuracy+amount,1)
        self.update_accuracy(new_accuracy)
    def decrease_accuracy(self, amount: float) -> None:
        if amount<0:
            raise ValueError
        new_accuracy=max(self._accuracy-amount,0)
        self.update_accuracy(new_accuracy)
model = AIModel("GPT", 0.90)

model.increase_accuracy(0.05)
print(model.get_accuracy())   

model.increase_accuracy(0.20)
print(model.get_accuracy())  
model = AIModel("GPT", 0.20)

model.decrease_accuracy(0.05)
print(model.get_accuracy())