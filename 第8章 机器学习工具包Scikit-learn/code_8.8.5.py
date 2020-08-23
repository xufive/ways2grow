# -*- encoding: utf-8 -*-

"""
8.8.5 模型持久化
"""

import joblib
from sklearn.datasets import load_wine
from sklearn.svm import SVC

X, y = load_wine(return_X_y=True)

svc = SVC()
svc.fit(X, y)

joblib.dump(svc, r'..\res\svc.m') # 持久化模型
svc = joblib.load(r'..\res\svc.m') # 加载模型
