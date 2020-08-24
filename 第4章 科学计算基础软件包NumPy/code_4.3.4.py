# -*- encoding: utf-8 -*-

"""
4.3.4 拆分
"""

import numpy as np

a = np.arange(16).reshape(2,4,2)
print(np.hsplit(a, 2)) # 水平方向拆分成2部分
print(np.vsplit(a, 2)) # 垂直方向拆分成2部分
print(np.dsplit(a, 2)) # 深度方向拆分成2部分
