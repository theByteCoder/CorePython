string = "Coding is best"

# not operator
if not string.__contains__("test"):
    print(string)

# pipe operator
if string.__contains__("test") | string.__contains__("best"):
    print(string)

# or operator
if string.__contains__("test") or string.__contains__("best"):
    print(string)

# & operator
if string.__contains__("test") & string.__contains__("best"):
    print(string)
else:
    print("Nothing")

# and operator
if string.__contains__("test") and string.__contains__("best"):
    print(string)
else:
    print("Nothing")
