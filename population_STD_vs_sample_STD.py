from pickle import APPEND
from socketserver import DatagramRequestHandler
import std 
import random 
import math 
import matplotlib.pyplot as plt


#Name: Liang Zhang 
#Email Address: Lianghui732@gmail.com
# generate 1000 random data. This represent as a population variance 



plt.figure(figsize=(20,8), dpi = 100) 
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



b = str(population_variance)

#randomly select sample of data from population_random_data 

for i in range(1,5050,1):
    random_sample_data = std.sample_of_data(population_random_data,i)
    #print('random_sample_data:',random_sample_data)
    # using population variance formula to calculate 
    plt.figure(1)
    population_variance_from_sample_data = std.calculate_population_variance(random_sample_data,accumualted_variance = 0)   
    plt.pause(0.1)    
    plt.annotate(b,[0,population_variance],fontsize = 10, c = 'black')
    plt.axhline(y = population_variance, c='darkblue',linewidth=2,alpha=0.5)
    plt.plot(len(random_sample_data),population_variance_from_sample_data, color = 'red', alpha = .75, lw = 4, ls = '-.', marker = 'o', markersize = 5)  
    print('population_variance_from_sample_data:', population_variance_from_sample_data,'# of sample:',len(random_sample_data)) 
       
    # using sample_variance_from_sample_data formula to calculate 
    #plt.figure(2) 
    #sample_variance_from_sample_data = std.calculate_sample_variance(random_sample_data, accumualted_variance = 0) 
    #plt.pause(0.1)   
    #plt.subplot(1,2,1)  
    #plt.scatter(sample_variance_from_sample_data,len(random_sample_data), c= 'Black' , s=50)   
    #print('sample_variance_from_sample_data:',sample_variance_from_sample_data,'# of sample:',len(random_sample_data))


plt.show()


 



    
