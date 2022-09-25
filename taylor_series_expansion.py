import sympy as smp 
import numpy as np 
import scipy as sp 
import matplotlib.pyplot as plt 
from scipy.misc import derivative  
import math 


x = smp.symbols('x', real = True) 
# Enter the function that you want to approximate. 
# ---> Enter Your Function Like This Then Run The Code <--- 
def taylor_series_expansion(f):  
    #x = smp.symbols('x', real = True) 
    point = int(input("Point To Approximate")) 
    n = int(input("# Of Derivative")) 
    taylor_series = 0  
    for i in range(0,n + 1 ):  
        dfn_dxn = smp.diff(f,x,i) 
        sub = dfn_dxn.subs([(x,point)]) 
        denom = 1/math.factorial(i)
        coeffient = (sub * denom)                       
        terms = coeffient * (x - point) ** i 
        taylor_series = terms + taylor_series   
    return taylor_series
        
expand_cos_x = taylor_series_expansion(smp.cos(x))
print(expand_cos_x)  





    
        

    
    
    
    
    
      
        
    
 
 




