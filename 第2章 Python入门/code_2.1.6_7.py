# -*- encoding: utf-8 -*-

"""
2.1.6十组最常用的内置函数
"""

for index, item in enumerate([True, False, None]):
    print(index, item, sep='->')
	
for index, item in enumerate('xyz'):
    print(index, item, sep='->')
	
a = ['x','y','z']
b = [3,4,5]
for k, v in zip(a,b):
    print(k, v, sep='->')

def extract(x): # 开3次方
    return pow(x, 1/3)

result = map(extract, [7,8,9]) # 函数extract()对列表元素逐一运算，返回迭代对象
print(list(result)) # 将迭代对象转为list：[1.912931182772389, 2.0, 2.080083823051904]

result = map(lambda x:pow(x, 1/3), [7,8,9]) # 使用lambda函数，更简洁
print(list(result))

print(chr(65)) # 'A'
print(ord('Z')) # 90

for i in range(26):
    print(chr(65+i), sep='', end='')

