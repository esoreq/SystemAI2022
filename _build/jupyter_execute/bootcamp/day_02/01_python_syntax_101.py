#!/usr/bin/env python
# coding: utf-8

# # PYTHON SYNTAX 101
# 
# ## What is a syntax
# 
# Syntax is the way words work together to make sentences, clauses, and phrases. "Syntax" means "arrange together," as well as "study of the syntactic properties of a language." The syntax of a computer language is the set of rules that define the combinations of symbols that are considered correct for that language.
# 
# 

# ## Syntax Essentials and Best Practices
# 
# One of the trickiest things for Python newcomers to adapt to is the syntax. 
# In this opening section, I'll go over some syntax essentials as well as some formatting best practices.
# This will help you keep your code consistent and hopefully elegant.
# 

# ### Syntax Essentials rules
# 
# 1. A naming convention simplifies collaboration - use them
# 1. Code blocks are defined by indentation (can be either space or tab)
# 1. Try to avoid using more than one statement per line
# 1. Python is case sensitive : $vara \neq  varA$
# 1. Path specification uses forward slashes (regardless of OS): `~/user/home`
# 1. There is no need to add a command terminator `;`
# 1. You can combine two executable statements using a semicolon `;`  (but avoid that if you can)
# 1. String literals can be defined using single `'` double `"` or even triple `'''` quotes 
# 1. It is considered good conduct to keep lines of code short 
# 1. Backslash \\ can be used to stack lines of code together
# 1. Expressions enclosed in brackets i.e. (), [] or {} don't need a backslash
# 1. Comments in Python begin with a hash mark (#) and whitespace character and continue to the end of the line. 
# 1. Keywords are protected and should not be used as variables
# 
# 

# ### Python statements are executed in a serial way
# A statement is a piece of code that can be executed by a Python interpreter.
# The simplest way to explain this is to argue that any Python code is a statement.
# To indicate the end of a statement, the token NEWLINE character is used. 
# Each statement in a Python script is represented by a line of code.

# In[1]:


print('This is a print statement')


# ### Code blocks are defined by indentation
# 
# A Python program is constructed from code blocks. A block is a piece of Python program text that is executed as a unit. 
# 

# In[2]:


if True: 
    print("I am part of a code block")
    print("I am also part of the same code block")


# 
# ### Indentations for structure
# - In contrast to the closing statements common in Bash (such as fi) or MATLAB (such as end) Python uses indentations to understand the structure of your code.
# - So you should make sure to use indentations correctly and consistently.
# - This makes code more straightforward to read and ultimately understand 
# - Indentations can be created using either tabs or spaces (usually four spaces) 
# - If the indentations are mixed the code will fail to excute 
# 

# In[3]:


print(brain_lobes[0])
    print(brain_lobes[0])


# ### Try to avoid using more than one statement per line
# 
# - Using the semi-colon symbol you can combine multiple statements in one line
# - However, If you put a line break in the wrong place, you will get an error message. 
# - To avoid that you should have one statement per line.
# - As with all rules, there are some exceptions some of which we will cover later in the course

# ### Naming convention simplifies collaboration
# 
# A naming convention is a set of rules for selecting the character sequence that should be used to name different data types and data structures. This can be confusing if you have little background. So without going into what the following are (we will discuss them as we continue) I would like to lay them out for future reflection.
# 
# | Identifier  | Example  |  Commonly used for  | 
# | :--- | :--- | :--- | 
# | single lowercase letter | `x` | mathematical notation variables  |  
# | single uppercase letter | `X` | mathematical notation variables |  
# | lowercase sequence | `lowercase` |  variables, modules, functions and package|  
# | uppercase sequence  | `UPPERCASE` | Constants |  
# | Snake lowercase | `lower_case_with_underscores` | Variables and functions|  
# | Snake uppercase | `UPPER_CASE_WITH_UNDERSCORES` | Constants |  
# | Camel case | `CamelCase` | Class |  
# | mixed case | `mixedCase` | ? |  
# | Camel snake case | `Camel_Snake_Case` | ? |  
# | single leading underscore | `_single_leading_underscore` | weak "internal use" indicator. E.g. from M import * does not import objects whose name starts with an underscore. |  
# | single trailing underscore | `single_trailing_underscore_` | Single trailing underscore naming convention is used to avoid conflicts with Python keywords. |  
# | double leading underscore | `__double_leading_underscore` | private variables and methods inside a class |  
# | single trailing underscore | `__double_leading_and_trailing_underscore__` | "magic" objects or attributes that are built in the language (e.g. `__init__`) |  
# 

# 
# ### Explicit line joining 
# - Using a backslash `\`, we can break long commands across many lines 
# - Using code that is longer than 80 char is perceived as bad practice 
# 
# 
# 

# In[3]:


print ('Multi line command')


# 
# ### Many commands in single line 
# - Using the semicolon \; we can achieve the opposite, i.e. to combine multiple commands in one line
# 
# 

# In[ ]:


print('Multi');print('Line');print('Output')


# ###  Implicit line joining
# 
# - Expressions in parentheses, square brackets or curly braces can be split over more than one physical line without using backslashes. 
# 
# 

# In[4]:


brain_lobes = ['Frontal',
               'Parietal',
               'Occipital',
               'Temporal']
print(brain_lobes)


# ### Comments Are Marked by `#`
# 
# ***"Code is more often read than written."***
# ***Guido van Rossum***
# 
# - It is important to add comments to your Python code. 
# - To do this use the # character, everything that comes after it won't be executed.
# 

# In[ ]:


print("This will run.")  # This won't run


# ### Commenting your code serves multiple purposes
# 
# - Planning and Reviewing, i.e. outline of the desired functionality of some future code
# - Code Description, i.e. explain the intent of specific sections of code
# - Algorithmic description, i.e. explain how the algorithm works or how it's implemented within your code or even add a link to the source
# - Tagging, i.e. label specific sections of your code where you need to take action, e.g. BUG, FIXME, TODO, UPGRADE.
# - Comments should be short, sweet, and to the point.
# 
# ***"Code tells you how; Comments tell you why."***
# ***Jeff Atwood (aka Coding Horror)***
# 
# 

# ### Use Multiline Comments 
# 
# - Multi-line comments can be achieved primitively using :
# 
# #### multiple stacking of hashtags #

# In[6]:


# This 
# is 
# stacking 


# #### Alternatively, docstrings can be used by combining three commas 
# 

# In[8]:


def some_function(arg1): 
    """Summary line. some_function will do some thing with arg1
  
    Extended description of the function. 
    some_function will get arg1 and do things with it
    some of the things are complex, and some are simple
    some_function will then return some value.  
    
    Parameters: 
    arg1: the thing we will do stuff to 
  
    Returns: 
    some_value_back 
    """
    some_value_back  = arg1 * 5
    return some_value_back


# ### Python Keywords
# 
# - Keywords are the reserved words in Python.
# - You cannot use a keyword as a variable name, function name or any other identifier. 
# - These 35 keywords are used to define the syntax and structure of the Python language.
# - To examine them you can run the following code 
# 

# In[9]:


import keyword
print(keyword.kwlist)


# ### Case matters
# 
# - Python is case sensitive. 
# - This means the **HELP** is not equal to **help**
# - Most of Python keywords are written with lowercase letters.
# - Notable exceptions to this rule are True and False boolean values and the **None** variable that all use a mixture of cases. 
# 

# In[10]:


print("HELP"=="help")


# ### Variable Names
# 
# ***Code is read much more often than it is written***
# ***Guido van Rossum 2001***
# 
# 
# 1. Variable names should use lowercase.
# 1. Variable names cannot:
#     - Start with a number
#     - Contain spaces
#     - Use any of these symbols : `'",<>/?|\()!@#$%^&*~-+`
# 1. Avoid using the characters:
#     - 'l' (lowercase letter el)
#     - 'O' (uppercase letter oh)
#     - 'I' (uppercase letter eye)
# 1. short_names vs long_name
# 1. long_names should be separated using the underscore symbol (_)
# 1. This makes them readable 
# 1. Remember that making variable names simple to understand minimizes the time spent on commenting 
# 

# ### Use blank lines
# 
# - Using blank lines is the simplest way to separate code blocks visually 
# - Even multiple blank lines to distinguish between different parts of the code. 
# - It won't affect the result of your script.

# 
# ### Use white spaces 
# 
# - Python allows white spaces in assignment 
# - This makes nicer looking code 
# 

# In contrast to bash where you are not allowed to use white space in assignment
# 
# ````{error}
# Try running the following code in your terminal 
# ```{code-block} console 
# NUM2 = 4 
# ```
# ````
# 
# Python ignores white spaces and all of these variables have the same value and will all compile 

# In[15]:


num_01 = 4 
num_02=4
num_03 =4
num_04 =            4
print(num_01 == num_02 == num_03 == num_04)


# ### Underscore `_` in Python
# 
# Python's underscore `_` is a unique character. It can be used for many different purposes.
# During this week we will use some of these cases so for the sake of completeness
# 
# 
# 1. Stores the value of the last expression executed
# 1. Leaving out values in different situations (in practice, we just store them on a  temporary variable) 
# 

#  ### Imports best practice 
# 
# Python is a community effort and it relies on many different modules and packages that can be imported to be used in various situations. 
# This is similar to a library in R.  
# We will go over this in detail tomorrow, but it should be stated. 
# 
# - Use **import x** for importing packages and modules.
# - Use **from x import y** where x is the package prefix, and y is the module name with no prefix.
# - Use **from x import y as z** if two modules named y are to be imported or if y is an inconveniently long name.
# - Use **import y as z** only when z is a standard abbreviation (e.g., np for NumPy). -->
# 

# ### Syntax Essentials rules recap
# 
# 1. A naming convention simplifies collaboration - use them
# 1. Code blocks are defined by indentation (can be either space or tab)
# 1. Try to avoid using more than one statement per line
# 1. Python is case sensitive : $vara \neq  varA$
# 1. Path specification uses forward slashes (regardless of OS): `~/user/home`
# 1. There is no need to add a command terminator `;`
# 1. You can combine two executable statements using a semicolon `;`  (but avoid that if you can)
# 1. String literals can be defined using single `'` double `"` or even triple `'''` quotes 
# 1. It is considered good conduct to keep lines of code short 
# 1. Backslash \\ can be used to stack lines of code together
# 1. Expressions enclosed in brackets i.e. (), [] or {} don't need a backslash
# 1. Comments in Python begin with a hash mark (#) and whitespace character and continue to the end of the line. 
# 1. Keywords are protected and should not be used as variables

# 
# ## Links to expand your understanding 
# 
# For those interested in learning more...
# 
# - [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)  
# - [PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)  
# - [The Zen of Python](https://www.python.org/dev/peps/pep-0020)  
# - [PEP-8 Tutorial: Code Standards in Python](https://www.datacamp.com/community/tutorials/pep8-tutorial-python-code?)
# 
