import numpy as  np 
import matplotlib.pyplot as plt  

def compute_model_output(x,y, w, b):
   
    m = len(x)
    f_wb = 0
    cost = 0

    for i in range(m):
        f_wb = w * x[i] + b 
        cost = cost + (f_wb - y[i])**2
    total_cost = 1/(2*m) * cost
    return total_cost

def compute_gradient(x,y,w,b): 
  """
  x : Data, m examples 
  y : target value 
  w,b : parameter
  """
  m = len(x)
  dj_dw = 0 
  dj_db = 0 
  
  for i in range(m): 
    f_wb = w * x[i] + b
    dj_dw_i = (f_wb - y[i]) * x[i]
    #print(dj_dw_i)
    dj_db_i = (f_wb - y[i])
    dj_dw += dj_dw_i
    dj_db += dj_db_i
    
  dj_dw = dj_dw / m 
  #print(dj_dw)
  dj_db = dj_db / m 
  #print(dj_db)
  return dj_dw, dj_db 

# For visualization 
def linear_regression(x, w, b):
    
    m = len(x)
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b   
    #print(f_wb)
    return f_wb

def gradient_descent(x,y,w,b,alpha,num_iters,cost_function,gradient_function,regression):
  J_history = []
  P_history = []
  a = regression(x,w,b)
  for i in range(num_iters): 
      dj_dw, dj_db = gradient_function(x,y,w,b)  
      w = w - alpha * dj_dw
      b = b - alpha * dj_db
      tmp_f_wb = regression(x,w,b)
      
      
      if i < 100000: 
        J_history.append(cost_function(x,y,w,b))
        P_history.append([w,b])
        #print(J_history)  
  print(tmp_f_wb)        
  plt.plot(x_train, tmp_f_wb, c='b',label='Our Prediction') 
  plt.scatter(x_train, y_train, marker='x', c='r',label='Actual Values')
  plt.title("Housing Prices")
  plt.ylabel('Price (in 1000s of dollars)')
  plt.xlabel('Size (1000 sqft)')
  plt.legend()
  plt.show()     
  return w,b,J_history,P_history  

x_train = np.array([1, 2,3,4,5,6,7,8,9,10,11,12,13])  
y_train = np.array([-300, -500,-800,-300,-500,-1000,-2000,-20,-50,-600,-800,-900,-1200])  

w_init = 0
b_init = 0
iterations = 100000
tmp_alpha = 0.001
w_final, b_final, J_hist, p_hist = gradient_descent(x_train ,y_train, w_init, b_init, tmp_alpha, iterations, compute_model_output, compute_gradient,linear_regression) 



