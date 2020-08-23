# -*- encoding: utf-8 -*-

"""
8.2.2 样本生成器
"""

from sklearn import datasets as dss
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

X, y = dss.make_blobs(n_samples=100)
plt.subplot(131)
plt.title('make_blobs()')
plt.plot(X[:,0], X[:,1], 'o')

X, y = dss.make_circles(n_samples=100, noise=0.05, factor=0.5)
plt.subplot(132)
plt.title('make_circles()')
plt.plot(X[:,0], X[:,1], 'o')

X, y = dss.make_moons(n_samples=100, noise=0.05)
plt.subplot(133)
plt.title('make_moons()')
plt.plot(X[:,0], X[:,1], 'o')

plt.show()
