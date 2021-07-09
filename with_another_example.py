# using list comprehensions
string_any = "Coding is best"
arr = [x for x in string_any[::-1]]
print(arr)


# same code with WITH statement
class with_another_example(object):
    def __init__(self, string):
        self.string = string

    def __enter__(self):
        return [x for x in self.string[::-1]]

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with with_another_example("Coding is best") as foo:
    print(foo)
