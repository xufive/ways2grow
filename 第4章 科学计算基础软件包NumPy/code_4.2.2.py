# -*- encoding: utf-8 -*-

"""
4.2.2 特殊数值法
"""

import numpy as np

print(np.zeros(6))
print(np.zeros((2,3)))
print(np.ones((2,3),dtype=np.int))
print(np.empty((2,3)))
print(np.eye(3, dtype=np.uint8))

a = np.empty((3,4), dtype=np.uint8)
a.fill(255)
print(a)
