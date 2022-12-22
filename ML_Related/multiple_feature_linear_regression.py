import numpy as np 
import time 
import matplotlib.pyplot as plt  




# training sets
x_train = np.array([[2104, 5, 1, 45], [1416, 3, 2, 40], [852, 2, 1, 35]]) # shape 3 by 4 
y_train = np.array([460, 232, 178])

print(x_train.shape)
print(y_train.shape)

def predict_single_loop(x, w, b): 
    n = x.shape[0]
    p = 0
    for i in range(n):
        p_i = x[i] * w[i]  
        p = p + p_i         
    p = p + b                
    return p  
# a faster approach is using vectoralization 
def predict(x,w,b): 
    p = np.dot(x,w) + b 
    return p 

x_vec = x_train[0,:]
b_init = 785.1811367994083
w_init = np.array([ 0.39133535, 18.75376741, -53.36032453, -26.42131618]) 

f_wb = predict_single_loop(x_vec, w_init, b_init)

def compute_cost(x, y, w, b):  # ---> this is the cost function <---
    m = x.shape[0]  
    print('m',m)
    cost = 0
    for i in range(m):                                
        f_wb_i = np.dot(x[i], w) + b     
        cost = cost + (f_wb_i - y[i])**2       
    cost = (1/(2 * m)) + cost                        
    return cost  

cost = compute_cost(x_train, y_train, w_init, b_init)
#print(f'Cost at optimal w : {cost}') 


def compute_gradient(x, y, w, b): 
    m,n = x.shape #(number of examples, number of features)
    dj_dw = np.zeros((n,))
    dj_db = 0.
    for i in range(m):                             
        err = (np.dot(x[i], w) + b) - y[i] 
        for j in range(n):  
            dj_dw[j] = dj_dw[j] + err * x[i, j]      
            dj_db = dj_db + err  
                                     
    dj_dw = dj_dw / m                                
    dj_db = dj_db / m                                
    return dj_db, dj_dw
    
#Compute and display gradient 
tmp_dj_db, tmp_dj_dw = compute_gradient(x_train, y_train, w_init, b_init)


def gradient_descent(x,y,w,b,alpha,num_iterations,gradient_function,cost_function):   
    J_history = []
    for i in range(num_iterations):
        dj_dw, dj_db = gradient_function(x,y,w,b)  
        w_n = w_n - alpha * dj_dw 
        b = b - alpha * dj_db
        if i < 100000: 
            J_history.append(cost_function(x,y,w,b))                   
        return J_history 
    

alpha = 0.01 
ilteration = 100000 
test = gradient_descent(x_train,y_train,0,0,alpha,ilteration,compute_gradient,compute_cost)    
print(test)         
            

    



 