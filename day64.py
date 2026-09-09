class JarvisModel:
        
    def respond(self,input_data) -> str:
        return f"Generic Jarvis response:{input_data}"
class TextModel(JarvisModel):
    def respond(self,input_data):
        return f"Text model responding to:{input_data}"
class VisionModel(JarvisModel):
    def respond(self,input_data):
        return f"Vision model analyzing:{input_data}"
class SpeechModel(JarvisModel):
    def respond(self,input_data):
        return f"Speech model processing:{input_data}"
models = [
    TextModel(),
    VisionModel(),
    SpeechModel()
]
for model in models:
    print(model.respond("Hello Jarvis"))