# -*- encoding: utf-8 -*-

"""
5.3.4 线条和点的样式
"""

import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 2*np.pi, 15)
y = np.sin(x)

plt.plot(x, y, ls='-', marker='o', label="ls='-', marker='o'")
plt.plot(x, y+0.1, ls='--', marker='x', label="ls='--', marker='x'")
plt.plot(x, y+0.2, ls=':', marker='v', label="ls=':', marker='v'")
plt.plot(x, y+0.3, ls='-.', marker='*', label="ls='-.', marker='*'")
plt.plot(x, y+0.4, ls='none', marker='D', label="ls='none', marker='D'")
plt.legend()
plt.show()
