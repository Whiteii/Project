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


# Geometric Brownian Motion Combining With Monte_Carlo_Simulation  
daily_percent_change = df.pct_change() 

daily_percent_change.hist()

u = daily_percent_change.mean()
standard_deviation = daily_percent_change.std()






