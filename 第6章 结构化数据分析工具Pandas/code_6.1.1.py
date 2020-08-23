# -*- encoding: utf-8 -*-

"""
6.1.1 安装和使用
"""

import pandas as pd

idx = ['2020','2019','2018']
colname = ['北京','广州','上海','杭州']
data = [
    [35200.00, 30500.00,31800.00,26300.00],
    [35500.00,31300.00,32200.00,28100.00],
    [34900.00,29600.00,30100.00,24700.00]
]

df = pd.DataFrame(data, columns=colname, index=idx)
print(df)
