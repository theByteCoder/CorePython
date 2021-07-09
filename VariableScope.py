def first_method():
    # local scope
    y = 20
    x = 20
    print(x, y)
    print(x + y)
    try:
        print(x / y)
    except ZeroDivisionError as e:
        print(e)


# global scope
x = 10
y = 0
first_method()
