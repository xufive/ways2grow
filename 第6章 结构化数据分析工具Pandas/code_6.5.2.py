# -*- encoding: utf-8 -*-

"""
6.5.2 可视化扩展Seaborn
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fn = r'..\res\fmri.csv'
ds = pd.read_csv(fn)

sns.set(style='darkgrid')
sns.relplot(x='timepoint', y='signal', hue='event', style='event', col='region', kind='line', data=ds)
plt.show()
