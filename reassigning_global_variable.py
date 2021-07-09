x = 100


def my_func():
    global x  # global changes global variable value
    print('local ' + str(x))
    x = 'Test'
    print('local ' + str(x))


print('global ' + str(x))
my_func()
print('new global ' + str(x))
