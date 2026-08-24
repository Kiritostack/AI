import shutil as s
from pathlib import Path
src_path=Path("Projects1/model.txt")
dis_path=Path("Projects1/backup/model_backup.txt")
dis_path.parent.mkdir(parents=True, exist_ok=True)
s.copy(src_path,dis_path)

