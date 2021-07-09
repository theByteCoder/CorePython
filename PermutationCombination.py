from itertools import permutations, combinations

perm = permutations([12, 23, 34], 2)
comb = combinations([12, 23, 34], 2)

arr = [x for x in perm]
print(arr)
arr = [x for x in comb]
print(arr)
