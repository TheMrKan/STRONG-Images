import pillow
import os

for path in os.listdir():
    new_name = path.split("_")[-1]
    try:
        os.rename(path, new_name)
    except:
        continue
