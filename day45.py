class AIModel:
    def __init__(self,name,accuracy):
        self.name=name
        self.accuracy=accuracy

    def display(self):
        print(f'{self.name}->{self.accuracy}')

    def is_accurate(self):
        return self.accuracy>=0.90
    def update_accuracy(self,new_accuracy):
        self.accuracy=new_accuracy
    def status(self):
        if self.is_accurate():
            return'Ready for deployment'
        else:
            return'Needs improvement'
model1=AIModel('GPT',0.86)
model1.display()
print(model1.status())
model2=AIModel('claude',0.82)
model1.update_accuracy(0.96)
model1.display()
print(model1.status())
print(model2.status())

   
        