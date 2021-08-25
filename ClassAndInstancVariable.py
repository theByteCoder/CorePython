class MyClass:
    increment_by = 10

    def __init__(self, increment):
        self.increment = increment

    @classmethod
    def get_increment_by(cls):
        return cls.increment_by

    @property
    def any_val(self):
        return self.any_val

    @any_val.setter
    def any_val(self, any_val):
        self.any_val = any_val

    @any_val.deleter
    def any_val(self):
        self.any_val = None


MyClass.increment_by = 20
print(MyClass.get_increment_by())
print(id(MyClass.any_val))
MyClass.any_val = 30
print(MyClass.any_val)
print(id(MyClass.any_val))
del MyClass.any_val
# print(MyClass.any_val)
