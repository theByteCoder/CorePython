for x in range(2, 10, 2):
    print(x)

my_list = list(range(2, 20, 2))
print(my_list)

# generate list within range
print(list(range(2, 20, 2)))

list_from_list = enumerate(list(range(2, 20, 2)))
print(list(list_from_list))
