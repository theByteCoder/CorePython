set_1 = {1, 2, 3, 4}
set_2 = set_1.copy()  # this is called shallow copy
print(set_1)
set_1.pop()
print(set_1)
set_1.pop()
print(set_1)
set_1.add(12)
print(set_1)
# update takes multiple values but they must be contained in an iterable like list or tuple
set_1.update([99, 88, 56])
# update takes multiple values but they must be contained in an iterable like list or tuple
set_1.update((99, 88, 56))
print(set_1)
set_1.remove(99)  # removing non existent values causes KeyError
print(set_1)
print(len(set_1))
set_1.discard(919)  # discarding non existent values does NOT cause KeyError
print(set_1)
print(set_2)
# union
set_3 = set_1.union(set_2)
print("set_3", set_3)
