# -*- encoding: utf-8 -*-

"""
8.6.1 k均值聚类
"""

from sklearn import datasets as dss
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

X_blob, y_blob = dss.make_blobs(n_samples=[300,400,300], n_features=2)
X_circle, y_circle = dss.make_circles(n_samples=1000, noise=0.05, factor=0.5)
X_moon, y_moon = dss.make_moons(n_samples=1000, noise=0.05)
y_blob_pred = KMeans(init='k-means++', n_clusters=3).fit_predict(X_blob)
y_circle_pred = KMeans(init='k-means++', n_clusters=2).fit_predict(X_circle)
y_moon_pred = KMeans(init='k-means++', n_clusters=2).fit_predict(X_moon)

plt.subplot(131)
plt.title('团状簇')
plt.scatter(X_blob[:,0], X_blob[:,1], c=y_blob_pred)
plt.subplot(132)
plt.title('环状簇')
plt.scatter(X_circle[:,0], X_circle[:,1], c=y_circle_pred)
plt.subplot(133)
plt.title('新月簇')
plt.scatter(X_moon[:,0], X_moon[:,1], c=y_moon_pred)
plt.show()
