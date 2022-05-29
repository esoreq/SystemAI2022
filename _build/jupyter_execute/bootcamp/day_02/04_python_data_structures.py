#!/usr/bin/env python
# coding: utf-8

# # PYTHON Data structures 101
# 
# ## What are Data structures?
# 
# Data structures organize and store data so that it's easy to access and use. The data and the operations on the data are defined by them. In data science and computer science, there are a variety of different data structures that make it easy for the researchers and engineers to concentrate on the basics and not get lost in the details of data description or access.
# 
# In fact all the Basic Data Types we just covered are considered Primitive Data Structures
# The non-primitive types are the more sophisticated data structures. Instead of just storing one value, they store a whole bunch of them.
# 

# ## What are Lists?
# - Lists are the basic sequence building block in Python.
# - They are mutable, therefore lists elements can be changed!
# - Lists are constructed with brackets \[\]
# - Every element in the list is separated by commas
# 

# 
# ### Constructing lists
# 
# - Lists can hold any basic data type
# - They can also hold mixed types
# 

# In[1]:


empty_list = []
print(empty_list)
some_list = ['frontal', 'parietal', 'temporal', 'occipital']
print(some_list)
another_list = [1, 2, 3, 4]
print(another_list)
mixed_list = ['frontal', 2.1, 0.112e-2, 2-2j,True,'a']
print(mixed_list)


# 
# ### lists have length
# 

# In[2]:


print(f"some_list length is \t:{len(some_list)}")
print(f"another_list length is \t:{len(another_list)}")
print(f"mixed_list length is \t:{len(mixed_list)}")  


# ### lists have indices
# 
# - Indexing and slicing works just like in strings 
# 

# In[3]:


print(f"{'Access start index using [0]':<50} = {mixed_list[0]}")
print(f"{'Access end index using  [-1]':<50} = {mixed_list[-1]}")
print(f"{'Use the colon [start:end] to perform slicing':<50} = {mixed_list[1:3]}")
print(f"{'Get everything UPTO [:end]':<50} = {mixed_list[:4]}")
print(f"{'Get everything FROM [start:]':<50} = {mixed_list[3:]}")
print(f"{'Get everything [:]':<50} = {mixed_list[:]}")
print(f"{'Get every second element [::2]':<50} = {mixed_list[::2]}")
print(f"{'Get list in reverse [::-1]':<50} = {mixed_list[::-1]}")
print(f"{'Access start index using [0]':<50} = {mixed_list[0]}")


# ### lists can be also be concatenated
# 
# - You can combine two lists together 
# - And you can multiply lists using integers
# 

# In[4]:


print(f"some_list + mixed_list length is \t:{len(some_list+mixed_list)}")
print(some_list*2)


# In[5]:


print(f"{'List can convert any sequence to a list ':<50} : {list('frontal')}")


# ### lists can be generated using a `range` type
#  
# 
# - The range type represents a way to create an immutable sequence of numbers quickly.
# - The constructor has 3 possible arguments 
#   - start the defines the range starting position
#   - stop the defines when the range ends 
#   - step the size of the gaps between each pair of units
# 

# In[6]:


print(f"{'Int lists can be created using range':<50} : {list(range(5))}")
print(f"{'This is quite flexible ':<50} : {list(range(45,49))}")
print(f"{'And allows even steps ':<50} : {list(range(56,69,3))}")
print(f"{'Also in reverse ':<50} : {list(range(-56,-69,-3))}")


# ### lists can hold lists to form arrays 
# 
# - This is slow and inefficient way to create these arrays
# - Next session we will see a better way to those 
# - And in Wednesday we will go over a way to do that even faster
# - But for completeness...   
# 

# In[7]:



array = [list(range(0,10)),
         list(range(10,20)),
         list(range(20,30)),
         list(range(30,40)),
         list(range(40,50)),
         list(range(60,70)),
         list(range(70,80)),
         list(range(80,90)),
         list(range(90,100))]
array


# 
# ### Items can be Appended, Inserted or removed to lists
# 

# In[8]:


letter_list = list('frontal')
letter_list.append('_R_')
print(f"{'Insert a number at index ':<50} : {letter_list}")
letter_list.insert(5, 'xxx')
print(f"{'Insert a number at index ':<50} : {letter_list}")
letter_list.pop(6)
letter_list.pop(6)
print(f"{'Remove a letter at index ':<50} : {letter_list}")


# ### lists can be sorted or reversed
# 

# In[9]:


letter_list.reverse()
print(f"In both directions\t:{letter_list}")
letter_list.sort()
print(f"lists can be sorted\t:{letter_list}")
letter_list.sort(reverse=True)
print(f"In both directions\t:{letter_list}")


# ###  lists items can be removed, changed, added, inserted and extended 
# 

# In[10]:


letter_list = list('frontal')
letter_list[2:-1] = []
print(f"{'We can remove everything from index 2 till -1':<50} : {letter_list}")
letter_list[2] = 'T'
print(f"{'We can change an item if its index exists':<50} : {letter_list}")
letter_list.extend(some_list[::-1]) 
print(f"{'Or extend the list with another one':<50} : {letter_list}")


# ## What are Tuples?
# 
# - In mathematics, a tuple is a finite ordered list of elements
# - And in Python tuples can be viewed as immutable lists 
# - In other words, once a tuple is constructed its elements can't change
# 
# 
# ### Creating Tuples
# 
# - Use parentheses () to construct an empty tuple
# - And place items separated by commas to fill it
# 

# In[11]:


empty_tuple = ()
print(empty_tuple)
some_tuple = ('frontal', 'parietal', 'temporal', 'occipital')
print(some_tuple)
another_tuple = (1, 2, 3, 4)
print(another_tuple)
mixed_tuple = ('frontal', 2.1, 0.112e-2, 2-2j,True,'a','a','c')
print(mixed_tuple)


# #### Tuples also have a length
# 

# In[12]:


print(f"some_tuple length is \t:{len(some_tuple)}")
print(f"another_tuple length is \t:{len(another_tuple)}")
print(f"mixed_tuple length is \t:{len(mixed_tuple)}")  


# #### And we can index the tuple exactly like a list
# 

# In[13]:


print(f"Access start index using [0]\t\t\t= {mixed_tuple[0]} \nAccess end index using  [-1] \t\t\t= {mixed_tuple[-1]} \nUse the colon [start:end] to perform slicing \t= {mixed_tuple[1:3]} \nGet everything UPTO [:end] \t\t\t= {mixed_tuple[:4]} \nGet everything FROM [start:] \t\t\t= {mixed_tuple[3:]} \nGet everything [:]\t\t\t\t= {mixed_tuple[:]} \nGet every second element [::2] \t\t\t= {mixed_tuple[::2]} \nGet tuple in reverse [::-1]\t\t\t= {mixed_tuple[::-1]}" )


# ### However tuple has only two basic Methods
# 
# - Use .index to get the index that matches the first occurrence of an item
# - Use .count to get the number of items in a tuple
# - What happens if a match isn't found?
# 

# In[14]:


mixed_tuple = ('frontal', 2.1, 0.112e-2, 2-2j,True,'a','a','c')
print(f"{'This is a mixed_tuple :':<35} : {mixed_tuple}")
print(f"{'You can find where a is :':<35} : {mixed_tuple.index('a')}")
print(f"{'And you can count the number of a :':<35} : {mixed_tuple.count('a')}")


# `````{admonition} Question
# What will happen if you search for a values that doesn't exist? 
# ````{dropdown} Try it 
# ```{code-block} python
# mixed_tuple.index('R')
# ```
# You get an error
# Error are a way to inform you that you tried to do something wrong 
# ````
# `````

# #### We can combine tuples 
# 

# In[15]:


combined_tuple = some_tuple + mixed_tuple
print(f"How many items are in combined_tuple \tn= {len(combined_tuple)}")
print(f"{combined_tuple}")
multiplied_tuple =some_tuple*2 
print(f"How many items are in multiplied_tuple \tn= {len(multiplied_tuple)}")
print(f"{multiplied_tuple}")


# #### What we can't do is change items 
# 
# - Tuples are immutable!!! (just like strings)
# 
# `````{admonition} Question
# What will happen if you try to change a value?
# ````{dropdown} Try it 
# ```{code-block} python
# mixed_tuple[2] = 'a'
# mixed_tuple[2] = [] 
# ```
# You get a different error
# ````
# `````
# 

# 
# ## What are Dictionaries?
# 
# - A dictionary is a data structure that maps keys to values
# - Dictionaries are unordered (i.e. no index)
# - Dictionaries rely on a data structure called hash tables
# - If you don't know what a [hash table](https://www.data-structures-in-practice.com/hash-tables/) and you are dying to find out 
# 

# 
# ### Important things about Dictionaries
# 
# - Each item in a dictionary has a key and a value
# - The key acts as the value index, so no two values can have the same key (i.e. keys are unique).
# - Keys must also be hashable (i.e. can be used as a key by a hash table)
# - Any built-in immutable data type is hashable 
# - immutable data types are int, float, complex, bool, str, tuple, Unicode and even None
# 

# 
# ### Creating a dictionary
# 
# - We create an empty dictionary using braces {}
# - We can use any valid key
# - And we can use any kind of data as a value
# - If we use the same key twice the last value counts
# 

# In[16]:


empty_dict = {}
print(empty_dict)
some_dict = {"SBC":"subcortical",
             "DMN":"default mode network",
             "ECN":"executive control", 
             "ATT":"attentional"}
print(some_dict)
mixed_dict = {1:{"SBC":"subcortical"},
              2:["DMN","default mode network"], 
              3:("ECN","executive control"),
              3:{"MD":"Multiple demands"}}
print(mixed_dict)


# ### nesting Dictionaries
# - Hierarchies can be nested in complex ways
# - And extract their values if we know how 
# 

# In[17]:


nested_dict = {"1":{"1.1":{"1.1.1":"Tada!!!"}}}
nested_dict["1"]["1.1"]["1.1.1"]


# ### And as you guessed Dictionaries have some basic methods
# 

# In[18]:


lobes = {1:'frontal', 2:'parietal', 3:'temporal', 4:'occipital',5:'insula'}
print(f"lobes keys :{lobes.keys()}") 
print(f"lobes values :{lobes.values()}") 
print(f"lobes items :{lobes.items()}")
print(f"lobes length :{len(lobes)}")


# ### Assigning an existing dictionary to a variable passes a reference
# 
# - That means that changes in either the source or the target variable will affect both
# - To break this chain, we use the copy function 
# 

# In[19]:


lobes_reference = lobes # assign the existing dict to a new variable
lobes_reference[1] = 'Changed on new'
lobes[3] = 'Changed on old'
print(f'old dict = {lobes}')
print(f'new dict = {lobes_reference}')


# #### To break this chain, we use the copy function 
# 

# In[20]:


lobes = {1:'frontal', 2:'parietal', 3:'temporal', 4:'occipital',5:'insula'}
lobes_reference = lobes.copy() # copy the existing dict to a new variable
lobes_reference[1] = 'Changed on new'
lobes[3] = 'Changed on old'
print(f'old dict = {lobes}')
print(f'new dict = {lobes_reference}')


# #### We can update items in a dictionary using another dictionary
# 

# In[21]:


lobes = {1:'frontal', 2:'parietal', 3:'temporal', 4:'occipital',5:'insula'}
lobes.update({6:'subcortical',7:'brainstem'})
lobes


# #### Or we can just add one item at a time 
# 

# In[22]:


lobes[8] = 'cerebellum'
lobes


# ## What are Sets
# 
# - Sets are a special data structure that holds **unique** unordered elements
# - In a way, sets are similar to keys in the dictionary 
# - Unsurprisingly, sets can only take hashable data types
# - Sets can be extremely powerful if used right
# 

# 
# ### What are sets used for 
# 
# - The list is endless,
# - From our narrow perspective, we will use them in the context of set theory
#     - This means finding intersections between sets
#     - Getting the union of several sets 
#     - Or even the differences of several sets 
# 

# ### creating sets 
# 
# - Sets can be created using a list 
# 

# In[23]:


empty_set = set()
print(f'This is an empty {type(empty_set)}')
some_set = {'frontal', 'parietal', 'temporal', 'occipital'}
print(f'This is also a set {type(some_set)}')
another_set = set([1, 2, 3, 4])
print(f'We can use lists as constructor for sets {type(another_set)}')
mixed_set = set(['frontal', 2,'c'])
print(f'And we can used mixed sets {type(mixed_set)}')


# 
# ### sets also have some basic methods
# 

# In[24]:


print(f'Sets have length {len(mixed_set)}')
mixed_set.remove('c');print(f'Elements can be removed {mixed_set}')
print(f'And elements can be removed from a set {mixed_set.pop()}')
print(f'Until it is empty  {mixed_set.pop()}')
mixed_set.add('c');print(f'And then added {mixed_set}')


# ### sets also have unique methods
# 
# - Consider the following three numeric sets
# 

# In[25]:


X = {1, 2, 5, 6, 7, 9}
Y = {1, 3, 4, 5, 6, 8} 
Z = {3, 5, 6, 7, 8, 10}


# #### sets can be intersected
# - The intersection of two or more sets is the set of elements which are common to all sets. 
# - For example, the intersection of three sets X, Y and Z is the set of elements that are common to sets X, Y and Z. 
# - It is denoted by X ∩ Y ∩ Z
# 
# 

# In[26]:


XnY = X.intersection(Y) # X ∩ Y
YnX = Y.intersection(X) # X ∩ Y
print(f'Intersection is indifferent to order X ∩ Y == Y ∩ X = {XnY==YnX}')
XnYnZ = X.intersection(Y,Z) # X ∩ Y ∩ Z
print(f'Intersection function can take multiple sets X ∩ Y ∩ Z = {XnYnZ}')
print(f'Intersection can be called using the & operator X & Y & Z = {X & Y & Z}')


# #### Set Difference
# 
# - The (set) difference (aka relative complement) between two sets X and Y is written X∖Y, 
# - This means the set that consists of the elements of X which are not elements of Y
# - The key take-home is that we are after the unique elements of X. 
# - Here order does matter!! 
# - Difference can be called using the difference function or using the - operator
# 

# In[27]:


print(f'X\Y={X-Y} and is not equal to Y\X {Y-X}')
print(f'The Difference of X\Y\Z={X.difference(Y,Z)}')


# ### Sets are a powerful tool 
# 
# - But for this course, the above is enough
# 

# 
# ## Summary 
#  
# - In this section we covered the different common data structures Python has  
# - We saw how Lists, Tuples, Dictionaries and Sets could be created 
# - We learned about some basic methods they have 
# - And we learned how to index and slice parts of them
# - You deserve a break before heading out to the last Programming section 
# 
# 

# 
# ## Links to expand your understanding 
# 
# For those interested in learning more...
# 
# - [Python Data Structures Tutorial](https://www.datacamp.com/community/tutorials/data-structures-python)
# 
