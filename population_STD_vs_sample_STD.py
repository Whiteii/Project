from pickle import APPEND
from socketserver import DatagramRequestHandler
import std 
import random 
import math 
import matplotlib as plt 

#Name: Liang Zhang 
#Email Address: Lianghui732@gmail.com
# generate 1000 random data. This represent as a population variance 
# Also, download the std.py and import into here. 



population_random_data = []
for i in range(20000):
    random_data = random.randint(1,1000)
    population_random_data.append(random_data) 

print('population_random_data:',population_random_data)

data = population_random_data 
population_variance = std.calculate_population_variance(data,accumualted_variance= 0)
print('true population_variance:',population_variance)
population_standard_deviation = math.sqrt(population_variance)
print('true population_standard_deviation:',population_standard_deviation)  
# Treat This The True Value Of Standard Deviation And Variance
###################################################################################################################################################################################################################################################################################################################  


#randomly select sample of data from population_random_data 

for i in range(10,5050,10):
    random_sample_data = std.sample_of_data(population_random_data,i)
    #print('random_sample_data:',random_sample_data)
    # using population variance formula to calculate 
 
    population_variance_from_sample_data = std.calculate_population_variance(random_sample_data,accumualted_variance = 0) 
    print('population_variance_from_sample_data:', population_variance_from_sample_data,'# of sample:',len(random_sample_data)) 
       
    # using sample_variance_from_sample_data formula to calculate 
    sample_variance_from_sample_data = std.calculate_sample_variance(random_sample_data, accumualted_variance= 0)   
    print('sample_variance_from_sample_data:',sample_variance_from_sample_data,'# of sample:',len(random_sample_data))








 



    
