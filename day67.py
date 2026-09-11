from abc import ABC, abstractmethod

class JarvisModel(ABC):
    def __init__(self,prompt:str):
      self.prompt=prompt
    @abstractmethod
    def respond(self: str) -> str:
       pass
    @abstractmethod
    def get_model_info(self) -> str:
       pass
class LocalLLM(JarvisModel):
   def respond(self):
      return f"Local model response:{self.prompt}"
   def get_model_info(self):
      return f"Local model ollama is running"
      
class CloudLLM(JarvisModel):
   def respond(self):
      return f"Cloud model response:{self.prompt}"
   def get_model_info(self):
      return f"Cloud llm is running"

model = LocalLLM("Hello Jarvis")


print(model.get_model_info())
print(model.respond())
