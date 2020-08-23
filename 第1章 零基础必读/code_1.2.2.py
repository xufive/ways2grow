# -*- encoding: utf-8 -*-

"""
1.2.2 使用IPython交互操作

本脚本文件是将IPython交互操作的每一行语句合并在一起连续执行。
请仔细体会交互操作和运行脚本文件的差异。
"""

import time
import numpy as np

print(time.time())
print(time.ctime())

arr = np.random.random((3,5))
print(arr)
