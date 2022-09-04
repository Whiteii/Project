

import mystat
import statistics


    
    
# Read this link over here https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/ 
#https://www.desmos.com/calculator/pyviauerg0

#normal_distribution = stat.probablity_density_function(0.06299598659374768,0,-0.06299598659374768,0.06299598659374768)
#print(normal_distribution)

#domain = np.arange(-4, 5, 1)
#plt.plot(domain, norm.pdf(domain,0,standard_deviation))
#plt.show()


note_files = open('%price_change.txt','r')
x = note_files.read()
b = x.split('\n')
a = b

daily_price_change = []
for element in a:
    daily_price_change.append(float(element))



mean = statistics.mean(daily_price_change)

second_mean = statistics.median(daily_price_change)




print(mean)




print(second_mean)




