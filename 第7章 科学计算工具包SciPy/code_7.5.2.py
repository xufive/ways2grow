# -*- encoding: utf-8 -*-

"""
7.5.2 边缘检测
"""

import cv2
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

im = cv2.imread(r'..\res\cup.jpg', cv2.IMREAD_GRAYSCALE)
pwt0 = ndimage.prewitt(im, axis=0) # 对0轴做prewitt边缘检测
pwt1 = ndimage.prewitt(im, axis=1) # 对1轴做prewitt边缘检测
im_pwt = np.zeros(im.shape, dtype=np.uint8)
im_pwt[(pwt0>128)|(pwt1>128)] = 255 # 合并prewitt边缘检测结果
sob0 = ndimage.sobel(im, axis=0) # 对0轴做sobel边缘检测
sob1 = ndimage.sobel(im, axis=1) # 对1轴做sobel边缘检测
im_sob = np.zeros(im.shape, dtype=np.uint8)
im_sob[(sob0>128)|(sob1>128)] = 255 # 合并sobel边缘检测结果
im_lap = ndimage.laplace(im) # 拉普拉斯边缘检测

plt.subplot(221)
plt.title('原始灰度图')
plt.imshow(im, cmap=plt.cm.gray)
plt.subplot(222)
plt.title('prewitt边缘检测')
plt.imshow(im_pwt, cmap=plt.cm.gray)
plt.subplot(223)
plt.title('sobel边缘检测')
plt.imshow(im_sob, cmap=plt.cm.gray)
plt.subplot(224)
plt.title('laplace边缘检测')
plt.imshow(im_lap, cmap=plt.cm.gray)
plt.show()
