
import sympy as smp 
import numpy as np 
import scipy as sp 
import matplotlib.pyplot as plt 
from scipy.misc import derivative  
import math




x = smp.symbols('x', real = True) 
t = smp.symbols('t', real = True)

# Enter the function that you want to approximate. 
# ---> Enter Your Function Like This Then Run The Code <--- 
f = smp.cos(x)  



n = 15 # taking the derivative to N
c = 0 # Point To Approximate 

sums = 0  
for i in range(0,n + 1 ): 
    x = smp.symbols('x', real = True) 
    dfn_dxn = smp.diff(f,x,i) 
    sub = dfn_dxn.subs([(x,0)]) 
    denom = 1/math.factorial(i)
    coeffient = (sub * denom)
    terms = round((coeffient),20) * (x-0) ** i 
    print(terms)
    
        
        
    
    
    
    
    
    
      
        
    
 
 




