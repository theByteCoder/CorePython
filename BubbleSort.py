lst = [5, 4, 3, 6, 1, 2, 77, -1, 2, 89, 111, 2, 3, 4]
swapped = True

while swapped:
    swapped = False
    for x in range(len(lst)):
        try:
            if lst[x] > lst[x + 1]:
                swapped = True
                lst[x], lst[x + 1] = lst[x + 1], lst[x]
        except IndexError:
            pass

print(lst)
