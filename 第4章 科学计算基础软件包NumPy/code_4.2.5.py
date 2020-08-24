# -*- encoding: utf-8 -*-

"""
4.2.5 重复构造法
"""

import numpy as np

a = np.arange(5)
print(a)
print(np.repeat(a, 3)) # 重复一维数组元素3次

a = np.arange(6).reshape((2,3))
print(a)
print(np.repeat(a, 3)) # 重复二维数组元素3次，不指定轴
print(np.repeat(a, 3, axis=0)) # 重复二维数组元素3次，指定0轴
print(np.repeat(a, 3, axis=1)) # 重复二维数组元素3次，指定1轴

a = np.arange(5)
print(np.tile(a, 3)) # 重复一维数组3次
print(np.tile(a, (3,2))) # 重复一维数组3行2列

a = np.arange(6).reshape((2,3))
print(a)
print(np.tile(a, 3)) # 重复二维数组3次
print(np.tile(a, (2,3))) # 重复二维数组2行3列
