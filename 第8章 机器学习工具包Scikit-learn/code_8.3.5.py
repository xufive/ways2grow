# -*- encoding: utf-8 -*-

"""
8.3.5 特征编码
"""

import numpy as np
from sklearn import preprocessing as pp

X = [['male', 'firefox', 'vscode'], 
	['female', 'chrome', 'vim'], 
	['male', 'safari', 'pycharme']]

oenc = pp.OrdinalEncoder().fit(X)
print(oenc.transform(X))

ohenc = pp.OneHotEncoder().fit(X)
print(ohenc.transform(X).toarray())
