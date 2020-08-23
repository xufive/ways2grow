# -*- encoding: utf-8 -*-

"""
2.1.6十组最常用的内置函数
"""

print(3, [1,2,3], {'name':'David'}) # 一次可以打印多个对象，对象可以是任意类型：3 [1, 2, 3] {'name': 'David'}
print(1, 2, 'x','y', sep='*') # 多个打印对象之间使用星号分割：1*2*x*y

for item in [1, 2, 'x','y']:
    print(item, end=',') # 不换行打印

with open(r'..\res\print_out.txt', 'w') as fp: # 打印到文件d:\print_out.txt
    print(1, 2, 'x','y', sep='*', file=fp)
