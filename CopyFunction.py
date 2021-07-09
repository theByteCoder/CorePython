import copy

arr = [1, [2, 10], 3, 4]
new_arr = arr
shallow_copy_arr = copy.copy(arr)
deep_copy_arr = copy.deepcopy(arr)
print("arr", arr)       
print("new_arr", new_arr)
print("shallow_copy_arr", shallow_copy_arr)
print("deep_copy_arr", deep_copy_arr)

arr[1][0] = 3
print("arr", arr)
print("new_arr", new_arr)
print("shallow_copy_arr", shallow_copy_arr)
print("deep_copy_arr", deep_copy_arr)
