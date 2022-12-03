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


def compute_cost(X, y, w, b): 
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
    m = X.shape[0] 
    print('m',m)
    cost = 0
    for i in range(m):                                
        f_wb_i = np.dot(X[i], w) + b     #(n,)(n,) = scalar (see np.dot) 
        print(f_wb_i)
        cost = cost + (f_wb_i - y[i])**2       #scalar
    cost = cost / (2 * m)                      #scalar    
    return cost  


cost = compute_cost(x_train, y_train, w_init, b_init)
print(f'Cost at optimal w : {cost}')