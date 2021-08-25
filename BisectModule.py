import bisect

input_number = 5.7
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sorted_list)
# where to insert to keep list sorted
print(bisect.bisect(sorted_list, input_number))
# insert, keeps list sorted
bisect.insort(sorted_list, input_number)
print(sorted_list)

unsorted_list = [2, 42, 33, 4, 95, 16, 997, 28, 89]
print(unsorted_list)
# where to insert to keep list sorted
print(bisect.bisect(unsorted_list, input_number))
# insert, keeps list sorted
bisect.insort(unsorted_list, input_number)
print(unsorted_list)
