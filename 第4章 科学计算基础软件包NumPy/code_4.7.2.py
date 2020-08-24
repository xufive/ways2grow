# -*- encoding: utf-8 -*-

"""
4.7.2 随机抽样
"""

import numpy as np

print(np.random.choice(1,5)) # 抽签样本只有1个元素0，抽取5次
print(np.random.choice(['a','b','c'], size=(3,5), p=[0.5,0.25,0.25])) # 指定权重
print(np.random.choice(np.arange(100), size=(2,5), replace=False)) # 不允许重复
