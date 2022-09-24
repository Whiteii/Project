from ast import Num
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



n = 9 # taking the derivative to N
c = 0 # Point To Approximate 




for i in range(0,n + 1 ):
    dfn_dxn = smp.diff(f,x,i) 
    sub = dfn_dxn.subs([(x,2)]) 
    denom = round(math.factorial(i))
    coeffient = sub/denom
    print(coeffient)
        
        
    
    
    
    
    
    
      
        
    
 
 




