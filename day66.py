from abc import ABC, abstractmethod

class JarvisComponent(ABC):
    def __init__(self, prompt: str):
        self.prompt = prompt
        
    @abstractmethod
    def process(self) -> str:
        pass

class SpeechComponent(JarvisComponent):
    def process(self) -> str:
        return f"Processing speech: {self.prompt}"

class LanguageComponent(JarvisComponent):
    def process(self) -> str:
        return f"Processing language: {self.prompt}"

class VisionComponent(JarvisComponent):
    def process(self) -> str:
        return f"Vision response: {self.prompt}"

def get_component(prompt: str) -> JarvisComponent:
  
    clean_prompt = prompt.lower().strip()
   
    if "hello jarvis" in clean_prompt:
        return LanguageComponent(prompt)
    

    elif clean_prompt.endswith(('.jpg', '.jpeg', '.png')):
        return VisionComponent(prompt)
    elif clean_prompt.endswith(('.mp3', '.wav', '.flac')):
        return SpeechComponent(prompt)
    else:
        return LanguageComponent(prompt)

inputs = ["Hello Jarvis", "image.jpg", "audio.mp3", "What is the weather today?"]

for user_input in inputs:
    component = get_component(user_input)
    print(component.process())
