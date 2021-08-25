lists = [1, 2, 3, 4, 5, 6, 7]

updated_list = [*lists, 8, 9]

print(updated_list)

first, *mid, last = lists

print(first, mid, last)

params = {'c': 2, 'd': 2, 'e': 2, 'b': 2, 'a': 1}
a, b, rest = (lambda a, b, **rest: (a, b, rest))(**params)

print(a, b, rest)
