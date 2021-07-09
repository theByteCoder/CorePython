lists = ["any value", 1, 2.5, True]

# remove from last
lists.pop()
print(lists)

# remove from any index
lists.pop(2)
print(lists)

# add to last
lists.append("coding is great")
print(lists)

# add at any index
lists[len(lists) - 1] = 78
print(lists)

# get length
print(len(lists))

# clear list
lists.clear()

# add 2 lists
new_list = lists + [1, 1, 2, 4, 6, 3, 5]
print(new_list)

# sort list
new_list.sort()
print(new_list)

# convert list to set
new_list = set(new_list)
print(new_list)

# convert set to list
new_list = list(new_list)
print(new_list)

# reverse list
new_list.reverse()
print(new_list)