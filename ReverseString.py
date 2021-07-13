# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 23:58:08 2021

@author: Admin
"""

# reverse words in string in half time
#string = "hey i am subhasish"
string = "hey my name is subhasish"
arr = string.split(" ") # split word
length = len(arr)
mid = int(length/2) # get mid length if length is even
if length % 2 != 0: # get mid length if length is odd
    mid = int(((length + 1)/2) - 1)

# reverse in half time
for i in range(mid):
    arr[i], arr[- (i + 1)] = arr[- (i + 1)], arr[i]  # swap
print(arr)

# reverse again in linear time
string = "hey my name is subhasish"
arr = string.split(" ") # split word
new_arr = []
length = len(arr)
for j in range(length):
    new_arr.append(arr[- (j + 1)])
print(new_arr)