# -*- encoding: utf-8 -*-

"""
5.2.5 直方图
"""

import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong'] # 设置字体以便正确显示汉字
plt.rcParams['axes.unicode_minus'] = False # 正确显示连字符

x1 = np.random.randn(1000)
x2 = np.random.randn(800)
c = ['r', 'b']

fig = plt.figure()
ax1 = fig.add_subplot(131)
ax1.set_title('两个数据集堆叠')
ax1.hist([x1,x2], bins=8, histtype='bar', color=c, stacked=True)
ax2 = fig.add_subplot(132)
ax2.set_title('单个数据集，无填充色')
ax2.hist(x1, bins=8, histtype='step')
ax3 = fig.add_subplot(133)
ax3.set_title('横向直方图')
ax3.hist([x1,x2], bins=8, histtype='bar', color=c, orientation='horizontal')
plt.show()
