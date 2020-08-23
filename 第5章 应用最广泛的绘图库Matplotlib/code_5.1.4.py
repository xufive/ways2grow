# -*- encoding: utf-8 -*-

"""
5.1.4 图例和文本标注
"""

import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong'] # 设置字体以便正确显示汉字
plt.rcParams['axes.unicode_minus'] = False # 正确显示连字符

x = np.linspace(-4, 4, 200)
y1 = np.power(10, x)
y2 = np.power(np.e, x)
y3 = np.power(2, x)

fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x, y1, 'r', ls='-', linewidth=2, label='$10^x$')
axes.plot(x, y2, 'b', ls='--', linewidth=2, label='$e^x$')
axes.plot(x, y3, 'g', ls=':', linewidth=2, label='$2^x$')
axes.axis([-4, 4, -0.5, 8]) # 设置坐标轴范围
axes.text(1, 7.5, r'$10^x$', fontsize=16) # 添加文本标注
axes.text(2.2, 7.5, r'$e^x$', fontsize=16) # 添加文本标注
axes.text(3.2, 7.5, r'$2^x$', fontsize=16) # 添加文本标注
axes.legend(loc='upper left') # 生成图例
fig.show()

input() # 利用input()阻塞进程，便于查看结果。敲击回车结束。
