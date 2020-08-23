# -*- encoding: utf-8 -*-

"""
8.6.5 层次聚类
"""

from sklearn import datasets as dss
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

X, y = dss.make_circles(n_samples=1000, noise=0.05, factor=0.5)
agg_1 = AgglomerativeClustering(n_clusters=2, linkage='ward')
agg_2 = AgglomerativeClustering(n_clusters=2, linkage='complete')
agg_3 = AgglomerativeClustering(n_clusters=2, linkage='average')
agg_4 = AgglomerativeClustering(n_clusters=2, linkage='single')

agg_1.fit(X)
agg_2.fit(X)
agg_3.fit(X)
agg_4.fit(X)

plt.subplot(221)
plt.title('ward：所有聚类内的平方差总和最小')
plt.scatter(X[:,0], X[:,1], c=agg_1.labels_)
plt.subplot(222)
plt.title('complete：两个聚类间最远样本距离值最小')
plt.scatter(X[:,0], X[:,1], c=agg_2.labels_)
plt.subplot(223)
plt.title('average：两个聚类间平均样本距离值最小')
plt.scatter(X[:,0], X[:,1], c=agg_3.labels_)
plt.subplot(224)
plt.title('single：两个聚类间最近样本距离值最小')
plt.scatter(X[:,0], X[:,1], c=agg_4.labels_)
plt.show()
