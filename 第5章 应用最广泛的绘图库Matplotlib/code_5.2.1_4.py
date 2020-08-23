# -*- encoding: utf-8 -*-

"""
5.2.4 矢量合成图
"""

import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong'] # 设置字体以便正确显示汉字
plt.rcParams['axes.unicode_minus'] = False # 正确显示连字符

y, x = np.mgrid[-3:3:12j, -5:5:20j]
p = np.hypot(x,y)

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.quiver(x, y, x, y, p, cmap='hsv')
plt.show()
