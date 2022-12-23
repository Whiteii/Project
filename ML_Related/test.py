import numpy as np 





def cost_function(x,y,w,b):  
    cost = 0 
    m = x.shape[0]
    #print(m)
    #print(x.shape)
    for i in range(m): 
        f_w_b = np.dot(x[i],w) + b 
        #print(f_w_b) 
        cost = cost +(f_w_b - y[i]) ** 2 
    cost = (1/(2*m)) * cost 
    return cost  

x_train = np.array([[2104, 5, 1, 45],[1416,3,2,40],[852,2,1,35]]) 
y_train = np.array([460,5,2]) 
w_init = np.array([ 0.39, 19, -53, -26])
b_inital =  785   

test = cost_function(x_train,y_train,w_init,b_inital)



print(x_train[0,1])



