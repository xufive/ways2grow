# -*- encoding: utf-8 -*-

"""
4.3.2 改变结构
"""

import numpy as np

a = np.arange(12)
b = a.reshape((3, 4)) # reshape()返回数组a的一个新视图，但不会改变数组a

print(a.shape) # (12,)
print(b.shape) # (3, 4)
print(b is a) # False
print(b.base is a) # True

a.resize([4,3]) # resize()没有返回值，但真正改变了数组a的结构
print(a.shape) # (4, 3)

print(a.ravel()) # 返回多维数组一维化的视图，但不会改变原数组
print(a.transpose()) # 返回行变列的视图，但不会改变原数组
print(a.T) # 返回行变列的视图，等价于transpose()
print(np.rollaxis(a, 1, 0)) # 翻滚轴，1轴变0轴

# 下面的代码生成了一个宽为800像素、高为600像素的彩色随机噪声图
# 使用翻转轴函数可以将其分离成RGB三个颜色通道

img = np.random.randint(0, 256, (600, 800, 3), dtype=np.uint8)
print(img.shape)
r, g, b = np.rollaxis(img, 2, 0) # 将图像数据分离成RGB三个通道
print(r.shape, g.shape, b.shape)

from PIL import Image # 导入pillow模块的Image
Image.fromarray(img).show() # 显示随机生成的噪声图
