# -*- encoding: utf-8 -*-

"""
3.3.3 读写hdf文件
"""

import numpy as np
import h5py

lats, lons = np.mgrid[-90:90:361j, -180:180:721j] # 生成纬度、经度网格
temp = np.random.randint(100, 300, lons.shape) # 生成随机的温度数据
print(lons.shape, lats.shape, temp.shape) # ((361, 721), (361, 721)), (361, 721))

fp = h5py.File(r'..\res\hdf5demo.h5', 'w')
lons_dataset = fp.create_dataset("lons", data=lons) # 写入经度数据集
lats_dataset = fp.create_dataset("lats", data=lats) # 写入纬度数据集
temp_dataset = fp.create_dataset("temp", data=temp) # 写入温度数据集
lons_dataset.attrs["lons_range"] = [-180, 180] # 写入经度属性
lats_dataset.attrs["lats_range"] = [-90, 90] # 写入经度属性
temp_dataset.attrs["temp_range"] = [100, 300] # 写入温度属性
fp.close()

fp = h5py.File(r'..\res\hdf5demo.h5', 'r')
lons = fp["lons"].value
lats = fp["lats"].value
temp = fp["temp"].value
print("LONS:", lons.shape, fp["lons"].attrs["lons_range"])
print("LATS:", lats.shape, fp["lats"].attrs["lats_range"])
print("TEMP:", temp.shape, fp["temp"].attrs["temp_range"])
fp.close()
