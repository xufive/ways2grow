# -*- encoding: utf-8 -*-

"""
4.2.3 随机数值法
"""

import numpy as np

print(np.random.random(3))
print(np.random.random((2,3)))
print(np.random.randint(5))
print(np.random.randint(1, 5, size=(2,3)))
print(np.eye(3, dtype=np.uint8))

import matplotlib.pyplot as plt # 导入绘图模块

tall = np.random.normal(170, 4, 1000) # 生成正态分布数据
bins = np.arange(156, 190, 2) # 从156厘米到190厘米，每2厘米一个分段
plt.hist(tall, bins) # 绘制柱状图
plt.show() # 显示图形
