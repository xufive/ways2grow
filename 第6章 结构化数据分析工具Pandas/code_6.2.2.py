# -*- encoding: utf-8 -*-

"""
6.2.2 带标签的一维同构数组Series 
"""

import pandas as pd

print(pd.Series([0,1,2])) # 用列表生成Series，使用默认索引
print(pd.Series(['a','b','c'])) # 用列表生成Series，使用默认索引
print(pd.Series([0,1,2], index=['a','b','c'])) # 用列表生成Series
print(pd.Series(range(3), index=list('abc'))) # 用迭代对象生成Series
print(pd.Series({'a':1,'b':2,'c':3})) # 用字典生成Series，使用字典的键做索引
print(pd.Series({'a':1,'b':2,'c':3}, index=list('abxy'))) # 指定索引

s = pd.Series({'a':1,'b':2,'c':3})
print(s.dtype) # Series对象的数据类型是最重要的三个属性之一
print(s.values) # Series对象的数组是最重要的三个属性之二
print(s.index) # Series对象的索引是最重要的三个属性之三
