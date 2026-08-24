from pathlib import Path
path=Path("predictions.txt")
try:
    with path.open("r") as file:
        print(file.read())
except FileNotFoundError:
    print("Predictions file not found")
finally:
    print("File operation finished")

    