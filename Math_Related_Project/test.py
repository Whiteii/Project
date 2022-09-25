import sympy as smp 
import numpy as np 
import scipy as sp 
import matplotlib.pyplot as plt 
from scipy.misc import derivative  
import math  
from sympy import diff, symbols, factorial, exp, pretty_print



x, c1 , c2 ,c3, c4 = smp.symbols('x c1 c2 c3 c4', real = True) 


def taylor_series_expansion(func):  
    x = smp.symbols('x', real = True) 
    point = int(input("Point To Approximate")) 
    n = int(input("Nth Degree Polynomial ")) 
    results = 0  
    for i in range(0,n):  
        taylor_polynomials = diff(func,x,i).subs(x,point) * (x - point) ** i / factorial(i)
        print(taylor_polynomials) 
        results = taylor_polynomials + results  
    return results   

expand_e_to_the_x = taylor_series_expansion(exp(1)**x) 

from sympy.plotting import plot  
plot(expand_e_to_the_x, line_color='red')

