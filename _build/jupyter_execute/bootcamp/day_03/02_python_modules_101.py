#!/usr/bin/env python
# coding: utf-8

# # PYTHON MODULES 101
# 
# ## Modules and Packages
# 
# - Python core language is compact. 
# - This is an intentional design feature to maintain simplicity. 
# - Much of the powerful functionality comes through external modules and packages.
# 
# 
# ###  What is a Module?
# - A module is simply a file with the `.py` extension, containing Python definitions, functions, and statements. 
# - Modules are imported from other modules using the import command.
# - The first time a module is loaded into a running Python script, it is initialized by executing the code in the module once.
# - If we change the module, we need to reload it for these changes to take effect
# 
# ### Modules are useful because they:
# 
# 1. Simplify your code by calling readable functions instead of multiple lines of code
# 2. Make it simpler to maintain, improve and collaborate 
# 3. Allow you to organize your code in different files (each a different module)
#     
# 
# ### Why use Modules? 
# 
# - Using modules, you can break down large programs into smaller, more manageable pieces. 
# - Code can also be reused through modules.
# - Instead of copying their definitions between different programs, we can create modules for our most commonly used functions.
# - a module is also the simplest way to share code with a collaborator
# 

# ### my_module example
# - Jupyter notebooks have a nifty thing called magic functions 
# - In the next session we will go over some of them in detail 
# - For now I will use magic to simplify the creation of a python script to act as my first module 
# - This file can be generated using magic or by creating a text file and renaming it. 
# - The example is not intended to be considered good practice, but rather to illustrate some functionality in general. 
# 

# In[1]:


get_ipython().run_cell_magic('writefile', 'my_module.py', 'sum_sq = lambda data: sum(x ** 2 for x in data)\nmean = lambda data: sum(data)/float(len(data))\nsq_mean = lambda data: sum_sq(data)/float(len(data)-1)\nvar = lambda data: sum((x - mean(data))**2/float(len(data)-1) for x in data)')


# `````{admonition} Imports best practice 
# - Use **import x** for importing packages and modules.
# - Use **from x import y** where x is the package prefix, and y is the module name with no prefix.
# - Use **from x import y as z** if two modules named y are to be imported or if y is an inconveniently long name.
# - Use **import y as z** only when z is a standard abbreviation (e.g., np for NumPy).
# `````

# ###  Using import to load my_module
# - Once the file is in the same folder as my notebook we can use import to load it 

# `````{admonition} Challenge
# - In a code cell use import to load `my_module`
# - Also use from x import y to load the lambda function `var` from `my_module`
# ````{dropdown} Solution 
# ```{code-block} python 
# import my_module
# from my_module import var
# ```
# ````
# `````

# ### How does importing in Python work?
# 
# - One limitation of the import approach is that it explicitly loads the contents of the script into the memory as an object 
# - For efficiency reasons, when you import a module in an interactive Python session, the Python interpreter executes two operations: It begins by determining if the module is already stored in the sys.module dictionary. And only if it is absent does it import the module. Python will ignore this request if you have previously imported the module (or imported another module that references it) and you attempt to import it again.
# - This means that if we change the file (by adding a function to it for example) we will need to re-import it to make it accessible  

# ### Using introspection to look under the hood
# - Using `dir` and `type` on `my_module` is revealing (look below) 
# - my_module is an object (everything in python is an object) of type module 
# - And it has as methods the different lambda functions we just created

# In[2]:


type(my_module)


# In[10]:


dir(my_module)


# ### How to reimport a module?
# - Often we want to change code that exists in a module we are developing for various reasons. 
# - The easiest way reload a module is to quit your interactive session and start it again. 
# - This also means you need to rerun all steps leading to that point which might not be very wise or efficient.
# - Working in a non-interactive settings the only way to reload your module to reflect change is via a module called `importlib`

# In[ ]:


import importlib
importlib.reload(my_module)


# #### In the jupyter interactive settings there are alternatives 
# - One option is to not use import and simply load the module into memory using the magic function `%run`
# - You can rerun a file as many times as you want and it will always update all the functions.
# - Running a file in IPython is extremely easy.

# In[ ]:


get_ipython().run_line_magic('run', 'my_module')


# ####  Using cache to keep my_module alive 
# 
# - In Jupyter we have another set of magic commands that deal with that 
# - The `%autoreload` magic command can be used to automatically track changes in any module and update them when a change occurs. 
# - Because it’s not enabled by default, you have to load it as an extension using a different magic command called `%load_ext`
# - So the first step is to call `%load_ext autoreload` that makes the `autoreload` command active 
# - Then use it 
# - There are 3 configuration options for the `autoreload` you can set
#   - `%autoreload 0` - disables the auto-reloading. This is the default setting.
#   - `%autoreload 1` - it will only auto-reload modules that were imported using the `%aimport` function 
#   - `%autoreload 2` - auto-reload all the modules. Great way to make writing and testing your modules much easier.
# - In the context of this course we will use `%autoreload 2`

# `````{admonition} Challenge
# - Update your import cell to contain the reload magic commands
# - Also use the `as` format to rename `my_module` to `utils`
# ````{dropdown} Solution 
# ```{code-block} python 
# import my_module as utils
# %load_ext autoreload
# %autoreload 2
# ```
# ````
# `````

# #### Lets test our module 
# - If you did everything so far you should get the same result as me
# 

# In[14]:


print(utils.var(list(range(3,20))))


# ###  Extend your module by adding sample standard deviation
# 
# 
# 
# `````{admonition} Challenge
# - The standard deviation of the sample mean is defined using the following formula 
# - $ s = \sqrt{\frac{1}{N-1}\sum^n_{i=1} (x_i-\bar{x})^2} $
# - Try to implement your std function and place it into your module file
# ````{dropdown} Solution 
# ```{code-block} python 
# %%writefile -a my_module.py
# std = lambda data: var(data)**0.5
# ```
# - Here I am using `-a` argument with magic %%writefile to append the line to the end of the file 
# - But you could have just opened the file and added the line manually 
# ````
# `````
# 

# ###  Testing your code against some gold standard package
# 
# 
# - We sometimes create our own mathematical functions for a variety of reasons
# - Testing these with established modules is a good habit to have
# - Recall that the assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.
# - You can write a message to be written if the code returns False, check the example below.
# 
# 

# In[15]:


import statistics 
seq = list(range(3,20))
assert utils.std(seq) == statistics.stdev(seq)
assert utils.var(seq) == statistics.stdev(seq) ,"variance is not equal to standard deviation" 


# ### We can call a module from within a function
# - Consider the code below 
# - We created a function that imports a module called datetime from a Python package called  datetime
# - It is safe to assume that this is a module that deals with dates and times
# - Because it was imported inside the functions scope it is only available to the function itself 
# 

# In[18]:


def temporal_hello():
    from datetime import datetime,time
    local_dt = datetime.now()
    if (time(6) < local_dt.time() < time(12)): 
        print("Good Morning")
    elif (time(12) < local_dt.time() < time(18)):    
        print("Good Afternoon")
    else:
        print("Good night") 


# In[19]:


temporal_hello()


# ### Import datetime to the main scope
# - Let's the anatomy of the datetime module using `dir`

# In[25]:


import datetime 
dir(datetime)


# ### Every module has a physical file associated with it 
# - In Python every module has a file that can be examined
# - This can be identified using the `__file__` property 
# - Using another nifty magic command we can peak into that file  

# In[26]:


datetime.__file__


# In[24]:


get_ipython().run_cell_magic('bash', '', 'head -n 20 /opt/anaconda3/envs/dcarte_tutorials/lib/python3.10/datetime.py')


# ### The module anatomy 
# - We see a docstring at the beginning 
# - Then a weird variable named `__all__` that receives a tuple 
# - Followed by a block of imports 
# 
# #### What does __all__ do?
# - It declares the semantically "public" names from a module. 
# - If there is a function name in __all__, it will be available when starr import the module contents to the scope.
# - However, if you omit __all__ in a module, the "starred import" will import all names (not starting with an underscore) defined in the module.

# ### Why does datetime have datetime inside? 
# = This is not a meta thing but rather an organizational tool
# - A module can have modules or classes contained inside it
# - In Python 3.0, user-defined class objects are instances of the object named type, which is itself a class.
# - We will go over this later on today

# In[34]:


from datetime import datetime
print(type(datetime))


# - This higher level of abstraction comprises modules or classes that can work independently, but have a common function in terms of time, and are thus part of the datetime  package.
# 

# ## How to define a package
# 
# - Packages are a way of structuring Python’s module namespace by using “dotted module names”
# - They are simple directories, containing several python scripts.
# - Defining a package in Python requires a unique folder name and used to require a special file called `__init__.py`
# 
# ### Make a directory called my_package
# 
# - We will use Jupyter magic to change the cell to `%%bash`
# - Use `mkdir` to create a folder 
# - Use `mv` to move and rename `my_module.py` into the newly created folder `my_package`
# - Finlay create an empty python file called `__init__.py` in `my_package` using `touch`
# 

# In[36]:


get_ipython().run_cell_magic('bash', '', 'mkdir -p my_package\n#rename the file and move it into my_package\nmv my_module.py my_package/my_stats.py \ntouch my_package/__init__.py ')


# ### Can we do the same using Python? 
# - We can using a module :) 
# - To achieve exactly the same chain of events (and some more) we will use the `Path` module
# - We will use the `mkdir` and `write_text` functions 
# - One limitation by design is that the Path module does not support appending text
# - This is only a means to teach you how to use the module to interact with the file system in an OS agnostic way
# - Pay close attention to the use of `__all__` in this context, I am only giving the user of my module access to the functions declared there. 

# In[40]:


from pathlib import Path

utils = Path('utils')
utils.mkdir() #make the directory 
(utils / '__init__.py').write_text("from .my_stats import *")
my_stats_module = utils / 'my_stats.py'
my_stats_module.write_text("""
__all__ = ['var','std']
sum_sq = lambda data: sum(x ** 2 for x in data)
mean = lambda data: sum(data)/float(len(data))
sq_mean = lambda data: sum_sq(data)/float(len(data)-1)
var = lambda data: sum((x - mean(data))**2/float(len(data)-1) for x in data)
std = lambda data: var(data)**0.5
""")


# In[41]:


import utils
dir(utils)


# In[42]:


utils.std(list(range(3,20)))


# ## Links to expand your understanding 
# 
# For those interested in learning more...
# 
# - [Modules in python](https://docs.python.org/3/tutorial/modules.html#modules)
# - [Packages in python](https://docs.python.org/3/tutorial/modules.html#packages) 
# 
# 
