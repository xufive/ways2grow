# -*- encoding: utf-8 -*-

"""
7.2.3 离散数据插值到网格
"""

import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

lons = np.random.random(300)*180 # 经度从0°到180°，随机生成300个点
lats = np.random.random(300)*90 # 纬度从0°到90°，随机生成300个点
# 生成300个点的温度数据
temp = ((lons-90)/45)*np.exp(-((lons-90)/45)**2-((lats-45)/45)**2)

# 将矩形区域数据裁剪成三角区域（去掉左上角和右上角）
triangle = np.where(((lons<90)&(lats<lons))|((lons>=90)&(lats<180-lons)))
lons = lons[triangle]
lats = lats[triangle]
temp = temp[triangle]

lat_grid, lon_grid = np.mgrid[0:90:91j, 0:180:181j] # 生成目标网格
# 使用三种插值方式生成插值数据
temp_nearest = griddata((lons,lats), temp, (lon_grid, lat_grid), method='nearest')
temp_linear = griddata((lons,lats), temp, (lon_grid, lat_grid), method='linear')
temp_cubic = griddata((lons,lats), temp, (lon_grid, lat_grid), method='cubic')

plt.subplot(221)
plt.title('原始数据')
plt.scatter(lons, lats, s=3, c=temp, cmap=plt.cm.hsv)
plt.axis('equal')

plt.subplot(222)
plt.title('临近点插值')
plt.scatter(lon_grid, lat_grid, s=3, c=temp_nearest, cmap=plt.cm.hsv)
plt.axis('equal')

plt.subplot(223)
plt.title('线性插值')
plt.scatter(lon_grid, lat_grid, s=3, c=temp_linear, cmap=plt.cm.hsv)
plt.axis('equal')

plt.subplot(224)
plt.title('三阶插值')
plt.scatter(lon_grid, lat_grid, s=3, c=temp_cubic, cmap=plt.cm.hsv)
plt.axis('equal')

plt.show()
