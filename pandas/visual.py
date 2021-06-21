import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.close("all")

ts = pd.DataFrame(np.random.randn(1000, 4), index=pd.date_range("1/1/2000", periods=1000), columns=list('abcd'))
ts = ts.cumsum()

ts.plot()

plt.show()

