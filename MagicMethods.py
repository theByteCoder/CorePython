a = b = 1

print(a + b)
print(int.__add__(a, b))


class A:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.b


class B:
    def __init__(self, b):
        self.b = b


a = A(10)
b = B(2)
print(a + b)

a = A('c')
b = B('d')
print(a + b)
