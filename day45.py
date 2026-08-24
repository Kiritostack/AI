from pathlib import Path

folder = Path("datasets")
folder.mkdir()

print(folder.exists())