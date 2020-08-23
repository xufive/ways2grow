# -*- encoding: utf-8 -*-

"""
8.4.3 决策树分类
"""

from sklearn.datasets import load_wine # 导入葡萄酒数据集模块
from sklearn import tree # 导入决策树子模块
from sklearn.model_selection import train_test_split as tsplit
from sklearn.metrics import classification_report

X, y = load_wine(return_X_y=True) # 获取葡萄酒数据集和分类标签集
x_train, x_test, y_train, y_test = tsplit(X, y, test_size=0.1)
m = tree.DecisionTreeClassifier() # 实例化决策树分类器
m.fit(x_train, y_train)

precision = m.score(x_test, y_test)
print('测试集分类准确率：%0.2f'%precision)

y_pred = m.predict(x_test)
report = classification_report(y_test, y_pred)
print('测试集分类结果报告：\n', report)
