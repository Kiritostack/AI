responses ={"hello":"Hello Kunal",
            "name":"I am Jarvis",
            "creator":"Kunal created me"}
while True:
    command = input("You: ").strip().lower()
    if command =="bye":
        print("Jarvis:Ok ,bye sir")
        break
    elif command in responses:
        print("Jarvis:",responses[command])
    else:
     print("Jarvis:I am still learning")
    