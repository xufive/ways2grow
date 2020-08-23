# -*- encoding: utf-8 -*-

"""
4.1.3 数组的数据类型
"""

import numpy as np

a = np.array([0, 1, 2])
print(a.dtype) # dtype('int32')

a = np.array([0, 1, 2.0])
print(a.dtype) # dtype('float64')

a = np.array([0, 1, 2], dtype=np.uint8)
print(a.dtype) # dtype('uint8')
