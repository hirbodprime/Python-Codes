from pathlib import Path
import os
BASE_DIR2 = Path(__file__).resolve().parent.parent
print("\npath: " , Path.cwd())

os.chdir(BASE_DIR2)

print("\npath: " , Path.cwd())
os.chdir("diginext")