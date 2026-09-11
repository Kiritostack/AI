import json
import os
class Jarvis:
    def __init__(self):
      self.learned_responses = {}
      self.intent_responses={}
      self.load_memory()
    def respond(self,command):
        intent=self.intent_detection(command)
        if intent =="bye":
            print("Jarvis: bye, sir")
            return False
        elif intent =="stats":
            self.stats()
            return True
        if intent in self.intent_responses:
            print("Jarvis:", self.intent_responses[intent])
            return True
            
        
        if command.startswith("forget "):
            forgotten_command=command.replace("forget ","",1)
            print(f"Jarvis:",self.forget(forgotten_command))
            return True
        if command in self.learned_responses:
            print("Jarvis:",self.learned_responses[command])
            return True
        
        print("Jarvis: I don't know this yet,Sir.")
        new_res = input("Jarvis: Teach me :")
        self.learn(command,new_res)
        print("Jarvis: Learned successfully")
        return True
    def learn(self,command,response):
        self.learned_responses[command]=response
        self.save_memory()
    def intent_detection(self,command:str)->str:
       command=command.lower()
       words=command.split()
       if any(greet in words for greet in ["hello","hi","hey"]):
          return "greetings"
       elif "creator" in words or "who created you" in command or "made you" in command:
          return "creator"
       elif "stats" in words:
          return "stats"
       elif "bye" in words or "goodbye" in words:
          return "bye"
       else:
          return "unknown"
          
    def forget(self,command):
       remove=self.learned_responses.pop(command,None)
       if remove is None:
          return("I don't know that command")
       self.save_memory()
       return f"I have forgotten the command:{command}"
    def stats(self):
        print("Total learned commands:", len(self.intent_responses)+len(self.learned_responses))
    def load_memory(self):
       if  os.path.exists("responses.json"):
          try:
             with open("responses.json","r") as file:
              data=json.load(file)
              self.intent_responses=data.get("intent_responses",{})
              self.learned_responses=data.get("learned_responses",{})
          except json.JSONDecodeError:
             self.gotointent()
       else:
          self.gotointent()
    def gotointent(self):
       self.intent_responses={
                    "greetings":"Hello Sir",
                    "creator":"Kirito created me."
                 }
       self.learned_responses={}
       self.save_memory()
    def save_memory(self):
       data={
          "intent_responses":self.intent_responses,
          "learned_responses":self.learned_responses
       }
       with open("responses.json","w")as file:
           json.dump(data,file,indent=4)
    def normalize_command(self,text):
       return text.strip().lower()
    def run(self):
        print("Jarvis:Online and ready, Sir.")
        while True:
            raw_command =input("You: ")
            command=self.normalize_command(raw_command)
            if not self.respond(command):
               break
if __name__=="__main__":
  assistant =Jarvis()
  assistant.run()

