# -*- encoding: utf-8 -*-

"""
7.2.2 二维插值
"""

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

y, x = np.mgrid[-2:2:20j,-3:3:30j] # 30x20 = 600
z = x*np.exp(-x**2-y**2)*10 + 20
y_new, x_new = np.mgrid[-2:2:80j,-3:3:120j] # 120x80 = 9600

f1 = interpolate.interp2d(x[0,:], y[:,0], z, kind='linear') # 线性插值
f2 = interpolate.interp2d(x[0,:], y[:,0], z, kind='cubic') # 三阶样条
f3 = interpolate.interp2d(x[0,:], y[:,0], z, kind='quintic') # 五阶样条

z1 = f1(x_new[0,:], y_new[:,0])
z2 = f2(x_new[0,:], y_new[:,0])
z3 = f3(x_new[0,:], y_new[:,0])

fig = plt.figure()
axes_1 = fig.add_subplot(221)
axes_2 = fig.add_subplot(222)
axes_3 = fig.add_subplot(223)
axes_4 = fig.add_subplot(224)

axes_1.set_title('原始数据')
mappable = axes_1.pcolor(x, y, z, cmap=plt.cm.jet)
plt.colorbar(mappable, ax=axes_1)
#axes_1.axis('equal')

axes_2.set_title('线性插值')
mappable = axes_2.pcolor(x_new, y_new, z1, cmap=plt.cm.jet)
fig.colorbar(mappable, ax=axes_2)
#axes_2.axis('equal')

axes_3.set_title('三阶样条')
mappable = axes_3.pcolor(x_new, y_new, z2, cmap=plt.cm.jet)
fig.colorbar(mappable, ax=axes_3)
#axes_3.axis('equal')

axes_4.set_title('五阶样条')
mappable = axes_4.pcolor(x_new, y_new, z3, cmap=plt.cm.jet)
fig.colorbar(mappable, ax=axes_4)
#axes_4.axis('equal')

plt.show()
