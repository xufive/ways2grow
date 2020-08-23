# -*- encoding: utf-8 -*-

"""
5.2.8 绘制图像
"""

import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong'] # 设置字体以便正确显示汉字
plt.rcParams['axes.unicode_minus'] = False # 正确显示连字符

r = np.tile(np.linspace(128,255, 10, dtype=np.uint8), (20,1)).T # 红通道
g = np.tile(np.linspace(128,255, 20, dtype=np.uint8), (10,1)) # 绿通道
b = np.ones((10,20), dtype=np.uint8)*96 # 蓝通道
a = np.random.randint(100, 256, (10,20), dtype=np.uint8) # 透明通道
v = np.dstack((r,g,b,a)) # 合成RGBA彩色图像数据

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.imshow(v)
plt.show()
