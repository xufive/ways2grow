# -*- encoding: utf-8 -*-

"""
8.4.5 支持向量机分类
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score
from sklearn import svm

ds = load_breast_cancer() # 加载乳腺癌数据集
msvc = svm.SVC() # 实例化SVC分类器
mnusvc = svm.NuSVC()# 实例化NuSVC分类器
mlsvc = svm.LinearSVC(dual=False) # 实例化LinearSVC分类器
score_msvc = cross_val_score(msvc, ds.data, ds.target, cv=10)
score_mnusvc = cross_val_score(mnusvc, ds.data, ds.target, cv=10)
score_mlsvc = cross_val_score(mlsvc, ds.data, ds.target, cv=10)

print(score_msvc.mean()) # SVC交叉验证10次的平均精度
print(score_mnusvc.mean()) # NuSVC交叉验证10次的平均精度
print(score_mlsvc.mean()) # LinearSVC交叉验证10次的平均精度
