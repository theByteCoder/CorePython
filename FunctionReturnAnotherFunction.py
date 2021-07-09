def first_method(val):
    def second_method():
        print(val)

    return second_method


newVal = first_method("Coding is great")
newVal()
