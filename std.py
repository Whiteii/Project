from cgitb import reset
from lib2to3.pytree import convert
from random import sample
from re import A
from statistics import variance
import numpy as np
import math
import random



# this is a module I'm currently working on and updating. 


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



















    