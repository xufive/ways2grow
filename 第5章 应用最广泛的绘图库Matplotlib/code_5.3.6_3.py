# -*- encoding: utf-8 -*-

"""
5.3.6 刻度——设置刻度文本样式
"""

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.dates as mdates

x = np.arange('2019-01', '2020-01', dtype='datetime64[D]')
y = np.random.rand(x.shape[0])

fig = plt.figure()
ax = fig.add_axes([0.1, 0.3, 0.8, 0.6])
ax.plot(x, y, c='g')
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))

for lobj in ax.get_xticklabels():
    lobj.set_rotation(35)
    lobj.set_size(12)
    lobj.set_color('blue')

plt.show()
