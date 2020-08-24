# -*- encoding: utf-8 -*-

"""
4.4.1 常量
"""

import numpy as np

a = np.array([1, 2, np.nan, np.inf])
print(a.dtype)

a[0] = np.nan
a[1] = np.inf
print(a)

print(a[0] == a[2]) # 两个np.nan不相等
print(a[1] == a[3]) # 两个np.inf则相等

print(np.isnan(a[0])) # 判断一个数组元素是否是np.nan
print(np.isinf(a[1])) # 判断一个数组元素是否是np.inf
