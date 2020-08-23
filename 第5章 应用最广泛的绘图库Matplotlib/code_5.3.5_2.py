# -*- encoding: utf-8 -*-

"""
5.3.5 坐标轴——反转坐标轴
"""

import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

y, x = np.mgrid[-2:2:200j, -3:3:300j]
z = np.exp(-x**2-y**2) - np.exp(-(x-1)**2-(y-1)**2)

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
ax1.imshow(z, cmap='jet', origin='lower')
ax2.imshow(z, cmap='jet', origin='lower')
ax3.imshow(z, cmap='jet', origin='lower')
ax4.imshow(z, cmap='jet', origin='lower')
ax2.invert_xaxis()
ax3.invert_yaxis()
ax4.invert_xaxis()
ax4.invert_yaxis()
ax1.set_title("正常的X、Y轴")
ax2.set_title("反转X轴")
ax3.set_title("反转Y轴")
ax4.set_title("反转X、Y轴")
plt.show()
