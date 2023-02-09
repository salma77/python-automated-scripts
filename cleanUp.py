import os, sys

type = sys.argv[1]
dir_path = sys.argv[2]
files = [f for f in os.listdir(dir_path)]
print(files)

for file in files:
    if os.path.isfile(dir_path + file) and file.endswith(str(type)):
        os.remove(dir_path + file)
        print("file has successfully been deleted")