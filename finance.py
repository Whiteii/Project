from statistics import covariance
import std 
import math
import numpy as np 

def CAPM(risk_free_rate,covariance,list,market_return): 
    expected_return_of_security = risk_free_rate + std.beta(covariance,list) * (market_return - risk_free_rate) 
    return expected_return_of_security 

#pass test 
capm = CAPM(0.01,0.01094,[0.08,0.10,0.13,0.11,-0.03,-0.05],0.0783) 