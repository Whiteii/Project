import numpy as np 

# training sets
x_train = np.array([[2104,5,1,45],[1416,3,2,40],[852,2,1,15]])
y_train = np.array([460,232,178]) 


def predict_single_loop(x, w, b): 
    """
    single predict using linear regression
    Args:
      x (ndarray): Shape (n,) example with multiple features
      w (ndarray): Shape (n,) model parameters    
      b (scalar):  model parameter     
    Returns:
      p (scalar):  prediction
    """
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
#print(f"x_vec shape {x_vec.shape}, x_vec value: {x_vec}")
b_init = 785.1811367994083
w_init = np.array([ 0.39, 18, -53, -26])
f_wb = predict_single_loop(x_vec, w_init, b_init)
#print(f_wb)

def compute_cost(x, y, w, b): 
    """
    compute cost
    Args:
      X (ndarray (m,n)): Data, m examples with n features
      y (ndarray (m,)) : target values
      w (ndarray (n,)) : model parameters  
      b (scalar)       : model parameter
      
    Returns:
      cost (scalar): cost
    """
    m = x.shape[0] 
    print('m',m)
    cost = 0
    for i in range(m):                                
        f_wb_i = np.dot(x[i], w) + b     
        cost = cost + (f_wb_i - y[i])**2       
    cost = cost / (2*m)                         
    return cost  

cost = compute_cost(x_train, y_train, w_init, b_init)
print(f'Cost at optimal w : {cost}') 


def compute_gradient(X, y, w, b): 
    """
    Computes the gradient for linear regression 
    Args:
      X (ndarray (m,n)): Data, m examples with n features
      y (ndarray (m,)) : target values
      w (ndarray (n,)) : model parameters  
      b (scalar)       : model parameter
      
    Returns:
      dj_dw (ndarray (n,)): The gradient of the cost w.r.t. the parameters w. 
      dj_db (scalar):       The gradient of the cost w.r.t. the parameter b. 
    """
    m,n = X.shape #(number of examples, number of features)
    print(X.shape)
    
    
    dj_dw = np.zeros((n,))
    dj_db = 0.

    for i in range(m):                             
        err = (np.dot(X[i], w) + b) - y[i]   
        for j in range(n):                         
            dj_dw[j] = dj_dw[j] + err * X[i, j]    
        dj_db = dj_db + err                        
    dj_dw = dj_dw / m                                
    dj_db = dj_db / m                                
        
    return dj_db, dj_dw
    

#Compute and display gradient 
tmp_dj_db, tmp_dj_dw = compute_gradient(x_train, y_train, w_init, b_init)
print(f'dj_db at initial w,b: {tmp_dj_db}')
print(f'dj_dw at initial w,b: \n {tmp_dj_dw}')



 