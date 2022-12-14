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

# Plot our model prediction
plt.plot(x_train, tmp_f_wb, c='b',label='Our Prediction')

# Plot the data points
plt.scatter(x_train, y_train, marker='x', c='r',label='Actual Values')

# Set the title
plt.title("Housing Prices")
# Set the y-axis label
plt.ylabel('Price (in 1000s of dollars)')
# Set the x-axis label
plt.xlabel('Size (1000 sqft)')
plt.legend()
plt.show()
