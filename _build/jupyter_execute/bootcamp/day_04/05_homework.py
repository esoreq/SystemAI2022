#!/usr/bin/env python
# coding: utf-8

# ## DAY 04 - HOMEWORK 
# 
# - Solve as many of the exercises below 

# ### E1. Use Python, Numpy or Pandas to create the following 
# 
# ~~~
# [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],
# [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
# [6, 12, 18, 24, 30, 36, 42, 48, 54, 60],
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],
# [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],
# [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]]
# ~~~

# ### E2. Use Python, Numpy or Pandas to create the following 
# 
# ~~~
# array([[ 2,  3,  4],
#        [ 5,  6,  7],
#        [ 8,  9, 10]])
# ~~~

# ### E3. Use Python, Numpy or Pandas to create the following 
# 
# ~~~
# [ 0 0 3 0 0 0 11 0 7 0 ]
# ~~~

# ### E4. Use Python, Numpy or Pandas to create the following  
# 
# ~~~
# [[ 25  28  31  34  37  40  43  46  49]
#  [ 52  55  58  61  64  67  70  73  76]
#  [ 79  82  85  88  91  94  97 100 103]]
# ~~~

# ### E5. Using the previous array reverse both rows and columns 
# 
# ~~~
# [[103 100  97  94  91  88  85  82  79]
#  [ 76  73  70  67  64  61  58  55  52]
#  [ 49  46  43  40  37  34  31  28  25]]
# ~~~

# ### E6. Using the previous array convert it to the following output
# 
# ~~~
# [[1 1 1 1 1 1 1 1 1]
#  [1 1 1 1 1 1 0 0 0]
#  [0 0 0 0 0 0 0 0 0]]
# ~~~

# ### E7. Write a NumPy program to create a 10x10 checker board pattern.
# 
# ~~~
# [[1 0 1 0 1 0 1 0 1 0]
#  [0 1 0 1 0 1 0 1 0 1]
#  [1 0 1 0 1 0 1 0 1 0]
#  [0 1 0 1 0 1 0 1 0 1]
#  [1 0 1 0 1 0 1 0 1 0]
#  [0 1 0 1 0 1 0 1 0 1]
#  [1 0 1 0 1 0 1 0 1 0]
#  [0 1 0 1 0 1 0 1 0 1]
#  [1 0 1 0 1 0 1 0 1 0]
#  [0 1 0 1 0 1 0 1 0 1]]
# ~~~

# ### E8. Write a Pandas program to create a DataFrame from the following dictionary data which has the index labels.
# 
# - Sample Python dictionary data and list labels:
# 
# ~~~python
# rng = np.random.default_rng(2022)
# n = 1000
# data = dict(
#     age = np.clip(rng.normal(50,20,size=(n,)).astype(int),0,100),
#     sex = rng.choice(['M','F'],size=(n,)),
#     height = np.clip(np.round(rng.normal(1.5,0.2,size=(n,)),2),1.2,2.1),
#     weight = np.clip(np.round(rng.normal(80,15,size=(n,)),1),45,125),
#     depressed = rng.choice([True, False],p=[0.05,0.95],size=(n,)),
#     group = rng.choice(['a','b','c','d'],p=[0.15,0.25,0.5,0.1],size=(n,))
# )
# ~~~

# ### E9. Write a Pandas program to display a summary of the basic information about the DataFrame you just created. 

# ### E10. Using pandas plot the DataFrame using three different visualization types 
