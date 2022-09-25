import sympy as smp #symbolic mathematics
import numpy as np 
import scipy as sp 
from sympy import diff, symbols, factorial, exp, pretty_print
import matplotlib.pyplot as plt 
from scipy.misc import derivative  
import math  
from sympy.plotting import plot  



x, c1 , c2 ,c3, c4 = smp.symbols('x c1 c2 c3 c4', real = True) 
# More visual understanding of taylor series click here ---> https://www.desmos.com/calculator/3xohtl4swp
# Enter the function that you want to approximate. 
# ---> Enter Your Function Like This Then Run The Code <--- 
def taylor_series_expansion(func):  
    x = smp.symbols('x', real = True) 
    point = int(input("Point To Approximate")) 
    n = int(input("Nth Degree Polynomial ")) 
    results = 0  

    for i in range(0,n):  
        taylor_polynomials = diff(func,x,i).subs(x,point) * (x - point) ** i / factorial(i)
        print(taylor_polynomials) 
        results = taylor_polynomials + results
        #p1 = plot(results, line_color = 'red')   
            
    return results  

#expand_cos_x = taylor_series_expansion(smp.cos(x),0) 
#pretty_print(expand_cos_x) 

expand_e_to_the_x = taylor_series_expansion(exp(1)**x)
pretty_print(expand_e_to_the_x)  

#p1 = plot(expand_e_to_the_x, line_color = 'red') 
#p2 = plot(exp(1)**x,line_color = 'blue') 
#p1.extend(p2)

plot.show()



#>--- Lagrange Error Bound <---

    
        

    
    
    
    
    
      
        
    
 
 




