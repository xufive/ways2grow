# -*- encoding: utf-8 -*-

"""
5.2.7 箱线图
"""

import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong'] # 设置字体以便正确显示汉字
plt.rcParams['axes.unicode_minus'] = False # 正确显示连字符

x = np.random.randn(500,4)
labels = list('ABCD')

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.boxplot(x, labels=labels)
ax2 = fig.add_subplot(122)
ax2.boxplot(x, labels=labels, vert=False)
plt.show()
