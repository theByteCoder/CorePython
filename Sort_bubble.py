# normal sort
arr = [2, 1, 3, 1, 45, -3]
new_arr = sorted(arr)
print(new_arr)

# bubble sort
last_index = len(arr) - 1
for x in range(last_index, -1, -1):
    for y in range(1, x + 1):
        if arr[y - 1] > arr[y]:
            temp = arr[y - 1]
            arr[y - 1] = arr[y]
            arr[y] = temp
print(arr)
