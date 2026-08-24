import shutil
import os

try:
    os.makedirs("project1/backup",exist_ok=True)
    shutil.copytree("datasets","project1/backup/datasets",dirs_exist_ok=True)
    if os.path.exists("project1/backup/datasets"):
       print("Copied folder:True")
    else:
       print("Copied folder:false")
except FileNotFoundError:
    print("File not found")

finally:
     print("Operation Successfull")
