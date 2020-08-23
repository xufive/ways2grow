# -*- encoding: utf-8 -*-

"""
7.2.1 一维插值
"""

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0,10,11) # 0-10之间11个离散点
y = np.exp(-np.sin(x)/3.0) # 11个离散点的函数值
x_new = np.linspace(0,10,100) # 期望在0-10之间插值100个数据点

f_linear = interpolate.interp1d(x, y, kind='linear')
f_nearest = interpolate.interp1d(x, y, kind='nearest')
f_zero = interpolate.interp1d(x, y, kind='zero')
f_slinear = interpolate.interp1d(x, y, kind='slinear')
f_cubic = interpolate.interp1d(x, y, kind='cubic')
f_quadratic = interpolate.interp1d(x, y, kind='quadratic')
f_previous = interpolate.interp1d(x, y, kind='previous')
f_next = interpolate.interp1d(x, y, kind='next')

plt.figure('Demo', facecolor='#eaeaea')
plt.subplot(221)
plt.plot(x, y, "o",  label=u"原始数据")
plt.plot(x_new, f_nearest(x_new), label=u"临近点插值")
plt.plot(x_new, f_next(x_new), label=u"后点线性插值")
plt.legend()

plt.subplot(222)
plt.plot(x, y, "o",  label=u"原始数据")
plt.plot(x_new, f_previous(x_new), label=u"前点插值")
plt.plot(x_new, f_zero(x_new), label=u"零阶样条插值")
plt.legend()

plt.subplot(223)
plt.plot(x, y, "o",  label=u"原始数据")
plt.plot(x_new, f_linear(x_new), label=u"线性插值")
plt.plot(x_new, f_slinear(x_new), label=u"一阶样条插值")
plt.legend()

plt.subplot(224)
plt.plot(x, y, "o",  label=u"原始数据")
plt.plot(x_new, f_slinear(x_new), label=u"一阶样条插值")
plt.plot(x_new, f_cubic(x_new), label=u"三阶样条插值")
plt.plot(x_new, f_quadratic(x_new), label=u"五阶样条插值")
plt.legend()

plt.show()
