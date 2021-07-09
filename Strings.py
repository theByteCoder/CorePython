val = "coding is great"
print(len(val))
print(val[1])
print(val[len(val) - 1])
print(val[-1])  # reverse indexing
print(val[-2])

# substrings
print(val[1:3])

# capitalize
print(val.capitalize())


# starting from position- includes character
print(val[1:])
# ending before position - excludes character
print(val[:3])
# step size - jumps 3 characters
print(val[::2])
# step size - jumps four characters
print(val[::3])

# split
print(val.split())
print(val.split("i"))
