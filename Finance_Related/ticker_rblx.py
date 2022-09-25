import finance
import mystat
import numpy as np
import statistics 
import matplotlib.pyplot as plt
from scipy.stats import norm 
import pandas as pd   


#turning a string of list to float of list 
#>------------------------------------------------------------------------------<
note_files = open('%price_change.txt','r')
x = note_files.read()
b = x.split('\n')
a = b
daily_price_change = []
for element in a:
    daily_price_change.append(float(element))
#>------------------------------------------------------------------------------<

#IN THOUSANDS 
df = pd.read_csv('RBLX_Balancesheet.csv')
print(df)
rblx_total_Asset = df.loc[df['Items'] == 'Total Asset', 'Q3 2022'] 
rblx_total_Liabilties = df.loc[df['Items'] == 'Total Liabilties', 'Q3 2022'] 
rblx_total_equity = 22686048086
long_term_debt = df.loc[df['Items'] == 'Long term debt', 'Q3 2022']
print('long_term_debt:',long_term_debt)   
# self-made module for finance. 
wacc = finance.WACC(rblx_total_equity,rblx_cost_of_debt,rblx_cost_of_equity,rblx_cost_of_debt,tax_rate = 0.02)
print('wacc:',wacc)

Ratings = 'BB'
US_YEAR_Treasury_Yield = 3.253
rblx_cost_of_debt = finance.Debt_Rating_approach('BB',3.253)
rblx_cost_of_equity  = finance.CAPM(US_YEAR_Treasury_Yield,0.11,daily_price_change,11)
print(rblx_cost_of_equity)


#>------------------------------------------------------------------------------<

dff = pd.read_csv('%_change_ticker.csv')
print(dff)
population_variance = dff['%change'].var()
std = np.sqrt(population_variance)  
print('std:',std) 
stat = dff.describe()

#>------------------------------------------------------------------------------<

#https://pandas.pydata.org/pandas-docs/dev/getting_started/intro_tutorials/03_subset_data.html


