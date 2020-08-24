# -*- encoding: utf-8 -*-

"""
4.2.6 网格构造法
"""

import numpy as np

lon = np.linspace(-180,180,37) # 精度为10°，共计37个经度点
lat = np.linspace(90,-90,19) # 精度为10°，共计19个纬度点

lons,lats = np.meshgrid(lon,lat) # 生成网格数组的第1种方式：meshgrid
print(lons.shape)
print(lats.shape)

print(lons[:,0]) # 经度数组首列都是-180°
print(lats[0]) # 纬度数组首行都是90°

lats, lons = np.mgrid[90:-91:-5, -180:181:5] # 生成网格数组的第2种方式：用实数指定网格精度
print(lons.shape, lats.shape)

lats, lons = np.mgrid[90:-90:37j, -180:180:73j] # 生成网格数组的第3种方式：用虚数指定分割点数
print(lons.shape, lats.shape)

# 构造复数的方法
r, i = 2, 5
print(complex(r, i))
