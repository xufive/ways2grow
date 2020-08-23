# -*- encoding: utf-8 -*-

"""
2.1.6十组最常用的内置函数
"""

print(type(5)) # <class 'int'>
print(type('ssdf')) # <class 'str'>
print(type([])) # <class 'list'>
print(type(print)) # <class 'builtin_function_or_method'>
print(type(range(5))) # <class 'range'>

a = [3,4,5]
b = ('x', 'y')
c = dict()
d = 'python'
print(isinstance(a, list)) # True
print(isinstance(b, list)) # False
print(isinstance(c, (dict,str))) # True
print(isinstance(d, (dict,str))) # True
print(isinstance(b, (dict,str))) # False

