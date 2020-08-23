# -*- encoding: utf-8 -*-

"""
8.5.5 随机森林回归
"""

import numpy as np
from sklearn.ensemble import RandomForestRegressor
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

rfr_1 = RandomForestRegressor(n_estimators=20,max_depth=10)
rfr_2 = RandomForestRegressor(n_estimators=50,max_depth=10)
rfr_1.fit(X_train, y_train) # 模型训练
rfr_2.fit(X_train, y_train) # 模型训练
z_1 = rfr_1.predict(X_test) # 模型预测
z_2 = rfr_2.predict(X_test) # 模型预测
score_1 = rfr_1.score(X_test, y_test) # 模型评估
score_2 = rfr_2.score(X_test, y_test) # 模型评估
print(score_1)
print(score_2)

ax = plt.subplot(121, projection='3d')
ax.scatter3D(_x, _y, _z, c='r')
ax.plot_surface(x,y,z_1.reshape(x.shape),cmap=plt.cm.hsv,alpha=0.5)
plt.title('score:%0.3f@n_estimators=20,max_depth=10'%score_1)
ax = plt.subplot(122, projection='3d')
ax.scatter3D(_x, _y, _z, c='r')
ax.plot_surface(x,y,z_2.reshape(x.shape),cmap=plt.cm.hsv,alpha=0.5)
plt.title('score:%0.3f@n_estimators=50,max_depth=10'%score_2)
plt.show()
