# -*- encoding: utf-8 -*-

"""
4.3.9 数组I/O
"""

import numpy as np

# 1. 读写CSV文件
a = np.random.random((15,5))
np.savetxt(r'..\res\np_demo.csv', a, delimiter=',') # 将数组a保存成csv格式的文件
data = np.loadtxt(r'..\res\np_demo.csv', delimiter=',') # 打开csv格式的文件
print(data.shape, data.dtype) 

# 2. 读写npy/npz文件
single_arr_fn = r'..\res\single_arr.npy' # 存储单个数组文件名
multi_arr_fn = r'..\res\multi_arr.npz' # 存储多个数组文件名
lon = np.linspace(10,90,9)
lat = np.linspace(20,60,5)

np.save(single_arr_fn, lon) # 用save()函数把经度数组保存成npy文件
lon = np.load(single_arr_fn) # 接着用load()函数读出来

np.savez(multi_arr_fn, longitude=lon, latitude=lat) #保存两个数组到一个文件
data = np.load(multi_arr_fn) # 用load()函数把这个npz文件读成一个结构data
print(data.files) # 查看所有的数组名 
print(data['longitude']) # data[数组名]，就可以取得想要的数据
print(data['latitude']) # data[数组名]，就可以取得想要的数据
