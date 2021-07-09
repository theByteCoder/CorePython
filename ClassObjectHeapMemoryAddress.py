class className:
    print("Anything")
    pass

    def __init__(self):
        self.val1 = "coding"
        self.val2 = "is great"


obj_1 = className()
obj_2 = className()

print(id(obj_1))
print(id(obj_2))

print(obj_1.val1, obj_1.val2)
