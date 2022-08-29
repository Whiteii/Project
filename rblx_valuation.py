import finance
import std as stat 
import numpy as np



#assume
#risk free rate is 0.02 
#Market Risk Return : 0.09 
#Beta : dafault is 1 
#Ticker: Monthly Return is [0.07,0.14,0.23,-0.04,-0.16,0.6,-0.8,0.11,0.25]

#Yield Curve In Python
#We need a prober risk-free-rate, covariance, a list in terms of the % change time-frame(quartly, annually up to you), market return,  
cost_of_equity = finance.CAPM(0.02,0.011,[0.07,0.14,0.23,-0.04,-0.16,0.6,-0.8,0.11,0.25],0.09)
print('cost_of_equity:', cost_of_equity)

cost_of_equity_beta_is_1 = finance.CAPM_BETA1(0.02,0.09)
print('cost_of_equity_only_if_beta_=_1',cost_of_equity_beta_is_1) 

#finding robust central tendency 

daily_price_change = [0.002198607
,0.029250383
,0.001776211
,-0.020449114
,-0.009168897
,-0.027881265
,-0.002596106
,0.025656916
,0.015347396
,-0.03427753
,-0.019102823
,-0.015454141
,0.0532159
,-0.055010312
,-0.01269391
,0.422337623
,-0.130204487
,0.030023105
,0.096412543]



stat.find_robust_central_tendency(daily_price_change)
price_median = stat.find_median(daily_price_change)
population_variance = stat.calculate_population_variance(daily_price_change) 
print('population_variance:', population_variance) 
#stat.find_z_scores(price_median, 0.6956387268780222,)

population_standard_deviation = np.sqrt(population_variance)
print('population_standard_DEVIATION:',population_standard_deviation) 

probablity_within_1std = stat.probablity_density_function(population_standard_deviation,price_median,-0.10799591652509857,0.10799591652509857)
print('probablity_within_1st',probablity_within_1std)

probablity_within_2std = stat.probablity_density_function(population_standard_deviation,price_median,-0.10511550633012415,0.10511550633012415)
print('probablity_within_1st',probablity_within_2std)



