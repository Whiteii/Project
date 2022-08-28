import finance
import std as stat 
import numpy as np




#stat.find_robust_central_tendency([0.90,0.84,0.79,0.81,0.60,0.78,0.58])
#stat.find_median([0.90,0.84,0.79,0.81,0.60,0.78,0.58])





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
print('cost_of_equity_beta_is_1:',cost_of_equity_beta_is_1)