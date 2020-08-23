# -*- encoding: utf-8 -*-

"""
6.3	基本操作
"""

import pandas as pd
import numpy as np

data = np.array([
    [10.70, 11.95, 10.56, 11.71, 789.10, 68771048],
    [7.28, 7.59, 7.17, 7.50, 57.01, 7741802],
    [48.10, 50.59, 48.10, 50.28, 223.06, 4496598],
    [66.70, 69.28, 66.66, 68.92, 1196.14, 17662768],
    [7.00, 7.35, 6.93, 7.11, 783.15, 109975919],
    [2.02, 2.10, 2.01, 2.08, 56.32, 27484360]
])

colnames = ['开盘价','最高价','最低价','收盘价','成交额','成交量']
idx = ['000625.SZ','000762.SZ','600132.SH','600009.SH','600126.SH','000882.SZ']
stock = pd.DataFrame(data, columns=colnames, index=idx)

# 6.3.1 数据预览

print(stock.head()) # 从头开始的5行
print(stock.tail()) # 尾部的5行
print(stock.describe()) # 均值、方差、极值的统计概要
print(stock.T) # 转置
print(stock.sort_index(axis=0)) # 按照索引排序
print(stock.sort_values(by='成交量')) # 按照指定列的数值排序

# 6.3.2 数据选择

print(stock[2:3]) # 行选择
print(stock['000762.SZ':'600009.SH']) # 行选择
print(stock['开盘价']) # 列选择。选择单列，也可以使用stock.开盘价
print(stock.loc['000762.SZ':'600009.SH', ['开盘价', '收盘价', '成交量']]) # 行列选择
print(stock.at['000762.SZ', '开盘价']) # 行列选择
print(stock[(stock['成交额']>500)&(stock['开盘价']>10)]) # 条件选择，支持复合条件
print(stock[stock['成交额'].isin([56.32,57.01,223.06])]) # 条件选择，使用isin()筛选多个特定值

# 6.3.3 改变数据结构

print(stock.reindex(index=idx, columns=colnames)) # 重新索引
print(stock.reindex(index=idx, columns=colnames, fill_value=0)) # 重新索引，指定填充值
print(stock.drop(['000762.SZ', '600132.SH'], axis=0)) # 删除指定行
print(stock.drop(['成交额', '最高价', '最低价'], axis=1)) # 删除指定列

idx = ['600161.SH', '600169.SH']
colnames = ['开盘价', '收盘价', '成交额', '成交量', '涨跌幅']
data = np.array([
    [31.00, 32.16, 284.02, 8932594, 0.03],
    [2.02, 2.13, 115.87, 54146894, 0.05]
])
s = pd.DataFrame(data, columns=colnames, index=idx)
print(stock.append(s)) # 行扩展
print(pd.concat((stock, s))) # 行扩展

stock['涨跌幅'] = [0.02, 0.03, 0.05, 0.01, 0.02, 0.03] # 列扩展，改变了原有的数据结构
print(stock)

# 6.3.4 改变数据类型

print(stock['涨跌幅'].dtype) # dtype('float64')
stock['涨跌幅'] = stock['涨跌幅'].astype('float32').values
print(stock['涨跌幅'].dtype) # dtype('float32')

# 6.3.5 广播与矢量化运算

stock['成交量'] /= 2 # 成交量减半
print(stock)

stock['最高价'] += stock['最低价'] # 最高价加上最低价
print(stock)

stock['开盘价'] = (stock['开盘价']-stock['开盘价'].mean())/stock['开盘价'].std() # 开盘价标准化
print(stock)

df_a = pd.DataFrame(np.arange(6).reshape((2,3)), columns=list('abc'))
df_b = pd.DataFrame(np.arange(6,12).reshape((3,2)), columns=list('ab'))

print(df_a + 1) # 对DataFrame对象的广播运算
print(df_a + df_b) # 两个DataFrame对象的矢量运算

# 6.3.6 行列级广播函数

f = lambda x:(x-x.min())/(x.max()-x.min()) # 定义归一化函数
print(stock.apply(f, axis=0)) # 0轴（行方向）归一化
print(stock.apply(f, axis=1)) # 1轴（列方向）归一化
