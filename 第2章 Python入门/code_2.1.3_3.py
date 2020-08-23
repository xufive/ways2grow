# -*- encoding: utf-8 -*-

"""
2.1.3 三种语句结构——顺序、分支和循环
"""

a = 3
while a > 0: # 判断循环条件
    print(a*'*')
    a -= 1 # 影响循环条件

a = 0
while True: # 死循环
    a += 1 # 影响循环出口条件
    if a > 3: # 设置循环出口条件
        break
    print(a*'*')
