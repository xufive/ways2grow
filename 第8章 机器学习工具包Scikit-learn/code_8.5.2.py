# -*- encoding: utf-8 -*-

"""
8.5.2 支持向量机回归
"""

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
from sklearn.svm import SVR

x, y = np.mgrid[-2:2:50j,-2:2:50j]
z = x*np.exp(-x**2-y**2)
_x = np.random.random(100)*4 - 2
_y = np.random.random(100)*4 - 2
_z = _x*np.exp(-_x**2-_y**2) + (np.random.random(100)-0.5)*0.1

X_train = np.stack((_x, _y), axis=1) # 训练样本集
y_train = _z # 训练标签集
X_test = np.stack((x.ravel(), y.ravel()), axis=1) # 测试样本集
y_test = z.ravel() # 测试标签集

svr_1 = SVR(kernel='rbf', C=0.1) # 实例化SVR模型，rbf核函数，C=0.1
svr_2 = SVR(kernel='rbf', C=100) # 实例化SVR模型，rbf核函数，C=100
svr_1.fit(X_train, y_train) # 模型训练
svr_2.fit(X_train, y_train) # 模型训练
z_1 = svr_1.predict(X_test) # 模型预测
z_2 = svr_2.predict(X_test) # 模型预测
score_1 = svr_1.score(X_test, y_test) # 模型评估
score_2 = svr_2.score(X_test, y_test) # 模型评估
print(score_1)
print(score_2)

ax = plt.subplot(121, projection='3d')
ax.scatter3D(_x, _y, _z, c='r')
ax.plot_surface(x,y,z_1.reshape(x.shape),cmap=plt.cm.hsv,alpha=0.5)
plt.title('score:%0.3f@kernel="rbf", C=0.1'%score_1)
ax = plt.subplot(122, projection='3d')
ax.scatter3D(_x, _y, _z, c='r')
ax.plot_surface(x,y,z_2.reshape(x.shape),cmap=plt.cm.hsv,alpha=0.5)
plt.title('score:%0.3f@kernel="rbf", C=100'%score_2)
plt.show()

# 如果将核函数更换为线性或多项式，就本例而言，回归效果明显变差
#-------------------------------------------------------------

svr_1 = SVR(kernel='linear', C=100) # 实例化SVR模型，linear核函数，C=100
svr_2 = SVR(kernel='poly', C=100) # 实例化SVR模型，多项式核函数，C=100
svr_1.fit(X_train, y_train) # 模型训练
svr_2.fit(X_train, y_train) # 模型训练
z_1 = svr_1.predict(X_test) # 模型预测
z_2 = svr_2.predict(X_test) # 模型预测
score_1 = svr_1.score(X_test, y_test) # 模型评估
score_2 = svr_2.score(X_test, y_test) # 模型评估
print(score_1)
print(score_2)

ax = plt.subplot(121, projection='3d')
ax.scatter3D(_x, _y, _z, c='r')
ax.plot_surface(x,y,z_1.reshape(x.shape),cmap=plt.cm.hsv,alpha=0.5)
plt.title('score:%0.3f@kernel="linear", C=100'%score_1)
ax = plt.subplot(122, projection='3d')
ax.scatter3D(_x, _y, _z, c='r')
ax.plot_surface(x,y,z_2.reshape(x.shape),cmap=plt.cm.hsv,alpha=0.5)
plt.title('score:%0.3f@kernel="poly", C=100'%score_2)
plt.show()
