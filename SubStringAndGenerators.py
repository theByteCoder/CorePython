string = "Coding is great"

print(string[0:2])  # prints Co

print(string[2:5])  # prints din

print(string[-1])  # prints last character. In this case t

print(string[::-1])  # prints in reverse


# using generator return a yield of reverse string captured in list
def generator_string():
    yield [x for x in string[::-1]]


for y in generator_string():
    print(y)
