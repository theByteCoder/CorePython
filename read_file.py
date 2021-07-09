file_content = open("ReadWriteAppendFile.txt", "r")


def file_read():
    print(file_content.read())


def file_read_line():
    print(file_content.readline())


def file_readable():
    print(file_content.readable())


def file_read_all_lines():
    for content in file_content.readlines():
        print(content)


def file_read_in_array():
    print(file_content.readlines())


# file_read_all_lines()
# file_read()
# file_read_in_array()
# file_read_line()
# file_read_line()
file_readable()
