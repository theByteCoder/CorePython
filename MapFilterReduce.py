lists = [item for item in range(10)]


def square(n):
    return n ** 2


def filter_primes(n):
    return n % 2 == 0


maps = list(map(square, lists))
print(maps)
filters = list(filter(filter_primes, lists))
print(filters)


def reducer(a, b):
    return a + b


from functools import reduce

reduces = reduce(reducer, lists)
print(reduces)
