import finance
import mystat
import numpy as np
import statistics 
import matplotlib.pyplot as plt
from scipy.stats import norm




https://iopscience.iop.org/article/10.1088/1742-6596/1377/1/012016/pdf

#risk free rate is 0.02 
#Market Risk Return : 0.09 
#Beta : dafault is 1 
#Ticker: RBLX Monthly Return is [0.07,0.14,0.23,-0.04,-0.16,0.6,-0.8,0.11,0.25]
cost_of_equity = finance.CAPM(0.02,0.011,[0.07,0.14,0.23,-0.04,-0.16,0.6,-0.8,0.11,0.25],0.09)
cost_of_equity_beta_is_1 = finance.CAPM_BETA1(0.02,0.09)


#Convert daily price change from list of string to list of float 
note_files = open('%price_change.txt','r')
x = note_files.read()
b = x.split('\n')
a = b

daily_price_change = []
for element in a:
    daily_price_change.append(float(element))
    

################################################################################################################################################################################

mystat.find_robust_central_tendency(daily_price_change)

median = mystat.find_median(daily_price_change)
print('median',median)

price_change_mean = statistics.mean(daily_price_change) 
print('price_change_mean',price_change_mean)

population_variance = mystat.calculate_population_variance(daily_price_change)
standard_deviation_samp = np.sqrt(population_variance)
print('standard_DEVIATION:',standard_deviation_samp)  


################################################################################################################################################################################
#Gaussian distribution also known as the normal distribution 


#https://www.desmos.com/calculator/pyviauerg0
probablity = mystat.probablity_density_function(standard_deviation_samp,median,-standard_deviation_samp,standard_deviation_samp)
print(probablity)
domain = np.arange(-4, 5, 1)
plt.plot(domain, norm.pdf(domain,0,standard_deviation_samp))
plt.show()
