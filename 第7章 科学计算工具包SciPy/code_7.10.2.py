# -*- encoding: utf-8 -*-

"""
7.10.2 三维旋转
"""

import numpy as np
from scipy.spatial.transform import Rotation as R
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

# 生成球面网格
lats, lons = np.mgrid[-0.5*np.pi:0.5*np.pi:19j, 0:2*np.pi:37j]
z = np.sin(lats) # 网格点的z坐标
x = np.cos(lats)*np.cos(lons) + 1 # 网格点的x坐标
y = np.cos(lats)*np.sin(lons) # 网格点的z坐标
v = np.dstack((x,y,z)) # 每个点的xyz坐标

# 先绕z轴旋转45°，再绕x轴旋转-30°，最后绕y轴旋转90°
r = R.from_euler('zxy', [45, -30, 90], degrees=True) # 生成旋转实例
v = r.apply(v.reshape((-1, 3))) # 变成二维数组，对球面上每一个点实施旋转
v = v.reshape((*z.shape, 3)) # 恢复成三维数组
o = r.apply(np.array([1,0,0])) 
print('旋转后的球心位置：', o)

ax = plt.subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap=plt.cm.hsv, alpha=0.8)
ax.plot_surface(v[:,:,0], v[:,:,1], v[:,:,2], cmap=plt.cm.hsv, alpha=0.8)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
