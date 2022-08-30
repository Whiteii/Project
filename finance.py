from statistics import covariance
from typing import List
import mystat
import math
import numpy as np 

def CAPM(risk_free_rate,covariance,list,market_return): 
    expected_return_of_security = risk_free_rate + mystat.beta(covariance,list) * (market_return - risk_free_rate) 
    return expected_return_of_security 


def CAPM_BETA1(risk_free_rate,market_return, beta = 1): 
    expected_return_of_security = risk_free_rate + beta * (market_return - risk_free_rate) 
    return expected_return_of_security



#this can be used for scholastic process and scholastic calculus  
#adding a risk-free-rate components 

def WACC(Equity,Debt,covariance,list,cost_Of_debt,tax_rate):
    capital_structure_of_the_firm = Equity + Debt
    Weighted_Equity = Equity/capital_structure_of_the_firm 
    Weighted_Debt = Debt/capital_structure_of_the_firm
    Wacc = Weighted_Equity * CAPM(covariance,list) + Weighted_Debt * cost_Of_debt * (1 - tax_rate)
    return  Wacc 

#rblx 
#CHECK_CALCULATION  
list = [1,2,3,4,5,6,7,8]
mystat.find_median(list)