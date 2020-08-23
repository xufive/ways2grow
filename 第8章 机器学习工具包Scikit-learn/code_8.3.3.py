# -*- encoding: utf-8 -*-

"""
8.3.3 正则化
"""

import numpy as np
from sklearn import preprocessing as pp

X_train = np.array([[ 1., -5.,  8.], [ 2.,  -3.,  0.], [ 0.,  -1., 1.]])

print(pp.normalize(X_train)) # 使用l2范式正则化，每行的范数为1
print(pp.normalize(X_train, norm='l1')) # 使用l1范式正则化，每行的范数为1
