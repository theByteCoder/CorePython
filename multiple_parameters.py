def abc(*numbers):
    return numbers


print(abc(1, 2, 3, 4, 5, 'a'))


def xyz(**numbers):
    return numbers


print(abc(1, 2, 3, 4, 5, 'a'))
print(xyz(a=1, b=12, c=3, d=4))
