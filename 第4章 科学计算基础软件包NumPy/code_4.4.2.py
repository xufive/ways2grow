# -*- encoding: utf-8 -*-

"""
4.4.2 命名空间
"""

import numpy as np

a = np.random.random(10)
print(a.max(), np.max(a))
print(a.sum(), np.sum(a))

a = np.random.random(5)
print(a.copy())
print(np.copy(a))

print(a.view()) # 这是正确写法
#print(np.view(a)) # 这样写就抛出异常：module 'numpy' has no attribute 'view'

print(np.where(a>0.5)) # 这是正确写法
#print(a.where(a>0.5)) # 这样写就抛出异常：'numpy.ndarray' object has no attribute 'where'
