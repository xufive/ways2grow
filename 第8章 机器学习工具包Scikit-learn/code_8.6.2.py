# -*- encoding: utf-8 -*-

"""
8.6.2 均值漂移聚类
"""

from sklearn import datasets as dss
from sklearn.cluster import MeanShift
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

X, y = dss.make_moons(n_samples=1000, noise=0.05)
msm_1 = MeanShift() # 默认参数
msm_2 = MeanShift(cluster_all=False) # 允许噪声和异常点
msm_3 = MeanShift(cluster_all=False, bandwidth=0.5) # 指定RBF内核带宽

msm_1.fit(X)
msm_2.fit(X)
msm_3.fit(X)

cneter_x1 = msm_1.cluster_centers_[:,0] # 模型1的质心x坐标
cneter_y1 = msm_1.cluster_centers_[:,1] # 模型1的质心y坐标
cneter_x2 = msm_2.cluster_centers_[:,0] # 模型2的质心x坐标
cneter_y2 = msm_2.cluster_centers_[:,1] # 模型2的质心y坐标
cneter_x3 = msm_3.cluster_centers_[:,0] # 模型3的质心x坐标
cneter_y3 = msm_3.cluster_centers_[:,1] # 模型3的质心y坐标

plt.subplot(131)
plt.title('默认参数')
plt.scatter(X[:,0], X[:,1], c=msm_1.labels_)
plt.scatter(cneter_x1, cneter_y1, marker='x', c='r')
plt.subplot(132)
plt.title('允许噪声和异常点')
plt.scatter(X[:,0], X[:,1], c=msm_2.labels_)
plt.scatter(cneter_x2, cneter_y2, marker='x', c='r')
plt.subplot(133)
plt.title('允许噪声和异常点，指定内核带宽')
plt.scatter(X[:,0], X[:,1], c=msm_3.labels_)
plt.scatter(cneter_x3, cneter_y3, marker='x', c='r')
plt.show()
