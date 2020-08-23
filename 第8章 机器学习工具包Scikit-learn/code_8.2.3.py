# -*- encoding: utf-8 -*-

"""
8.2.3 加载其他数据集
"""

from sklearn import datasets as dss

chess = dss.fetch_openml(name='kropt')

print(chess.DESCR)
print(chess.keys())
print(chess.data.shape, chess.data.dtype)
