# -*- encoding: utf-8 -*-

"""
5.2.3 等值线图
"""

import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong'] # 设置字体以便正确显示汉字
plt.rcParams['axes.unicode_minus'] = False # 正确显示连字符

y, x = np.mgrid[-3:3:600j, -4:4:800j]
z = (1-y**5+x**5)*np.exp(-x**2-y**2)

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.set_title('无填充的等值线图')
c1 = ax1.contour(x, y, z, levels=8, cmap='jet') # 无填充的等值线
ax1.clabel(c1, inline=1, fontsize=12) # 为等值线标注值
ax2 = fig.add_subplot(122)
ax2.set_title('有填充的等值线图')
c2 = ax2.contourf(x, y, z, levels=8, cmap='jet') # 有填充的等值线
fig.colorbar(c1, ax=ax1) # 添加ColorBar
fig.colorbar(c2, ax=ax2) # 添加ColorBar
plt.show()
