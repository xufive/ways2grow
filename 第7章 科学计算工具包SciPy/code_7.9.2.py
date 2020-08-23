# -*- encoding: utf-8 -*-

"""
7.9.2 层次聚类
"""

import numpy as np
from scipy.spatial.distance import pdist # 导入计算样本点距离的包
import scipy.cluster.hierarchy as sch # 导入层次聚类的包
import matplotlib.pylab as plt

ps = np.random.randn(20,3) # 生成正态分布的随机点
dist = pdist(ps) # 计算20个样本点之间的距离，返回190个距离
Z = sch.linkage(dist, method='average') # 返回此次聚类的连接矩阵
print(Z) # 查看结果，索引序号为0和14的两点距离最近，5和7次之

S = sch.fcluster(Z, t=1, criterion='inconsistent') # 返回平面聚类
print(S)

P = sch.dendrogram(Z) # 绘制层次聚类树
plt.show()
