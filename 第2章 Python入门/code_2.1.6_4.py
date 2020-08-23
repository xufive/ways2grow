# -*- encoding: utf-8 -*-

"""
2.1.6十组最常用的内置函数
"""

Y,M,D,h,m,s = 2019,5,1,8,0,0 # 2019年5月1日8时0分0秒
print('{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}'.format(Y,M,D,h,m,s)) # 格式化：'2019-05-01 08:00:00'
print('%04d-%02d-%02d %02d:%02d:%02d'%(Y,M,D,h,m,s)) # 用%格式化：'2019-05-01 08:00:00'

print(sorted([3,2,7,1,5])) # 一维列表排序
print(sorted([3,2,7,1,5], reverse=True)) # 一维列表排序，逆序输出

a = [[6, 5], [3, 7], [2, 8]]
print(sorted(a, key=lambda x:x[0])) # 根据每一行的首元素排序：[[2, 8], [3, 7], [6, 5]]
print(sorted(a, key=lambda x:x[-1])) # 根据每一行的尾元素排序：[[6, 5], [3, 7], [2, 8]]

a = [{'name':'C', 'age':18},{'name':'A', 'age':20}, {'name':'B', 'age':19}]
print(sorted(a, key=lambda x:x['name'])) # 根据name键排序
print(sorted(a, key=lambda x:x['age'])) # 根据age键排序
