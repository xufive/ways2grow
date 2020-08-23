# -*- encoding: utf-8 -*-

"""
7.9.1	K均值聚类
"""

import numpy as np
from scipy.cluster import vq # 导入聚类模块的vq包
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

def create_data_set(*cores): # 生成k-means聚类测试用数据集
    ds = list()
    for x0, y0, z0 in cores:
        x = np.random.normal(x0, 0.1+np.random.random()/3, z0)
        y = np.random.normal(y0, 0.1+np.random.random()/3, z0)
        ds.append(np.stack((x,y), axis=1))
    
    return np.vstack(ds)

ds = create_data_set((1,2,100),(3,2,100),(2,3,100)) # 生成300个测试样本
dsw = vq.whiten(ds) # 样本归一化
core, label = vq.kmeans2(dsw, 3, iter=10) # 聚类，迭代10次
c = ['b', 'g', 'm'] # 为3个簇指定3种颜色

for i in range(3): # 根据聚类结果，使用不同的颜色，分簇画出样本点
		g = dsw[label==i]
		plt.scatter(g[:,0], g[:,1], c=c[i])
	
plt.scatter(core[:,0], core[:,1], c='r', marker='x') # 画出3个质心
plt.show()
