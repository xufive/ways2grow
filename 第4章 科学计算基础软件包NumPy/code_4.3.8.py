# -*- encoding: utf-8 -*-

"""
4.3.8 筛选
"""

import numpy as np

a = np.random.random((3,4))
print(a)
print(a[np.where(a>0.5)]) # 返回大于0.5的元素（使用np.where()返回的python元组）
print(a[(a>0.3)&(a<0.7)]) # 返回大于0.3且小于0.7的元素（使用逻辑表达式返回的布尔型数组）
print(a[np.array([2,1])]) # 返回整型数组指定的项（使用整型数组）

a = a.ravel()
print(a[np.array([3,5,7,11])]) # 返回整型数组指定的项（使用整型数组）
print(a[np.array([[3,5],[7,11]])]) # 返回整型数组指定的项（使用整型数组）

# 使用整型数组来筛选数组元素的用途是什么呢？
# 一个看似不起眼的功能，却蕴含着无穷的想象空间
# 我们用一个例子来演示通过整型数组筛选数组元素的神奇魔法

from PIL import Image

im = Image.open(r'..\res\girl.jpg') # 打开图像文件
im_gray = im.convert('L') # 转为灰度图像

width = 120
height = int(width*im_gray.size[1]/im_gray.size[0])
im_gray = im_gray.resize((width, height)) # 设置分辨率

img = np.array(im_gray) # PIL对象转为NumPy数组
img = 255 - img # 反白处理
img = (img/32).astype(np.uint8) # 将256级灰度转为8级灰度
chs = np.array([' ', '.', '-', '+', '=', '*', '#', '@']) # 灰度字符集
img_char = chs[img] # 用整型数组筛选字符数组元素（我认为这是NumPy最精彩之处！）

# 输出到控制台（为了平衡宽高比，水平方向每个字符之间增加了一个空格）
for i in range(img_char.shape[0]):
    for j in range(img_char.shape[1]):
        print('%s '%img_char[i,j], end='')
    print()

# 保存为文本文件
with open(r'..\res\girl.txt', 'w') as fp:
	for line in img_char.tolist():
		fp.write(''.join(line))
		fp.write('\n')
