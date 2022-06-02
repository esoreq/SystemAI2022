#!/usr/bin/env python
# coding: utf-8

# # PYTHON CLASSES 101
# 
# ## Python Scopes and Namespaces
# - A namespace is a mapping from names to objects. 
# - This is just a link between a name and an object 
# -  In a Python program, there are four types of namespaces:
#   - Built-In - The set of [built-in](https://docs.python.org/3/library/functions.html) function names (e.g. abs, range etc)
#   - Global
#   - Enclosing
#   - Local
# - The interpreter searches for a name from the inside out, looking in the local, enclosing, global, and finally the built-in scope
# 
# 

# ###  The Built-In Namespace
# - The built-in namespace contains the names of all of Python’s built-in objects. 
# - These are available at all times when Python is running. 
# - We can separate the built-in namespace roughly to four groups 
#   - Builtin Function Type
#   - Errors
#   - Constants
#   - Base classes (e.g. data types and other things)
# - We used the introspective function `dir` before to look into the namespace of functions (before we knew it was a namespace)  
# - In IPython which is the backbone of the Jupyter Python Kernel there are other stuff and you are welcome to go over them and search for the usage using the code below 

# In[1]:


import types
builtin_scope = dir(__builtins__)
builtin_functions = [func for func in builtin_scope if isinstance(eval(func),types.BuiltinFunctionType)]
basic_types = [func for func in builtin_scope if isinstance(eval(func),type) and not func.endswith('Error')]
errors = [func for func in builtin_scope if func.endswith('Error')]
constants = set(builtin_scope).difference(basic_types + builtin_functions + errors)


# ### The Global namespace 
# - The global namespace contains any names defined at the level of the main program. 
# - Python creates the global namespace when the main program body starts, and it remains in existence until the interpreter terminates (in the case of a notebook this is the kernel).
# - It will contain anything you add, but it will also contain many IPython specific variables (and if you are using vscode then additional vscode names)
# - It will become intractable very fast 
# - Therefore, to examine the actual variables and functions at the global level use the jupyter magic command `%whos` function that plots the user defined variables and functions 

# #### The `%whos` magic command
# - lists the name type and info of the global namespace
# - Can be filtered by type 
# - For example below I am just printing the list variables in the global namespace  

# In[2]:


get_ipython().run_line_magic('whos', 'list')


# ### The Enclosing and Local namespace 
# - Every time a function is initialized, the interpreter creates a new namespace. 
# - That namespace is local to the function and remains in existence until the function terminates.
# - Functions don’t exist independently from one another only at the level of the main program. 
# - You can also define one function inside another.
# - Let's give an example 

# In[3]:


def local_namespace(a):
    b= a**2
    print(dir())
local_namespace(5)


# In[4]:


def enclosing_namespace(a):
    def power(a,p):
        return a**p
    b = power(a,5)
    print(dir())
enclosing_namespace(5)


# 
# ## Python Classes and Methods
# 
# - In Python, most code is implemented with a special construct called a class, which is one of the core features of object-oriented programming. 
# - Classes provide a means of bundling data and functionality together.
# - Classes are used by programmers to group related items together. 
# - Classes allow us to combine methods and attributes which share a common purpose.
# - Creating a new class creates a new type of object, allowing new instances of that type to be made. 
# - Each class instance can have attributes attached to it for maintaining its state. 
# - Class instances can also have methods (defined by its class) for modifying its state.
# 

# ### The simplest example - class as a data storage 
# - You create an empty class 
# - Then create a new instance of that class 
# 

# In[5]:


class DataStorage():
    pass
storage = DataStorage()


# - And now you can use the dot notation to add information into the class 
# - You can add any type of info you like 

# In[6]:


storage.title = 'Project Title'
storage.number_of_obs = (50,50,50)
storage.number_of_groups = 3
storage.group_names = [f'group_{i:2}' for i in range(storage.number_of_groups)]
storage.lambda_fun = lambda x: x**2
storage.bool = True
storage.chr_fun = chr


# - You can also use the `setattr` to create a new attribute
# - The `vars` function to list all the variables in the instance 
# - And the `getattr` can be used to get the value of the attribute 
# 

# In[7]:


setattr(storage,'test','t-test')
for v in vars(storage):
    print(f'{v} = {getattr(storage,v)}')
   


# - But you can also use the dot notation to get the value 

# In[8]:


print(f'The attribute title = {storage.title}')


# - Finally we can delete attributes using the `delattr`  function

# In[9]:


delattr(storage,'title')
print(vars(storage))


# ### Classes can be initialized 
# - Using the protected method `__init__` we can define what information is necessary to create an instance 
# - You can also define default values like in a function
# - Using the protected word `self` we can set the attributes when we create the instance 

# In[10]:


from datetime import datetime 
class Participant():
    
    def __init__(self,
                 first_name,
                 last_name,
                 Data_type = 'EEG',
                 date = datetime.now().date()):
        self.first_name = first_name
        self.last_name = last_name
        self.Data_type = Data_type
        self.date = date
    
sub_01 = Participant('Eyal','Soreq')
print(vars(sub_01))


# ### Setting instance output using the `__repr__` method
# - The `__repr__` method is used in callable objects in python that return some information on the object that can be predefined 

# In[11]:


class Participant():
    
    def __init__(self,
                 first_name,
                 last_name,
                 Data_type = 'EEG',
                 date = datetime.now().date()):
        self.first_name = first_name
        self.last_name = last_name
        self.Data_type = Data_type
        self.date = date

        
    def __repr__(self):
        return f'Participant {self.first_name} {self.last_name} was admitted at {self.date} for a {self.Data_type} experiment'           
    
sub_01 = Participant('Eyal','Soreq')
sub_01


# ### We can add some object specific methods 
# - For example we can extend this toy example by creating a function that registers a task and captures the time this was triggered 
# 

# In[12]:


from time import sleep 
class Participant():
    
    def __init__(self,
                 first_name,
                 last_name,
                 Data_type = 'EEG',
                 date = datetime.now().date()):
        self.first_name = first_name
        self.last_name = last_name
        self.Data_type = Data_type
        self.date = date
        self.tasks = []
        
    def add_task(self, task):
        task = dict(name = task,time = datetime.now())    
        self.tasks.append(task)

        
    def __repr__(self):
        name = f'Participant {self.first_name} {self.last_name}'
        admittance = f' was admitted at {self.date} for a'
        experiment = f' {self.Data_type} experiment' 
        tasks = "".join([f'\n{task["name"]} registered at {task["time"].strftime("%H:%M:%S")}' for task in self.tasks])
        return name + admittance + experiment + tasks
    
sub_01 = Participant('Eyal','Soreq')
sub_01.add_task('Odd one out')
sleep(2)
sub_01.add_task('Stroop word test')
print(sub_01)


# ### Methods come in three different flavours 
# - Instance methods - that takes the `self` keyword we covered already 
# - The two other method types are:
#   - Class methods - points to the parent class and has access to the `cls` keyword
#   - Static methods - That doesn't have access to the instance attributes nor to the class
#  - The way to define these is by using another special type of function called a decorator 
#  - We will start with a simple example of the classmethod example 
# 

# In[13]:


class Task:
    
    def __init__(self,
                 name,
                 modality):
        self.name = name
        self.modality = modality
        self.registered = datetime.now()
        self.data = []
    
    def __repr__(self):
        rep = f'\n{self.name} using {self.modality} was registered at {self.registered.strftime("%H:%M:%S")}'
        return rep
        
    @classmethod
    def eeg_stroop(cls):
        return cls('stroop','EEG')
    
    @classmethod
    def mri_stroop(cls):
        return cls('stroop','MRI')
    
    @classmethod
    def eye_tracker_stroop(cls):
        return cls('stroop','eye_tracker')
    

task_01 = Task.eeg_stroop()
print(task_01)
sleep(2)
task_02 = Task.mri_stroop()
print(task_02)
sleep(2)
task_03 = Task.eye_tracker_stroop()
print(task_03)
            
        


# ### Static method is just a way of keeping things tidy
# - To illustrate that I will give another example
# - Here are a set of words we want a way to randomly shuffle this list every time an object is called 
# 

# In[14]:


words = ['rest','awake','tired','dream','blanket','doze','slumber','snore','pillow','peach','yawn','drowsy']
import random

class WordShuffle():
    
    def __init__(self,words,seed=2022):
        random.seed(seed)
        self.words = words
        self.seed = seed
    
    @staticmethod    
    def shuffle(seq):
        random.shuffle(seq)
        return seq
        
    def __repr__(self):
        return ", ".join(self.shuffle(self.words))    
    
word_scramble = WordShuffle(words)    
print(word_scramble)
print(word_scramble)


# ## Links to expand your understanding 
# 
# For those interested in learning more...
# 
# - [Python Classes and Objects](https://www.w3schools.com/python/python_classes.asp)
# - [Inheritance](https://www.w3schools.com/python/python_inheritance.asp) 
# - [Classes in python](https://docs.python.org/3/tutorial/classes.html) 
