# -*- encoding: utf-8 -*-

"""
8.6.3 基于密度的空间聚类
"""

from sklearn import datasets as dss
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

X, y = dss.make_moons(n_samples=1000, noise=0.05)
dbs_1 = DBSCAN() # 默认核心样本半径0.5，核心样本邻居5个
dbs_2 = DBSCAN(eps=0.2) # 核心样本半径0.2，核心样本邻居5个
dbs_3 = DBSCAN(eps=0.1) # 核心样本半径0.1，核心样本邻居5个

dbs_1.fit(X)
dbs_2.fit(X)
dbs_3.fit(X)

plt.subplot(131)
plt.title('eps=0.5')
plt.scatter(X[:,0], X[:,1], c=dbs_1.labels_)
plt.subplot(132)
plt.title('eps=0.2')
plt.scatter(X[:,0], X[:,1], c=dbs_2.labels_)
plt.subplot(133)
plt.title('eps=0.1')
plt.scatter(X[:,0], X[:,1], c=dbs_3.labels_)
plt.show()
