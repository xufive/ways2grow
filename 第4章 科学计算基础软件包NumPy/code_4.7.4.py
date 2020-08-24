# -*- encoding: utf-8 -*-

"""
4.7.4 伪随机数的深度思考
"""

import numpy as np

np.random.seed(12345) # 使用'12345'随机种子初始化伪随机数生成器
print(np.random.random(5))
print(np.random.random((2,3)))

np.random.seed(12345) # 再次使用'12345'随机种子初始化伪随机数生成器
print(np.random.random(5)) # 和上面完全一致
print(np.random.random((2,3))) # 和上面完全一致

r = np.random.RandomState(12345) # 使用随机数生成器也同样
print(r.random(5)) # 和上面完全一致
print(r.random((2,3))) # 和上面完全一致
