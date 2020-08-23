# -*- encoding: utf-8 -*-

"""
5.3.5 坐标轴——设置坐标轴范围
"""

import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.plot(x, y, c='r')
ax1.set_ylim(-0.8, 0.8)
ax2 = fig.add_subplot(122)
ax2.plot(x, y, c='g')
ax2.set_xlim(-np.pi, 3*np.pi)
plt.show()
