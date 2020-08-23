# -*- encoding: utf-8 -*-

"""
6.4.4 表级广播函数
"""

import pandas as pd
import numpy as np

dt = ['2020-03-11', '2020-03-12','2020-03-13']
sc = ['000625.SZ','000762.SZ','600132.SH','600009.SH','600126.SH']
cn = ['成交额', '成交量']
idx = pd.MultiIndex.from_product([dt, sc], names=['日期', '代码'])
data = np.array([
	[422.08, 37091400],
	[73.65, 9315300],
	[207.04, 4127800],
	[510.59, 7233100],
	[63.28, 28911100],
	[471.78, 42471700],
	[59.2, 7724200],
	[156.82, 3143100],
	[853.83, 12350400],
	[52.84, 24828900],
	[789.1, 68771048],
	[57.01, 7741802],
	[223.06, 4496598],
	[1196.14, 17662768],
	[56.32, 27484360]
])

vom1 = pd.DataFrame(data, index=idx, columns=cn)
print(vom1)

def scale(x, k): # 对x进行缩放，缩放系数为k
    return x*k

def adder(x, dx):
    return x+dx

print(vom1.pipe(scale, 0.2)) # 对vom1所有数据执行缩放函数，缩放系数0.2
print(vom1.pipe(scale, 0.2).pipe(adder, 5)) # 链式调用


