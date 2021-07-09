#  list
item_list = ["one", "two"]
item_list[1] = "edit"
item_list.insert(2, "three")
print(item_list)
print(type(item_list))
#  tuple - create new tuple
item_tuple = (1, 2, 3, 4)
print(item_tuple)
print(type(item_tuple))
#  tuple - convert list to tuple
item_new_tuple = tuple(item_list)
print(item_new_tuple)
print(type(item_new_tuple))
# convert tuple to list
item_list = list(item_new_tuple)
print(item_list)
print(type(item_list))
