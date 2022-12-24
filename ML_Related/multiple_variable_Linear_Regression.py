import numpy as np 
import math  
import copy, math
import matplotlib.pyplot as plt



X_train = np.array([[2104, 5, 1, 45], [1416, 3, 2, 40], [852, 2, 1, 35]])
y_train = np.array([460, 232, 178])  
b_init = 785.1811367994083
w_init = np.array([ 0.39133535, 18.75376741, -53.36032453, -26.42131618])


def compute_cost(x,y,w,b):
    m = x.shape[0] 
    cost = 0 
    for i in range(m): 
        f_w_b = np.dot(x[i],w) + b 
        cost = (f_w_b - y[i]) ** 2  + cost 
    cost = (1/ (2 * m)) + cost
    return cost 

def compute_gradient(x , y , w , b): 
    m,n = x.shape
    dj_dw = np.zeros((n,))
    dj_db = 0.
    for i in range(m): 
        err = (np.dot(x[i],w) + b) - y[i]
        for j in range(n):  
            dj_dw[j] = dj_dw[j] + err * x[i,j] 
            dj_db = dj_db + err 
    dj_dw = dj_dw/m
    dj_db = dj_db/m
    return dj_dw, dj_db



def gradient_descent(X, y, w_in, b_in, cost_function, gradient_function, alpha, num_iters): 
   
    
    # An array to store cost J and w's at each iteration primarily for graphing later
    J_history = []
    w = copy.deepcopy(w_in)  #avoid modifying global w within function
    b = b_in
    
    for i in range(num_iters):

        # Calculate the gradient and update the parameters
        dj_dw,dj_db = gradient_function(X, y, w, b) 

        # Update Parameters using w, b, alpha and gradient
        w = w - alpha * dj_dw 
        #print(w)##None
        b = b - alpha * dj_db               ##None
      
        # Save cost J at each iteration
        if i<100000:      # prevent resource exhaustion 
            J_history.append( cost_function(X, y, w, b)) 
            
        if i % math.ceil(num_iters / 10) == 0:
            print(f"Iteration {i:4d}: Cost {J_history[-1]:8.2f}   ")
 
    return w, b, J_history #return final w,b and J history for graphing  
    
    
  
initial_w = np.zeros_like(w_init)
initial_b = 0.
iterations = 1000
alpha = 5.0e-7



    
w_final, b_final, J_hist = gradient_descent(X_train, y_train, initial_w, initial_b,compute_cost, compute_gradient, alpha, iterations)

#print(w_final)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
X_train = np.array([[2104, 5, 1, 45], [1416, 3, 2, 40], [852, 2, 1, 35]])
y_train = np.array([460, 232, 178])
initial_b = 0.
iterations = 1000
w_init = np.array([ 0.39133535, 18.75376741, -53.36032453, -26.42131618])
initial_w = np.zeros_like(w_init)
alpha = 5.0e-7 

w_final, b_final, J_hist = gradient_descent(X_train, y_train, initial_w, initial_b,compute_cost, compute_gradient, alpha, iterations)

print(w_final)



#w_z,b_z,ilteration,J_history = gradient_descent(X_train,y_train_set,initial_w,b_init,set_alpha,ilteration,compute_gradient,compute_cost)
#print(w_z) 
#print(b_z)