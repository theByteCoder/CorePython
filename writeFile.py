with open("newReadWriteAppendFile.txt", "w") as writeContent:
    writeContent.write("Coding is the best")

with open("newReadWriteAppendFile.txt", "a") as appendContent:
    appendContent.write("\nCoding is the best thing")

with open("newReadWriteAppendFile.txt", "r") as readContent:
    print(readContent.read())
