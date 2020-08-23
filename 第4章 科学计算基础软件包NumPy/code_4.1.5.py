# -*- encoding: utf-8 -*-

"""
4.1.5 数组的方法
"""

import numpy as np

a = np.arange(6)
print(a) # array([0, 1, 2, 3, 4, 5])
print(a.shape) # (6,)
print(a.dtype) # dtype('int32')

a = a.reshape((2,3)) # 改变数组结构
print(a)

a = a.astype(np.float) # 改变数据类型
print(a.dtype) # dtype('float64')
