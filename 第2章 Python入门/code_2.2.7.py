# -*- encoding: utf-8 -*-

"""
2.2.7 lambda函数
"""

print(lambda x,y: x+y) # <function <lambda> at 0x000001C248EC6678>
print((lambda x,y: x+y)(3,4)) # 因为匿名函数没有名字，使用的时候要用括号把它包起来

f = lambda x,y: x+y # 也可以给匿名函数取个名字，像普通函数那样调用它
result = f(3, 4)
print(result)

a = [{'name':'B','age':50},{'name':'A','age':30},{'name':'C','age':40}]
a_sorted_by_name = sorted(a, key=lambda x:x['name']) # 按姓名排序
a_sorted_by_age = sorted(a, key=lambda x:x['age']) # 按年龄排序

print(a_sorted_by_name)
print(a_sorted_by_age)
