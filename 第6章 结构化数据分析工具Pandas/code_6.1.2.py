# -*- encoding: utf-8 -*-

"""
6.1.2 Pandas的特点
"""

import pandas as pd

data = pd.read_html('http://ditu.92cha.com/dizhen.php')
print(data[0].head())
