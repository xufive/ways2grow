# -*- encoding: utf-8 -*-

"""
4.4.6 多项式拟合函数
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong'] # 指定字体以保证汉字正常显示
plt.rcParams['axes.unicode_minus'] = False # 正确显示连字符

_x = np.linspace(-1, 1, 201)
_y = ((_x**2-1)**3 + 0.5)*np.sin(2*_x) + np.random.random(201)/10 - 0.1

plt.plot(_x, _y, ls='', marker='o', label="原始数据")

for k in range(4, 8):
    g = np.poly1d(np.polyfit(_x, _y, k)) # g是k次多项式
    loss = np.sum(np.square(g(_x)-_y)) # g(x)和f(x)的误差
    plt.plot(_x, g(_x), label="%d次多项式，误差：%0.3f"%(k,loss))
	
plt.legend()
plt.show()
