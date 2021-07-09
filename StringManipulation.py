string_input = "1A6B8C4D"
input_to_arr = list(string_input)
num = 0
for each in input_to_arr:
    try:
        num = int(each)
    except ValueError:
        import sys

        sys.stdout.write(num * each)
