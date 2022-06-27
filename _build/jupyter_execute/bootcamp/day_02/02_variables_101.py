#!/usr/bin/env python
# coding: utf-8

# # PYTHON Basic Data Types
# 
# ## Variables and Basic Data Types
# 
# A variable implies change and is a way of referring to some space in your computer memory that is allocated by your computer program to store a specific type of information. In other words, it is a symbolic name for a physical address in memory that contains static or dynamic values. Python supports many different Data Types, and in contrast to other programming languages where you need to specify the data type of a variable, python will automatically find out the data type at the process of allocation.
# 
# - None (aka null object or variable) 
# - Boolean Type (True or False)
# - Strings (strings in Python are arrays of bytes representing unicode characters)
# - Integers $\pm\mathbb{Z}$
# - Floats $\pm\mathbb{R}$
# - Complex $\pm\mathbb{C}$

# #### For example: 

# In[1]:


my_none_variable = None 
my_bool_variable = True 
my_string_variable = 'STRING'
my_int_variable = 1
my_float_variable = 1.1
my_complex_variable = 1.1+1j


# ### Variables Naming Styles
# 
# #### lowercase/UPPERCASE
#     - single letter - b/B
#     - single name - var/VAR
#     - lower_with_underscores/UPPER_WITH_UNDERSCORES
# 
# #### For example
# 
# 

# In[2]:


a = A = 5
number = NUMBER = 154.456
first_name = FIRST_NAME = 'EYAL'


# #### mixed cases
#     - CamelCase - capitalize all the starting letters
#     - mixedCase - initial lowercase character
#     
#     
# #### For example

# In[3]:


Last_Name = last_Name = 'Soreq'


# ### Introspective functions 
# 
# - Introspection is the ability to interrogate objects at runtime.
# - Everything in python is an object. 
# - Every object in Python may have attributes and methods. 
# - By using introspection, we can dynamically examine python objects. 
# 

# #### `type` function returns the type of an object.

# In[4]:


type(None) 


# #### The `dir` function return list of methods and attributes associated with that object.

# In[5]:


dir(None) 


# #### The id function returns a special id of an object representing a specific location in memory.

# In[6]:


id(None) 


# #### The `help` function is used to find what other functions do
# - You can either call it explicitly or using question mark `?` symbol after the function

# In[7]:


help(None) 


# In[8]:


get_ipython().run_line_magic('pinfo', 'len')


# #### The `print` function prints the specified message to the screen, or other standard output devices.

# In[9]:


print(None) 


# ### Variables are just skins to a place in memory
# 
# - The id of a variable returns a unique integer representing the identity of an object
# - This is also the address of the object in memory
# - When you change the variable, you are creating a new object 
# 
# 

# In[10]:


some_var = None
print(f'The ID of some_var is {id(some_var)}')


# In[11]:


some_var = 'some different data'
print(f'When I change the content of some_var the id changes as well {id(some_var)}')


# ## Basic Data Types
# 
# Everything in python is an instance (a copy) of a class (an object).   
# 
# We can use type to examine the different classes these variables are instances of 
# 

# ### NoneType (`None`)
# 
# NoneType is the type for the None object, which is an object that indicates no value. 
# None is the return value of functions that "don't return anything".
# It is also a typical default return value for functions that search for something and may or may not find it.

# In[12]:


print(f'{type(my_none_variable)}')


# ### Integers (`int`)
# - Integers are numbers without fractional parts derived from the Latin word integer, which means "whole." 
# - Integers consist of zero, positive natural numbers (1, 2, 3, etc. ), whole numbers or counting numbers, additive inverses, and negative integers (-1, -2, -3, etc.). 
# - Often, the set of integers is denoted by the boldface (Z) or bold blackboard letter $\pm\mathbb{Z}$ which comes from the German words Zahlen ("numbers").

# In[13]:


print(f'{type(my_int_variable)}')


# ### Boolean (`bool`)
# 
# Booleans in Python are special case of integers (subclass of integer). 
# There are only two booleans, `False` and `True`. 
# They are also interpreted as 0 and 1 respectively. 

# In[14]:


print(f'{type(my_bool_variable)}')


# ### Floating-point (`float`)
# A floating point number is a whole number with a decimal point, which can be positive or negative.
# Because the decimal point is able to "float" to any place, floating point numbers are named after this fact.
# `float` is a 64-bit representation of a double-precision floating-point number in Python, which is analogous to double in other programming languages such as C or Matlab.
# A few examples of floating point numbers are: 5.2, 0.5, and -10001.67.
# The range of possible numbers limited by $-1.797e+308 <= f <= 1.797e+308$ and anything above or below that number is converted to $\pm$ inf

# In[15]:


print(f'{type(my_float_variable)}')


# ### Complex (`complex`)
# An complex number is represented by “ x + yi “. Python converts the real numbers x and y into complex using the function complex(x,y). The real part can be accessed using the method real() and imaginary part can be represented by imag().
# 

# In[16]:


print(f'{type(my_complex_variable)}')


# ### String (`str`) and character (`chr`)
# Textual data in Python is handled with str objects, or strings. 
# Strings are sequences of Unicode code points represented in python as `chr`.
# Which are just a mapping between numbers and symbols
# For example the mapping of uppercase english symbols starts at 65 and ends at 90
# Therefore `chr(67)` is interpreted as the letter `C` and is of type string. 

# In[17]:


print(f'{type(my_string_variable)}')
print(f'{type(chr(67))}')


# ## Immutable vs Mutable Objects
# 
# - In Python, there are two types of objects:
#     - Immutable objects can't be changed
#     - Mutable objects can be changed
#     
# - All the basic data types are immutable!!!  

# ## Links to expand your understanding 
# 
# For those interested in learning more...
# 
# - [realpython - Basic Data Types in Python](https://realpython.com/python-data-types/)
# - [Variables and Types](https://www.learnpython.org/en/Variables_and_Types)
# 
