# -*- encoding: utf-8 -*-

"""
8.3.2 归一化
"""

import numpy as np
from sklearn import preprocessing as pp

X_train = np.array([[ 1., -5.,  8.], [ 2.,  -3.,  0.], [ 0.,  -1., 1.]])
scaler = pp.MinMaxScaler().fit(X_train) # 默认数据压缩范围为[0,1]
print(scaler)
print(scaler.transform(X_train))

scaler = pp.MinMaxScaler(feature_range=(-2, 2)) # 设置数据压缩范围为[-2,2]
scaler = scaler.fit(X_train)
print(scaler.transform(X_train))
