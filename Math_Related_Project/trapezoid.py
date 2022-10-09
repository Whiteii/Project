import math
import numpy 
 



#link https://www.desmos.com/calculator/hek8crqqj5
# Fastest Solution 

# upper bound 
B = float(input("Enter Upper Bound")) #2
# Lower Bound 
A = float(input("Enter Lower Bound")) #1
# Let N = number of trapzoid 
N = int(input("Number Of N")) #4


W = (B - A)/N   



# solving it with riemann sum notation. 
# this is for cos

i_i = 0 
def x_parameter_for_cos(t = 0):  
    for i_i in range(0, N - 1 ):   
        i_i += 1    
        y = 2 * math.cos(math.pow(i_i * W + A,2)) 
        t = t + y 
    return t   


portion_area_for_cos = x_parameter_for_cos(t=0)
print((W/2) * (math.cos(math.pow(A,2)) + portion_area_for_cos  + math.cos(math.pow(B,2))))  


# this is for sin


i = 0 
def x_parameter_for_sin(t = 0):  
    for i in range(0, N - 1 ):   
        i = i + 1   
        y = 2 * math.sin(math.pow(i * W + A,2)) 
        t = t + y 
    return t   


portion_area_for_sin = x_parameter_for_sin(t=0)
print((W/2) * (math.sin(math.pow(A,2)) + portion_area_for_sin  + math.sin(math.pow(B,2))))    













 
















        
 



































