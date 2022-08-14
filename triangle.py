
from cgi import test
from cgitb import small
import math
from re import A, L, M 

# law of sin 
# law of cos 
 
l = float(input("largest_side_length")) # 5
m =  float(input("middle_side_length")) # 4
s = float(input("smallest_side_length"))  # 3


if (l < m + s) and (m < l + s) and (s < l + m) and (l >= m) and (m >= s) and (l > 0) and (m > 0) and (s > 0):

    #manuipation of law of cos to find the highest_degree => manuipate to find middle degree
    output_for_acos_function = round(math.pow(m,2) + math.pow(s,2) - math.pow(l,2),2)/(2 * m * s) 
    highest_degree = math.acos(output_for_acos_function) * 57.2958  ## In radian   
    print(highest_degree)   
    middle_degree = math.asin((math.sin(math.acos(output_for_acos_function))/l) * m) * 57.2958 
    print(middle_degree) 
    lowest_degree = 180 - highest_degree - middle_degree 
    print(lowest_degree)
else : 
    print("Don't satisfy the triangle inequality, descending order, side lengths entered are not all postive")



 
















