# -*- encoding: utf-8 -*-

"""
4.1.6 维、秩、轴
"""

import numpy as np

# 例1 数值型数组的各个元素加1 

a = [0, 1, 2, 3, 4]
for i in range(len(a)):
    a[i] += 1
	
print(a)

a = np.array([0, 1, 2, 3, 4])
a += 1
print(a)

# 例2 两个等长的数值型数组的对应元素相加

a = [0, 1, 2, 3, 4]
b = [5, 6, 7, 8, 9]
print([i+j for i, j in zip(a, b)])

a = np.array([0, 1, 2, 3, 4])
b = np.array([5, 6, 7, 8, 9])
print(a + b)
