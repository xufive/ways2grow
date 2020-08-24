# -*- encoding: utf-8 -*-

"""
4.3.6 排序
"""

import numpy as np

a = np.random.random((2,3))
print(a)
print(np.argsort(a)) # 返回行内从小到大排序的索引序号（列排序），相当于axis=1（最后的轴）
print(np.sort(a)) # 返回行内从小到大排序的一个新数组（列排序）
print(np.sort(a,axis=0)) # 返回列内从小到大排序的一个新数组（行排序）

dt = np.dtype([('name',  'S10'),('age',  int)])
a = np.array([("zh",21),("wang",25),("li",17),  ("zhao",27)], dtype = dt)
print(np.sort(a, order='name')) # 如果指定姓名排序，结果是李王张赵
print(np.sort(a, order='age')) # 如果指定年龄排序，结果则是李张王赵
