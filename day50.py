import shutil
from pathlib import Path

src = Path("Projects1/archive")
dst = Path("Projects1/datasets_backup")
dst.parent.mkdir(parents=True, exist_ok=True)
shutil.copytree(src, dst,dirs_exist_ok=True)
print(dst.exists())
shutil.rmtree("Projects1/datasets_backup")
print(dst.exists())