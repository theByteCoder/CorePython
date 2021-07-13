# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 00:19:38 2021

@author: Admin
"""
from datetime import datetime

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
length = len(arr)
mid = int(length/ 2)

print("linear traverse")
start_time = datetime.now()
for i in range(length):
    print(arr[i])
end_time = datetime.now()
time_taken = end_time - start_time
print("time taken ", time_taken)

print("\n")

print("Optimised traverse")
start_time = datetime.now()
for i in range(mid):
    print(arr[i], arr[-(i + 1)])
end_time = datetime.now()
time_taken = end_time - start_time
print("time taken ", time_taken)