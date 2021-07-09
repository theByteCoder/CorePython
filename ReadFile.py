read_file = open("newReadWriteAppendFile.txt")
print(read_file.read())
read_file.seek(0)  # take cursor to first line
print(read_file.readline())
print(read_file.readline())
read_file.seek(0)
print(read_file.readlines())
read_file.seek(0)

for eachLine in read_file.readlines():
    print(eachLine)

read_file.close()
