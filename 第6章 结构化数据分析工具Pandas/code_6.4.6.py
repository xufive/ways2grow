# -*- encoding: utf-8 -*-

"""
6.4.6 数据可视化
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

idx = pd.date_range(start='08:00:00',end='9:00:00',freq='T') # 间隔1分钟
y = np.sin(np.linspace(0,2*np.pi,61)) # 0~2π之间61个点的正弦值
s = pd.Series(y, index=idx) # 创建Series对象，索引是时间序列
s.plot() # 绘制折线图
plt.show() # 显示绘图结果

data = np.random.randn(10,4)
idx = pd.date_range('08:00:00', periods=10, freq='H')
df = pd.DataFrame(data, index=idx, columns=list('ABCD'))
df.plot()
plt.show()

df = pd.DataFrame(np.random.rand(10,4),columns=list('ABCD'))
fig = plt.figure( )
ax = fig.add_subplot(131)
df.plot.bar(ax=ax)
ax = fig.add_subplot(132)
df.plot.bar(ax=ax, stacked=True)
ax = fig.add_subplot(133)
df.plot.barh(ax=ax, stacked=True)
plt.show()
