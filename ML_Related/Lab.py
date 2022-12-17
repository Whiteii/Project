import numpy as np 
import time  



# NumPy routines which allocate memory and fill arrays with value
a = np.zeros(4); print(f"np.zeros(4) :   a = {a}, a shape = {a.shape}, a data type = {a.dtype}") 
#a = np.zeros((4,)); print(f"np.zeros(4,) :  a = {a}, a shape = {a.shape}, a data type = {a.dtype}") 
#a = np.random.random_sample(4); print(f"np.random.random_sample(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}") 
# These are single value for a 1-D result or a tuple(n,m,...) 

# NumPy routines which allocate memory and fill arrays with value but do not accept shape as input argument


#a = np.arange(4.);print(f"np.arange(4.):     a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
#a = np.random.rand(4);          print(f"np.random.rand(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}") 


# Let construct a vector that is a = {2,3,4,1} 
#a = np.array([2,3,4,1]); print("np.array([2,3,4,1]: a = {a}, a data type = {a.dtype}") 
#Let construct a vector that is a = {1,0,0,1}
#a = np.array([1,0,0,1]); print("np.array([1,0,0,1]): a = {a}, a data type = {a.dtype}")

a = np.arange(10)
#print(f"a = {a}") 

c = a[:3]
#print(c)  

c = a[3:]
#print(c) 


x = [ 
     [0,1,2,3,4,5], 
     [6,7,8,9], 
     [10,11,12,13]     
     ]


print(x[2])