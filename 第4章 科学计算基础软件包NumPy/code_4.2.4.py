# -*- encoding: utf-8 -*-

"""
4.2.4 定长分割法
"""

import numpy as np

print(np.arange(5))
print(np.arange(5, 11))
print(np.arange(5,11,2))
print(np.arange(5.5, 11, 1.5))
print(np.arange(3,15).reshape(3,4))

print(np.linspace(0, 5, 5)) # 0到5之间返回5个等距数值，包括0和5
print(np.linspace(0, 5, 5, endpoint=False)) # 返回5个等距数值，包括0但不包括5
