import mystat
import random 
import math 
import matplotlib.pyplot as plt
import numpy as np


#Name: Liang Zhang 
#Email Address: Lianghui732@gmail.com
# generate 1000 random data. This represent as a population variance 
# Also, download the std.py and import into here. 


#The main reason I'm doing this is to collect sample data. Using the sample variance formula is more effective than the population variance formula. 


population_random_data = []


for i in range(80000):
    random_data = np.random.randint(1,20)
    population_random_data.append(random_data) 

print('population_random_data:',population_random_data)
data = population_random_data 
population_variance = mystat.calculate_population_variance(data,accumualted_variance= 0)
print('true population_variance:',population_variance)
population_standard_deviation = math.sqrt(population_variance)
print('true population_standard_deviation:',population_standard_deviation)  
# Treat This The True Value Of Standard Deviation And Variance
###################################################################################################################################################################################################################################################################################################################  



b = str(population_variance)

#randomly select sample of data from population_random_data 

list = [np.random.randint(1,20)]

plt.figure(figsize=(20,8), dpi = 100) 
for i in range(1,200,1):
    random_sample_data = np.random.randint(1,20)
    list.append(random_sample_data)
    # using population variance formula to calculate 
    plt.figure(1)
    
    
    
    #population_variance_from_sample_data
    population_variance_from_sample_data = mystat.calculate_population_variance(list,accumualted_variance = 0)  
   # print('population_variance_from_sample_data:',population_variance_from_sample_data)  
    #plt.annotate(b + 'real variance',[0,population_variance],fontsize = 10, c = 'black')
   # plt.axhline(y = population_variance, c='darkblue',linewidth=2,alpha=0.5) 
   # plt.pause(0.10)
   # plt.plot(len(list),population_variance_from_sample_data, color = 'red', alpha = .75, marker = 'o', markersize = 5)  

    # sample_variance_from_sample_data
    plt.figure(1)  
    plt.axhline(y = population_variance, c='darkblue',linewidth=2,alpha=0.5) 
    #sample_variance_from_sample_data = std.calculate_sample_variance(list,accumualted_variance=0)
   # print('sample_variance_from_sample_data:',sample_variance_from_sample_data)
    #plt.plot(len(list),sample_variance_from_sample_data,color = 'black', alpha = .75,marker = 'o', markersize = 5)
 
    # look at these data and see how far are they away from the true variance.  
      
      
#plt.show()  













 



    
