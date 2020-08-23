# -*- encoding: utf-8 -*-

"""
8.4.1 k-近邻分类
"""

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier # 导入K-近邻分类器
from sklearn.model_selection import train_test_split as tsplit

iris = load_iris() # 获取鸢尾花数据集
print(iris.data.shape) # 150个样本，每个样本4项特征：花萼长度和宽度，花瓣长度和宽度
print(iris.target_names) # 鸢尾花三个品种的名字
print(iris.target) # 150个样本的分类标签编号，0，1，2分别对应三个品种

X, y = load_iris(return_X_y=True) # 获取鸢尾花数据集，返回样本集和标签集
X_train, X_test, y_train, y_test = tsplit(X, y, test_size=0.1) # 拆分
m = KNeighborsClassifier() # 实例化模型。n_neighbors参数指定k值，默认k=5
m.fit(X_train, y_train) # 模型训练
score = m.score(X_test, y_test) # 模型测试精度（介于0~1之间）
print(score)
