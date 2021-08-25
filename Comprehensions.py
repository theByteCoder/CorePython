# list comprehension
def generator():
    for x in range(100):
        yield x


all_lists = generator()
prime_numbers = [item for item in all_lists if item % 2 != 0]
for y in prime_numbers:
    # print(y)
    pass

# dict comprehension
any_dict = {'a': 1, 'b': 2, 'A': 3}
sum_only_a = {key.lower(): (any_dict.get(key.lower(), 0) + any_dict.get(key.upper(), 0)) for key in any_dict.keys()}
print(sum_only_a)

# dict comprehension
any_set = {1, 2, 3, 4, 5, 4, 3, 2, 1}
print({item ** 2 for item in any_set})
