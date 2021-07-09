my_list1 = [1, 2, 3]
my_list2 = ["a", "b", "c"]

for item in zip(my_list1, my_list2):
    print(item)

zipped_list = tuple(zip(my_list1, my_list2))
print(zipped_list)
