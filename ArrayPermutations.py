from itertools import permutations

# input array
arr = [12, 20, 76, 7, 3, 10, 18239, 2, 3, 21]
# create permutations using permutations function from itertools class, set of 3 elements
perm = permutations(arr, 3)  # return an object
mul_arr = []
new_arr = []

# create a list of permutations from perm
for each in perm:
    new_arr.append(each)

# loop through list
for x in new_arr:
    mul = 1
    # loop through tuple
    for y in x:
        # multiply each value of a tuple
        mul *= y
    # add mul to mul_arr list
    mul_arr.append(mul)

# sort the list
mul_arr.sort()
# get the last element
print(mul_arr.pop())
