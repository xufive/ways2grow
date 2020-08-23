# -*- encoding: utf-8 -*-

"""
8.8.2 交叉验证
"""

from sklearn.datasets import load_wine

X, y = load_wine(return_X_y=True)

# 使用交叉验证分离器

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

dtc = DecisionTreeClassifier() # 实例化决策树分类器
cv = KFold(n_splits=3, shuffle=True, random_state=0) # 实例化交叉验证分离器
print(cross_val_score(dtc, X, y, cv=cv)) # 交叉验证

# 使用随机交叉分离器

from sklearn.model_selection import ShuffleSplit
cv = ShuffleSplit(n_splits=3, test_size=.25, random_state=0)
print(cross_val_score(dtc, X, y, cv=cv)) # 交叉验证

# 留一法

from sklearn.model_selection import LeaveOneOut
cv = LeaveOneOut()
print(cross_val_score(dtc, X, y, cv=cv))
print(cross_val_score(dtc, X, y, cv=cv).mean())
