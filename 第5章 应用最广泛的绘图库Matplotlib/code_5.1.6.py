# -*- encoding: utf-8 -*-

"""
5.1.4 图例和文本标注
"""

import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0,10,100)
y = np.exp(-x)
plt.plot(x, y) # 调用pyplot的plot函数
plt.show() # 调用pyplot的show函数

x = np.linspace(0,10,100)
y1 = np.exp(-x)
y2 = np.sin(x)
plt.subplot(121) # 现在开始在一行两列的第一个位置绘图
plt.plot(x,y1)
plt.subplot(122) # 现在开始在一行两列的第二个位置绘图
plt.plot(x,y2)
plt.show()

f1 = plt.figure() # 以面向对象的风格创建画布
f2 = plt.figure() # 以面向对象的风格创建画布
ax1 = f1.add_axes([0.1, 0.1, 0.8, 0.8]) # 以面向对象的风格添加子图
ax2 = f2.add_axes([0.1, 0.1, 0.8, 0.8]) # 以面向对象的风格添加子图
x = np.arange(5)
ax1.plot(x) # 以面向对象的风格绘图
ax2.plot(x) # 以面向对象的风格绘图
plt.show() # 以类Matlab风格显示画布，同时显示两块画布
