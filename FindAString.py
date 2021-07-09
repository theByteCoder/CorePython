inp_str = "Coding is best"

# break string into array using list function
print(list(inp_str))

# using list comprehensions
arr = [each for each in inp_str]
print(arr)

#  find position of characters
is_found = inp_str.find("Coding is best")
print(is_found)
