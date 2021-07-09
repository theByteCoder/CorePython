my_list = [1, 2, 3]

# in python anonymous funcs are defined by expression lambda
print(list(map(lambda x: x * 2, my_list)))

for items in map(lambda x: x * 2, my_list):
    print(items)


# normal function
def my_func(num):
    if num % 2 == 0:
        return num
    else:
        return 'odd'


my_list = [2, 3, 6]
# lambda expression of function with map
print(list(map(lambda num: num if num % 2 == 0 else 'odd', my_list)))
print(list(filter(lambda num: num if num % 2 == 0 else 'odd', my_list)))
