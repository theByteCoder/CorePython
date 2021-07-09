string = "a1b2c3d4"
arr = [x for x in string]
for y in range(0, len(arr) - 1, 1):
    try:
        val = int(arr[y])
        # below return true and is NOT proper way to check
        if type(val) == int:
            print(arr[y - 1] * val)
        # below returns true and is proper way to check
        if isinstance(val, int):
            print(arr[y - 1] * val)
    except ValueError:
        pass
