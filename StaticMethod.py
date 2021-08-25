class A(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b


class B(A):
    b = 1

    def __init__(self, a):
        super().__init__(a, self.b)

    @staticmethod
    def show(class_object):
        return tuple([class_object.a, class_object.b])


# obj_a = A(1, 2)
# print(B.show(obj_a))

obj_b = B(1)
print(B.show(obj_b))
