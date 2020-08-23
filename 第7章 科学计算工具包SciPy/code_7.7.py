# -*- encoding: utf-8 -*-

"""
7.7	非线性方程求根
"""

import numpy as np
from scipy import optimize

# 7.7.1 非线性方程

def f(x):
    return x*x - np.sin(x) - 0.2

result = optimize.root_scalar(f, bracket=[0, 2]) # bracket指定求根区间
print(result.function_calls) # 函数被调用的次数
print(result.iterations) # 迭代求解的次数
print(result.root) # 方程的根
print(f(result.root)) # 检验方程根

# 7.7.2	非线性方程组

def f(v): # v为未知数x、y、z组成的向量
    return [4*v[0]*v[0]-2*np.sin(v[1]*v[2]), 5*v[1]+3, v[0]*v[2]-1.5]

result = optimize.root(f, [1,1,1]) # 第2个参数为猜测的初始向量
print(result.success) # 成功标志
print(result.x) # 方程组的根
print(f(result.x)) # 将求得的根代入向量函数，返回的向量都接近于0