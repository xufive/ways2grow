# -*- encoding: utf-8 -*-

"""
7.5.4 图像测量
"""

import cv2
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

im = cv2.imread(r'..\res\cup.jpg', cv2.IMREAD_GRAYSCALE)
hist = ndimage.histogram(im, 0, 255, 256)
hist = hist.astype(np.float)
hist[hist==0] = np.nan

plt.subplot(121)
plt.title('浅灰像素数量远多于深灰')
plt.bar(np.arange(256), hist, align="center", width=1, alpha=0.5)
plt.subplot(122)
plt.title('纵轴取对数，显示深灰分布细节')
plt.bar(np.arange(256), np.log(hist), align="center", width=1, alpha=0.5)
plt.show()
