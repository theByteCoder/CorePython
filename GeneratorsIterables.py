def fibonacci(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b


num = 4
generator = fibonacci(num)
try:
    for x in range(num + 3):
        print(next(generator))
except StopIteration:
    print('End')
