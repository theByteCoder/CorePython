for item in enumerate('coding is great'):
    print(item)

for val in enumerate("Coding is best"):
    print(type(val))

each = enumerate("Everything")
print("Type of obj ", type(each))

# convert to a list
list_of_each = list(each)
print(list_of_each)

list_of_each = enumerate("Everything")
print(type(list_of_each))  # returns obj of type enumerate
print(list(list_of_each))  # return list
