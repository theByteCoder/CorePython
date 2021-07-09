# without using with
# write file
val = open("ReadWriteAppendFile.txt", "w")
try:
    val.write("Coding is great")
finally:
    val.close()
# read file
val = open("ReadWriteAppendFile.txt", "r")
print(val.read())
val.close()

# in the above code, notice that write and close have been handled in try finally blocks to avoid exception

# performing same action with WITH statement
# write file
with open("ReadWriteAppendFile.txt", mode="w") as new_val:
    new_val.write("Coding is best")
# WITH statement automatically handles exceptions and closes the file
# read file
with open("ReadWriteAppendFile.txt", mode="r") as foo:
    print(foo.read())
