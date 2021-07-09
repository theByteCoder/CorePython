string = "Coding is best"
sub_string = "i"
result = [x for x in range(len(string)) if string.startswith(sub_string, x)]
print(result)
