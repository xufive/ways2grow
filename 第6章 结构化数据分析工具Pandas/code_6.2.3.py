# -*- encoding: utf-8 -*-

"""
6.2.3 带标签的二维异构表格DataFrame
"""

import pandas as pd
import numpy as np

data = {
    '华东科技': [1.91, 1.90, 1.86, 1.84],
    '长安汽车': [11.27, 11.14, 11.28, 11.71],
    '西藏矿业': [7.89, 7.79, 7.61, 7.50],
    '重庆啤酒': [50.46, 50.17, 50.28, 50.28]
}

print(pd.DataFrame(data))

idx = ['2020-03-10','2020-03-11','2020-03-12','2020-03-13']
print(pd.DataFrame(data, index=idx))

colnames = ['华东科技', '长安汽车', '杭钢股份', '西藏矿业', '重庆啤酒']
print(pd.DataFrame(data, columns=colnames, index=idx))

data = np.array([
    [ 1.91, 11.27,  7.89, 50.46],
    [ 1.9 , 11.14,  7.79, 50.17],
    [ 1.86, 11.28,  7.61, 50.28],
    [ 1.84, 11.71,  7.5 , 50.28]
])

idx = ['2020-03-10','2020-03-11','2020-03-12','2020-03-13']
colnames = ['华东科技', '长安汽车', '西藏矿业', '重庆啤酒']
print(pd.DataFrame(data, columns=colnames, index=idx))

df = pd.DataFrame(data, columns=colnames, index=idx)
print(df.dtypes) # dtypes属性，是由所有列的数据类型组成的Series
print(df.values) # DataFrame的重要属性之一
print(df.index) # DataFrame的重要属性之一
print(df.columns) # DataFrame的重要属性之一
