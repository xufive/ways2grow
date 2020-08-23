# -*- encoding: utf-8 -*-

"""
7.3.1 最小二乘法拟合
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares


plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

_x = np.array([0.0 , 0.2, 0.4, 0.6, 0.8, 1.0 , 1.2, 1.4, 1.6, 1.8, 2.0 ])
_y = np.array([1.68, 2.25, 2.42, 3.18, 4.00, 4.00, 6.64, 8.65, 11.42, 15.42, 20.60])
plt.plot(_x, _y, 'o', c='m')
plt.show()

def func(p, x): # 定义目标函数
    return p[0]*np.exp(p[1]*x) + p[2]

def residual(p, x, oy): # 定义残差函数
    return func(p, x) - oy

p0 = [1,1,0] # 初始的参数
res = least_squares(residual, p0, args=(_x, _y)) # 调用最小二乘法函数
print(res.x) # 这就是最优的一组参数：array([0.80283453, 1.60228346, 0.92933568])

x = np.linspace(0, 2, 100) # 在原始自变量的值域范围内，生成一组新的自变量
y = func(res.x, x) # 使用拟合函数生成因变量

plt.plot(_x, _y, 'o', c='m')
plt.plot(x, y)
plt.show()
