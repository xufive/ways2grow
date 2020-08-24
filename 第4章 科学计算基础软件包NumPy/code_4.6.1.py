# -*- encoding: utf-8 -*-

"""
4.6.1 创建矩阵
"""

import numpy as np
import numpy.matlib as mat

print(np.mat([[1,2,3],[4,5,6]], dtype=np.int)) # 使用列表创建矩阵
print(np.mat(np.arange(6).reshape((2,3)))) # 使用数组创建矩阵
print(np.mat('1 4 7; 2 5 8; 3 6 9')) # 使用Matlab风格的字符串创建矩阵

print(mat.zeros((2,3))) # 全0矩阵
print(mat.ones((2,3))) # 全1矩阵
print(mat.eye(3)) # 单位矩阵
print(mat.empty((2,3))) # 空矩阵
print(mat.rand((2,3))) # [0,1)区间随机数矩阵
print(mat.randn((2,3))) # 均值0方差1的高斯（正态）分布矩阵
