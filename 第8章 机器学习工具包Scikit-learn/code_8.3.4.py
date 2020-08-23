# -*- encoding: utf-8 -*-

"""
8.3.4 离散化
"""

import numpy as np
from sklearn import preprocessing as pp

X = np.array([[-2,5,11],[7,-1,9],[4,3,7]])

bina = pp.Binarizer(threshold=5) # 指定二值化阈值为5
print(bina.transform(X))

est = pp.KBinsDiscretizer(n_bins=[2, 2, 3], encode='ordinal').fit(X)
print(est.transform(X)) # 三个特征列离散化为2段、2段、3段
