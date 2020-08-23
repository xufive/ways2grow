# -*- encoding: utf-8 -*-

"""
3.3.4 读写netCDF文件
"""

import netCDF4
import numpy as np

fp = netCDF4.Dataset(r'..\res\netcdfdemo.nc' , 'w', format='NETCDF4')
fp.createDimension('lons', size=721) # 设置经度的维度
fp.createDimension('lats', size=361) # 设置纬度的维度
lons_var = fp.createVariable("lons", 'f' ,("lons",)) # 创建lons数据集
lats_var = fp.createVariable("lats", 'f' ,("lats",)) # 创建lats数据集
fp.variables['lons'][:] = np.linspace(-180,180,721) # lons数据集赋值
fp.variables['lats'][:] = np.linspace(-90,90,361) # lats数据集赋值
lons_var.lon_range = [-180, 180]
lats_var.lat_range = [-90, 90]
fp.createVariable('temp','f8',('lats','lons')) # 创建temp数据集
fp.variables['temp'][:] = np.random.randint(100, 300, (361,721)) # temp数据集赋值
fp.close()

fp = netCDF4.Dataset(r'..\res\netcdfdemo.nc' , 'r', format='NETCDF4')
lons = fp.variables['lons'][:]
lats = fp.variables['lats'][:]
temp = fp.variables['temp'][:]
print(lons.shape, fp.variables['lons'].lon_range)
print(lats.shape, fp.variables['lats'].lat_range)
print(temp.shape)
fp.close()
