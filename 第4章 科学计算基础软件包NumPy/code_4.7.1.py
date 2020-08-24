# -*- encoding: utf-8 -*-

"""
4.7.1 随机数
"""

import numpy as np

print(np.random.random())
print(np.random.random(2))
print(np.random.random((2,3)))

print(np.random.randint(10))
print(np.random.randint(10, size=5))
print(np.random.randint(10, size=(2,5)))
print(np.random.randint(10, 100, size=(2,5)))
