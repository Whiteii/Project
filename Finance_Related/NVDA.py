import mystat
import numpy as np
import statistics 
import matplotlib.pyplot as plt
from scipy.stats import norm 
import pandas as pd   
import math 


note_files = open('nvda_price_change.txt','r')  
x = note_files.read()
b = x.split('\n') 
a = b  

#---------------------
nvda_price_change = []
for element in a:
    nvda_price_change.append(float(element))  
mystat.find_robust_central_tendency(nvda_price_change) 
median = mystat.median(nvda_price_change) 
print(median)

#---------------------
df = pd.read_csv('NVDA.csv')
print(df)
close_price = df['%change'] 
describe = close_price.describe()
variance =  close_price.var() 
print('variance:',variance)  
std = math.sqrt(variance) * 100
print(std) 

print(mystat.probablity_density_function(std,median,-std,std)) # Within -1σ and 1σ    
print(mystat.probablity_density_function(std,median,-std * 2,std * 2)) # Within -2σ and 2σ














domain = np.arange(-15, 16, 1)  






plt.plot(domain, norm.pdf(domain,0,std)) 
plt.xlabel(' Price % Change ') 
plt.ylabel('Frequency')
plt.show() 



 







