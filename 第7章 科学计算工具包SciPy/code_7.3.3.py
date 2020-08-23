# -*- encoding: utf-8 -*-

"""
7.3.3 多项式拟合
"""

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

def sci_polyfit(_x, _y, k):
    """多项式拟合函数"""
    
    def residual(p, x, oy):
        result = 0
        for i in range(k+1):
            result += p[i]*np.power(x,i)
        return result - oy
    
    p0 = np.ones(k+1)
    res = optimize.least_squares(residual, p0, args=(_x, _y))
    
    def func(x):
        result = 0
        for i in range(k+1):
            result += res.x[i]*np.power(x,i)
        return result
        
    return func

_x = np.linspace(0, 12, 13) # 原始离散数据
_y = np.array([17,19,21,28,33,38,37,37,31,23,19,18,17]) # 原始离散数据
x = np.linspace(0, 12, 100) # 验证拟合结果的自变量

f2 = sci_polyfit(_x, _y, 2) # 2次多项式函数
f3 = sci_polyfit(_x, _y, 3) # 3次多项式函数
f4 = sci_polyfit(_x, _y, 4) # 4次多项式函数
f5 = sci_polyfit(_x, _y, 5) # 5次多项式函数
f6 = sci_polyfit(_x, _y, 6) # 6次多项式函数
f7 = sci_polyfit(_x, _y, 7) # 7次多项式函数

err2 = (f2(_x)-_y).std() # 2次多项式残差的标准差
err3 = (f3(_x)-_y).std() # 3次多项式残差的标准差
err4 = (f4(_x)-_y).std() # 4次多项式残差的标准差
err5 = (f5(_x)-_y).std() # 5次多项式残差的标准差
err6 = (f6(_x)-_y).std() # 6次多项式残差的标准差
err7 = (f7(_x)-_y).std() # 7次多项式残差的标准差

plt.plot(_x, _y, 'o', c='m', label='原始数据')
plt.plot(x, f2(x), label='2次多项式拟合，误差%0.6f'%err2)
plt.plot(x, f3(x), label='3次多项式拟合，误差%0.6f'%err3)
plt.plot(x, f4(x), label='4次多项式拟合，误差%0.6f'%err4)
plt.plot(x, f5(x), label='5次多项式拟合，误差%0.6f'%err5)
plt.plot(x, f6(x), label='6次多项式拟合，误差%0.6f'%err6)
plt.plot(x, f7(x), label='7次多项式拟合，误差%0.6f'%err7)
plt.legend()
plt.show()
