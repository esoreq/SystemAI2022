#!/usr/bin/env python
# coding: utf-8

# # PYTHON ANACONDA 102

# ## Installing packages and modules from PyPI
# - The most common usage of pip is to install from the Python Package Index using a requirement specifier. 
# - The Python Package Index, abbreviated as PyPI and also known as the Cheese Shop, is the official third-party software repository for Python. 
# - Some package managers, including pip, use PyPI as the default source for packages and their dependencies.
# - If you create an anconda environment you can use pip to install the specific packages into the environment
# 
# ### But what about the dependencies 
# 
# - Using a package manager such as Anaconda makes it easy to install almost any additional package. 
# - Moreover, it simplifies collaboration by sending a jupyter notebook with a special file called `.yml` as you should recal from day one of this boot camp
#   
# 
# ## SYS_2022 environment  
# 
# - One thing that is very useful when working with collaborators of different levels of proficiency is creating a setup file that automates the whole process of setting an environment for you.
# - Here is how you set up your environment for the this course using a `.yml` file 
# - Create a new python notebook and name it `setup_SYS_2022.ipynb`
# - It is up to you to decide what text to include in your markdown cells to remind yourself why you do what you do
# - This is an introductory course so we are much simpler 😊
# 

# ### Step 1. create a folder structure

# In[1]:


from pathlib import Path
project_root = '~/SYS_2022/bootcamp'
sub_folders = ['data','notebooks','code','report','background']
_ = [Path(project_root + f'/{folder}').mkdir(parents=True, exist_ok=True) for folder in sub_folders]


# ### Step 2. create a .yml file with required dependencies

# In[2]:


project_root = Path('~/SYS_2022')
SYS_2022 = project_root / 'SYS_2022.yml'
SYS_2022.write_text("""
name: SYS_2022
channels:
  - conda-forge
dependencies:
  - numpy
  - pandas
  - jupyterlab
  - scipy
  - statsmodels
  - pingouin
  - scikit-learn
  - matplotlib
  - seaborn
  - plotly
  - pip
  - ipykernel
  - watermark
  - nb_conda_kernels
""")


# ### Step 3. Use the yml file to create and register the environment
# ~~~python
# %%bash
# conda env create --file  ./SYS_2022/SYS_2022.yml
# conda activate SYS_2022
# python -m ipykernel install --user --name SYS_2022 --display-name "Python (SYS_2022)"
# ~~~

# ### Step 4. Test that the kernel exists and that the packages are installed
# - If you are using Jupyter lab or notebook search the launch pad 
# - In VScode just search for the kernel in the right hand side of the UI
# - Once you selected these let's test that everything is installed correctly 

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px 
import sys
sys.path.append("./bootcamp/code/")
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# ### Step 5. Verify the key module versions using the watermark magic function
# 

# In[2]:


get_ipython().run_line_magic('watermark', '-p numpy,pandas,matplotlib,seaborn,plotly')


# ### Step 6. If everything worked... 
# 
# - I mentioned that we can export our environment once everything is working properly
# - By using the following command, you can create a tml file that captures all the dependencies that your project depends on
# - While conda does have some versioning under the hood, a simple approach to exporting stable environments can save you and any potential collaborators hours of work and frustration.
# 

# In[3]:


get_ipython().system(' conda env export --name SYS_2022 > ./SYS_2022/env_frozen.yml')


# ### What to do when things go wrong
# 
# 
# #### In the gwdg cloud 
# - Here's what you do when your Notebook won't start, your Kernel won't connect, or the environments you created have grown out of control and you have to start over.
# 
# - In a new terminal just run the following code ([Based on this link](https://info.gwdg.de/docs/doku.php?id=en:services:application_services:jupyter:start#notebook_does_not_start_kernel_can_not_connect)): 
# 
# ~~~bash
# mv -v .local/ .local.gwdg-disable 
# ~~~
# 
# - Renaming all our local configuration files instructs the cloud to  spawn a new virtual machine with default settings. 
# 
# 
# 
# ##### Is it enough? 
# 
# - No, I still need to delete the different environments I created. Hence the recommendation to keep them together in one place.
# 
# ##### What about removing specific environments
# 
# - This can be done using `conda env remove` and `jupyter kernelspec remove`
# - Or if you are brave just delete the specific kernel and env folder   
# 
# ##### What about updating packages (adding or removing?)
# 
# - Just use the following (after you updated the file)
# 
# ~~~bash
# conda env update --name SYS_20221 --file ~/SYS_2022/SYS_2022.yml
# ~~~
# 
# ##### What about updating the contents of the environment 
# 
# ~~~bash
# conda update --name SYS_2022 --all
# ~~~
# 
# 

# 
# 
# ## Links to expand your understanding 
# 
# For those interested in learning more...
# 
# - [Creation of virtual environments](https://docs.python.org/3/library/venv.html)
# - [Pyenv in python](https://github.com/pyenv/pyenv) 
# - [Poetry in python](https://python-poetry.org/) 
# 
# 
