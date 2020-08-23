# -*- encoding: utf-8 -*-

"""
8.3.1 标准化
"""

import numpy as np
from sklearn import preprocessing as pp

d = np.array([[ 1., -5.,  8.], [ 2.,  -3.,  0.], [ 0.,  -1., 1.]])
d_scaled = pp.scale(d) # 对数据集d做标准化
print(d_scaled)
print(d_scaled.mean(axis=0)) # 标准化以后的数据集，各特征列的均值为0
print(d_scaled.std(axis=0)) # 标准化以后的数据集，各特征列的标准差为1

X_train = np.array([[ 1., -5.,  8.], [ 2.,  -3.,  0.], [ 0.,  -1., 1.]])
scaler = pp.StandardScaler().fit(X_train)
print(scaler.mean_) # 训练集各特征列的均值
print(scaler.scale_) # 训练集各特征列的标准差
print(scaler.transform(X_train)) # 标准化训练集

X_test = [[-1., 1., 0.]] # 使用训练集的缩放标准标准化测试集
print(scaler.transform(X_test))
