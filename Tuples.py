tuples = (1, 2, 3)
print(tuples[1])

# tuples are immutable

# concat
tuples1 = (1, 2, 3)
tuples2 = (4, 5, 6)
print(tuples1 + tuples2)
tuples1 += tuples2
print(tuples1)

# repetition
print(tuples * 2)

# slicing
tuples *= 2
print(tuples[1:4])
print(tuples[1:4:2])
print(tuples[::-1])
