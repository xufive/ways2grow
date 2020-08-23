# -*- encoding: utf-8 -*-

"""
8.5.3 k-近邻回归
"""

import numpy as np
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

x, y = np.mgrid[-2:2:50j,-2:2:50j] # 生成50x50的网格
z = x*np.exp(-x**2-y**2) # 计算网格上每一点的高度值
_x = np.random.random(100)*4 - 2 # 随机生成[-2,2)区间内的100个x
_y = np.random.random(100)*4 - 2 # 随机生成[-2,2)区间内的50个y
_z = _x*np.exp(-_x**2-_y**2) + (np.random.random(100)-0.5)*0.1

X_train = np.stack((_x, _y), axis=1) # 训练样本集
y_train = _z # 训练标签集
X_test = np.stack((x.ravel(), y.ravel()), axis=1) # 测试样本集
y_test = z.ravel() # 测试标签集

knr = KNeighborsRegressor() # 实例化模型
knr = KNeighborsRegressor().fit(X_train, y_train) # 模型训练
z_knr = knr.predict(X_test) # 模型预测
score = knr.score(X_test, y_test) # 模型评估
print(score)

ax = plt.subplot(111, projection='3d')
ax.scatter3D(_x, _y, _z, c='r')
ax.plot_surface(x,y,z_knr.reshape(x.shape),cmap=plt.cm.hsv,alpha=0.5)
plt.show()
