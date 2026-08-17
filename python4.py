response={
    "hello":"Hello Kunal",
            "name":"I am Jarvis",
            "creator":"Kunal created me",
            "ai":"Ai stands for Artificial Intelligence",
            "python":"python is a programming language",
            "future": "The future belongs to AI engineers like you"
}
while True:
    command=input("You: ").strip().lower()
    if(command =="bye"):
        print("Jarvis: I have learned ",len(response),"commands")
        print("bye, sir")
        break
    elif command in response:
        print("Jarvis: ",response[command])
    else:
        print("Jarvis: I don't know yet.")
        new_res=input("Teach me What should I reply: ")
        response[command]=new_res
        print("Jarvis: Got it,I learned something new.")