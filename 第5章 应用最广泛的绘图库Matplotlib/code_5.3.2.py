# -*- encoding: utf-8 -*-

"""
5.3.2 子图布局
"""

from matplotlib import pyplot as plt
import matplotlib.gridspec as gspec

fig = plt.figure()
gs = gspec.GridSpec(3, 4, width_ratios=[1,1,2,1], height_ratios=[1,1,1])
ax1 = fig.add_subplot(gs[0, :-1])
ax2 = fig.add_subplot(gs[:-1, -1])
ax3 = fig.add_subplot(gs[1:, :2])
ax4 = fig.add_subplot(gs[1, 2])
ax5 = fig.add_subplot(gs[-1, 2:])
plt.show()
