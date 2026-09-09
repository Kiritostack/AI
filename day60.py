class AIModel:
    def __init__(self, name: str, accuracy: float):
        self.name = name
        if 0<=accuracy<=1:
         self._accuracy = accuracy
        else:
            raise ValueError("out of range") 
    def get_accuracy(self):
       return self._accuracy
    def update_accuracy(self,new_accuracy:float)->None:
       if 0.0<=new_accuracy<=1.0:
          self._accuracy=new_accuracy
       else:
          raise ValueError("out of range")    
    def display(self):
       print(f"Name:{self.name},Accuracy:{self._accuracy}")  
    def improve(self,amount:float)->None:
       if amount < 0:
        raise ValueError("Improvement amount cannot be negative")
       new_accuracy=min(self._accuracy+amount,1.0)
       self.update_accuracy(new_accuracy)
aimodel=AIModel("GPT",0.2)
aimodel.improve(0.4)
aimodel.display()

    
    