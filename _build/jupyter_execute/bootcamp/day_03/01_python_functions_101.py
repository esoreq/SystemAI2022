#!/usr/bin/env python
# coding: utf-8

# # PYTHON FUNCTIONS 101
# 
# ## What are Functions?
# - Python is full of functions: we've already encountered a variety of built-in functions that can be used for many different tasks. It is likely, however, that it will be necessary for you to write your own functions to deal with problems that your data presents.
# - A function is a sequence of statements in a certain order, with a unique name that can be called upon to be executed. 
# - When it is executed the sequence is re-used again. 
# 
# Functions in Python fall into three types:
# - Built-in functions (all the functions we have used so far are considered built-in)
# - Lambda or anonymous functions are very similar to the mathematical definition above; they receive input and return it after applying some rule or expression. 
# - General purpose functions that are created to do something useful.
# 
# ## What are Functions good for?
# 
# The two most important reasons that we use functions are *reusability* and *abstraction*
# 
#  - Reusability: Once defined, a function can be used repeatedly. By reusing functions in your program, you can save time and effort.
# - Abstraction. To use a particular function, you have to know its name, its function, the arguments you need to give it, and what results you will receive.
# - Writing large programs that actually work is possible because of the ability to break them up into many abstract, reusable parts.
# 

# ## Creating and Calling a Function
# 
# - In Python a function is defined using the def keyword:
# 

# In[1]:


def my_first_function():
  print("Hello from my first function")
type(my_first_function)  


# - You call a function, using it's name followed by parenthesis
# 

# In[2]:


my_first_function()


# ## Parameters, Arguments and Function scope
# 
# - A parameter is a variable name declared when the function is created.
# - Normally, a variable is only available from inside the region it is created. This is called scope.
# - Parameters are specified after the function name, inside the parentheses. 
# - Arguments are the data you pass into the method's parameters
# - You can add as many parameters as you want, just separate them with a comma.
# 
# - Consider the following example: 
# 

# In[3]:


def my_second_function(first_name):
  print(f"Hello this function is {first_name}'s second function")
my_second_function('eyal')


# ### What will happen if we run our function without passing an argument?
# 
# `````{admonition} Try it 
# ~~~python
# my_second_function() 
# ~~~
# `````

# - When creating a function you declare what is the minimum amount of data the function requires in order to run
# - By adding a default value, we can fix the above problem
# 

# In[4]:


def my_second_function(first_name='eyal'):
  print(f"Hello this function is {first_name}'s second function")
my_second_function()


# ### Number of Arguments
# 
# - What will happen if we add another argument not declared in the function scope
# 
# 
# `````{admonition} Try it 
# ~~~python
# my_second_function('Eyal','Soreq') 
# ~~~
# `````
# 
# 
# 

# ### Consider the following example: 
# 
# ~~~python
# last_name = 'soreq'
# def my_third_function(first_name):
#     print(f"Hello this function is {first_name} {last_name} third function")
# my_third_function('eyal')  
# ~~~
# 
# #### What do you think will happen?

# - In Python, whenever a function is called, a dictionary of name-value pairs is searched for arguments needed. 
# - The process begins with the local scope, moves to the enclosing scope, then moves to the global scope, and ends with the built-in scope. 
# - If the  variable name cannot be found, an error will be returned
# 

# ### To emphasis this, I will explicitly delete `last_name` using the function `del`
# 
# ~~~python
# del last_name
# def my_third_function(first_name):
#     print(f"Hello this function is {first_name} {last_name} third function")
# my_third_function('Eyal')  
# ~~~
# 
# #### What do you think will happen now?
# 
# 

# ### Let's add a last name  parameter
# 

# In[5]:


def my_fourth_function(first_name='eyal',last_name='soreq'):
    print(f"Hello this function is {first_name} {last_name}'s fourth function")
my_fourth_function()


# ## Functions are objects of type function
# - Every time you create a function you are in fact creating an instance of type function 
# - This means that you have all the different methods the developers of Python thought a function should have
# 
# 
# `````{admonition} Challenge
# Use the right introspection function to list the methods `my_fourth_function` has
# ````{dropdown} Solution 
# ```{code-block} python 
# dir(my_fourth_function)
# ```
# ````
# `````

# ## `return` values from a function
# 
# - If we define a function without returning anything, it returns `None`
# 

# In[6]:


function_value = my_fourth_function()
print(function_value)


# - We can use the protected keyword `return` to give the function the ability to return values

# In[7]:


def my_fourth_function(first_name='eyal',last_name='soreq'):
    full_name = f'{first_name} {last_name}'
    print(f"Hello this function is {full_name}'s fourth function")
    return full_name
full_name = my_fourth_function()
print(full_name)


# ### `return` more than one value
# 
# - A function in python can return more than one value 
# - In fact it returns a tuple of the objects
# - Let's try this 

# In[8]:


def multiple_returns(arg):
    return arg,arg*2,arg*3,arg*4
value = multiple_returns(3)
print(value)
print(type(value))


# ### Unpack multiple values 
# 
# - If we know the number of values a function returns we can unpack the tuple to individual variables
# 

# In[9]:


a,b,c,d = multiple_returns(3)
c


# ````{admonition} Test it
# What will happen if we have more variables than output values?
# ```{code-block} python 
# a,b,c,d,e = multiple_returns(3)
# ```
# ````

# ### Unpack creatively
# 
# - If we don't know the number of values a function returns (but we know it's at least more than one) we can use star unpacking to do some creative unpacking 
# 

# In[10]:


a,*b,c = multiple_returns(3)
b


# ### Pass variable number of arguments
# - Using ths same logic we can create a function that can receive arbitrary number of variables

# In[11]:


def multiple_inputs(*args):
    output = [arg**i for i,arg in enumerate(args)]
    return output
a,b,*c = multiple_inputs(2,5,7,8)
c


# ### Pass multiple keyword arguments 
# - A neighbour of the `*args` statement is the `**kwargs` one
# - The key take home idea here is that you are creating a function that can get any number of key argument pairs which we will use extensively on Thursday when we go over visualization tools in Python

# In[12]:


def multiple_kwargs_inputs(**kwargs):
    output = [f'{key}_{value}' for key,value in kwargs.items()]
    return output
multiple_kwargs_inputs(one=1,two=2)


# ### Conditional returns 
# - A function can use conditional statements to return different values based on the condition
# - In this example I am introducing a new keyword `in` that allows us to check if a variable exists in an iterable 
# - 

# In[13]:


def conditional_return(number):
    if type(number) in [float,int]:
        return number**2
    else:
        print('This function requires a number')
        return False
conditional_return('test')


# ## Documenting functions 
# - Functions in Python have a unique property called a docstring 
# - It is the ability to document the function in a way that can be used later 
# - Remember you are documenting at first for your future self 
# - While we are at it, it is useful to name function explicitly to declare their utility
# 

# In[14]:


def output_bespoke_greeting(first_name='eyal',last_name='soreq'):
    """output_bespoke_greeting personalised greetings printed

    output_bespoke_greeting get's a person first and last name merges them
    and outputs a personalised greeting
    It also returns a full name composed of the two names

    Args:
        first_name (str, optional):  Defaults to 'eyal'.
        last_name (str, optional):  Defaults to 'soreq'.

    Returns:
        full_name (str): the full name in title mode combining the first and last names
    """
    full_name = f'{first_name.title()} {last_name.title()}'
    print(f"Hello this function is {full_name}'s fourth function")
    return full_name


# ### Once defined we will can use help to remind us of the function requirements
#   

# In[15]:


help(output_bespoke_greeting)


# ## Some useful built-in functions
# - Yesterday we used several built-in functions 
# - Today we will add several more to the pile
# - This is to illustrate the utility and versatility of generalised functions

# ### What is the map function
# 
# - The map function allows you to "map" a function to an iterable object. 
# - in other words, we call the same function for every item in an iterable, such as a list. 
# - For example, the function below is used to convert numeric age to a categorical age_group.
# 

# In[16]:


def age_group(age):
    if age<=11:
        return 'children'
    elif age<=21:
        return 'teens'
    elif age<=65:
        return 'adults'
    else: 
        return 'elderly'
age_group = list(map(age_group,  list(range(1,90,3))))
print(age_group)


# `````{admonition} Challenge
# Change the function above to add a toddler group
# ````{dropdown} Solution 
# ```{code-block} python 
# def age_group(age):
#     if age<=5:
#         return 'toddler'
#     elif age<=11:
#         return 'children'
#     elif age<=21:
#         return 'teens'
#     elif age<=65:
#         return 'adults'
#     else: 
#         return 'elderly'
# ```
# ````
# `````

# #### what about multiple iterables?
# 
# - `map` can accept more than one iterable. 
# - However, the iterables should be the same length
# - If they are not, the shortest iterable will terminate the function
# 
# ##### Without running the code try to guess what the output will look like

# In[17]:


lobe_names = ['frontal','parietal','temporal', 'occipital','insula']
def combine_strings(a, b):
  return a[:3].upper() + b[-3:].lower()
x = list(map(combine_strings, lobe_names[1:], lobe_names[::-1]))


# ##### And what about this example

# In[18]:


def triangle(s,e):
    return list(range(s,e))
grid = list(map(triangle,  [1]*20,list(range(2,20,1))))


# ### filter function
# 
# - The filter function creates an iterator containing only items for which a function(item) is true. 
# - In other words, similar to map() you combine a function with a list.
# - The list is then filtered returning only **True** results.
# 

# In[19]:


def is_children(age_group):
    return age_group == 'children'
print(list(filter(is_children, age_group)))


# ### assert function/statement 
# 
# - The assert statement in Python enables you to perform sanity tests in your code. These tests are known as assertions, and you may use them to determine if particular assumptions continue to hold true as you build code. If any of your assertions are false, your code contains a flaw.
# 
# - The syntax is simple : 
# ~~~python
# assert expression[, assertion_message]
# ~~~
# 
# #### For example 
# 

# In[20]:


age = 'Ten'
def is_teen(age,teen_bounds = (11,18)): 
    assert str(age).isnumeric(), 'age needs to be a number'
    return teen_bounds[0] < age < teen_bounds[1]
is_teen(age)


# In[58]:


is_teen(15)


# ## What are Lambda functions?
# 
# - Lambda functions are anonymous functions in Python or functions with no name. 
# - It's a small and restricted function with only one  line. 
# - As with normal functions, Lambda functions can take more than one argument.
# 
# ### Python anonymous functions have three  parts:
# 1. The lambda keyword.
# 1. The parameters (or bound variables), and
# 1. The function body.
# 
# 
# ### Syntax
# 
# `lambda arguments : expression`
# 

# In[66]:


",".join(list(map(lambda x: f'{x**3 + x**2 - x}',range(20))))


# `````{admonition} Challenge
# Try using a lambda function to recreate the following output:
# - `0,1,10,33,76,145,246,385,568,801,1090,1441,1860,2353,2926,3585,4336,5185,6138,7201`
# - Based on the following expression $ f(x) = x^3 + x^2 - x $
# - Can you this using one line only?
# ````{dropdown} Solution 
# ```{code-block} python 
# ",".join(list(map(lambda x: f'{x**3 + x**2 - x}',range(20))))
# ```
# - This solution is just to demonstrate how to use lambda functions with the map function
# - However, writing dense lines in not uncommon in data science, therefore learning to read these lines is important
# ````
# `````

# ### Why are Lambda Expressions useful?
# 
# - A lambda function is used for creating small, one-time, anonymous function object in Python. 
# - Because a lambda function is an expression, it can be named. 
# - Multi-arguments are expressed by separating arguments with a comma (,)
# - However, Lambda expressions are rarely named - these are just to make a point
# 
# 
# 
# ### Here are some more examples 
# 

# In[ ]:


square = lambda x: x**2
product = lambda x,y: x*y
power = lambda x,y: x**y


# ### Using if else in Lambda function
# 
# - Using conditional statements (if-else) in lambda function is little tricky, the syntax is as follows 
# - if you shouted Ternary Operators pat yourself on the back
# 
# ~~~python
# lambda <arguments> : <Value if True> if <condition> else <Value if False>
# ~~~
# 

# 
# `````{admonition} Challenge
# Try using a lambda function to recreate the age2group function:
# ````{dropdown} Solution 
# ```{code-block} python 
# age2group = lambda age: 'children' if age<=11 else 'teens' if age<=21 else 'adults' if age<=65 else 'elderly'
# print(list(map(age2group,  list(range(1,30,1)))))
# ```
# ````
# `````

# ## Links to expand your understanding 
# 
# For those interested in learning more...
# 
# - [python-scope-legb-rule](https://realpython.com/python-scope-legb-rule/)
# - [lambda-expressions](https://docs.python.org/3/tutorial/controlflow.html?highlight=lambda#lambda-expressions)
# - [filter](https://docs.python.org/3/library/functions.html#filter) 
# - [writing-functions-in-python](https://learn.datacamp.com/courses/writing-functions-in-python)
# 
