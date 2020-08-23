# -*- encoding: utf-8 -*-

"""
3.2.1 PIL和pillow模块
"""

from PIL import Image, ImageDraw, ImageGrab
from PIL import ImageFilter, ImageFont, ImageColor

# 2. 打开和保存图像文件
# ------------------------------

im = Image.open(r'..\res\flower.jpg') # 打开图像文件
print(im.mode) # 图像模式：'RGB'
print(im.size) # 图像分辨率：(600, 600)
im.show() # 调用系统默认的图像查看工具显示图像

im_gray = im.convert('L') # 将RGB彩色模式转为L灰度模式
print(im_gray.mode) # 图像模式：'L'

im_gray.save(r'..\res\flower_gray.jpg') # 保存图像

# 3. 通道合并与拆分
# ------------------------------

im = Image.open(r'..\res\flower.jpg') # 打开图像文件
r,g,b = im.split() # 将RBG图像拆分成独立的3个通道
g.save(r'..\res\flower_g.jpg') # 保存绿色通道为文件
im_bgr = Image.merge("RGB",(b,g,r)) # 交换红蓝通道，则会得特殊的效果
im_bgr.save(r'..\res\flower_bgr.jpg') # 保存交换后的图像

# 4. 旋转、缩放、裁切、复制与粘贴
# ------------------------------

im = Image.open(r'..\res\flower.jpg') # 打开图像文件
im_30 = im.rotate(30) # 逆时针旋转30°，以原图分辨率返回新图像
print(im_30.size) # 图像分辨率：(600, 600)
im_30.save(r'..\res\flower_30.jpg')

im.rotate(30, expand=True).show() #逆时针旋转30°，返回扩展的新图像
im_box = im.crop((150,50,400,200)) # 裁切250x150的局部图像
im_copy = im_box.copy() # 复制这个局部图像，并非粘贴之必需，仅为演示复制功能
im.paste(im_copy, (350,450)) # 粘贴到底图右下角
im.save(r'..\res\flower_paste.jpg') # 保存粘贴后的图像

# 5. 使用滤镜
# ------------------------------

im = Image.open(r'..\res\flower.jpg') # 打开图像文件
im_detail = im.filter(ImageFilter.DETAIL)
im_detail.save(r'..\res\flower_detail.jpg')
im_blur = im.filter(ImageFilter.BLUR)
im_blur.save(r'..\res\flower_blur.jpg')
im_contour = im.filter(ImageFilter.CONTOUR)
im_contour.save(r'..\res\flower_contour.jpg')
im_edges = im.filter(ImageFilter.FIND_EDGES)
im_edges.save(r'..\res\flower_edges.jpg')

# 6. 绘图
# ------------------------------

im = Image.new("RGB", (800, 300), color=(32,64,128))
draw = ImageDraw.Draw(im)
draw.line((0, 200, 800, 200), width=2, fill=(255,255,255)) 
draw.arc([20,20,180,180], 0, 270, fill=(0,255,255)) 
draw.arc([200,40,360,160], 0, 360, fill=(0,255,255)) 
draw.pieslice([380,20,540,180], 30, 330, fill='red', outline='white')
draw.ellipse ([560,20,780,180], fill='yellow', outline='white')
draw.point([660,100,670,100,680,100], fill='red')
draw.rectangle([100,220,700,280], fill=(64,192,192), outline='white') 
font = ImageFont.truetype("simfang.ttf", 32)
draw.text([130,230], "人生苦短，我用Python", font=font, fill='white') 
im.show()

# 7. 截屏
# ------------------------------

im = ImageGrab.grab((1200,600,1920,1080)) # 截取720x480大小的屏幕区域
im.show()
im = ImageGrab.grab() # 截取整个屏幕
im.show()
