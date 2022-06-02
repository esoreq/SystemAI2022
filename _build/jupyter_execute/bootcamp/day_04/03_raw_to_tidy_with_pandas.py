#!/usr/bin/env python
# coding: utf-8

# # From raw to structured 
# 
# ### [Disentangling the cognitive, physical, and mental health sequelae of COVID-19.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4008565)
# - Finding real messy raw data in the cognitive domain is not simple 
# - For this example I chose the control dataset from the above paper which examined 12 established cognitive tests to examine intelligence in an online settings 
# - It has two control datasets
#   - One with the actual cognitive test summary scores 
#   - Another with an online questioner regarding various demographic questions
# - Our objective in this session is to create a joint table that contains information from both tables 
# - The secondary objective is to combines everything we learned in the previous session and some additions 
# - And we also need some interesting real life data to practice plotting for the next session and tomorrow 
# 

# ### Start by importing the pandas module
# - Notice that I am using a method called set_option to extend the display constrains imposed by pandas

# In[1]:


import pandas as pd
pd.set_option('display.max_rows', 100)
pd.set_option("display.max.columns", None)


# ### Use the following links to read the two datasets into a dataframe
# - Pandas has many ways to read and write tables into a dataframe in many formats 
# - [for an exhaustive list](https://pandas.pydata.org/docs/user_guide/io.html)
# - Here we will use the `pd.read_csv` command that is able to download a url containing data in csv format and import it 
# - Use the pd.read_csv command to complete the following code
# 
# ~~~
# tasks_url = 'https://tinyurl.com/bwfzme4r'
# demo_url = 'https://tinyurl.com/2s4cfah6'
# measures = 
# demographics = 
# ~~~
# 

# ### Now use the `head` command to peak into the first five rows of the two datasets
# - You will see that tbe demographics is fine 
# - In contrast, the measures headers are spanned over 3 rows (including the columns)
# - We want to tidy these column names to simplify data exploration 

# ### Fix the column names 
# #### Write a list comprehension for loop to go over the columns of the measures and strip the point suffix
# 
# ~~~python
# col_top = [ ___ for __ in ___ ]
# ~~~
# 
# #### Extract the first row of the measures dataframe as an array
# ~~~python
# col_bottom = 
# ~~~
# 
# #### Change the first two cells in col_top to `info` 
# ~~~python
# col_top___ = ___
# ~~~
# 
# #### Change the first two cells in col_bottom to `user` and `device` 
# ~~~python
# col_bottom___ = ___
# ~~~

# ### Pandas has a MultiIndex class
# - We will use the `MultiIndex.from_tuples` method to convert our two sequences `col_top` and `col_bottom` to column name pairs
# - In three steps, 
#   1. first use list comprehension and zip to merge the two lists in to a list of tuple pairs
#   2. Using that list create MultiIndex object and name the two columns ["task", "measure"]
#   3. Finally assign this index to the measures dataframe
# - 
# 
# ~~~python
# multi_index = [ __ for __ in ___ ]
# index = pd.MultiIndex.from_tuples(multi_index, names=["task", "measure"]) 
# measures.columns = index
# ~~~

# ### Remove the first two rows 
# - Now use indexing to overwrite the first two rows of the measures data frame using the iloc method
# - And look at the results of your hard work using head or tail
# 
# ~~~python
# measures = 
# measures.head()
# ~~~
# 

# ### Prepend the word 'info' onto the demographics data frame
# - Before we can combine the two dataframes it will be useful to augment the columns index to be a multi-index also 
# - There are many different ways to do that, in this example we will be using the function `concat`
# - It is used to concatenate (combine) together Series and Dataframes either by stacking them one over the other or stacking them side by side 
# - By concatenating the a dictionary containing a Dataframe we are extending the index with one level 
# 
# ~~~python 
# demographics = pd.concat({'info': demographics},axis=1)
# ~~~
# 
# - Which is the same as writing this
# 
# ~~~python 
# demographics.columns = pd.MultiIndex.from_tuples([('info',col) for col in demographics.columns])
# ~~~

# ### Almost final step we now can merge both dataframes with ease 
# - The merge command is designed to merge together dataframes using ideas and concepts from SQL 
# - In this context we will use an inner join which gives us only users that have some tasks completed and some questioner data 
# - In this class, this will be our primary data set, which will enable us to investigate various analytical tasks using a data set that is as close to reality as possible while still being simple enough to fit in this timeframe. 
#   
# ![](https://res.cloudinary.com/practicaldev/image/fetch/s--07Go4Ldi--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/u4rx9tnq7ei4fstlafec.png)
# 
# ~~~python 
# df = pd.merge(measures.set_index(('info','user')),
#               demographics.set_index(('info','user')),
#               how='inner',
#               left_index=True,
#               right_index=True)
# ~~~

# ### If everything worked as planned...
# - Then we now have 13 high level headings each aggregating all the relevant information together 
# - Next session we will start exploring how to use that to our advantage to produce both summary tables and preliminary rapid visualizations 
# - For now, just run the following command to examine the demographics of the joint dataset 
# 
# ~~~python
# df[['info']]
# ~~~
# 

# ### To make it usable in other notebooks we need to be able to save this file 
# - Pandas supports multiple output types 
# - I am using the pickle format for two reasons: 
#   - It preserves the datatypes and multi-index heading 
# 
# ~~~python 
# df.to_pickle('12_tasks.pkl')
# df = pd.read_pickle('12_tasks.pkl')
# ~~~

# In[19]:


from pathlib import Path


# ### Final step create a reproducible function that captures this process and can be adapted to other projects with minor changes
# 
# ~~~python
# def download_data():
#     tasks_url = 'https://tinyurl.com/bwfzme4r'
#     demo_url = 'https://tinyurl.com/2s4cfah6'
#     measures = pd.read_csv(tasks_url)
#     demographics = pd.read_csv(demo_url)
#     return measures,demographics
# 
# def fix_measures_columns(measures):
#     col_top = [ v.split('.')[0] for v in measures.columns ]
#     col_bottom = measures.iloc[0,:].to_numpy()
#     col_top[0:2] = ['info','info']
#     col_bottom[0:2] = ('user','device')
#     multi_index = [tuple(v) for v in zip( col_top, col_bottom )]
#     measures.columns = pd.MultiIndex.from_tuples(multi_index, names=["task", "measure"]) 
#     measures = measures.iloc[2:,:]
#     return measures
# 
# def load_clean_data():
#     import pandas as pd 
#     from pathlib import Path
#     file_name = '12_tasks.pkl'
#     if Path(file_name).exists():
#         return df = pd.read_pickle(file_name)
#     else:
#         measures,demographics = download_data()
#         measures = fix_measures_columns(measures)
#         demographics = pd.concat({'info': demographics},axis=1)
#         df = pd.merge(measures.set_index(('info','user')),
#               demographics.set_index(('info','user')),
#               how='inner',
#               left_index=True,
#               right_index=True)
#         df.to_pickle(file_name)
#         return df
# ~~~
# 

# ## Links to expand your understanding 
# 
# For those interested in learning more...
# - [Merge, join, concatenate and compare](https://pandas.pydata.org/docs/user_guide/merging.html#merge-join-concatenate-and-compare)
# - [Input output tools in Pandas (text, CSV, HDF5, …)](https://pandas.pydata.org/docs/user_guide/io.html#io-tools-text-csv-hdf5)
