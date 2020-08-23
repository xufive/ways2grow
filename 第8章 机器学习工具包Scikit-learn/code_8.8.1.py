# -*- encoding: utf-8 -*-

"""
8.8.1 估计器得分
"""

# 分类估计器

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split as tsplit
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = tsplit(X, y, test_size=0.1)
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
print(accuracy_score(y_test, y_pred)) # 使用准确性指标评价函数
print(knn.score(X_test, y_test)) # 直接使用测试集对训练效果做出准确性评价

# 回归估计器

from sklearn.svm import SVR
from sklearn.model_selection import train_test_split as tsplit
from sklearn import metrics

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = tsplit(X, y, test_size=0.1)
svr = SVR()
svr.fit(X_train, y_train)

y_pred = svr.predict(X_test)
print(metrics.mean_squared_error(y_test, y_pred)) # 均方误差指标评价函数
print(metrics.median_absolute_error(y_test, y_pred)) # 中位数绝对误差指标评价函数
print(metrics.r2_score(y_test, y_pred)) # 复相关系数指标评价函数
print(svr.score(X_test, y_test)) # 直接使用估计器得分函数
