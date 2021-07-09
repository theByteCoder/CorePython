def parameters(a, b):
    print(a + b)


def new_parameters(a, b=3):
    print(a + b)


def test_func():
    print("coding is great")


parameters(1, 2)
new_parameters(1)
new_parameters(1, 2)
parameters(a=1, b=2)

test_func()
