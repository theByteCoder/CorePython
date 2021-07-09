for x in "banana":
    print(x)

for y in range(len("banana")):
    print(y)

for z in range(2, 100, 3):
    print(z)

count = 1
while count < 10:
    print(count)
    count += 1

# tuple unpacking
json_object = [
    (1, 2, 10),
    (3, 4, 11),
    (5, 6, 12),
]
for a, b, c in json_object:
    print(a, b, c)
    print(a)
    print(b)
    print(c)

# dictionary unpacking
dict_obj = {
    "one": 1,
    "two": 2,
    3: 3,
    4: [11, 12, 13]
}
for items in dict_obj.items():
    print(items)
for key, values in dict_obj.items():
    print(key)
    print(values)
