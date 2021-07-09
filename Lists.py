lists = ["one", "one", "test", 1, 2]

lists[2] = 5
print(lists[2])
print(lists[-1])

lists.pop()
print(lists)

# range
print(lists[1:])
print(lists[1:3])
print(lists[1:3:2])

# reverse
print(lists[::-1])
# OR try below
lists.reverse()
print(lists)

lists.append("Appended")
print(lists)

print(len(lists))

# count number of repeating elements
print(lists.count("one"))

# add 2 lists
secondList = [1, 2, 3, 4]
newList = lists + secondList
print(newList)

# copy lists
newList = lists.copy()
lists.append("Copy")  # copy creates a new entity
print(newList)

# extend
lists.extend(["coding is great"])
print(lists)

# insert
lists.insert(3, [123, 456])
print(lists)
