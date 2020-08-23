# -*- encoding: utf-8 -*-

"""
8.4.4 随机森林分类
"""

from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

ds = load_breast_cancer() # 加载乳腺癌数据集
dtc = DecisionTreeClassifier() # 实例化决策树分类器
rfc = RandomForestClassifier() # 实例化随机森林分类器

dtc_scroe = cross_val_score(dtc, ds.data, ds.target, cv=10) # 交叉验证
print(dtc_scroe) # 决策树交叉验证10次的结果
print(dtc_scroe.mean()) # 决策树交叉验证10次的平均精度

rfc_scroe = cross_val_score(rfc, ds.data, ds.target, cv=10) # 交叉验证
print(rfc_scroe) # 随即森林交叉验证结果10次的
print(rfc_scroe.mean())# 随即森林交叉验证10次的平均精度
