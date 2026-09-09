class AIModel:
    def __init__(self,name:str,accuracy:float):
        self.name=name
        self.accuracy=accuracy
    def get_info(self):
        print(f"name:{self.name}->accuracy:{self.accuracy}")

class LanguageModel(AIModel):
    def __init__(self,name,accuracy,language):
        super().__init__(name, accuracy)
        self.language=language
    def get_info(self):
        print(f"name:{self.name},accuracy:{self.accuracy},language:{self.language}")
    def generate_response(self,prompt:str):
        print(f"{self.name} is generating text to:{prompt}")
class VisionModel(AIModel):
    def __init__(self,name,accuracy,image_path):
            super().__init__(name, accuracy)
            self.image_path=image_path
    def analyze_image(self):
        print(f"Jarvis Vision is analyzing:{self.image_path}")
    def get_info(self):
            print(f"name:{self.name},accuracy:{self.accuracy},image_size:{self.image_path}")
model=VisionModel(" Jarvis",0.96,"image.jpg")
print(model.analyze_image())
model1=LanguageModel("Jarvis",0.96,"eng")
print(model1.generate_response("Jarvis"))
model2=AIModel("GPT",0.96)
print(model2.get_info())