from pathlib import Path
path=Path("models.txt")
with path.open("r") as file:
    print(file.read())

with path.open("a") as file:
    file.write("\nMistral")
with path.open("r") as file:
    print(file.read())
with open("models.txt", "x") as file:
    file.write("\nGPT")
