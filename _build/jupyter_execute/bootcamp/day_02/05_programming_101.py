#!/usr/bin/env python
# coding: utf-8

# # Python Programming 101
# 
# ## Programming Fundamentals
# 
# - In this section, we will go over the things that make programming so powerful 
# - We will cover conditional statements 
# - And finally, cover for and while loops 

# ## Conditional statements
# 
# - A conditional statement allows us to take alternate actions based on a set of rules
# - In these types of procedures, `if`, `elif`, and `else` keywords are used.
# - Using the "if" and "else" combinations, we can construct a rule tree to perform some logic  
# 
# ~~~python
# if rule1:
#     do something
# elif rule2:
#     do something different
# else: # if both are False
#     do another thing
# ~~~

# ### Simple example

# In[1]:


rule1 = True
if rule1:
    print(f'Rule 1 is {rule1}')


# #### What will happen if we change rule1 to *False*?

# ### Add complexity to the example
# 
# - Without running the code assess which statement will be executed 
# 
# ~~~python
# rule1 = False    
# if not rule1:
#     print(f'Only if Rule 1 is {rule1} go here')
# else: 
#     print(f"Not Rule 1 is {not rule1}")
# ~~~

# ### Multiple *if*, *elif* and *else* Branches example 
# 
# - Guess what the output will be without running the code
# - Then try to change values to reach a specific branch
# 
# ~~~python
# rule1,rule2 = True,False    
# if not rule1:
#     print(f'Only if Rule 1 is {rule1} go here')
# elif not rule2:
#     print(f'Only if Rule 2 is {rule2} go here')
# else: 
#     print(f"Not Rule 1 is {not rule1}")
# ~~~

# ### Nested *if* example (see Indentation!!!)
# ~~~python
# var1, var2 = 'CRTX','FPN'
# 
# if var1 == 'CRTX':
#     if var2 == 'FPN':
#         print(f'The {var2} is part of the {var1}')
# ~~~

# ### Ternary operator
# 
# - Python supports ternary in a nice way 
# - If you don't know what ternary operator and want to dive in the rabbit hole check this [link](https://en.wikipedia.org/wiki/%3F:) 
# - However, for our cases, it is just a short form of conditional statements that takes the following form: 
# 
# ```python
# one_line = 'yes' if expression==True else 'no'
# ```

# ### Here's an example
# 
# ~~~python
# age = 13
# teen = True if age>=13 and age <=18 else False
# print(f'It is {teen} that you are a teen if you are {age}')
# ~~~
# 

# ## Conditional Loop *While*
# 
# - The idea of conditional statements can be combined to generate a statement that will repeat until the condition is no longer valid.
# - The general syntax of a while loop is:
# 
# ~~~python
# while condition:
#     do something until condition is False
# else:
#     do once and exit the loop
# ~~~

# ### Simple example
# 

# In[2]:


counter = 20
while counter>0:
    print(f'{counter}',end='|')
    counter -= 1


# ### While loops are dangerous 
# - Think what will happen if you type + instead of minus in the previous example
# - Unless we add another condition, this loop will run forever 
# - When this happens by mistake, you can always use the stop icon at the top to break the loop

# ### Lets add conditional fences

# In[3]:


counter = 30
while counter > 0 and counter < 50:
    print(f'{counter}',end='|')
    counter += 1
else: 
    print(f'\n\nDone !!')


# 
# `````{admonition} Challenge
# How would I change the code above so it will output a sequence that ends with 50 instead of 49
# ````{dropdown} Solution 
# ```{code-block} python
# # Option one change the upper fence conditional statement to include 50
# while counter>0 and counter<=50:
#     print(f'{counter}',end='|')
#     counter += 1
# else: 
#     print(f'\n\nDone !!')
# # Option two change the upper fence conditional statement to include 50    
# while counter>0 and counter<51:
#     print(f'{counter}',end='|')
#     counter += 1
# else: 
#     print(f'\n\nDone !!')
# ```
# ````
# `````

# ### We can adjust the loop internaly using *break*, *continue* and *pass* 
# - We can use control statements in our loops to add additional functionality for various cases
# - `Break` Breaks out of the current loop.
# - `Continue` Goes to the top of current loop
# - `Pass` do nothing 

# #### Why do we need a control statement that does nothing? 
# - Python requires that code blocks (after if, except, def, class etc.) will not be empty.
# - Empty code blocks are however useful in a variety of different contexts
# - One main one is during implementation as a place holder to remember to deal with
# - let's test this with some silly function 

# In[4]:


num = -5
while num<5:
    if not num % 2: # Even numbers are divided by 3
            print(f'f({num})={num/3:.3f}')
    elif num<0: # odd negative numberes become positive
        print(f'f({num})={(num**2)**.5:.3f}')
    else: # Otherwise, I still haven't decided 
        pass
    num+=1


# `````{admonition} Challenge
# Add a rule that is applied on the odd positive numbers
# ````{dropdown} Solution 
# ```{code-block} python
# # Here is one possible solution
# num = -5
# while num<5:
#     if not num % 2: # Even numbers are divided by 3
#             print(f'f({num})={num/3:.3f}')
#     elif num<0: # odd negative numberes become positive
#         print(f'f({num})={(num**2)**.5:.3f}')
#     else: # Otherwise, I still haven't decided 
#         print(f'f({num})={(-num**3)**.5:.3f}')
#     num+=1
# ```
# ````
# `````

# `````{admonition} Challenge
# Change the code to go from -50 to 50 with steps of 10
# ````{dropdown} Solution 
# ```{code-block} python
# # Here is one possible solution
# start_condition = -50
# stop_condition = 50
# num = start_condition
# steps = 10
# while num<stop_condition:
#     if not num % 20: # Even numbers are divided by 3
#             print(f'f({num})={num/3:.3f}')
#     elif num<0: # odd negative numberes become positive
#         print(f'f({num})={(num**2)**.5:.3f}')
#     else: # Otherwise, I still haven't decided 
#         print(f'f({num})={(-num**3)**.5:.3f}')
#     num+=steps
# ```
# ````
# `````

# In[5]:


start_condition = -50
stop_condition = 50
num = start_condition
steps = 10
while num<stop_condition:
    if not num % 20: # Even numbers are divided by 3
            print(f'f({num})={num/3:.3f}')
    elif num<0: # odd negative numberes become positive
        print(f'f({num})={(num**2)**.5:.3f}')
    else: # Otherwise, I still haven't decided 
        print(f'f({num})={(-num**3)**.5:.3f}')
    num+=steps


# ### `range()` function is a useful way to control loops
# - The `range()` generates a sequence of numbers and is immutable 
# - It takes one to three input arguments (i.e. start, stop and step)
# - The stop is not included 
# - [Click on this link to learn more about the range object](https://treyhunner.com/2018/02/python-range-is-not-an-iterator/#:~:text=Unlike%20zip%20%2C%20enumerate%20%2C%20or%20generator,range%20objects%20are%20not%20iterators.)

# ### Using the range simplifies the task 

# In[6]:


start = -50
stop = 51
step = 10
seq = range(start,stop,step)
index = 0
while index<len(seq):
    print(seq[index],end=',')
    # do something
    index+=1


# 
# ## `for` loops using iterable objects
# - If we know in advance the sequence perhaps we don't need the condition
# - A `for` loop goes through items that are in any iterable objects
# - Iter-**able** objects are any data type that can be iterated over
# - These include strings, lists, tuples, dictionaries, sets and range

# ### Same concept using `for` and `range`

# In[7]:


start,stop,step = -50,51,10
for number in range(start,stop,step):
    # do something
    print(number,end=',')


# ### Iterators doing the hard work 
# - Iter-**ators** are the agents that perform the iteration.
# - An iterator is an object that allows us to go over a sequence one element at a time using the `iter()` function and the `next` method
# - There is a big difference between an iterable object and an iterator derived from that object: the former has no memory, while the latter is like a stack -- with each use of it you have one fewer element in the stack
# 

# #### Let's look at another example
# - Compare the output below 

# In[8]:


for i in range(3):
    for number in range(-50,51,10):
        print(number,end=',')
    print(f'- #{i} iter')   


# - To this section of code

# In[9]:


range_iterator = iter(range(-50,51,10))
for i in range(3):
    for number in range_iterator:
        print(number,end=',')
    print(f'- #{i} iter')  


# - And this one

# In[10]:


for i in range(3):
    range_iterator = iter(range(-50,51,10))
    for number in range_iterator:
        print(number,end=',')
    print(f'- #{i} iter') 


# ### Using `enumerate()` function to keep index 
# - enumerate is a function that returns an enumerate object that produces a sequence of tuples, and each of the tuples is an index-value pair.
# 

# In[11]:


seq = range(5,15,2)
enumerated_seq = enumerate(seq)
list(enumerated_seq)


# `````{admonition} Discussion
# Why do we need a function like this? 
# Try to come-up with some ways that one can use it
# `````

# #### lets answer with an example 
# - Here we take a list of names and map out a possible abbreviation name pair 

# In[12]:


lobe_names = ['frontal','parietal','temporal', 'occipital','insula']
lobes_mapper = {}
for index,lobe in enumerate(lobe_names):
    lobes_mapper[index+1] = {'abbreviation':lobe[:3].upper(),'name':lobe}
lobes_mapper


# #### Let's unpack the whole thing
# 
# | Code | Explenation | Data structures  | 
# | :--- |:--- |:--- |
# | `lobe_names = ['frontal','parietal','temporal', 'occipital','insula']` | Assign list with strings to a variable | `list`, `variable` | 
# | `lobes_mapper = {}` | Create an empty dictionary and assign it to a variable named lobes_mapper| `variable`,`dict` | 
# | `for index,lobe in enumerate(lobe_names):` | Declare a for loop that iterates over all the elements in lobe_names using enumerate to construct an index value pair, and unpack that pair to the two variables  index and lobe | `variable`, `tuple`, `list` `iterator` |
# | `lobes_mapper[index] = {'abbreviation':lobe[:3].upper(),'name':lobe}` | Create a dictionary with two keys and two values. In the first pair, we transform the first three letters into uppercase and assign them to the key abbreviation. The second pair simply adds the lobe name to the key. We can now assign this local dictionary to the lobes_mapper dictionary we created at the beginning, with the key being the current  index +1| `dict` | 
# | `lobes_mapper` | print out the contents of the dict to the screen  | `dict` |

# ## What are list comprehensions?
# 
# - List comprehension is a way to define and create lists building on existing lists.
# - The syntax is elegant `some_list = [expression for item in list]`
# - Consider the following example:

# In[13]:


grid = []
for row in range(5):
    grid.append(list(range(5)))
grid   


# - Now compare it to this form: 

# In[14]:


grid = [list(range(5)) for row in range(5)]
grid


# ### Nested List comprehensions rotated grid example 
# - In the same way we can created hierarchy in for loops we can create nested lists
# 

# In[15]:


grid_rot90 =[]
for col in range(5):
    tmp = []
    for row in grid:
        tmp.append(row[col])
    grid_rot90.append(tmp)   
grid_rot90 


# `````{admonition} Challenge
# Now try to rewrite the code using list comprehensions 
# ````{dropdown} Solution 
# ```{code-block} python
# grid_rot90 = [[row[col] for row in grid] for col in range(5)]
# ```
# ````
# `````

# ## Using `zip()` to create complex combinations
# - Zip creates an iterator of tuples, where each tuple contains the i-th element of each argument sequence or iterable. When the shortest input iterable is exhausted, the iterator stops. 

# In[16]:


num_list = list(range(1,7))
str_list  = list('string')
result = list(zip(num_list[::-1], str_list))
result


# ### In contrast to enumerate we are not limited to two lists 

# In[17]:


num_list = list(range(1,7))
str_list  = list('string')
result = list(zip(num_list[::-1], str_list,num_list))
result


# ### Zip has the ability to unpack a list of tuples as well

# In[18]:


a1,a2,a3 = zip(*result)
print(a1)
print(a2)
print(a3)


# ## Links to expand your understanding 
# 
# For those interested in learning more...
# 
# - [Python Range() Function](https://www.datacamp.com/community/tutorials/python-range-function)
# - [Playing with iterators](https://campus.datacamp.com/courses/python-data-science-toolbox-part-2/using-iterators-in-pythonland)
# - [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
# - [list-comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
# - [Zip](https://docs.python.org/3/library/functions.html#zip)
