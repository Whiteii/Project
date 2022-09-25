
import sympy as smp 
import numpy as np 
import scipy as sp 
import matplotlib.pyplot as plt 
from scipy.misc import derivative  
import math




x = smp.symbols('x', real = True) 


# Enter the function that you want to approximate. 
# ---> Enter Your Function Like This Then Run The Code <--- 




#n # taking the derivative to N
#c # Point To Approximate 

sums = 0  
def taylor_series_expansion(x = smp.symbols('x', real = True),f =  smp.sin(x),n = int(input("# Of Derivative"))):
    for i in range(0,n + 1 ): 
        x = smp.symbols('x', real = True) 
        dfn_dxn = smp.diff(f,x,i) 
        sub = dfn_dxn.subs([(x,2)]) 
        denom = 1/math.factorial(i)
        coeffient = (sub * denom)
        terms = (coeffient) * (x-2) ** i 
        print(terms)
        
        
taylor_series_expansion()
    
        
        
    
    
    
    
    
    
      
        
    
 
 




