# -*- encoding: utf-8 -*-

"""
7.6 积分
"""

import numpy as np
from scipy import integrate

# 7.6.1 对给定函数的定积分

def fe(x):
    return np.exp(-x)

print(integrate.quad(fe, -1, 1)) # 积分函数的三个参数：积分函数、积分下限和上限

# 7.6.2 对给定样本的定积分

x = np.linspace(-1, 1, 1000)
y = np.exp(-x)
print(integrate.trapz(y, x))

# 7.6.3 二重定积分

def z(x, y): # 定义函数z=√(1-x^2-y^2 )
    return np.sqrt(1 - x*x - y*y)

def g(x): # y的积分下限是-√(1-x^2 )
    return -np.sqrt(1-x*x)

def h(x): # y的积分上限是√(1-x^2 )
    return np.sqrt(1-x*x)

print(integrate.dblquad(z, -1, 1, g, h)) # x的积分区间是[-1,1]
