# -*- encoding: utf-8 -*-

"""
4.6.2 矩阵特有属性
"""

import numpy as np

m = np.mat(np.arange(6).reshape((2,3)))
print(m)
print(m.T) # 返回自身的转置矩阵
print(m.H) # 返回自身的共轭转置矩阵
print(m.I) # 返回自身的逆矩阵
print(m.A) # 返回自身数据的视图（ndarray类）
