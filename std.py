from cgi import test
from cgitb import reset
from cmath import sqrt
from lib2to3.pytree import convert
from random import sample
from re import A, I
from statistics import mean, median, variance
import numpy as np
import math
import random 
import statistics

http://www.z-table.com/

# this is a module I'm currently working on and updating. 

#sorting the list in ascending order
def sorting_list(list): 
    for i in range(0,len(list)):
        for j in range(i + 1,len(list)):
            if list[j] < list[i] : # so one scenario is when i = 1 and j = 0. That where b < c. 
                  temp = list[i] #5
                  list[i] = list[j] #4
                  list[j] = temp # 5
    return list 
        
#calculate median
def find_median(list): 
    if len(list)%2 == 0:
        i = int(len(list)/2)
        median =(list[i-1] + list[i])/2
        print('median:',median) 
        
    elif len(list)%2 == 1:
        i = int((len(list)-1)/2)
        median = (list[i])
        print('median:',median)
    return median  
      
# convert a string into a list
def Convert(string):
    li = list(string.split(','))
    return li
 
# calculate population variance
def calculate_population_variance(str1, accumualted_variance = 0):  
    res = str1
    population_mean = sum(res)/len(res)
    for i in range(0,len(res)):
        population_variance = math.pow(res[i] - population_mean,2)
        accumualted_variance = (population_variance + accumualted_variance)
        variance = accumualted_variance/len(res)
        #print(variance)
        #print(len(str1))
    return variance



# calculate mean_absolute deviation 
def mean_absolute_deviation(str1, mad = 0):
    res = str1 
    sample_mean = sum(res)/len(res)
    for i in range(0,len(res)):
        absolute_deviation = np.abs(str1[i] - sample_mean)/len(res)
        mad += absolute_deviation
    return mad
        

# calculate sample variance 
def calculate_sample_variance(str1,accumualted_variance = 0):  
    res = str1 
    sample_mean = sum(res)/len(res)
    for i in range(0,len(res)):
        sample_variance = math.pow(res[i] - sample_mean,2)
        accumualted_variance = (sample_variance + accumualted_variance)
        variance = accumualted_variance/(len(res) - 1) # the problem here if len(res) is one. This function doesn't work. 
        #print(len(res))
    return variance    


#randomly selected a data from a list and store into a new list
def sample_of_data(list,amount_of_data):    
    sample_collection = []
    for i in range(0,amount_of_data):
        random_data = random.randint(1,1000)
        sample_data = list[random_data]
        sample_collection.append(sample_data)
    return sample_collection




#IQR 
num_list = [11,17,21,18,2,3]
# check if the even or odd.


# mean get affect by outlier 
# Median doesn't get affect by outlier
# Mode somewhat gets affect by outlier
# To find a robust_central_tency. The skewness of the distribution must be 0. this way it's not right skewed or left skewed that could be impacted by outlier.

 
def find_robust_central_tendency(list): 
    new_list = sorting_list(list)
    print(new_list)
    arithmetic_mean = sum(new_list)/len(new_list)
    #print('arithmetic_mean:',arithmetic_mean)
    
    if len(new_list)%2 == 0:
        i = int(len(new_list)/2)
        median =(new_list[i-1] + list[i])/2
        #print('median:',median)
    elif len(list)%2 == 1:
        i = int((len(new_list)-1)/2)
        median = (new_list[i])
        print('median:',median) 
        #Case 1
    if arithmetic_mean > median:
        print('Population_Standard Deviation: ',math.sqrt(calculate_sample_variance(list)))
        print('Pearson Mode Skness:', 3 * (arithmetic_mean - median)/math.sqrt(calculate_sample_variance(list)))
        print('distribution is postively skewed(Right-Skewed))')       
        #Case 2    
    elif arithmetic_mean < median: 
        print(arithmetic_mean,median)
        print('Population_Standard Deviation: ',math.sqrt(calculate_sample_variance(list)))
        print('Pearson Mode Skness:', 3 * (arithmetic_mean - median)/math.sqrt(calculate_sample_variance(list)))
        print('distribution is negatively skewed(Left-skewed))')

#find_robust_central_tendency(num_list)


#calculate z-scores 
def find_z_scores(central_tendency,standard_deviation,z_scores):
    one_std = central_tendency + standard_deviation
    delta_one_std = np.abs(central_tendency - one_std)
    #print('z_scores:',(z_scores - central_tendency)/delta_one_std) 
    
find_z_scores(81,6.3,65) 


#WIP
def beta(covariance, list):
    variance = calculate_sample_variance(list)
    #print('variance:',variance)
    #print('covariance:',covariance)
    beta = covariance/variance
    #print('beta:',beta)
    return beta       


def lower_quartile(list):
    Q1_list = []
    new_list = sorting_list(list)
    if len(new_list)%2 == 0:
        for i in range(0,int(len(new_list)/2)): 
            test = new_list[i]
            Q1_list.append(test)
            if i == ((int(len(new_list))/2) - 1):
                #print(Q1_list)
                Q1 = find_median(Q1_list)          
    return Q1 



def upper_quartile(list):
    Q3_list = []
    new_list = sorting_list(list) 
    for j in range(int(len(new_list)/2), int(len(new_list))): 
        test2 = new_list[j] #5,6,7,8 in ilteration fashion 
        Q3_list.append(test2)
        print(j)
        if j == (int(len(new_list)) - 1):
            #print(Q3_list) # this should print [5,6,7,8]
            Q3 = find_median(Q3_list)
    return Q3 

# Interquartile range
def IQR(list): 
    Q3 = upper_quartile(list)
    Q1 = lower_quartile(list)
    IQR = Q3 - Q1
    print('IQR:',IQR)
    return IQR 



# Probablity density calculation. Finding the area between lower and upper little. 
def p_(standard_deviation,central_tendency,lower_limit,upper_limit,area =0,x_position = 0):
    accumulate_area = 0

    while x_position < upper_limit:   
        dx = (upper_limit - lower_limit)/1000        
        x_position = x_position + dx
        first_expression = 1/np.sqrt(2 * math.pi * standard_deviation ** 2)
        z_score = -1/2 * ((x_position - central_tendency)/standard_deviation) ** 2
        second_expression = np.power(np.exp(1),z_score)
        height = first_expression * second_expression 
        area = height * dx
        accumulate_area = area + accumulate_area 
    return accumulate_area

a = p_(1,0,0,1)
print('area',a)
        

        



    
    

    
    








    
