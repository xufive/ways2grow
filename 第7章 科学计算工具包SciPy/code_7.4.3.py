# -*- encoding: utf-8 -*-

"""
7.4.3 二维傅里叶变换的应用
"""

from scipy import fft as spfft
import numpy as np
import cv2
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

im = cv2.imread(r'..\res\flower.jpg', cv2.IMREAD_GRAYSCALE)
fd = spfft.fft2(im) # 对图像进行二维傅里叶变换
print(fd.shape) # 和原始图像数组形状相同，元素类型、含义类似一维傅里叶变换
fds = spfft.fftshift(fd) # 将低频分量移到数组中心，高频分量移到数组外层
fd_abs = np.log(np.abs(fd)) # 计算各分量强度
fds_abs = np.log(np.abs(fds)) # 计算移频后的各分量强度
fd_top = np.hstack((fd[:100,:100], fd[:100, 500:])) # 取左上角、右上角
fd_bot = np.hstack((fd[500:,:100], fd[500:, 500:])) # 取左下角、右下角
fd_low = np.vstack((fd_top, fd_bot)) # 四角合并，相当于去掉了数组中心的高频分量
im_low = np.abs(spfft.ifft2(fd_low)) # 去掉高频分量，再反变换成灰度图像

plt.subplot(221)
plt.title('原始灰度图')
plt.imshow(im, cmap=plt.cm.gray)
plt.subplot(222)
plt.title('频谱图，低频在四角')
plt.imshow(fd_abs, cmap=plt.cm.jet)
plt.subplot(223)
plt.title('去除高频分量的灰度图')
plt.imshow(im_low, cmap=plt.cm.gray)
plt.subplot(224)
plt.title('频谱图，低频在中心')
plt.imshow(fds_abs, cmap=plt.cm.jet)
plt.show()

