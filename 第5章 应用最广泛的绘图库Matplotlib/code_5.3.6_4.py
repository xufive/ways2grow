# -*- encoding: utf-8 -*-

"""
5.3.6 刻度——设置刻度文本内容
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter

plt.rcParams['font.sans-serif'] = ['FangSong'] # 设置字体以便正确显示汉字
plt.rcParams['axes.unicode_minus'] = False # 正确显示连字符

x = np.linspace(0, 10, 200)
y = np.square(x)

def func_x(x, pos):
    return '%0.2f秒'%x

def func_y(y, pos):
    return '%0.2f°C'%y

formatter_x = FuncFormatter(func_x)
formatter_y = FuncFormatter(func_y)

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(x, y, c='r')
ax.xaxis.set_major_formatter(formatter_x)
ax.yaxis.set_major_formatter(formatter_y)
plt.show()
