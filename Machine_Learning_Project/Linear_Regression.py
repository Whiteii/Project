# The goal of this project is to get familiar with data cleaning and data exploration
# Then implented ML Algo 


import numpy as  np 
import matplotlib.pyplot as plt  



# let make a data table containing column size(1000 sqft), Price(1000s of dollars) 

x_train = np.array([1, 2,3]) #<--- our training length is 3 for our example 
y_train = np.array([300, 500,800])  
print(f"x_train = {x_train}")
print(f"y_train = {y_train}")


m = len(x_train)
i = 0 
x_i = x_train[i] 
y_i = y_train[i]
print(x_i,y_i)




def compute_model_output(x, w, b):
    """
    Computes the prediction of a linear model
    Args:
      x (ndarray (m,)): Data, m examples 
      w,b (scalar)    : model parameters  
    Returns
      y (ndarray (m,)): target values
    """
    m = x.shape[0]
    f_wb = np.zeros(m)

    for i in range(m):
        f_wb[i] = w * x[i] + b 
        print(x[i])  
        #print(f_wb[i])
    return f_wb 

w = 0
b = 0 

tmp_f_wb = compute_model_output(x_train, w, b,)






# --->  we pick w,b to be any  <---
def compute_gradient(x, y, w, b): 
    """
    Computes the gradient for linear regression 
    Args:
      x (ndarray (m,)): Data, m examples 
      y (ndarray (m,)): target values
      w,b (scalar)    : model parameters  
    Returns
      dj_dw (scalar): The gradient of the cost w.r.t. the parameters w
      dj_db (scalar): The gradient of the cost w.r.t. the parameter b     
     """
    
    # Number of training examples
    m = x.shape[0]    
    dj_dw = 0
    dj_db = 0
    
    for i in range(m):
        f_wb = w * x[i] + b 
        dj_dw_i = 5
        dj_db_i = (f_wb - y[i]) 
        dj_db += dj_db_i #<--- this is updating derivative
        dj_dw += dj_dw_i #<--- this is updating derivative  
        print(dj_dw,'test')   
    dj_dw = dj_dw/m 
    print(dj_dw,'test2')
    dj_db = dj_db/m      
    return dj_dw, dj_db 
  
  
compute_gradient(x_train,y_train,0,0)

       