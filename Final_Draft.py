#>-----< Final Draft 
import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns
import datetime as dt 


ticker = 'RBLX'
df = pdr.DataReader(ticker, data_source='yahoo', start='2021-3-1')['Close']

daily_percent_change = df.pct_change() 
daily_percent_change.hist()





# terms we need for monte_carlo simulation of brownian motion 
u = daily_percent_change.mean()
standard_deviation = daily_percent_change.std()
variance = np.power(standard_deviation,2)
drift = u - (1/2 * variance)

z = norm.ppf(np.random.rand(50,10000))
#print(z)

daily_returns = np.exp(drift + standard_deviation * z)
print(daily_returns)

