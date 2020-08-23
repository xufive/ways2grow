# -*- encoding: utf-8 -*-

"""
3.2.2 PyOpenCV模块
"""

import cv2
from PIL import Image
import numpy as np


# 2. 打开、显示和保存图像文件
# ------------------------------

im = cv2.imread(r'..\res\coffee.png')
print(im.shape) # (1089, 1261, 3)：图像分辨率为1261x1089，RGB模式
cv2.imshow('image',im)
cv2.waitKey(0)
cv2.imwrite(r'..\res\coffee.jpg', im)

im = cv2.imread(r'..\res\coffee.png', cv2.IMREAD_UNCHANGED)
print(im.shape) # (1089, 1261, 4)：图像分辨率为1261x1089，RGBA模式
im = cv2.imread(r'..\res\coffee.png', cv2.IMREAD_GRAYSCALE)
print(im.shape) # (1089, 1261)：图像分辨率为1261x1089，灰度模式
cv2.imwrite(r'..\res\coffee_gray.jpg', im)

# 3. 绘图
# ------------------------------

im = np.zeros((300, 800, 3), dtype=np.uint8) # 生成800x300的黑色背景图
im = cv2.line(im, (0,200), (800,200), (0,0,255), 2) # 画线
im = cv2.rectangle(im,(20,20),(180,180),(255,0,0),1) # 画矩形
im = cv2.circle(im, (320,100), 80, (0,255,0), -1) # 画圆
font = cv2.FONT_HERSHEY_SIMPLEX
im = cv2.putText(im, 'Hello, wold.', (420,100), font, 2, (255,255,255), 2, cv2.LINE_AA) # 写文本（仅限英文，如需要中文，请转pillow实现）
cv2.imshow('Image', im)
cv2.waitKey(0)

# 4. cv2格式和PIL格式的互转
# ------------------------------

im_pil = Image.open(r'..\res\coffee.png')
im_cv2 = np.array(im_pil)
cv2.imwrite(r'..\res\coffee.jpg', im_cv2[:,:,[2,1,0]])

im_cv2 = cv2.imread(r'..\res\coffee.png')
im_pil = Image.fromarray(im_cv2[:,:,[2,1,0]])
im_pil.save(r'..\res\coffee.jpg')


