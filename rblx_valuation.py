from genericpath import sameopenfile
import finance
import mystat
import numpy as np
import statistics 
import matplotlib.pyplot as plt
from scipy.stats import norm 

#https://iopscience.iop.org/article/10.1088/1742-6596/1377/1/012016/pdf
# Calculating WACC 
################################################################################################################################################################################
#https://www.spglobal.com/marketintelligence/en/news-insights/latest-news-headlines/roblox-places-1b-of-senior-notes-at-par-to-yield-3-875-terms-67270896
# https://www.researchgate.net/figure/Estimated-default-spreads-by-credit-rating_tbl2_288227112


# Risk Free Rate we use is the 10-year treasury bond 
#1) YTM Method(Can't apply)
#2) taking the interest expense/Book Value of Debt 
#3) --> Debt Rating approach <-- Using this
#4) Synethetic Rating Approach 
#5) Interest on Debt Approach 






#list is the stock_market

#https://www.spglobal.com/marketintelligence/en/news-insights/latest-news-headlines/roblox-places-1b-of-senior-notes-at-par-to-yield-3-875-terms-67270896

################################################################################################################################################################################
# Converting string of list into float of list using note files 

note_files = open('%price_change.txt','r')
x = note_files.read()
b = x.split('\n')
a = b

daily_price_change = []
for element in a:
    daily_price_change.append(float(element))

rblx_total_equity = 22686048086 
rblx_total_debt = 988345
rblx_covariance = 0.11

Ratings = 'BB'
US_YEAR_Treasury = 3.253
rblx_cost_of_debt = finance.Debt_Rating_approach('BB',3.253)
rblx_cost_of_equity  = finance.CAPM(3.253,0.11, daily_price_change,11.89)


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

#1) ----> check cost_of_debt <-----   
print('cost_of_debt:',rblx_cost_of_debt) #pass

#2) ----> check cost_of_equity <----  

print('cost_of_equity',rblx_cost_of_equity) #pass

#4)----> check WACC calculation < ---- 
print('WACC:',finance.WACC(rblx_total_equity,rblx_total_debt,rblx_cost_of_equity,rblx_cost_of_debt,0.02))







