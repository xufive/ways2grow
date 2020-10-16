# -*- encoding: utf-8 -*-

"""
7.4.1 时域-频域的转换
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import fft as spfft # 导入傅里叶变换子模块

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 4*np.pi, 257) # 以256Hz的采样频率采样1秒（0~4π）
s1 = np.sin(x)
s2 = 0.4*np.sin(3*x)
s3 = 0.3*np.sin(5*x)
s = s1 + s2 + s3

plt.plot(x, s1, label='s1-2Hz分量')
plt.plot(x, s2, label='s2-6Hz分量')
plt.plot(x, s3, label='s3-10Hz分量 ')
plt.plot(x, s, label='s–复合信号')
plt.legend()
plt.show()

fd = spfft.fft(s) # fd是对复合信号s进行一维快速傅里叶变换的结果
print(s.shape, fd.shape) # fd是一个和s形状相同的数组
((257,), (257,))
print(fd[:12]) # fd的元素类型是复数（这里只显示了前12个元素）
print(fd[-12:]) # 最后12个元素

fig = plt.figure()
axes_1 = fig.add_subplot(221)
axes_2 = fig.add_subplot(222)
axes_3 = fig.add_subplot(223)
axes_4 = fig.add_subplot(224)
axes_1.set_title('双边频谱图')
axes_1.plot(np.abs(fd)) # 复数的模表示幅度
axes_2.set_title('双边相位图')
axes_2.plot(np.angle(fd)) # 复数的幅角表示相位
axes_3.set_title('单边频谱图')
axes_3.plot(np.abs(fd[:129]/257)) # 只画前一半数据，标准化（除以采样总数）
axes_4.set_title('单边相位图')
axes_4.plot(np.angle(fd[:129]/257))
plt.show()
