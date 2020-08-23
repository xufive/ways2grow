# -*- encoding: utf-8 -*-

"""
8.2.1 Scikit-learn自带的数据集
"""

from sklearn import datasets as dss
import matplotlib.pyplot as plt

lfwp = dss.fetch_lfw_pairs() # 加载数据集

print(lfwp.keys()) # 数据集带有若干子集
print(lfwp.data.shape, lfwp.data.dtype) # data子集有2200个样本
print(lfwp.pairs.shape, lfwp.pairs.dtype) # pairs子集有2200个样本，每个样本2张图片
print(lfwp.target_names) # 有两个标签：不是同一个人、是同一个人
print(lfwp.target.shape, lfwp.target.dtype) # 2200个样本的标签，表示样本是否是一个人


plt.subplot(121)
plt.imshow(lfwp.pairs[0,0], cmap=plt.cm.gray)
plt.subplot(122)
plt.imshow(lfwp.pairs[0,1], cmap=plt.cm.gray)
plt.show()
