import numpy as np 
import math 




def compute_cost(x,y,w,b):
    m = x.shape[0] 
    cost = 0 
    for i in range(m): 
        f_w_b = np.dot(x[i],w) + b 
        cost = (f_w_b - [y]) ** 2  + cost 
    cost = (1/ (2 * m)) + cost
    return cost 

def compute_gradient(x,y,w,b): 
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



X_train = np.array([[2104, 5, 1, 45], [1416, 3, 2, 40], [852, 2, 1, 35]])
y_train_set = np.array([460, 232, 178])
w_init = np.array([ 0.39133535, 18.75376741, -53.36032453, -26.42131618])
b_init = 785.1811367994083




tmp_dj_dw, tmp_dj_db = compute_gradient(X_train, y_train_set, w_init, b_init)
print(f'dj_dw at initial w,b: {tmp_dj_dw}')
print(f'dj_db at initial w,b: \n {tmp_dj_db}')









   
def gradient_descent(X,y,w,b,alpha,ilterate,gradient,cost):
    J_history = []
    w_z = w
    b_z = b
    for i in range(ilterate): 
        dj_dw, dj_db = gradient(X,y,w,b)
        w_z = w_z - alpha * dj_dw
        b_z = b_z - alpha * dj_db 
        if i < 10000:
            J_history.append(cost(X,y,w,b))
            
        return w_z,b_z,ilteration,J_history
    
    
    
    
    
X_train = np.array([[2104, 5, 1, 45], [1416, 3, 2, 40], [852, 2, 1, 35]])
y_train_set = np.array([460, 232, 178])
b_init = 0.
ilteration = 1000
w_init = np.array([ 0.39133535, 18.75376741, -53.36032453, -26.42131618])
initial_w = np.zeros_like(w_init)
set_alpha = 0.0000005


w_z,b_z,ilteration,J_history = gradient_descent(X_train,y_train_set,initial_w,b_init,set_alpha,ilteration,compute_gradient,compute_cost)

##print(b_z)