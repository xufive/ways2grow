# -*- encoding: utf-8 -*-

"""
5.3.7 文本
"""

from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong'] # 设置字体以便正确显示汉字
plt.rcParams['axes.unicode_minus'] = False # 正确显示连字符

fig = plt.figure()
fig.suptitle('画布标题')

ax = fig.add_axes([0.1, 0.2, 0.8, 0.6])
ax.set_title('子图标题')
ax.set_xlabel('x轴标注文本', fontdict={'fontsize':14})
ax.set_ylabel('y轴标注文本', fontdict={'fontsize':14})
ax.text(3, 8, '边框颜色', style='italic', bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
ax.text(2, 6, r'LaTex: $E=mc^2$', fontsize=15)
ax.text(0.95, 0.01, '坐标内绿色文字', verticalalignment='bottom', horizontalalignment='right', transform=ax.transAxes, color='green', fontsize=15)
ax.plot([2], [1], 'o')
ax.annotate('annotate文字', xy=(2, 1), xytext=(3, 4), arrowprops={'facecolor':'black', 'shrink':0.05})
ax.set_xlim(0,10)
ax.set_ylim(0,10)
plt.show()
