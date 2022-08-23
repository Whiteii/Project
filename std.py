from cgitb import reset
from lib2to3.pytree import convert
from random import sample
from re import A, I
from statistics import median, variance
import numpy as np
import math
import random



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
        


#IQR 
num_list = [35,50,50,50,56,60,60,75,1]
# check if the even or odd.

# If the arithmetic_mean > median => we use central-tendency and IQR 
def robust_central_tendency(list):
    new_list = sorting_list(list)
    print(new_list)
    arithmetic_mean = sum(new_list)/len(new_list)
    print('arithmetic_mean:',arithmetic_mean)
    if len(new_list)%2 == 0:
        i = int(len(new_list)/2)
        median =(new_list[i-1] + list[i])/2
        print('median:',median)
    elif len(list)%2 == 1:
        i = int((len(new_list)-1)/2)
        median = (new_list[i])
        print('median:',median)
        if arithmetic_mean > median:
            print('use median as central-tendency and IQR')
        else: 
            print('use arthmetic mean as central-tendency and standard deviation')

  
robust_central_tendency(num_list)
  
  
  
            
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



















    