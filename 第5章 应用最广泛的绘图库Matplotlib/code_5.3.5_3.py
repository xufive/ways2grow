# -*- encoding: utf-8 -*-

"""
5.3.5 坐标轴——显示双轴
"""

import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(-2*np.pi, 2*np.pi, 200)
y1 = np.square(x)
y2 = np.cos(x)

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax_twinx = ax.twinx()
ax.plot(x, y1, c='r')
ax_twinx.plot(x, y2, c='g', ls='-.')
plt.show()
