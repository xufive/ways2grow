# -*- encoding: utf-8 -*-

"""
7.5.3 侵蚀和膨胀
"""
import cv2
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

im = cv2.imread(r'..\res\cup.jpg', cv2.IMREAD_GRAYSCALE)
im_lap = ndimage.laplace(im) # 拉普拉斯边缘检测
open_ero = ndimage.binary_erosion(im_lap) # 开操作：先侵蚀
im_open_ero = np.zeros(im_lap.shape)
im_open_ero[open_ero] = 255
open_dil = ndimage.binary_dilation(im_open_ero) # 开操作：后膨胀
im_open_dil = np.zeros(im_lap.shape)
im_open_dil[open_dil] = 255
close_dil = ndimage.binary_dilation(im_lap) # 闭操作：先膨胀
im_close_dil= np.zeros(im_lap.shape)
im_close_dil[close_dil] = 255
close_ero = ndimage.binary_erosion(im_close_dil) # 闭操作：后侵蚀
im_close_ero= np.zeros(im_lap.shape)
im_close_ero[close_ero] = 255

plt.subplot(131)
plt.title('laplace边缘检测')
plt.imshow(im_lap, cmap=plt.cm.gray)
plt.subplot(132)
plt.title('开操作：先侵蚀后膨胀')
plt.imshow(im_open_dil, cmap=plt.cm.gray)
plt.subplot(133)
plt.title('闭操作：先膨胀后侵蚀')
plt.imshow(im_close_ero, cmap=plt.cm.gray)
plt.show()
