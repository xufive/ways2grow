# -*- encoding: utf-8 -*-

"""
7.3.2 使用curve_fit函数拟合
"""

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

_x = np.linspace(0, 12, 13) 
_y = np.array([17,19,21,28,33,38,37,37,31,23,19,18,17])

plt.plot(_x, _y, 'o', c='m')
plt.show()

def func(x,a,b,c): # 定义目标函数
    return a*np.sin(x*np.pi/6+b)+c

fita, fitb = optimize.curve_fit(func, _x, _y, [1,1,1]) # 拟合
print(fita) # 这就是一组最优的拟合参数a,b,c)

x = np.linspace(0, 12, 100) # 在原始自变量的值域范围内，生成一组新的自变量
y = func(x, *fita) # 使用拟合参数生成因变量

plt.plot(_x, _y, 'o', c='m', label='原始数据')
plt.plot(x, y, label='拟合曲线')
plt.legend()
plt.show()
