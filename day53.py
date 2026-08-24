from pathlib import Path
import shutil

models = Path("Projects1/models")
backup = Path("Projects1/backups")

models_backup = backup / "models_backup"
gpt_source = models / "gpt.txt"
gpt_backup = backup / "gpt_metadata.txt"

try:
    backup.mkdir(parents=True, exist_ok=True)

    if not models.exists():
        raise FileNotFoundError(f"Source folder not found: {models}")

    shutil.copytree(models, models_backup, dirs_exist_ok=True)

    print(f"models_backup exists: {models_backup.exists()}")

    shutil.copy2(gpt_source, gpt_backup)

except FileNotFoundError as e:
    print(f"Error: {e}")

finally:
    print("Backup operation completed")