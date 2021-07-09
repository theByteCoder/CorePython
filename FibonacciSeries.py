series = 0
n1 = 0
n2 = 1
print(n1)
print(n2)
for x in range(2, 7, 1):
    series = n1 + n2
    n1 = n2
    n2 = series
    print(series)
