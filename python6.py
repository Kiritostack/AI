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
            self.responses[command]=new_res
            print("Jarvis: Learned successfully")
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
        
            self.respond(command)
 
assistant =Jarvis()
assistant.run()

