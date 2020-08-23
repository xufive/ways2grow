# -*- encoding: utf-8 -*-

"""
2.2.3 三元表达式
"""

y = 5
if y < 0:
    print('y是一个负数')
else:
    print('y是一个非负数')

y = 5
print('y是一个负数' if y < 0 else 'y是一个非负数')

y = 5
x = -1 if y < 0 else 1
print(x)

