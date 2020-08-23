# -*- encoding: utf-8 -*-

"""
8.5.4 决策树回归
"""

import numpy as np
from sklearn.tree import DecisionTreeRegressor
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

dtr_1 = DecisionTreeRegressor(max_depth=5) # 实例化模型，决策树深度5
dtr_2 = DecisionTreeRegressor(max_depth=10) # 实例化模型，决策树深度10
dtr_1.fit(X_train, y_train) # 模型训练
dtr_2.fit(X_train, y_train) # 模型训练
z_1 = dtr_1.predict(X_test) # 模型预测
z_2 = dtr_2.predict(X_test) # 模型预测
score_1 = dtr_1.score(X_test, y_test) # 模型评估
score_2 = dtr_2.score(X_test, y_test) # 模型评估
print(score_1)
print(score_2)

ax = plt.subplot(121, projection='3d')
ax.scatter3D(_x, _y, _z, c='r')
ax.plot_surface(x,y,z_1.reshape(x.shape),cmap=plt.cm.hsv,alpha=0.5)
plt.title('score:%0.3f@max_depth=5'%score_1)
ax = plt.subplot(122, projection='3d')
ax.scatter3D(_x, _y, _z, c='r')
ax.plot_surface(x,y,z_2.reshape(x.shape),cmap=plt.cm.hsv,alpha=0.5)
plt.title('score:%0.3f@max_depth=10'%score_2)
plt.show()
