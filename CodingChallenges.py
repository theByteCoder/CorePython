# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# my_list = []
#
#
# def cuboid():
#     for i in range(x + 1):
#         for j in range(y + 1):
#             for k in range(z + 1):
#                 if i + j + k != n:
#                     my_list.append([i, j, k])
#     print(my_list)
#
#
# cuboid()

# n = int(input())
# arr = map(int, input().split())
# my_list = list(arr)
# my_list.sort()
# my_set = set(my_list)
# my_list = list(my_set)
# my_list.sort()
# my_list.pop()
# print(my_list[-1])

# my_list = []
# my_dict = {}
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     my_list.append(score)
#     my_dict[name] = score
# my_set = set(my_list)
# my_list = list(my_set)
# my_list.sort()
# my_list.reverse()
# my_list.pop()
# lowest_num = my_list.pop()
# my_stud_list = list(my_dict.keys())
# my_stud_list.sort()
# print(my_stud_list)
# for stud in my_stud_list:
#     if my_dict[stud] == lowest_num:
#         print(stud)

# my_dict = {}
# for _ in range(int(input())):
#     values = input()
#     my_list = values.split(' ')
#     name = my_list[0]
#     m = float(my_list[1])
#     p = float(my_list[2])
#     c = float(my_list[3])
#     avg = (m + p + c) / 3
#     my_dict[name] = f"{avg:1.2f}"
# print_name = input()
# print(my_dict[print_name])

# from collections import Counter, OrderedDict
#
#
# class counter(Counter, OrderedDict):
#     pass
#
#
# words = counter(input() for _ in range(int(input())))
# print(len(words))
# print(*words.values())

# from collections import OrderedDict
#
# my_dict = OrderedDict()
# for x in range(10):
#     my_dict[x] = x + 1
# print(*my_dict.values())

# first_multiple_input = input().rstrip().split()
#
# n = int(first_multiple_input[0])
#
# m = int(first_multiple_input[1])
#
# matrix = []
# letters = []
# each_alphaNum = ''
# each_SpChar = ''
# decoded_str = ''
# coded_str = ''
# for _ in range(n):
#     matrix_item = input()
#     matrix.append(matrix_item)
# for words in matrix:
#     letters.append(list(words))
# for col in range(m):
#     for row in range(n):
#         starting_row = not (str(letters[0][col]).isalnum()) or str(letters[0][col]).isspace()
#         ending_row = not (str(letters[n - 1][col]).isalnum()) or str(letters[0][col]).isspace()
#         row_result = starting_row or ending_row
#         each_alphaNum = (' ', str(letters[row][col]))[str(letters[row][col]).isalnum()]
#         each_SpChar = (' ', str(letters[row][col]))[(row_result and not (str(letters[row][col]).isalnum()))]
#         coded_str += str(letters[row][col])
#         decoded_str += (each_alphaNum + each_SpChar)
# print(decoded_str)
import re

n, m = map(int, input().split())
a, b = [], ""
for _ in range(n):
    a.append(input())

for z in zip(*a):
    b += "".join(z)

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))
