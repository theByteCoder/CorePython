# in loops
for i in range(1, 3):
    print(i)
else:
    print("*")

# in exception handling
try:
    print(10 / 10)
except ArithmeticError:  # if exception, then no else
    print("Except coding is best")
else:  # if no exception, then else
    print("Else coding is best")
finally:
    print("Finally coding is best")

# with if condition
a = 10
if a < 2:
    print(10)
else:
    print(2)
