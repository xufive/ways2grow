# -*- encoding: utf-8 -*-

"""
5.1.5 显示和保存
"""

import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong'] # 设置字体以便正确显示汉字
plt.rcParams['axes.unicode_minus'] = False # 正确显示连字符

fig = plt.figure()
fig.set_size_inches(5, 3) # 设置画布为5英寸宽3英寸高
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
x = np.random.rand(50) # 随机生成散点x坐标
y = np.random.rand(50) # 随机生成散点y坐标
color = 2 * np.pi * np.random.rand(50) # 随机生成散点颜色
axes.scatter(x, y, c=color, alpha=0.5, cmap='jet') # 绘制散点图
axes.set_title("散点图")
fig.savefig(r'..\res\scatter.png', dpi=300) # 保存为文件，同时设置分辨率为300dpi

print('绘图结果已保存为文件')
