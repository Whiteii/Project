
import math 
import random
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np



#Contact Information: Lianghui732@gmail.com
#Name : Liang Zhang
#Monte Carlo Simulation 


number_of_simulation = int(input("Number Of Simulation"))
point_inside = []
point_outside = []
x_axis = [] # for i 
y_axis = [] # for y axis 
inside_x_position = []
inside_y_position = []
outside_x_position = []
outside_y_position = []


plt.figure(figsize=(20,8), dpi = 100) 



isFirst1 = True
isFirst2 = True

i = 0
for i in range(number_of_simulation):
    i = i + 1
    random_x = random.uniform(-1, 1)
    random_y = random.uniform(-1, 1) 
    if math.sqrt(random_x**2 + random_y **2) == 1 or math.sqrt(random_x ** 2 + random_y ** 2) < 1: 
        point_inside.append((random_x,random_y)) 
        inside_x_position.append(random_x) 
        inside_y_position.append(random_y) 
    else:
        point_outside.append((random_x,random_y))    
        outside_x_position.append(random_x)
        outside_y_position.append(random_y)  
        estimate_pi = (int(len(point_inside))/i) * 4
       # print(estimate_pi)
        x_axis.append(i)
        #print(x_axis)
        y_axis.append(estimate_pi)   
        

        plt.subplot(1,2,2) 
        plt.figure(1)
    if i%100  ==  1:
        
        
        if isFirst1: 
            
            plt.scatter(inside_x_position,inside_y_position, c= 'Yellow' , s=50, label='Drop inside' ) 
            isFirst1 = False 
            plt.legend(loc=(0.75, 0.9))
        else: 
           
           plt.scatter(inside_x_position,inside_y_position, c='Yellow' , s=50, label='Drop inside') 
           #print(inside_x_position)
                  
  
        plt.figure(1)
        if isFirst2:
             
            plt.scatter(outside_x_position,outside_y_position, c='Black' ,s=50,label='Drop outside')
            isFirst2 = False
            plt.legend(loc=(0.75, 0.9))
        else:
           
           plt.scatter(outside_x_position,outside_y_position, c='Black' ,s=50, label='Drop outside') 
           plt.figure(1) 
           plt.draw()
           plt.pause(0.1)     
           plt.subplot(1,2,1)  
           plt.annotate('π',[0,np.pi],fontsize=20, c = 'green')
           plt.axhline(y=np.pi, c='darkblue',linewidth=2,alpha=0.5)
           plt.plot(x_axis,y_axis, color = 'navy', alpha = .75, lw = 2, ls = '-.', marker = 'o', markersize = 2)  
           
            
plt.show()   
        
        
        
    
         
         
         
         
         

            
        
         



