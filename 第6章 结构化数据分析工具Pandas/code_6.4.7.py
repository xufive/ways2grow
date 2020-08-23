# -*- encoding: utf-8 -*-

"""
6.4.7 数据I/O
"""

import pandas as pd
import numpy as np

# 1. 读写CSV格式的数据文件
df = pd.DataFrame(np.random.rand(10,4),columns=list('ABCD')) # 生成模拟数据
df.to_csv(r'..\res\random.csv') # 保存为CSV文件

df = pd.read_csv(r'..\res\random.csv') # 读取CSV文件
print(df)

df = pd.read_csv(r'D:\NumPyFamily\data\random.csv', index_col=0) # 读取CSV文件时，使用index_col参数指定首列（0列）为索引
print(df)

# 2. 读写Excel文件
idx = pd.date_range('08:00:00', periods=10, freq='H')
df = pd.DataFrame(np.random.rand(10,4),columns=list('ABCD'),index=idx)
df.to_excel(r'..\res\random.xlsx', sheet_name='随机数') # 保存为xecel文件

df = pd.read_excel(r'..\res\random.xlsx', sheet_name='随机数') # 读取xecel文件
print(df)

df = pd.read_excel(r'..\res\random.xlsx', sheet_name='随机数', index_col=0) # 读取xecel文件，使用index_col参数指定首列（0列）为索引
print(df)

# 3. 读写HDF文件

idx = pd.date_range('08:00:00', periods=10, freq='H')
df = pd.DataFrame(np.random.rand(10,4),columns=list('ABCD'),index=idx)
df.to_hdf(r'..\res\random.h5', key='random') # 保存为HDF文件

df = pd.read_hdf(r'..\res\random.h5', key='random') # 读取HDF文件
print(df)
