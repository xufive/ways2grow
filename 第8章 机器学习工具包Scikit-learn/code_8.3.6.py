# -*- encoding: utf-8 -*-

"""
8.3.6 缺失值补全
"""

import numpy as np
from sklearn.impute import SimpleImputer

X = np.array([[3, 2], [np.nan, 3], [4, 6], [8, 4]]) # 首列有缺失

simp = SimpleImputer().fit(X) # 默认插补均值，当前均值5
print(simp.transform(X))

simp = SimpleImputer(strategy='median').fit(X) # 中位数插补，当前中位数4
print(simp.transform(X))

simp = SimpleImputer(strategy='constant', fill_value=0).fit(X) # 插补0
print(simp.transform(X))
