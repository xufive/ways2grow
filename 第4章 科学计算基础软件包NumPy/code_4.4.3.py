# -*- encoding: utf-8 -*-

"""
4.4.3 数学函数
"""

import numpy as np
import math

print(math.e == np.e) # 两个模块的自然常数相等
print(math.pi == np.pi) # 两个模块的圆周率相等
print(np.ceil(5.3))
print(np.ceil(-5.3))
print(np.floor(5.8))
print(np.floor(-5.8))
print(np.around(5.87, 1))
print(np.rint(5.87))
print(np.degrees(np.pi/2))
print(np.radians(180))
print(np.hypot(3,4)) # 求平面上任意两点的距离
print(np.power(3,1/2))
print(np.log2(1024))
print(np.exp(1))
print(np.sin(np.radians(30))) #正弦、余弦函数的周期是2pi
print(np.sin(np.radians(150)))
print(np.degrees(np.arcsin(0.5))) # 反正弦、反余弦函数的周期则是pi

# 平面直角坐标系中，有1000万个点，x坐标和y坐标都分布在[0,1)区间，哪一个点距离点(0.5,0.5)最近呢

p = np.random.random((10000000,2))
x, y = np.hsplit(p,2) # 分离每一个点的x和y坐标
d = np.hypot(x-0.5,y-0.5) # 计算每一个点距离点(0.5,0.5)的距离
i = np.argmin(d) # 返回最短距离的点的索引号
print('距离(0.5,0.5)最近的点坐标是(%f, %f)，距离为%f'%(*p[i], d[i]))
