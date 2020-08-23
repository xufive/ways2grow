# -*- encoding: utf-8 -*-

"""
2.1.5 五大内置类——列表、字典、元组、集合、字符串
"""

d = dict() # 固然可以写成 d = {}，但我喜欢这样写
d = dict(a=1,b=2)
print(d) # {'a': 1, 'b': 2}

d = dict([('a',1),('b',2)])
print(d) # {'a': 1, 'b': 2}

d.update({'c':3}) # 用赋值语句也可以插入和更新字典，但不如这样优雅
print(d) # {'a': 1, 'b': 2, 'c': 3}

d.pop('c') # 删除元素
print(d) # {'a': 1, 'b': 2}

print(list(d.items())) # [('a', 1), ('b', 2)]
print(list(d.keys())) # ['a', 'b']
print(list(d.values())) # [1, 2]

for key in d: # 遍历字典的标准写法
		print(key, d[key])

print(dict.fromkeys('xyz',0)) # 返回{'x': 0, 'y': 0, 'z': 0}。fromkeys是dict类的静态方法，实例也可以调用
