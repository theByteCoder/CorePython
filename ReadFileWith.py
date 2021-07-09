# by using with-as, we do not need to close the file
with open("newReadWriteAppendFile.txt", mode='r') as read_file:
    print(read_file.read())
    read_file.seek(0)  # take cursor to first line
    print(read_file.readline())
    print(read_file.readline())
    read_file.seek(0)
    print(read_file.readlines())
    read_file.seek(0)

    for eachLine in read_file.readlines():
        print(eachLine)

    print(read_file.readable())
