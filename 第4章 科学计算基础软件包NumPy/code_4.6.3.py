# -*- encoding: utf-8 -*-

"""
4.6.3 矩阵乘法
"""

import numpy as np

a = np.random.randint(0,10,(2,3))
print(a)

b = np.random.randint(0,10,3)
print(b)

print(a*b) # shape不同的两个数组也可以相乘
print(b*a)

a = np.random.randint(0,10,(2,3))
b = np.random.randint(0,10,3)
c = np.random.randint(0,10,(3,2))

print(np.dot(a,b))
print(np.dot(a,c))

def rotate(p,d):
    a = np.radians(d)
    m = np.array([[np.cos(a), np.sin(a)],[-np.sin(a), np.cos(a)]])
    return np.dot(np.array(p), m)

print(rotate((5.7,2.8), 35)) # 旋转35°
print(rotate((5.7,2.8), 90)) # 旋转90°
print(rotate((5.7,2.8), 180)) # 旋转180°
print(rotate((5.7,2.8), 360)) # 旋转360°
