# -*- encoding: utf-8 -*-

"""
5.2.2 散点图
"""

import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong'] # 设置字体以便正确显示汉字
plt.rcParams['axes.unicode_minus'] = False # 正确显示连字符

x = np.random.randn(50) # 随机生成50个符合标准正态分布的点（x坐标）
y = np.random.randn(50) # 随机生成50个符合标准正态分布的点（y坐标）
color = 10 * np.random.rand(50) # 随即数，用于映射颜色
area = np.square(30*np.random.rand(50)) # 随机数表示点的面积
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.scatter(x, y, c=color, s=area, cmap='hsv', marker='o', edgecolor='r', alpha=0.5)
plt.show()
