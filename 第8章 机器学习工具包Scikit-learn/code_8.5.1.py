# -*- encoding: utf-8 -*-

"""
8.5.1 线性回归
"""

from sklearn.datasets import make_sparse_uncorrelated
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import train_test_split as tsplit
from sklearn import metrics

import matplotlib.pyplot as plt
import numpy as np

X, y = make_sparse_uncorrelated(n_samples=100, n_features=4)
X_train, X_test, y_train, y_test = tsplit(X, y, test_size=0.1)
reg = LinearRegression() # 实例化最小二乘法线性回归模型
reg.fit(X_train, y_train) # 训练
y_pred = reg.predict(X_test) # 预测

print(y_pred) # 预测结果
print(y_test) # 实际结果


print(metrics.mean_squared_error(y_test, y_pred)) # 均方误差
print(metrics.r2_score(y_test, y_pred)) # 复相关系数
print(metrics.median_absolute_error(y_test, y_pred)) # 中位数绝对误差

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False
plt.subplot(121)
plt.title('残差图')
plt.plot(y_pred-y_test, 'o')
plt.plot(np.array([0,9]),np.array([0,0]))
plt.xlabel('测试样本序号')
plt.ylabel('残差：预测值-实际值')
plt.subplot(122)
plt.title('实际值-预测值')
plt.plot(y_test, y_pred, 'o')
y_range = np.linspace(y_test.min(), y_test.max(), 100)
plt.plot(y_range, y_range)
plt.xlabel('实际值')
plt.ylabel('预测值')
plt.show()

X = np.array([[0, 0], [0, 0], [1, 1]]) # 样本特征相关性强
y = np.array([0, .1, 1])
reg_linear = LinearRegression() # 实例化最小二乘回归器
reg_ridge = Ridge(alpha=0.5) # 实例化岭回归器
reg_linear.fit(X, y) # 训练
reg_ridge.fit(X, y) # 训练

print(reg_linear.coef_) # 受样本的强相关性影响，回归结果明显异常
print(reg_linear.intercept_)
print(reg_ridge.coef_) # alpha参数很好地控制了系数的收缩量
print(reg_ridge.intercept_)

