# -*- encoding: utf-8 -*-

"""
5.1.3 坐标轴与刻度和名称
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

plt.rcParams['font.sans-serif'] = ['FangSong'] # 设置字体以便正确显示汉字
plt.rcParams['axes.unicode_minus'] = False # 正确显示连字符

x = np.linspace(-10,10,50)
y = np.power(x, 2)

fig = plt.figure()
axes = fig.add_axes([0.2, 0.2, 0.7, 0.7])
axes.set_title("设置轴的刻度和名称", fontdict={'size':16}) # 设置子图标题
axes.plot(x, y) # 绘制连线

xmajorLocator = MultipleLocator(4)
xmajorFormatter = FormatStrFormatter('%1.1f')

axes.xaxis.set_major_locator(xmajorLocator) # 设置刻度的疏密
axes.xaxis.set_major_formatter(xmajorFormatter) # 设置刻度字符格式

axes.set_xlabel('x', fontdict={'size':14}) # 设置横轴名称
axes.set_ylabel('$y=x^2$', fontdict={'size':14}) # 设置纵轴名称

fig.show()

input() # 利用input()阻塞进程，便于查看结果。敲击回车结束。
