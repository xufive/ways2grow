# -*- encoding: utf-8 -*-

"""
4.3.1 索引和切片
"""

import numpy as np

a = np.arange(9)
print(a[-1]) # 最后一个元素
print(a[2:5]) # 返回第2到第5个元素
print(a[:7:3]) # 返回第0到第7个元素，步长为3
print(a[::-1]) # 返回逆序的数组

a = np.arange(24).reshape(2,3,4) # 2层楼，每层楼内的房间都是3行4列
print(a)
print(a[1][2][3]) # 虽然可以这样索引
print(a[1,2,3]) # 但这样才是规范的用法
print(a[:,0,0]) # 所有楼层的第0排第0列
print(a[0,:,:]) # 1楼的所有房间，等价于a[0]或a[0,...]
print(a[:,:,1:3]) # 所有楼层所有排的第1到第3列
print(a[1,:,-1]) # 2楼每一排的最后一个房间

a = np.arange(12).reshape(3,4)
print(a)
b = a[1:,2:] # 数组b是数组a的切片
print(b)
b[:,:] = 99 # 改变数组b的值，也会同时影响数组a
print(b)
print(a) # 数组a也被改变，证明数组b是数组a的视图
