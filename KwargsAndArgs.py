def method_kwargs(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f'{key}: {value}')


def method_args(*args):
    print(type(args))
    for val in args:
        print(val)


method_args(1, 2, 3, 4, 5)
method_kwargs(name='Subhasish', surname='Ghosh')
