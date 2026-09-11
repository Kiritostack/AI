class Jarvis:
    def __init__(self):
      self.responses={
            "hi":"Hello Sir",
            "creator":"Kunal created me"
        }
    def respond(self,command):
        if command in self.responses:
            print("Jarvis:", self.responses[command])
        else:
            print("Jarvis: I don't know this yet.")
            new_res = input("Jarvis: Teach me :")
            self.learn(command,new_res)
            print("Jarvis: Learned successfully")
    def learn(self,command,response):
        self.responses[command]=response
    def forget(self,command):
       remove=self.responses.pop(command,None)
       if remove is None:
          return("I don't know that command")
       return f"I have forgotten the command:{command}"
    def stats(self):
        print("Total learned commands:", len(self.responses))
    def run(self):
        while True:
            command =input("You: ").strip().lower()

            if(command =="bye"):
             print("Jarvis: bye, sir")
             break
            elif(command =="stats"):
               self.stats()
               continue
            elif command.startswith("forget"):
               forgotten_command=command.replace("forget "," ",1)
               print(f"Jarvis:",self.forget(forgotten_command))
               continue
            self.respond(command)
 
assistant =Jarvis()
assistant.run()

