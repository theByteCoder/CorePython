from abc import ABC, abstractmethod


class A(ABC):
    y = 10

    def __init__(self, x):
        self.x = x

    @abstractmethod
    def abstract_method_1(self):
        pass

    @abstractmethod
    def abstract_method_2(self):
        pass

    @staticmethod
    def concrete_method():
        print('concrete method')

    @classmethod
    def class_method(cls):
        print(cls.y)


class B(A):
    def __init__(self):
        super().__init__('abstract parent')
        print('constructor')

    def abstract_method_1(self):
        print('abstract_method_1')

    def abstract_method_2(self):
        print('abstract_method_2')


b = B()
print(b.x)
b.abstract_method_1()
b.abstract_method_2()
B.concrete_method()
B.class_method()