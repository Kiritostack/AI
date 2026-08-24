import shutil as s
from pathlib import Path

src=Path("model.txt")
dis=Path("Projects1/metadata_backup/model.txt")
try:
    
    dis.parent.mkdir(parents=True,exist_ok=True)
    s.copy2(src,dis)
    print(dis.exists())
except FileNotFoundError:
    print("File not found")