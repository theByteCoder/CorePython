class A:
    def __init__(self):
        print('A')

    def __str__(self):
        return self.a


class B:
    def __init__(self):
        print('B')

    def __str__(self):
        return self.b


class C(A, B):
    def __init__(self):
        super().__init__()
        print('C')

    def __str__(self):
        return self.c


c = C()
