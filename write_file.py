file_content = open("ReadWriteAppendFile.txt", "w")


def is_writable():
    print(file_content.writable())


def write_new_file():
    old_file_content = open("ReadWriteAppendFile.txt", "r")
    new_file_content = open("newReadWriteAppendFile.txt", "w")
    existing_text = old_file_content.read()
    new_file_content.write(existing_text)


def write_old_file():
    file_content.write("Coding is the best thing that ever happened to to")


write_new_file()
# is_writable()
