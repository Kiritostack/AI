class JarvisModule( ):
    def __init__(self,request:str):
       self.request=request
    def process(self) ->str:
     return f"Generic Jarvis processing :{self.request}"
class LanguageModule(JarvisModule):
   def process(self)->str:
      return f"Jarvis is processing language :{self.request}"
class VisionModule(JarvisModule):
   def process(self)->str:
      return f"Jarvis is processing an image request:{self.request}"
class SpeechModule(JarvisModule):
   def process(self)->str:
      return f"Jarvis is processing speech request: {self.request}"

modules=[
  JarvisModule("Command"),
  LanguageModule("eng"),
  VisionModule("image.jpg"),
  SpeechModule("audio.mp3")

]
for module in modules:
   print(module.process())

def run_module(module: JarvisModule) -> None:
    print(module.process())