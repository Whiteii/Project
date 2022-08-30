
import finance
import std as stat 
import numpy as np
import statistics 
import matplotlib.pyplot as plt
from scipy.stats import norm





#assume
#risk free rate is 0.02 
#Market Risk Return : 0.09 
#Beta : dafault is 1 
#Ticker: Monthly Return is [0.07,0.14,0.23,-0.04,-0.16,0.6,-0.8,0.11,0.25]

#Yield Curve In Python
#We need a prober risk-free-rate, covariance, a list in terms of the % change time-frame(quartly, annually up to you), market return,  
cost_of_equity = finance.CAPM(0.02,0.011,[0.07,0.14,0.23,-0.04,-0.16,0.6,-0.8,0.11,0.25],0.09)
#print('cost_of_equity:', cost_of_equity)

cost_of_equity_beta_is_1 = finance.CAPM_BETA1(0.02,0.09)
#print('cost_of_equity_only_if_beta_=_1',cost_of_equity_beta_is_1) 

#finding robust central tendency 




price_change = open('price_change.txt','r')
x = price_change.read()
b = x.split('\n')
a = b

daily_price_change = []
for element in a:
    daily_price_change.append(float(element))
    
#print(daily_price_change)


stat.find_robust_central_tendency(daily_price_change)
price_change_median = stat.find_median(daily_price_change)
#print('price_median',price_median) 
price_change_mean = statistics.mean(daily_price_change)
#print('price_mean',price_mean)
population_variance = stat.calculate_population_variance(daily_price_change)
#print('population_variance:', population_variance) 
standard_deviation = np.sqrt(population_variance)
#print('standard_DEVIATION:',standard_deviation) 




# Read this link over here https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/ 
#https://www.desmos.com/calculator/pyviauerg0

normal_distribution = stat.probablity_density_function(0.06299598659374768,0,-0.06299598659374768,0.06299598659374768)
#print(normal_distribution)

domain = np.arange(-4, 5, 1)
plt.hist(domain, norm.pdf(domain,0,standard_deviation))
plt.show()

