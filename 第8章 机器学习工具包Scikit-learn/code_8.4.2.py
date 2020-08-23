# -*- encoding: utf-8 -*-

"""
8.4.2 贝叶斯分类
"""

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer # TF-IDF向量
from sklearn.naive_bayes import MultinomialNB # 导入多项式分布的朴素贝叶斯模型
from sklearn.model_selection import train_test_split as tsplit
from sklearn.metrics import classification_report # 导入分类结果评估报告函数

X, y = fetch_20newsgroups(return_X_y=True) # 获取新闻数据集和分类标签集
vectorizer = TfidfVectorizer()
vdata = vectorizer.fit_transform(X) # 文本转为TF-IDF向量

x_train, x_test, y_train, y_test = tsplit(vdata, y, test_size=0.1)
m = MultinomialNB() # 实例化多项式分布的朴素贝叶斯分类器
m.fit(x_train, y_train) # 模型训练

precision = m.score(x_test, y_test)
print('测试集分类准确率：%0.2f'%precision)

y_pred = m.predict(x_test)
report = classification_report(y_test, y_pred)
print('测试集分类结果报告：\n', report)
