#!/usr/bin/env python
# coding: utf-8

# # Pandas 101
# 
# 
# ## Data wrangling using Pandas
# - In science we make a distinction between raw data and tidy data
# - The former is usually not annotated, is closer to the acquisition source  (i.e. sensor or measurement device ) and requires some steps to perform analytics on 
# - The latter represents a statistical table that is the foundation for at least one (but often many) questions to be asked on 
# - The term Data wrangling is a commonly used catch-all to describe the early stages of the data analytics process. 
# - It reflects the steps required to transition from raw to tidy datasets 
#   - While the steps can change from project to project the most common ones are: 
#     1. Collecting\Extracting data: 
#        1. The first step is to identify the data you need, 
#        2. Where to acquire\download it from, and then, of course, 
#        3. How to collect it
#     2. Structuring the data  
#        1. Most raw data is unstructured and requires some attention to the way you structure it 
#        2. In some cases you will use summary scores to simplify the data 
#        3. Other cases may call for statistical data mining and transformation 
#        4. But in the end we want to transform the data into a format where the following rules apply:
#           1. Each row reflects an observation
#           2. Each column reflects a variable/feature of the dataset 
#           3. Each cell reflects a measurement
#           4. Ideally, both rows and columns are labelled 
#     3. Exploratory data analysis
#        1. Describe the data components using both summary tables and data visualisation  
#        2. Identify redundancy 
#        3. Identify outliers
#        4. Measure missingness 
#        5. Identify association between features and categories 
#     4. Data cleaning, enriching and fusion 
#        1. Removing or clipping outliers 
#        2. Removing errors and duplications 
#        3. Standardising category names, dates and numeric formats 
#        4. Fusing together complementary datasets to improve available information
# 

# 
# ## What is Pandas?
# - While part of this list can be achieved using Numpy it not what it was designed for 
# - Pandas, is a package that was designed from scratch to support all of the above list and more. 
# - It extends all the elements in numpy by creating three abstract objects
#   - `Index` - Immutable sequence used for indexing and alignment. The basic object storing axis labels for all pandas objects.
#   - `Series` - One-dimensional `ndarray` with axis labels (including time series).
#   - `DataFrame` - Two-dimensional, size-mutable, tabular data. Data structure also contains labelled axes (rows and columns). 
# - These three tools provides efficient access to these sorts of "data munging" tasks that occupy much of a data scientist's time.
# 
# 
# 

# ## Pandas practicalities 
# ### Importing pandas
# - Most of the times we will import both Numpy and Pandas 
# - The syntax uses the `as` command to create shortcuts to speed up the code writing 

# In[1]:


import numpy as np 
import pandas as pd
import datetime as dt
from IPython.display import display, Markdown


# ### Pandas basic structures 
# #### The Index class 
# - As stated above the major component missing from numpy is the ability to add some context to the arrays 
# - The Index class provides this context 
# - It is in fact the parent of a family of classes each designed to provide the means to efficiently perform various operations on the two dimensions of the tidy table format. 
# - For example: 
#   - RangeIndex : Index of some monotonic integer range (i.e. start stop and step)
#   - CategoricalIndex : Index of categories 
#   - DatetimeIndex : Index of datetime64 data.
#   - MultiIndex : A multi-level, or hierarchical Index.
# 
# ```{Important}
# When you call pd.Index the class will automatically try to infer which of it's many sub-classes to use for the sake of efficiency  
# ```
# - For example:
#   

# In[2]:


print(pd.Index(['a','b','c','d','e']))
print(pd.Index(range(2,11,2)))
print(pd.Index([2,4,6,8,10]))
print(pd.Index(pd.Categorical(['a','b','c','d','e'])))
print(pd.Index([dt.datetime(2020,10,1),dt.datetime(2020,10,5)]))
print(pd.Index([('a',1),('a',2),('b',1),('b',3)]))


# ##### Index are very similar to an immutable numpy array
# - For example, you can use standard indexing notation to retrieve values or slices
# - And it has many of the attributes that NumPy arrays have
# - However you cannot change indices, only replace the whole thing
# 

# In[3]:


A2Z = pd.Index([chr(n) for n in range(65,91)])
print(A2Z[2])
print(A2Z[2:5])
print(A2Z[1:6:3])
print(f'size = {A2Z.size}, shape = {A2Z.shape}, dtype = {A2Z.dtype}')


# ##### Index support many set operations 
# - Python's built-in set methods such as Difference, Intersection or Union are supported either by set notation
# - Or as builtin functions

# In[4]:


ix_01 = pd.Index(range(1,11,3))
ix_02 = pd.Index(range(1,11,2))
print(f'Index 01 = {list(range(1,11,3))} and Index 02 = {list(range(1,11,2))}')
print(f'{"Symmetric Difference of ix_01 and ix_02":<50} = {ix_01 ^ ix_02}')
print(f'{"Intersection of ix_01 and ix_02":<50} = {ix_01 & ix_02}')
print(f'{"Union of ix_01 and ix_02":<50} = {ix_01 | ix_02}')


# In[5]:


print(f'{"Difference of ix_01 and ix_02":<50} = {ix_01.difference(ix_02)}')
print(f'{"Difference of ix_02 and ix_01":<50} = {ix_02.difference(ix_01)}')
print(f'{"Intersection of ix_01 and ix_02":<50} = {ix_01.intersection(ix_02)}')
print(f'{"Union of ix_01 and ix_02":<50} = {ix_01 | ix_02}')


# #### The Pandas Series Object
# - A Pandas `Series` is an object that contains at least three attributes 
#   - one-dimensional array of values
#   - a pandas index, 
#   - and a dtype.
# - It can be created from any sequence that can create a numpy array - because it is a numpy array (at least the value data is)
# - If you wish you can explicitly define an index 
# - You can also add a name 
#   

# In[6]:


print(pd.Series((1,2,3)))
print(pd.Series(np.ones(3),index = ('a','b','c')))
print(pd.Series(range(4,7,2),name='46'))


# ##### Series provide the power of numpy arrays with the flexibility of dictionaries 
# - For example, you can use standard indexing notation to retrieve values or slices
# - And it has many of the attributes that NumPy arrays have
# - It also has access to many analytical methods 
# - A series cell can contain any type of data 
# - And they are of course mutable 
# - Also by default a Series Index will be implicitly sorted 

# ##### Series are by definition vectors
# - As you can see they have only one dimension 
# - We can convert them to a 1D array that is called a data frame
# - The Series name becomes the column header and every element becomes a row 

# In[7]:


vector_a = pd.Series(np.ones(3),index = ('a','b','c'),name='vector_a')
print(f'shape = {vector_a.shape}')
vector_a.to_frame()


# #### The Pandas DataFrame Object
# - The Series object can be viewed as a coupling of a numpy array with a pandas Index object 
# - The DataFrame object is just a set of Series objects that share a pandas Index object for their rows and have another index object that identifies each Series 
# - Can be thought of as a dict-like container for Series objects.
# - If for example we combine several Series that have overlapping indices Pandas will automatically combine these Series and create missing values (using `NaN`) in the parts that misalign. 
# - Let's see this in action  

# #### Constructing DataFrame objects (selected methods)
# 
# - A Pandas `DataFrame` can be constructed in many ways.
# 
#  

# ##### The simplest approach - Dictionary  
# - The keys are treated as a columns
# - The values are the rows 
# - The only caveat that is that the values need to have the same length 

# In[8]:


pd.DataFrame({'col_A':[1,2],'col_B':[3,4]})


# ##### We can also supply a list of dict 
# - The same rules apply 
# - Keys are column names
# - Values are elements 
# - Pandas adapts to new columns by implicitly adding missing values
# 

# In[9]:


data = [{'col_A': 1,'col_B': 2},
        {'col_A': 4,'col_B': 3},
        {'col_A': 2,'col_C': 5}]
pd.DataFrame(data)


# ##### We can define the values using Series with index and then Pandas can adapt
# - If we supply a Series with indices this will be taken into account 

# In[10]:


col_A = pd.Series((1,2,3))
col_B = pd.Series(list(range(3,7)))
col_C = pd.Series(['a','b','c'],index=[1,5,2])
pd.DataFrame({'col_A':col_A,'col_B':col_B,'col_C':col_C})


# ##### From a 2d NumPy array
# - We can create a DataFrame with 2d matrix
# - By default an integer index will be used for both columns and indices
# - Alternatively, one can supply both of them or either they just need to be at the right shape 
# - In contrast to sets or dictionaries index can contain multiple copies
# 

# In[11]:


x = np.array([range(1,5)])
pd.DataFrame(x*x.T)


# In[12]:


pd.DataFrame(x*x.T, index = ['a','b','x','a'])


# ### Data Selection in Series and DataFrames
# - Let's create some simulated data to explore some selection basics 

# In[13]:


np.clip(np.round(rng.normal(80,15,size=(n,)),2),45,125)


# In[3]:


rng = np.random.default_rng(2022)
n = 100
data = dict(
    age = np.clip(rng.normal(50,20,size=(n,)).astype(int),0,100),
    sex = rng.choice(['M','F'],size=(n,)),
    height = np.clip(np.round(rng.normal(1.5,0.2,size=(n,)),2),1.2,2.1),
    weight = np.clip(np.round(rng.normal(80,15,size=(n,)),1),45,125),
    depressed = rng.choice([True, False],p=[0.05,0.95],size=(n,)),
    group = rng.choice(['a','b','c','d'],p=[0.15,0.25,0.5,0.1],size=(n,))
)

df = pd.DataFrame(data,index=np.arange(100,100+n))
df.head()


# ##### Data Selection using pandas data access methods 
# - We can access a single value for a row/column label pair (for this to work the indices need to be unique).
# - We can do the same using actual indices

# In[172]:


print(f'The sex of subject 104 is {df.at[104,"sex"]}')
print(f'The sex of subject 104 is {df.iat[4,1]}')


# - We can Access a group of rows and columns by label(s)
# - This simply returns the range between the two index labels (which might not be useful if the dataframe isn't sorted by the index)
# - We can also slice based on real hidden index that reflects the current state of the dataframe 
# 

# In[234]:


display(Markdown( '### Slice the rows between labels 104 and 122'))
display(df.sort_values('age').loc[104:122])
display(Markdown( '### Slice the rows between index 4 and 7'))
display(df.sort_values('age').iloc[4:7])


# ##### Data Selection using standard Python / NumPy expressions
# - We can slice a data frame using the standard numpy notation  

# In[235]:


display(Markdown( '### Slice the last two rows'))
display(df[-3:-1])
display(Markdown( '### Slice row 1'))
display(df[1:2])
display(Markdown( '### Slice odd rows from 1 - 5'))
display(df[1:6:2])
display(Markdown( '### Slice odd rows from 1 - 5 just for sex and group '))
display(df[1:6:2][['sex','group']])
display(Markdown( '### Extract all Sex values for odd rows from 1 - 5'))
display(df[1:6:2].sex)


# ##### Data Selection using masking via conditional statements 
# - We can mask a data frame using boolean sequence
#   - This can be done for both rows and columns
#   - It has to be in the size of the rows
# - But we can use any conditional statement on the series that compose the data frame 
# - Pandas even has a special function that is declarative to make this more explicit and easier to read

# In[236]:


m,n = df.shape
rng = np.random.default_rng(2022)
row_mask = rng.choice([True, False],p=[0.05,0.95],size=(m,))
display(Markdown( '### Select 5% of the rows using masking'))
display(df[row_mask])
display(Markdown( '### Select people between 30 - 35 '))
display(df[(df.age > 30 ) & (df.age < 35)])
display(Markdown( '### Select the first 3 people from group a '))
display(df[df.group == 'a'].head(3))
display(Markdown( '### Use the query function to filter males age 42 '))
display(df.query('sex == "M" and age == 42'))
display(Markdown( '### You can combine slicing and masking using pandas indexers'))
display(df.loc[df.age > 90,['sex','age']])


# ## Data operations in Pandas
# ### Basic arithmetic operations
# NumPy's ability to do rapid element-wise operations (addition, subtraction, multiplication, etc.) is migrated into the Pandas framework and is available for both series and DataFrame objects. 
# 
# The following table lists Python operators and their equivalent Pandas object methods:
# 
# | Operator | Pandas Method(s)                      |
# |-----------------|---------------------------------------|
# | `+`           | `add()`                            |
# | `-`           | `sub()` |
# | `*`           | `mul()` |
# | `/`           | `div()` |
# | `//`          | `floordiv()`                        |
# | `%`           | `mod()`                             |
# | `**`          | `pow()`                             |
# 

# In[4]:


display(Markdown( '### For example multiply height by a constant to convert to feet'))
height_feet = (df.height * 3.280).rename('height_feet')
height_feet = (df.height.mul(3.280) ).rename('height_feet')
display(height_feet.head(5))

display(Markdown( '### Or calculate BMI based on the ratio between mass and height<sup>2</sup>'))
bmi = (df.weight/( df.height ** 2)).rename('BMI')
display(bmi.head(5))


# ### Index is preserved 
# - Because the index is preserved we can assign this to the original df
# - Note that I can use pandas methods using the dot notation 
# 

# In[245]:


df = df.assign(
    bmi = (df.weight/( df.height ** 2)).round(2),
    height_feet = (df.height * 3.280).round(2)
)
df


# #### The `insert` method
# - The insert column into DataFrame at specified location.
# - Note that you can add duplicate columns
# - This is a good opportunity to also introduce two vital tools 
#   - `pd.cut` and `categorical` dtype 
# 

# ##### `pd.cut` bins values into discrete intervals
# - Use cut when you need to segment and sort data values into bins. 
# - This function is also useful for going from a continuous variable to a categorical variable. 
# - For example:

# In[278]:


age_labels = ['baby','toddler','children','teens','adults','elderly']
age_bins = [0,2,5,11,18,65,100]
age_groups = pd.cut(df.age,age_bins,labels=age_labels )
df.insert(1,'age_groups',age_groups)


# In[279]:


df


# #### But you can also just add a column like in a dictionary 
# - Note that if this column already exists it will overwrite the contents 

# In[280]:


df['age_groups'] = age_groups


# In[281]:


df


# #### `pd.concat`
# - Finally you can concatenate different data frames and Series 
# - 

# ### Data operations in Pandas using Numpy Universal Functions
# 
# - Pandas derives most of this capability from Universal Functions in NumPy. 
# - The neat thing is that you can apply the numpy functions directly on a Pandas object and get a Series in return. 

# In[264]:


display(Markdown( '### We can transform values using numpy functions'))
display(np.log(df.age).head())
display(Markdown( '### We can also standardise values using `mean` and `std`'))
display((((df.age - np.mean(df.age)))/np.std(df.age)).head())


# ### Extend dataframes using ufunc and assign 
# - This effectively means that you can use numpy ufunc to extend the original data frame also
# - You can even use scipy to the same functionality 
# - For example, using scipy Z-score transformation compared to the equivalent manual using NumPy
# 

# In[9]:


from scipy.stats import zscore
df = df.assign(
    age_log = np.log(df.age).round(2),
    age_zscore = zscore(df.age).round(2),
    age_Z = (((df.age - np.mean(df.age)))/np.std(df.age)).round(2)
)
df


# ### Pandas dataframe have information to share 
# - Pandas has several methods to describe the properties of a dataset 

# In[265]:


display(Markdown( '#### We can output the technical info of the data frame '))
display(df.info())


# In[271]:


display(Markdown( '#### We can describe the statistical properties of the dataset'))
display(Markdown( '##### For numerical features (columns)'))
display(df.describe())
display(Markdown( '##### For categorical object or boolean features (columns)'))
display(df.describe(include=['O','bool']))


# ## Links to expand your understanding 
# 
# For those interested in learning more...
# - [Pandas online documentation](http://pandas.pydata.org/)
# - [Pandas on PyVideo](http://pyvideo.org/search?q=pandas)
