# -*- encoding: utf-8 -*-

"""
5.2.1 曲线图
"""

import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong'] # 设置字体以便正确显示汉字
plt.rcParams['axes.unicode_minus'] = False # 正确显示连字符

x = np.linspace(-4, 4, 100)
y1 = np.power(np.e, x)
y2 = np.sin(x)*10 + 30
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x, y1, c='green', label='$e^x$', ls='-.', alpha=0.6, lw=2)
axes.plot(x, y2, c='m', label='$10*sin(x)+10$', ls=':', alpha=1, lw=3)
axes.legend()
plt.show()

x = np.arange(100)
y = np.exp(x)
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
ax1.set_title("plot")
ax1.plot(x,y,c='r')
ax2.set_title("semilogx")
ax2.semilogx(x,y,c='g')
ax3.set_title("semilogy")
ax3.semilogy(x,y,c='m')
ax4.set_title("loglog")
ax4.loglog(x,y,c='k')
plt.show()
