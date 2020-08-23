# -*- encoding: utf-8 -*-

"""
5.2.9 极坐标绘图
"""

import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong'] # 设置字体以便正确显示汉字
plt.rcParams['axes.unicode_minus'] = False # 正确显示连字符

theta = np.linspace(0, 2*np.pi, 500)
r1 = 1.4*np.cos(5*theta)
r2 = 1.8*np.cos(4*theta)
r3 = theta/5
angles = range(0, 360, 45)
tlabels = ('东','东北','北','西北','西','西南','南','东南')

plt.polar(theta, r1, c='r')
plt.polar(theta, r2, lw=2)
plt.polar(theta, r3, ls='--', lw=3)
plt.thetagrids(angles, tlabels)
plt.rgrids(np.arange(-1.5, 2, 0.5))
plt.show()
