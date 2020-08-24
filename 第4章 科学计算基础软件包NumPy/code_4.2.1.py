# -*- encoding: utf-8 -*-

"""
4.2.1 蛮力构造法
"""

import numpy as np

a = np.array([[1,2,3],[4,5,6]]) # 创建2行3列数组
print(a)
print(a.dtype)

a = np.array([[1,2,3],[4,5,6]], dtype=np.uint8) # 创建8位无符号整型数组
print(a)
print(a.dtype)
