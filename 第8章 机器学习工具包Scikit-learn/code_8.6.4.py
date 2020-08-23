# -*- encoding: utf-8 -*-

"""
8.6.4 谱聚类
"""

from sklearn import datasets as dss
from sklearn.cluster import SpectralClustering
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

X, y = dss.make_circles(n_samples=1000, noise=0.05, factor=0.5)
scm_1 = SpectralClustering() # 默认参数
scm_2 = SpectralClustering(n_clusters=2) # 指定簇数2
scm_3 = SpectralClustering(affinity='nearest_neighbors', n_clusters=2)

scm_1.fit(X)
scm_2.fit(X)
scm_3.fit(X)

plt.subplot(131)
plt.title('默认参数')
plt.scatter(X[:,0], X[:,1], c=scm_1.labels_)
plt.subplot(132)
plt.title('指定簇数')
plt.scatter(X[:,0], X[:,1], c=scm_2.labels_)
plt.subplot(133)
plt.title('指定簇数和亲和矩阵构造方式')
plt.scatter(X[:,0], X[:,1], c=scm_3.labels_)
plt.show()
