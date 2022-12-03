import numpy as np 
import time  



# NumPy routines which allocate memory and fill arrays with value
#a = np.zeros(4); print(f"np.zeros(4) :   a = {a}, a shape = {a.shape}, a data type = {a.dtype}") 
#a = np.zeros((4,)); print(f"np.zeros(4,) :  a = {a}, a shape = {a.shape}, a data type = {a.dtype}") 
#a = np.random.random_sample(4); print(f"np.random.random_sample(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}") 
# These are single value for a 1-D result or a tuple(n,m,...) 

# NumPy routines which allocate memory and fill arrays with value but do not accept shape as input argument


a = np.arange(4.);              print(f"np.arange(4.):     a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

#a = np.random.rand(4);          print(f"np.random.rand(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")