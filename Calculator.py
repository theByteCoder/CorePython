# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 12:28:55 2021

@author: Admin
"""

def add(a, b):
    return a + b

def substract(a, b):
    if a > b:
        return a - b
    else:
        return b - a

def divide(a, b):
    if b == 0:
        return 'Infinite'
    else:
        return a / b

def multiply(a, b):
    return a * b