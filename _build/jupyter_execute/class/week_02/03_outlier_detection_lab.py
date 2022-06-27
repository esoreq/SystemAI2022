#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import (StandardScaler, 
                                   PowerTransformer, 
                                   MinMaxScaler, 
                                   RobustScaler,
                                   MaxAbsScaler,
                                   QuantileTransformer)
import seaborn as sns
import utils
pd.options.display.precision = 2
pd.set_option('display.max_rows', 100)
pd.set_option("display.max.columns", None)
df = pd.read_pickle('12_tasks.pkl')
plt.style.use('bmh')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# ## We start by creating several subset datasets
# 
# - Using the same dataset as last week create two datasets 
#   - One for cognitive scores that will take either avg or final score 
#   - Another for response time that collects all features that contain `ms` in them
# 

# In[108]:


### Your code comes here 

scores = None
response_time = None


# # What is the difference between the datasets? 
# - can you explain this using domain knowledge? 

# # Challenge 2
# 
# - Using the two datasets select two different tasks one that records response time per_item and one that records correct rt 
#   - Use the appropriate visualisation method to examine if there are outliers in the reaction time data
#   - If there are try to use one of the methods covered in the lecture to deal with these 
# 

# # Challenge 3
# 
# - Now try to create a function that automatically detects outliers and deals with them 
# - Apply it to the entire dataset and re-examine your exploration from last week assignment 
# 
