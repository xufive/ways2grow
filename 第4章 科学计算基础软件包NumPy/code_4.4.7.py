# -*- encoding: utf-8 -*-

"""
4.4.7 自定义广播函数
"""

import numpy as np

def func_demo(x, y):
    if x == 0 or y == 0 or x == y:
        return 0
    elif x&(x-1) == 0 and y&(y-1) == 0: # x和y都是2的整数次幂
        return max(x, y)
    elif x&(x-1) == 0: # 仅有x等于2的整数次幂
        return x
    elif y&(y-1) == 0: # 仅有y等于2的整数次幂
        return y
    else:
        return max(x, y)

# 1. 使用np.frompyfunc()定义广播函数
uf = np.frompyfunc(func_demo, 2, 1)
a = np.random.randint(0, 256, (2,5), dtype=np.uint8)
b = np.random.randint(0, 256, (2,5), dtype=np.uint8)
c = uf(a, b)
print(c.dtype) # 此时c的数据类型为object
c = c.astype(np.uint8) # 改变类型
print(c)

#2. 使用np.vectorize()定义广播函数
uf = np.vectorize(func_demo, otypes=[np.uint8])
c = uf(a, b)
print(c) # 此时c的数据类型为uint8
