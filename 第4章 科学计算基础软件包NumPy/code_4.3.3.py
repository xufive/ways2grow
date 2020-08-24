# -*- encoding: utf-8 -*-

"""
4.3.3 合并
"""

import numpy as np

# 使用append()合并数组

print(np.append([[1, 2, 3]], [[4, 5, 6]]))
print(np.append([[1, 2, 3]], [[4, 5, 6]], axis=0)) 
print(np.append([[1, 2, 3]], [[4, 5, 6]], axis=1))

# 使用stack()函数以及hstack()函数、vstack()函数和dstack()函数合并数组

a = np.arange(4).reshape(2,2)
b = np.arange(4,8).reshape(2,2)
print(np.hstack((a,b))) # 水平合并
print(np.vstack((a,b))) # 垂直合并
print(np.dstack((a,b))) # 深度合并

a = np.arange(60).reshape(3,4,5)
b = np.arange(60).reshape(3,4,5)
print(a.shape, b.shape)
print(np.stack((a,b), axis=0).shape)
print(np.stack((a,b), axis=1).shape)
print(np.stack((a,b), axis=2).shape)
print(np.stack((a,b), axis=3).shape)
