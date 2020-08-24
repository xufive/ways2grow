# -*- encoding: utf-8 -*-

"""
4.4.4 统计函数
"""

import numpy as np
import math

a = np.random.random(10)
print(np.max(a), np.min(a))

a[1::2] = np.nan # 将索引1,3,5,7,9的元素设置为nan
print(a)
print(np.max(a), np.min(a)) # 此时，min()和max()失效了
print(np.nanmax(a), np.nanmin(a)) # 必须使用nanmax()和nanmin()

a = np.random.randint(0,50,(3,4))
print(np.sum(np.square(a-a.mean()))/a.size) # 用方差定义求方差
print(np.var(a)) # 直接用方差函数求方差，结果相同

print(np.sqrt(a.var())) # 对方差开方，即是标准差
print(a.std()) # 直接用标准差函数求标准差，结果相同

# 综合运用统计函数，分析两只股票的关联关系和收益率

pa = np.array([
    79.66, 81.29, 80.37, 79.31, 79.84, 78.53, 78.29, 78.51, 77.99, 79.82, 
    80.41, 79.27, 80.26, 81.61, 81.39, 80.29, 80.18, 78.38, 75.06, 76.15, 
    75.66, 73.90, 72.14, 74.27, 75.27, 76.15, 75.40, 76.51, 77.57, 77.06
])

pb = np.array([
    30.93, 31.61, 31.62, 31.77, 32.01, 31.52, 30.09, 30.54, 30.78, 30.84, 
    30.80, 30.38, 30.88, 31.38, 31.05, 29.90, 29.96, 29.59, 28.71, 28.95, 
    29.19, 28.71, 27.93, 28.35, 28.92, 29.17, 29.02, 29.43, 29.12, 29.11
])

print(np.corrcoef(pa, pb)) # 两只股票的相关系数为0.867，关联比较密切

pa_re = np.diff(pa)/pa[:-1] # 股价收益率
pb_re = np.diff(pb)/pb[:-1] # 股价与前一个交易日股价差除以最后一个交易日的股价

import matplotlib.pyplot as plt

plt.plot(pa_re)
plt.plot(pb_re)
plt.show()
