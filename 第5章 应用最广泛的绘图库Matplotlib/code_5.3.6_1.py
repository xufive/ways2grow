# -*- encoding: utf-8 -*-

"""
5.3.6 刻度——设置主副刻度
"""

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.dates as mdates

x = np.arange('2019-01', '2019-06', dtype='datetime64[D]')
y = np.random.rand(x.shape[0])

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(x, y, c='g')
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('\n%Y-%m-%d'))
ax.xaxis.set_minor_locator(mdates.DayLocator(bymonthday=(1,11,21)))
ax.xaxis.set_minor_formatter(mdates.DateFormatter('%d'))
plt.show()
