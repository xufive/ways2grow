# -*- encoding: utf-8 -*-

"""
7.5.1 图像卷积
"""

import cv2
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

im = cv2.imread(r'..\res\flower.jpg', cv2.IMREAD_GRAYSCALE)
w3 = np.ones((3,3)) # 生成3×3的权重数组
w3 /= np.sum(w3) # 累计权重为1
w9 = np.ones((9,9)) # 生成9×9的权重数组
w9 /= np.sum(w9) # 累计权重为1
im_w3 = ndimage.convolve(im, w3) # 使用3×3的权重数组对图像做卷积
im_w9 = ndimage.convolve(im, w9) # 使用9×9的权重数组对图像做卷积

plt.subplot(131)
plt.title('原始灰度图')
plt.imshow(im, cmap=plt.cm.gray)
plt.subplot(132)
plt.title('3x3卷积灰度图')
plt.imshow(im_w3, cmap=plt.cm.gray)
plt.subplot(133)
plt.title('9x9卷积灰度图')
plt.imshow(im_w9, cmap=plt.cm.gray)
plt.show()
