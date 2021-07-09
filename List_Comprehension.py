word = "coding is great"

# old method
my_list = []
for letter in word:
    my_list.append(letter)
print(my_list)

# comprehension method
my_list = [letter for letter in word]
print(my_list)

# comprehension method
my_list = [num for num in range(1, 100)]
print(my_list)

# comprehension method - add conditions
my_list = [num for num in range(1, 100) if num % 2 == 0]
print(my_list)


def add_suffix(each_letter):
    return f'{each_letter} suffix'


chars = []
each_name = [add_suffix(each_letter) for each_letter in word]
print(each_name)
