# -*- encoding: utf-8 -*-

"""
4.2.7 自定义数据类型
"""

import numpy as np

mytype = np.dtype([('name','S32'), ('tall',np.float), ('bw',np.int)])
print(np.array([('Anne', 1.70, 55)], dtype=mytype))
