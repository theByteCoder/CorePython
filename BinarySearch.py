# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 23:58:51 2021

@author: Admin
"""
import math

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5


def binary_search(arr, target):
    l = 0
    r = len(arr) - 1
    while l < r:
        mid = math.floor((r + l) / 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
    else:
        return -1


print(binary_search(arr, target))
