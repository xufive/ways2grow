# -*- encoding: utf-8 -*-

"""
6.5.1 统计扩展模块Statsmodels
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.datasets.longley import load_pandas

df = load_pandas().data
print(df)

y = load_pandas().endog
X = load_pandas().exog
X = sm.add_constant(X)
ols_model = sm.OLS(y,X).fit()
print(ols_model.summary())
