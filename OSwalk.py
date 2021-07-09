import os

print(next(os.walk("C:/Code/Python/CorePython")))
paths, dirs, files = next(os.walk("C:/Code/Python/CorePython"))

print(paths)
for each in files:
    print(each)
