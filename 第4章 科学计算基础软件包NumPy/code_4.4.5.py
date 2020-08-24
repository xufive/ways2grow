# -*- encoding: utf-8 -*-

"""
4.4.5 插值函数
"""

import numpy as np
import matplotlib.pyplot as plt

_x = np.linspace(0, 2*np.pi, 11)
_y = np.sin(_x)
x = np.linspace(0, 2*np.pi, 33)
y = np.interp(x, _x, _y)

plt.plot(x, y, 'o')
plt.plot(_x, _y, 'o')
plt.show()
