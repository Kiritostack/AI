import os
print(os.getcwd())
print(os.listdir())
print(os.path.exists("main.py"))
path=os.path.join("Projects","main.py")
print(path)
print(os.path.exists(path))
