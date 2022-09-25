import sympy as smp 
import numpy as np 
import scipy as sp 
from sympy import diff, symbols, factorial, exp, pretty_print
import matplotlib.pyplot as plt 
from scipy.misc import derivative  
import math 




x, c1 , c2 ,c3, c4 = smp.symbols('x c1 c2 c3 c4', real = True) 
# More visual understanding of taylor series click here ---> https://www.desmos.com/calculator/3xohtl4swp

# Enter the function that you want to approximate. 
# ---> Enter Your Function Like This Then Run The Code <--- 
"""def taylor_series_expansion(f_x):  
    x = smp.symbols('x', real = True) 
    point = int(input("Point To Approximate")) 
    n = int(input("# Of Derivative")) 
    taylor_series = 0  
    for i in range(0,n + 1 ):  
        dfn_dxn = smp.diff(f_x,x,i) 
        sub = dfn_dxn.subs([(x,point)]) 
        denom = 1/math.factorial(i)
        coeffient = (sub * denom)                       
        terms = coeffient * (x - point) ** i 
        taylor_series = terms + taylor_series   
    return taylor_series
        
expand_cos_x = taylor_series_expansion(smp.cos(x))
print(expand_cos_x) """  




x0 = 0
n = 10

func = smp.cos(x)
results = func.subs([(c1,5)]) 
apply_diff_to_function = diff(results,x,1) 
#pretty_print(apply_diff_to_function) 
dummy = 0


for i in range(0,n): 
    something = diff(results,x,i).subs(x,0) * (x - x0) ** i / factorial(i)
    dummy = something + dummy
    print(dummy)
    pretty_print(dummy)
    
    


    














#-0.00833333333333333*(x - 5)**5*sin(5) + 0.0416666666666667*(x - 5)**4*cos(5) + 0.166666666666667*(x - 5)**3*sin(5) - 0.5*(x - 5)**2*cos(5) - 1.0*(x - 5)*sin(5) + 1.0*cos(5)
#Need these in fraction form


#>--- Lagrange Error Bound <---

    
        

    
    
    
    
    
      
        
    
 
 




