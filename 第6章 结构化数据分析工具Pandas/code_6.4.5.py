# -*- encoding: utf-8 -*-

"""
6.4.5 日期时间索引对象
"""

import pandas as pd

print(pd.DatetimeIndex(['2020-03-10', '2020-03-11', '2020-03-12']))
print(pd.DatetimeIndex(pd.Index(['2020-03-10', '2020-03-11', '2020-03-12'])))

idx = pd.Index(['2020-03-10', '2020-03-11', '2020-03-12'])
sdt = pd.Series(['2020-03-10', '2020-03-11', '2020-03-12'])

print(idx)
print(sdt)
print(pd.DatetimeIndex(idx))
print(pd.DatetimeIndex(sdt))

print(pd.to_datetime(['2020-03-10', '2020-03-11', '2020-03-12', '2020-03-13']))
print(pd.to_datetime(idx))
print(pd.to_datetime(sdt))

print(pd.date_range(start='2020-05-12', end='2020-05-18'))
print(pd.date_range(start='2020-05-12 08:00:00', periods=6, freq='3H'))
print(pd.date_range(start='08:00:00', end='9:00:00', freq='15T'))
