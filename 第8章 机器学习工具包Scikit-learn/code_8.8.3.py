# -*- encoding: utf-8 -*-

"""
8.8.2 交叉验证
"""

from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split as tsplit

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = tsplit(X, y, test_size=0.1)

svc = SVC() # 实例化支持向量机分类器
svc.fit(X_train, y_train) # 训练
y_pred = svc.predict(X_test) # 预测

print(confusion_matrix(y_test, y_pred)) # 返回混淆矩阵
print(svc.score(X_test, y_test)) # 模型精度

print(accuracy_score(y_test, y_pred)) # 模型精度
print(precision_score(y_test, y_pred)) # 模型准确率
print(recall_score(y_test, y_pred)) # 模型召回率
print(f1_score(y_test, y_pred)) # f1分值
