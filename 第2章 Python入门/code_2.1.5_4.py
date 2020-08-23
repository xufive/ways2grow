# -*- encoding: utf-8 -*-

"""
2.1.5 五大内置类——列表、字典、元组、集合、字符串
"""

a = set()

a.update({'x','y','z'})
print(a) # {'x', 'y', 'z'}

a.remove('z')
print(a) # {'x', 'y'}

a.add('w')
print(a) # {'x', 'y', 'w'}

a = {'A','D','B'}
b = {'D','E','C'}
print(a.difference(b)) # 返回a和b的差集{'B', 'A'}
print(a - b) # 等价于difference()
print(a.union(b)) # 返回a和b的并集。虽然差集可以用a-b替代，但并集不能用a+b
print(a.intersection(b)) # 返回a和b的交集{'D'}
print(a.symmetric_difference(b)) # 返回a和b非重复元素的集合{'C', 'B', 'A', 'E'}

print(list(set([1,2,5,2,3,4,5,'x',4,'x']))) # 去除数组 [1,2,5,2,3,4,5,'x',4,'x'] 中的重复元素
[1, 2, 3, 4, 5, 'x']
