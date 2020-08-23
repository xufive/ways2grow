# -*- encoding: utf-8 -*-

"""
8.7.1 主成分分析
"""

from sklearn import datasets as dss
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

ds = dss.load_iris()
print(ds.data.shape) # 150个样本，4个特征维

m = PCA() # 使用默认参数实例化PCA类，n_components=None
m.fit(ds.data)

print(m.explained_variance_) # 正交变换后各成分的方差值
print(m.explained_variance_ratio_) # 正交变换后各主分的方差值占总方差值的比例

m = PCA(n_components=0.97)
m.fit(ds.data)

print(m.explained_variance_)
print(m.explained_variance_ratio_)

d = m.transform(ds.data)
print(d.data.shape) # 150个样本，2个特征维（从4个降至2个）

plt.scatter(d[:,0], d[:,1], c=ds.target)
plt.show()
