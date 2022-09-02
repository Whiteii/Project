from statistics import covariance
from typing import List
import mystat 
import math
import numpy as np 






# The cost of equity with a pre-determine covariance. 
def CAPM(risk_free_rate,covariance,price_change_in_list,market_return): 
    expected_return_of_security = risk_free_rate + mystat.beta(covariance,price_change_in_list) * (market_return - risk_free_rate) 
    print('beta',mystat.beta(covariance,price_change_in_list))
    return expected_return_of_security


#essentially the calculation for cost of equity
def CAPM_BETA1(risk_free_rate,market_return, beta = 1): 
    expected_return_of_security = risk_free_rate + beta * (market_return - risk_free_rate) 
    return expected_return_of_security




#three method to calculate for bps = 1/100 

# https://www.researchgate.net/figure/Estimated-default-spreads-by-credit-rating_tbl2_288227112


# Risk Free Rate we use is the 10-year bond 

#1) YTM Method(Can't apply)
#2) taking the interest expense/Book Value of Debt 
#3) Debt Rating approach <-- Using this
#4) Synethetic Rating Approach 
#5) Interest on Debt Approach 




def Debt_Rating_approach(search_for_rating,risk_free_rate):  
    ''' for passing into the paramter for risk_free_rate. Based on general convention we use 10 YRS yield'''
    
    # Using fitch rating 
    rating = ['AAA','AA','A+','A','A-','BBB','BB','B+','B','B-','CCC','CC','C','D']
    #print(len(rating)) 
    bps_in_percent = [0.20,0.50,0.80,1,1.25,1.50,2,2.50,3.25,4.25,5,6,7.50,10]
    #print(bps_in_percent)
    for i in range(0,len(rating)):
        if rating[i] == search_for_rating:
            cost_of_debt = bps_in_percent[i] + risk_free_rate
    return cost_of_debt



#this can be used for scholastic process and scholastic calculus  
#adding a risk-free-rate components 

def WACC(Equity,Debt,cost_of_equity,cost_Of_debt,tax_rate):
    capital_structure_of_the_firm = Equity + Debt
    Weighted_Equity = (Equity/capital_structure_of_the_firm) 
    print(Weighted_Equity) 
    Weighted_Debt = (Debt/capital_structure_of_the_firm)  
    print(Weighted_Debt)
    Wacc = (Weighted_Equity * cost_of_equity) + (Weighted_Debt * cost_Of_debt * (1 - tax_rate))
    return  Wacc 



