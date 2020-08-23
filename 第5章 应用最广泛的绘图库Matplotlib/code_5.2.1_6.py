# -*- encoding: utf-8 -*-

"""
5.2.6 饼图
"""

import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong'] # 设置字体以便正确显示汉字
plt.rcParams['axes.unicode_minus'] = False # 正确显示连字符

x = np.array([10, 10, 5, 70, 2, 10])
labels = ['娱乐', '育儿', '饮食', '房贷', '交通', '其他']
explode = (0, 0, 0, 0.1, 0 ,0)

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.pie(x, explode=explode, labels=labels, autopct='%1.1f%%', startangle=150)
plt.show()
