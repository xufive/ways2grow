# -*- encoding: utf-8 -*-

"""
8.7.2 因子分析
"""

from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.decomposition import FactorAnalysis

X, y = load_digits(return_X_y=True)
print(X.shape) # 1797个样本，64个特征维

rfc = RandomForestClassifier()
scroe = cross_val_score(rfc, X, y, cv=10) # 交叉验证10次
print(scroe.mean())

fa = FactorAnalysis(n_components=16, random_state=0) # 降至16个特征维
X_fa = fa.fit_transform(X)
scroe = cross_val_score(rfc, X_fa, y, cv=10)
print(scroe.mean())

fa = FactorAnalysis(n_components=8, random_state=0) # 降至8个特征维
X_fa = fa.fit_transform(X)
scroe = cross_val_score(rfc, X_fa, y, cv=10)
print(scroe.mean())
