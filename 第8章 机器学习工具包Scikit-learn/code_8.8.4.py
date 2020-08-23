# -*- encoding: utf-8 -*-

"""
8.8.4 参数优化
"""

import numpy as np
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

x, y = np.mgrid[-2:2:50j,-2:2:50j]
z = x*np.exp(-x**2-y**2)
_x = np.random.random(1000)*4 - 2
_y = np.random.random(1000)*4 - 2
_z = _x*np.exp(-_x**2-_y**2) + (np.random.random(1000)-0.5)*0.1
X_train = np.stack((_x, _y), axis=1) # 训练样本集
y_train = _z # 训练标签集
X_test = np.stack((x.ravel(), y.ravel()), axis=1) # 测试样本集
y_test = z.ravel() # 测试标签集

args = {
    'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000], # 指定C的7种取值
    'gamma': [0.001, 0.01, 0.1, 1, 10, 100, 1000] # 指定C的7种取值
}
gs = GridSearchCV(SVR(), args, cv=5) # 实例化网格搜索器
gs.fit(X_train, y_train)

print(gs.score(X_test, y_test)) # 评估网格搜索器
print(gs.best_params_) # 当前最佳参数

z_gs = gs.predict(X_test) # 对测试集做回归分析

ax = plt.subplot(111, projection='3d')
ax.scatter3D(_x, _y, _z, c='r')
ax.plot_surface(x, y, z_gs.reshape(x.shape), cmap=plt.cm.hsv, alpha=0.5)
plt.show()
