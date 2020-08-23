# -*- encoding: utf-8 -*-

"""
8.7.3 截断奇异值分解
"""

from sklearn.datasets import load_digits
from sklearn.decomposition import TruncatedSVD
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

X, y = load_digits(return_X_y=True)
print(X.shape) # 1797个样本，64个特征维

rfc = RandomForestClassifier()
scroe = cross_val_score(rfc, X, y, cv=10) # 交叉验证10次
print(scroe.mean())

tsvd = TruncatedSVD(n_components=16) # 降至16个特征维
X_tsvd = tsvd.fit_transform(X)
scroe = cross_val_score(rfc, X_tsvd, y, cv=10)
print(scroe.mean())

tsvd = TruncatedSVD(n_components=8) # 降至8个特征维
X_tsvd = tsvd.fit_transform(X)
scroe = cross_val_score(rfc, X_tsvd, y, cv=10)
print(scroe.mean())
