a = [1]
b = a  # make dependent copy of a. Any changes to a will effect b
print(b)
a[0] = 0
print(b)

x = [1]
y = x[:]  # make independent copy of x. Any changes to x will not effect y
print(y)
x[0] = 0
print(y)
