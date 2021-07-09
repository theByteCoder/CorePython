# keyword arguments return dictionary
def my_kwargs_func(**kwargs):
    print(kwargs)


my_kwargs_func(one='2', two='4')


# args return tuple
def my_args_func(*args):
    print(args)


my_args_func(1, 2, 3, 4, 5, 55, 6, 66, 777, 8, 9)


# non positional arguments
def kwargs_test(*test):
    return test


val = kwargs_test(1, 2, 3, 4, 5)
print(val)


# positional arguments
def kwargs_positional_test(**args):
    return args


val = kwargs_positional_test(one='a', two='b')
print(val)
