class AIModel:
    def __init__(self, name, accuracy):
        self.name = name
        self.accuracy = accuracy

    def get_best(models):
     
      if not models:
          return None
      return max(models,key=lambda models:models.accuracy)

    def display(self):
        print(f"{self.name} -> {self.accuracy}")
models = [
   
]

best =AIModel.get_best(models)
if best is not None:
    best.display()
else:
    print('No model to display')    



    