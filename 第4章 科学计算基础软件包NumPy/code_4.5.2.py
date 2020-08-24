# -*- encoding: utf-8 -*-

"""
4.5.2 访问掩码数组
"""

import numpy as np
import numpy.ma as ma

# 1. 索引和切片
a = np.array([1, np.nan, 2, np.inf, 3])
a = ma.masked_invalid(a)
print(a[0], a[1], a[-1])
print(a[1:-1])

# 2. 函数应用
a = np.array([1, np.nan, 2, np.inf, 3])
a = ma.masked_invalid(a)
print(a.min(), a.max(), a.mean(), a.var())
#print(np.sin(a)) # 虽然可以执行，但会弹出警告
print(ma.sin(a)) # 这才是正确的用法

# 3. 掩码数组转为普通数组
a = ma.array([1, np.nan, 2, np.inf, 3])
print(a)

x = a.data
y = a.__array__()
z = ma.getdata(a)
w = np.copy(a.__array__()) # 复制数据视图

print(x)
print(y)
print(z)
print(w)

a[-1] = 9
print(x)
print(y)
print(z)
print(w)

# 4. 修改掩码
a = ma.masked_invalid(np.array([1, np.nan, 2, np.inf, 3]))
print(a.mask)
print(a)

a[:2] = ma.masked
print(a)

a = ma.masked_invalid(np.array([1, np.nan, 2, np.inf, 3]))
a[1] = 1.5
a[2:4] = 5
print(a)
