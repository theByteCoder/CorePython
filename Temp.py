# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 01:16:53 2021

@author: Admin
"""


def execute_lambda():
    return lambda val: [char for char in val]


x = execute_lambda()('hello world')
print(x)


def lambda_filters(val):
    return list(filter(lambda char: char == 'e', val))
x = lambda_filters('hello world')
print(x)



def lambda_reduce():
    val = [1,2,3,5 ]
    from functools import reduce
    return reduce(lambda a, b: a + b, val)


z = lambda_reduce()
print(z)

val = {'a': 1, 'b': 2}
for x in val.items():
    print(x)

# iteration
val = [1,2,3,5]
my_iter = iter(val)
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
#print(next(my_iter))


val = "hello world"
my_iter = iter(val)
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


import os
print(dir(os))
print(os.getcwd())


#from calculator import add, substract, divide, multiply
import calculator  as calc
print(calc.add(1,2))
print(calc.substract(1,2))
print(calc.divide(1,2))
print(calc.multiply(1,2))
print(dir(calc))

import sys
print(sys.path)


class ClassA:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b


obj = ClassA(1, 2)
print(dir(obj))
print(obj.sum())


class ClassB(ClassA):
    def substract(self):
        print(ClassA.sum(self))



obj = ClassB(1,2)
obj.substract()


# generator
def gene():
    yield 1
    yield 2
    yield 3
    yield 4
    
my_gen = gene()
print(my_gen)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
try:
    print(next(my_gen))
except StopIteration:
    print('StopIteration exception')
    
    
lists = [1,2,'test']
tuples = tuple(lists)
print(tuples)

#  enumarate
val = ['subhasish', 'the', 'great']
for i in enumerate(val):
    print(type(i))
for index, val in enumerate(val):
    print(index, val)