import os

path, dirs, files = next(os.walk("C:\Code\Python\CorePython"))

print("path is", path)
print("dirs are", dirs)

print("files are", files)
print("total number of files is", len(files))

file_count = 0
for file in files:
    if file.endswith(".py"):
        file_count += 1

print("total number of .py files is", file_count)
