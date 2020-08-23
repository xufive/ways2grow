# -*- encoding: utf-8 -*-

"""
2.1.3 三种语句结构——顺序、分支和循环
"""

for i in range(3): # 这是for循环最经典的用法
    print(i)

for i in [3,4,5,6,7,8,9,10]: # 遍历数组是for循环最频繁的应用
    if i%2 == 0:
        continue
    if i > 8:
        break
    print(i*'*')

d = {'a':1, 'b':2}
for key in d: # 遍历字典的标准写法
    print(key, d[key])

