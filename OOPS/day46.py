class AIModel:
    def __init__(self, name, accuracy):
        self.name = name
        self.accuracy = accuracy

    def display(self):
        print(f"{self.name} -> {self.accuracy}")

    def compare(self,other):
        if self.accuracy>other.accuracy:
            return f'{self.name} is better'
        elif other.accuracy>self.accuracy:
         return f'{self.name} is better'
        else:
            return'Both models have equal accuracy'
model1 = AIModel("GPT", 0.96)
model2 = AIModel("Claude", 0.92)


print(model1.compare(model2))

