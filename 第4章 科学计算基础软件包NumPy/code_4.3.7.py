# -*- encoding: utf-8 -*-

"""
4.3.7 查找
"""

import numpy as np

# 1. 最大值和最小值查找
a = np.random.random((2,3))
print(a)
print(np.argmax(a))
print(np.argmin(a))

# 2. 非零元素查找
a = np.random.randint(0, 2, (2,3))
print(a)
print(np.nonzero(a))

# 3. 使用逻辑表达式查找
a = np.arange(10).reshape((2,5))
print(a)
print((a>3)&(a<8))

# 4. 使用where条件查找
a = np.arange(10)
print(a)
print(np.where(a < 5))

a = a.reshape((2, -1))
print(a)
print(np.where(a < 5))
print(np.where(a < 5, a, 10*a)) # 满足条件的元素不变，其他元素乘以10
