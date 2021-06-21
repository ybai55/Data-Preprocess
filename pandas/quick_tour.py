import numpy as np
import pandas as pd


s = pd.Series([1, 3, 5, np.nan, 7])

dates = pd.date_range("20130101", periods=6)

print(s)
