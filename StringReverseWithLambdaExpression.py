def my_string(val):
    words = val.split(' ')
    return list(map(lambda word: words[::-1], words))[0]


print(my_string('coding is great'))
