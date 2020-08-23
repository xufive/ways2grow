# -*- encoding: utf-8 -*-

"""
5.4.2 3D绘图工具包
"""

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

y, x = np.mgrid[-5:5:100j, -5:5:100j]
r = np.hypot(x, y)
z = np.sin(r)

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], projection='3d')
surf = ax.plot_surface(x, y, z, cmap='hsv', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
