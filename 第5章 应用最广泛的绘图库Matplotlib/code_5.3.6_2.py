# -*- encoding: utf-8 -*-

"""
5.3.6 刻度——设置刻度显示密度
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 4*np.pi, 500)

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.plot(x, np.sin(x), c='m')
ax1.yaxis.set_major_locator(MultipleLocator(0.3))
ax2 = fig.add_subplot(122)
ax2.plot(x, np.sin(x), c='m')
ax2.xaxis.set_major_locator(MultipleLocator(3))
ax2.xaxis.set_minor_locator(MultipleLocator(0.6))
ax1.set_title('X轴刻度自动调整，Y轴设置刻度间隔0.3')
ax2.set_title('X轴设置主刻度间隔3副刻度间隔0.6，Y轴刻度自动调整')
plt.show()
