import numpy as np 
import math 


X_train_set = np.array([[2104, 5, 1, 45],[1416,3,2,40],[852,2,1,35]])
y_train_set = np.array([460, 232, 178])
w_init = np.array([ 0.39133535, 18.75376741, -53.36032453, -26.42131618])
b_init = 785.1811367994083

def compute_cost(x,y,w,b):
    m = x.shape[0]
    for i in range(m): 
        f_w_b = np.dot(x[i],w) + b 
        cost = (f_w_b - [y]) ** 2  + cost 
    cost = (1/ (2 * m)) + cost
    return cost 

def compute_gradient(x,y,w,b): 
    m,n = X_train_set.shape
    dj_dw = np.zeros((n,))
    dj_db = 0.
    for i in range(m): 
        err = (np.dot(x[i],w) + b) - y[i]
        #print('err',err)
        
        
        
        
        
        for j in range(n):  
            dj_dw[j] = dj_dw[j] + err * x[i,j] 
            print('dj_dw',dj_dw)
        
        dj_db = dj_db + err 
    dj_dw = dj_dw/m
    dj_db = dj_db/m
    
    return dj_dw, dj_db
    
    
    
test = compute_gradient(X_train_set,y_train_set,w_init,b_init)   
#print(test)





