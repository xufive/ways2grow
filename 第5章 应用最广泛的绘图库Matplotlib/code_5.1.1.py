# -*- encoding: utf-8 -*-

"""
5.1.1 画布
"""

from matplotlib import pyplot as plt

fig = plt.figure() # 创建画布
fig.set_size_inches(5, 3) # 设置画布大小，单位英寸
fig.set_facecolor('gray') # 设置画布颜色
fig.show() # 显示画布

input() # 利用input()阻塞进程，便于查看结果。敲击回车结束。
