# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 22:13:03 2021

@author: Admin
"""

a = 10
b = a
c = 10
print(a, id(a))
print(b, id(b))
print(c, id(c))


def func():
    global a
    a = 20
    print(a, id(a))
    print(b, id(b))
    print(c, id(c))


func()
print(a, id(a))
print(b, id(b))
print(c, id(c))
