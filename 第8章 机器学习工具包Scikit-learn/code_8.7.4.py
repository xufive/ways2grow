# -*- encoding: utf-8 -*-

"""
8.7.4 独立成分分析（ICA）
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import FastICA

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

# 用正弦波和三角波表示两位演讲者的声音s_1和s_2，两个合成信号x_1和x_2表示两台录音设备的记录数据

_x = np.linspace(0, 8*np.pi, 1000)
k1 = np.where(np.int_(0.5*_x/np.pi)%2==0, 1, -1)/np.pi
k2 = np.where(np.int_(_x/np.pi)%2==0, 1, 0)
k3 = np.where(np.int_(_x/np.pi)%2==0, 0, 1)

s1 = np.sin(_x) # 第1位演讲者的声音
s2 = _x%(np.pi)*k1*k2 + (np.pi-_x%(np.pi))*k1*k3 # 第2位演讲者的声音
x1 = 0.4*s1 + 0.5*s2 # 录音1
x2 = 1.2*s1 - 0.3*s2 # 录音2

plt.subplot(121)
plt.plot(_x, s1, label='s1')
plt.plot(_x, s2, label='s2')
plt.legend()
plt.subplot(122)
plt.plot(_x, x1, label='x1')
plt.plot(_x, x2, label='x2')
plt.legend()
plt.show()

# 从合成信号x_1和x_2中分离出s_1和s_2这样的独立音源

X = np.stack((x1,x2), axis=1) # 将两个信号合并成矩阵

fica = FastICA(n_components=2) # 快速独立成分分析类实例化
fica.fit(X)

X_ica = fica.transform(X) # 独立成分分析结果
print(X_ica.shape) # (1000, 2)

plt.plot(_x, X_ica[:,0], label='独立成分1')
plt.plot(_x, X_ica[:,1], label='独立成分2')
plt.legend()
plt.show()
