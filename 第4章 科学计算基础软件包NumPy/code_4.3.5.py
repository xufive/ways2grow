# -*- encoding: utf-8 -*-

"""
4.3.5 复制
"""

import numpy as np

a = np.arange(6).reshape((2,3))

b = a.view()
print(b is a) # False
print(b.base is a) # False
print(b.flags.owndata) # False

c = a.copy()
print(c is a) # False
print(c.base is a) # False
print(c.flags.owndata) # True
