#!/usr/bin/env python
# coding: utf-8

# # Numpy 101
# 
# ## Why do we need Numpy? 
# - NumPy provides quick and efficient ways to create and manipulate arrays. 
# - Python lists can include diverse data types, while NumPy arrays must be homogenous. 
# - This enables efficient mathematical operations, but also smaller memory footprint.
# 
# ## What is an array?
# - An array is a grid of values that contains raw data, element location, and interpretation. 
# - It's a grid of indexable elements. 
# - As I said previously in Numpy all array elements have the same data type `dtype`.
# 
# ## From vectors to tensors 
# 
# - In Numpy vectors are simply a sequence of elements all sharing the same data type.
# - A vector is an array with a single dimension. 
# - In Numpy an array is referred to as a `ndarray` which is shorthand for “N-dimensional array.” 
# - An N-dimensional array is simply an array with any number of dimensions. 
# - A 1-D array is different from vector because it has a shape that reflects orientation (i.e. is )
# - The NumPy `ndarray` class is used to represent both matrices and vectors. A vector is an array with a single dimension (there’s no difference between row and column vectors), while a matrix refers to an array with two dimensions. For 3-D or higher dimensional arrays, the term tensor is also commonly used.

# In[1]:


import numpy as np 
print(type(np.array([])))


# ## Scalars, Strings and dtypes
# - In Python we only have a very minimal set of data types, scientific computing requires additional control. 
# - NumPy adds 24 new Python types for scalars. 
# - These type descriptors are largely based on CPython's C types, with numerous comparable Python types.
# - The immediate benefit of this is a smaller memory footprint, but it also means potential information loss
# - Let's review these quickly 
# 

# ### signed integer $\mathbb {Z}$ 
# - Signed integers are numbers with a “+” or “-“ sign.
# - Numpy supports a range of precision 
# - And a range of data types
# 

# #### The simplest is the boolean `bool`

# In[2]:


lb,ub = np.array([0,1],dtype='bool')
print(f"{f'bool domain is':<20}: {'{'}{lb},{ub}{'}'}")


# #### Then have unsigned integer 

# In[3]:


for power in [8,16,32,64]:
    print(f"{np.iinfo(f'uint{power}').__repr__()}")


# #### signed integer is just shifting the ranges above to center around zero

# In[4]:


for power in [8,16,32,64]:
    print(f"{np.iinfo(f'int{power}').__repr__()}")


# #### floats (aka double in Matlab) are inexact numbers that have decimal points
# 

# In[5]:


for power in [16,32,64,128]:
    print(f"{np.finfo(f'float{power}').__repr__()}")


# ##### Each float type has a range but it also has a unique resolution 
# - The smaller the resolution the better the approximation 
# - But the take home message is that very small numbers are not represented as accurately as you would like to think

# #### Complex numbers also have three types 
# - 32 bit-precision 
# - 64 bit-precision 
# - And 128 bit-precision 
# 

# #### Numpy also supports strings, and a special set of python objects 
# - We will use some of these and I will point them out when needed

# ### Arrays are all driven from a generic class 
# - In the generic class a wide set of useful methods exist
# - Some are obvious by name
# - We will go over a selected set, but it is useful to know that they exist 

# In[6]:


print([func for func in dir(np.generic) if not func.startswith('_')])


# ### Type Conversion
# `astype` method converts the data type of an array to other data types. 
# 
# ```{note} 
# When you use `astype` to cast an array from one type to another you are in fact creating a copy of the original array 
# ```

# In[7]:


arr = np.array([-127,126,127], dtype='int16')
print(id(arr))
print(id(arr.astype('int8')))


# ````{admonition} Challenge
# Without running the code try to guess what will the print function output
# ```{code-block} console
# arr = np.array([254,126,127], dtype='int16') 
# print(arr.astype('int8'))
# ```
# ````

# ### String and Unicode Data Type
# - Numpy will implicitly create a fixed length array cell based on the longest word in the passed input
# - For example the array below is of dtype `<U8` which means that every element in the array will be of type unicode with length of 8 chr

# In[8]:


unicode_array = np.array(['frontal', 'parietal', 'temporal'])
print(unicode_array.dtype)


# - You can explicitly set the cell length which will truncate (cut) the elements that are larger than the defined length 

# In[9]:


truncated_array = np.array(['frontal', 'parietal', 'temporal'],dtype='U3')
truncated_array


# ## The different ways to create an array in Numpy
# ### 1. Conversion from other Python structures
# - NumPy arrays can be defined using Python sequences such as lists, tuples and range. 
# - A list of numbers will create a 1D array
# - A list of lists will create a 2D array
# - And if you are able to you can create any kind of tensor using the right nesting
# - `.T` = transpose (i.e. flipping the array over its diagonal)

# In[10]:


arr_1d = np.array([1,2,3,4,5])
arr_2d = np.array([(1,2,3,4,5),(1,2,3,4,5)])
arr_3d = np.array([[(1,2,3,4,5),(1,2,3,4,5)],
                   [(1,2,3,4,5),(1,2,3,4,5)]])
vector_row = np.array(range(1,11))
array_1d_column = np.array([range(1,11)])
array_1d_row = np.array([range(1,11)]).T


# #### Naturally you can be creative in how construct these 

# In[11]:


array_2d_wide = np.array([range(1,11,1) for _ in range(6)])
array_2d_tall = np.array([range(1,6,1) for _ in range(11)])
array_3d_wide = np.array([[[0.5]*3]*200]*100)
array_3d_tall = np.array([[[0.5]*3]*100]*200)


# #### Created arrays have shapes and size
# - Shape reflects the dimensionality of the array 
# - Size reflects the number of cells the array contains
# - Note that 1d arrays are by default defined as vectors (i.e. neither a sequence of rows nor a columns)
# - Height, width, depth = array_3d.shape
# - Note, however, that ndarray has matrix coordinates (i,j), which are opposite to image coordinates (x,y).
# 

# In[12]:


print(f'Shape = {arr_1d.shape} and size = {arr_1d.size}')
print(f'Shape = {arr_2d.shape} and size = {arr_2d.size}')
print(f'Shape = {arr_3d.shape} and size = {arr_3d.size}')
print(f'Shape = {vector_row.shape} and size = {vector_row.size}')
print(f'Shape = {array_1d_column.shape} and size = {array_1d_column.size}')
print(f'Shape = {array_1d_row.shape} and size = {array_1d_row.size}')
print(f'Shape = {array_2d_wide.shape} and size = {array_2d_wide.size}')
print(f'Shape = {array_2d_tall.shape} and size = {array_2d_tall.size}')
print(f'Shape = {array_3d_wide.shape} and size = {array_3d_wide.size}')
print(f'Shape = {array_3d_tall.shape} and size = {array_3d_tall.size}')


# ### 2. NumPy array-creation functions
# - NumPy has many functions specifically created to speed the process of creating arrays
# - These could be roughly split to sequence specific (1d), array specific (2d) and tensor general (nd)
# 
# #### 1D array creation functions (selected)
# - `arange` : Return evenly spaced values within a given interval
#   - `np.arange([start, ]stop, [step, ]dtype=None)`
# - `linspace` : Return evenly spaced numbers over a specified interval 
#   - `np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)`
# - `logspace` : Return evenly spaced numbers over a specified interval 
#   - `np.logspace(start, stop, num=50, endpoint=True, dtype=None)`

# In[13]:


print(f'np.arange(3) = {np.arange(3)}')
print(f'np.arange(0.5,3) = {np.arange(0.5,3)}')
print(f'np.arange(0.5,2,0.5) = {np.arange(0.5,2,0.5)}')
print(f'np.linspace(0,3,3) = {np.linspace(0,3,3)}')
print(f'np.linspace(0,3,3,dtype="int") = {np.linspace(0,3,3,dtype="int")}')
print(f'np.linspace(0,3,3,endpoint=False) = {np.linspace(0,3,3,endpoint=False)}')
print(f'np.linspace(0,3,3,retstep=True) = {np.linspace(0,3,3,retstep=True)}')
print(f'np.logspace(0,3,3) = {list(np.logspace(0,3,3))}')
print(f'np.logspace(0,3,3,dtype="int") = {list(np.logspace(0,3,3,dtype="int"))}')
print(f'np.logspace(0,3,3,endpoint=False) = {list(np.logspace(0,3,3,endpoint=False))}')


# #### 2D array creation functions (selected)
# - `eye` : Return a 2-D array with ones on the diagonal and zeros elsewhere
#   - `np.eye(N, M=None, k=0, dtype=<class 'float'>, order='C')`
# - `diag` : Extract a diagonal or construct a diagonal array.
#   - `np.diag(v, k=0)`
# - `tri` : Return evenly spaced numbers over a specified interval 
#   - `np.tri(N, M=None, k=0, dtype=<class 'float'>)`

# In[14]:


print(f'np.eye(3) = \n {np.eye(3)}')
print(f'np.eye(3,4) = \n {np.eye(3,4)}')
print(f'np.eye(3,4,1) = \n {np.eye(3,4,1)}')
print(f'np.diag(range(1,4)) = \n {np.diag(range(1,4))}')
print(f'np.diag(np.eye(3)) = \n {np.diag(np.eye(3))}')
print(f'np.tri(3) = \n {np.tri(3)}')
print(f'np.tri(3,k=1) = \n {np.tri(3,k=1)}')


# #### nD array general creation functions (selected) (vector - tensor) 
# - `empty` : Return a new array of given shape and type, without initializing entries.
#   - `np.empty(shape[, dtype])`
# - `zeros` \ `ones` : Return a new array of given shape and type, filled with either zeros or ones
#   - `np.ones(shape[, dtype)`
#   - `np.zeros(shape[, dtype)`
# - `full` : Return a new array of given shape and type, filled with fill_value.
#   - `np.full(shape, fill_value, dtype=None)`

# In[15]:


print(f'np.empty(3) = \n {np.empty(3)}')
print(f'np.empty((3,3), dtype=int) = \n {np.empty((3,3), dtype=int)}')
print(f'np.zeros(3) = \n {np.zeros(3)}')
print(f'np.ones((3,3), dtype=int) = \n {np.ones((3,3), dtype=int)}')
print(f'np.full(3,"*") = \n {np.full(3,"*")}')
print(f'np.full((3,3), np.NaN) = \n {np.full((3,3), np.NaN)}')


# ### 3. NumPy Random Generator methods (selected)
# - Provides access to a wide range of distributions that can generate nd arrays
# - A complete list

# In[16]:


rng = np.random.default_rng()
print([mtd for mtd in dir(rng) if not mtd.startswith('_')])


# #### To make examples identical set fixed seed
# - Some key distributions every data scientist should know are 
#   - `binomial`: Probability of outcomes of 'number of successes' when throwing k coins with p fairness
#     - `rng.binomial(n, p, size=None)`
#   - `integers` : Return random integers from low to high.
#     - `rng.integers(low, high=None, size=None, dtype=np.int64, endpoint=False)`
#   - `choice` : Generates a random sample from a given array
#     - `rng.choice(a, size=None, replace=True, p=None, axis=0, shuffle=True)`
#   - `uniform` : Samples are uniformly distributed over the half-open interval [low, high)
#     - `rng.uniform(low=0.0, high=1.0, size=None)`
#   - `normal` : Draw random samples from a normal (Gaussian) distribution.
#     - `rng.normal(loc=0.0, scale=1.0, size=None)`

# In[17]:


seed = 2022
rng = np.random.default_rng(seed)
print(f'{"rng.binomial(30,0.3,size=6)":<50} =  {rng.binomial(30,0.3,size=6)}')
print(f'{"rng.integers(10,size=6)":<50} =  {rng.integers(10,size=6)}')
print(f'{"rng.integers(10,20,size=6)":<50} =  {rng.integers(10,20,size=6)}')
print(f'{f"rng.choice([True,False],size=6)":<50} =  {rng.choice([True,False],size=6)}')
print(f'{f"rng.choice([True,False],size=6,p=[0.2,0.8])":<50} =  {rng.choice([True,False],size=6,p=[0.2,0.8])}')
print(f'{f"rng.choice(range(7),size=6)":<50} =  {rng.choice(range(7),size=6)}')
print(f'{f"rng.choice(range(7),size=6,replace=False)":<50} =  {rng.choice(range(7),size=6,replace=False)}')
print(f'{f"rng.choice(range(7),size=6,replace=True)":<50} =  {rng.choice(range(7),size=6,replace=True)}')
print(f'{f"rng.uniform(0,2,size=6)":<50} =  {np.round(rng.uniform(0,2,size=6),2)}')
print(f'{f"rng.normal(0,2,size=6)":<50} =  {np.round(rng.normal(0,2,size=6),2)}')


# ## Indexing in Numpy vectors
# - Indexing in Numpy is far simpler than in multidimensional lists
# - lets explore some examples

# ### 1D indexing 

# In[18]:


vector = np.array(range(1,11))# 10 rows
print(f'{"Vector":<50} =  {vector}')
print(f'{"First element":<50} =  {vector[0]}')
print(f'{"Last element":<50} =  {vector[-1]}')
print(f'{"Middle elements":<50} =  {vector[len(vector)//2-1:len(vector)//2+1]}')
print(f'{"All elements starting from 4 ":<50} =  {vector[4:]}')
print(f'{"Last 4 elements ":<50} =  {vector[-4:]}')
print(f'{"Everything but last 4 elements":<50} =  {vector[:-4]}')
print(f'{"Every other element":<50} =  {vector[::2]}')


# ### Two-Dimensional Indexing and Slicing in Numpy arrays
# 

# In[19]:


x = np.array([range(1,7)])
print(f'Create a 1d array x = [{x[0,0]} ... {x[0,-1]}] with shape of {x.shape}')
print(f"Perform element wise multiplication between x and it's transposed x")
array = x.T*x
print(array)
print(f"To create an array of shape = {array.shape} and size = {array.size} ")


# #### Column and row specific index examples 
# 

# In[20]:


print(f'{"First row":<50} =  {array[0,:]}')
print(f'{"Second col":<50} =  {array[:,1]}')
print(f'{"2 columns from 3 upto 5":<50} =  {array[:,3:5].flatten()}')
print(f'{"Last 4 columns":<50} =  {array[:,-4:].flatten()}')
m,n = array.shape
print(f'{"Center of array":<50} =  {array[m//2-1:m//2+1,n//2-1:n//2+1].flatten()}')
print(f'{"First element":<50} =  {array[0,0]}')
print(f'{"Last element":<50} =  {array[-1,-1]}')
print(f'{"All rows above the 4th row":<50} =  {array[4:,:]}')
print(f'{"Everything but last 4 elements":<50} =  {array.flatten()[-4:]}')
print(f'{"First row":<50} =  {array[0::3,0::4].flatten()}')


# ## Change existing arrays using methods 
# 

# ## Arithmetic operations on arrays
# 
# ### You can apply any arithmetic function to an array with a single scalar 
# - This is element-wise arithmetic's

# In[21]:


vector_row = np.array(range(1,5))
array_2d_wide = np.array([range(1,5,1) for _ in range(3)])
array_2d_tall = np.array([range(1,5,1) for _ in range(3)])
X = 5
display(vector_row * X)
display(array_2d_wide / X)
display(array_2d_tall % X)
display(array_2d_tall ** X)
display(array_2d_tall - X)


# ### Limitation of Array Arithmetic
# -You can perform arithmetic directly on NumPy arrays, such as addition and subtraction.
# - Strictly, arithmetic may only be performed on arrays that have the same dimensions and dimensions with the same size.
# - This means that a one-dimensional array with the length of 5 can only perform arithmetic with another one-dimensional array with the length 5.

# In[22]:


a = np.array([range(1,5)])
b = np.array(a)
a + b


# #### But what happens when we try to do the following ?
# 
# ~~~python
# a = np.array([range(1,5)]) 
# b = np.array([range(4,6)])
# c = a * b
# d = a + b
# ~~~

# ### Broadcasting to the rescue 
# 
# - Broadcasting is the name given to the method that NumPy uses to allow array arithmetic between arrays with a different shape or size.
# - Broadcasting solves the problem of arithmetic between arrays of differing shapes by in effect replicating the smaller array along the last mismatched dimension.
# - However, even broadcasting has it's limitation.
# - It can only be performed when the shape of each dimension in the arrays are equal or one has the dimension size of 1. 
# - The dimensions are considered in reverse order, starting with the trailing dimension; for example, looking at columns before rows in a two-dimensional case.
# 

# In[23]:


a = np.array([range(1,7)]).T 
b = np.array([range(1,5)])
print(a*b)


# 
