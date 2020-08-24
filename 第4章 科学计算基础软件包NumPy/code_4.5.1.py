# -*- encoding: utf-8 -*-

"""
4.5.1 创建掩码数组
"""

import numpy as np
import numpy.ma as ma

# 1. 由列表生成掩码数组
a = ma.array([0, 1, 2, 3], mask=[0, 0, 1, 0]) # 指定第3个元素无效
print(a)
print(type(a))
print(a.min(), a.max(), a.mean(), a.var())

# 2. 由数组生成掩码数组
a = np.arange(5)
print(ma.asarray(a))

a = np.array([1, np.nan, 2, np.inf, 3]) # 包含特殊值的数组
print(ma.asarray(a))

# 3. 对数组中的无效值做掩码处理
a = np.array([1, np.nan, 2, np.inf, 3])
print(ma.masked_invalid(a))

# 4. 对数组中的给定值做掩码处理
a = np.arange(3).repeat(2)
print(ma.masked_equal(a, 1)) # 对数组元素1做掩码

# 5. 对数组中符合条件的特定值做掩码处理
a = np.arange(8)
print(ma.masked_greater(a, 4)) # 掩码大于4的元素
print(ma.masked_greater_equal(a, 4)) # 掩码大于等于4的元素
print( ma.masked_less(a, 4)) # 掩码小于4的元素
print(ma.masked_less_equal(a, 4)) # 掩码小于等于4的元素
print(ma.masked_inside(a, 2, 5)) # 掩码 [2,5]之间的元素
print(ma.masked_outside(a, 2, 5)) # 掩码 [2,5]之外的元素

# 6. 用一个数组的条件筛选结果对另一个数组做掩码处理
a = np.arange(8)
b = np.random.random(8)
print( ma.masked_where(a>5, b)) # 用a>5的条件掩码数组b 
