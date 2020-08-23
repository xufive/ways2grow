# -*- encoding: utf-8 -*-

"""
5.1.2 子图与子图布局
"""

from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong'] # 设置字体以便正确显示汉字

fig = plt.figure()
fig.suptitle("add_subplot方法示例") # 画布标题
ax1 = fig.add_subplot(221)
ax1.set_title("2行2列中的第1个子图")
ax2 = fig.add_subplot(222)
ax2.set_title("2行2列中的第2个子图")
ax3 = fig.add_subplot(223)
ax3.set_title("2行2列中的第3个子图")
ax3 = fig.add_subplot(224)
ax3.set_title("2行2列中的第4个子图")
fig.show()

input() # 利用input()阻塞进程，便于查看结果。敲击回车结束。
