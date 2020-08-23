# -*- encoding: utf-8 -*-

"""
5.1.2 子图与子图布局
"""

from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong'] # 设置字体以便正确显示汉字

fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # 添加子图1
ax2 = fig.add_axes([0.5, 0.5, 0.4, 0.2]) # 添加子图2
ax1.set_title("子图1") # 设置子图1的标题
ax2.set_title("子图2") # 设置子图2的标题
ax1.set_facecolor('#E0E0E0') # 设置子图1的背景色
ax2.set_facecolor('#F0F0F0') # 设置子图2的背景色
fig.show()

input() # 利用input()阻塞进程，便于查看结果。敲击回车结束。
