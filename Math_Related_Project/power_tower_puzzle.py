import math 
import numpy 


#This program is inspire by 3blue1blue 
#>---- https://www.youtube.com/watch?v=elQVZLLiod4&t=1482s ----< 
# tetration 
#     ^2  
#   ^2
# ^2
#2^



#Answer is should 65,536 with 4 ilteration.  
results = 0 
func_x = 0  
func_sqrt_x_pow_2 = 1
n = 0  
'''for n in range(0,6): 
    a_sub_next = 2 ** a_sub_next
    #print('n:',n,a_sub_next)'''
         
# Using this tools kit. 
# Find the solution for sqrt(2)^x = x  
for n in range(0,10):  
   print('ilteration',n,func_x,func_sqrt_x_pow_2) 
   func_x = math.pow(2,1/2) ** func_x   
   func_sqrt_x_pow_2 = math.pow(2,1/2) ** func_sqrt_x_pow_2  
   