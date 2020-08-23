# -*- encoding: utf-8 -*-

"""
4.1.6 维、秩、轴
"""

import numpy as np

a = np.arange(18).reshape((3,2,3)) # 3层2行3列的结构
print(a)
print(a.sum()) # 全部数组元素之和
print(a.sum(axis=0)) # 0轴方向求和：3层合并成1层，返回二维数组
print(a.sum(axis=1)) # 1轴方向求和：2行合并成1行，返回二维数组
print(a.sum(axis=2)) # 2轴方向求和：3列合并成1列，返回二维数组
print(a.sum(axis=1).sum(axis=1)) # 分层求和方法1
print(a.sum(axis=2).sum(axis=1)) # 分层求和方法2
