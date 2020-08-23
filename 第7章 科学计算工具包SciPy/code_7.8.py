# -*- encoding: utf-8 -*-

"""
7.8 线性代数
"""

import numpy as np
from scipy import linalg as sla
from numpy import linalg as nla

# 7.8.1 计算矩阵的行列式

m = np.mat('0 1 2; 1 0 3; 4 -3 8')
print(sla.det(m)) # scipy.linalg
print(nla.det(m)) # numpy.linalg

# 7.8.2 求解逆矩阵

m = np.mat('0 1 2; 1 0 3; 4 -3 8')
print(m.I) # 矩阵对象的逆矩阵属性
print(m*m.I) # 矩阵和其逆矩阵的乘积为单位矩阵
print(sla.inv(m)) # scipy.linalg
print(nla.inv(m)) # numpy.linalg

# 7.8.3	计算特征向量和特征值

A = np.mat('0 1 2; 1 0 3; 4 -3 8') # 生成3阶矩阵
print(sla.eigvals(A)) # 返回3个特征值
print(sla.eig(A)) # 返回3个特征值和3个特征向量组成的元组
print(nla.eigvals(A)) # 返回3个特征值
print(nla.eig(A)) # 返回3个特征值和3个特征向量组成的元组

# 7.8.4	矩阵的奇异值分解

A = np.mat(np.random.randint(0,10,(3,4)))
print(A)

u, s, v = sla.svd(A)
print(u.shape, s.shape, v.shape)
print(u)
print(s)
print(v)

u, s, v = nla.svd(A)
print(u)
print(s)
print(v)

# 7.8.5 求解线性方程组

A = np.array([[1,-2,1],[0,2,-8],[-4,5,9]]) # 系数数组
b = np.array([0,8,-9]) #常数数组
print(sla.solve(A, b)) # 调用scipy.linalg的函数，返回x、y、z的方程解
print(nla.solve(A, b)) # 调用numpy.linalg的函数，返回x、y、z的方程解
