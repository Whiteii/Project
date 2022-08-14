

#https://www.geeksforgeeks.org/python-program-convert-string-list/

from random import sample
from re import A
import numpy
import math


# convert a string into a list
def Convert(string):
    li = list(string.split(","))
    return li
 
# calculate population variance
def calculate_population_variance(accumualted_variance = 0,str1 = str(input("Please Enter The Data Set As A Population"))):  
    list = Convert(str1)
    res = [eval(i) for i in list]   # turn string into a interger list  
    population_mean = sum(res)/len(res)
    for i in range(0,len(res)):
        population_variance = math.pow(res[i] - population_mean,2)
        accumualted_variance = (population_variance + accumualted_variance)
        variance = accumualted_variance/len(res)
        #print(variance)
    return variance


variance = calculate_population_variance()
print('variance:',variance)
#calculate the population standard deviation
population_standard_deviation = math.sqrt(variance)
print('population standard deviation:', population_standard_deviation)   

# calculate sample variance
def calculate_sample_variance(accumualted_variance = 0,str1 = str(input("Please Enter The Data Set As A Sample"))):  
    list = Convert(str1)
    res = [eval(i) for i in list]   # turn string into a interger list  
    sample_mean = sum(res)/len(res)
    for i in range(0,len(res)):
        sample_variance = math.pow(res[i] - sample_mean,2)
        accumualted_variance = (sample_variance + accumualted_variance)
        variance = accumualted_variance/(len(res) - 1)
    return variance   


sample_variance = calculate_sample_variance()   
print('sample variance:', sample_variance)
# calculate the sample standard deviation
sample_standard_deviation = math.sqrt(sample_variance)
print('sample_standard_deviation', sample_standard_deviation)


              
        
    



















# sample standard deviation 