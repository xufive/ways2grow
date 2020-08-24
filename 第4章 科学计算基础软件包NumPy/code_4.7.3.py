# -*- encoding: utf-8 -*-

"""
4.7.3 正态分布
"""

import numpy as np

print(np.random.randn()) # 标准正态分布，均值为0，标准差为1
print(np.random.randn(5))
print(np.random.randn(2,5))

print(np.random.normal()) # 默认均值为0，标准差为1
print(np.random.normal(loc=2, size=5)) # 参数loc指定均值为2
print(np.random.normal(loc=2, scale=0.2, size=(2,5))) # 参数loc指定均值为2，参数scale指定标准差为0.2
