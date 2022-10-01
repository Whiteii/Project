

import math 
import numpy as np 



#I'm work on this soon 

c1 = float(input('c1'))
c2 = float(input('c2')) 
c3 = float(input('c3'))
b = float(input('b'))
t1 = float(input('t1')) 
t2 = float(input('t2')) 
t3 = float(input('t3'))
err = float(input("Error Tolerance"))

    
def f(x):    
    f_of_x = c1 * np.power(math.exp(1),(-x * t1)) + c2 * np.power(math.exp(1),(-x * t2)) + c3 * np.power(math.exp(1),(-x * t3)) - b
    #print(f_of_x)
    return f_of_x 

def df(x):       
    dy_dx_of_fx = -t1 * c1 * np.power(math.exp(1),(-x * t1)) - t2 * c2 * np.power(math.exp(1),(-x * t2)) - t3 * c3 * np.power(math.exp(1),(-x * t3))
    #print(dy_dx_of_fx)
    return dy_dx_of_fx
    

def newton(x, err ):
    for i in range(1,101): 
        f(x)
        df(x)
        xn = x - f(x)/df(x) 
        if abs(xn) < err: 
            print(x)
            break
        x = xn
    return x
    
          
a = newton(0.10,err)   
print(a)     

