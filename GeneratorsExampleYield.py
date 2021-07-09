def gen_func():
    n = [4, 3, 2, 1]
    yield [1, 2, 3, 4]
    yield n
    return n


for x in gen_func():
    print(x)

new_arr = gen_func()
print(type(new_arr))
