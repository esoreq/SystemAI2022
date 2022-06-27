#!/usr/bin/env python
# coding: utf-8

# # DAY 04 - Numpy and Pandas 101
# 
# ### Why do we need modules?
# - Modules are simply a time-saving method of combining multiple pieces of useful functionality that serve a similar purpose. 
# - When a module can be easily disassociated from the larger programme, it is much simpler for a scientist to understand what they should anticipate receiving from that module.
# - In addition to this, they are an effective method of working together toward the same goal.
# 
# ### The scientific Python ecosystem
# - Consider the image below that illustrates the scientific eco-system that is based on Python 
# - At the core level we have three tools we already used extensively
#   - Anaconda for managing our environment 
#   - Jupyter as our notebook framework that enables both documenting code and running it in the same time 
#   - And under the hood we used the IPython which stands for interactive Python that powers our kernel 
#   - Today we will extend our reach to cover two and half additional players, specifically Numpy and Pandas, with some backstage support from Matplotlib, which we will cover extensively tomorrow.  
# ![](../../images/eco_system.png)
# 
# ### What is [Pandas](https://pandas.pydata.org/)?
# - Pandas is Pythons basic data analytics package that provides quick, versatile, and expressive data structures that make dealing with "relational" or "labelled" data straightforward. 
# - It's a high-level building component for real-world Python data analysis. 
# - It is probably the most powerful and useful open source data analysis/manipulation tool for small to mid size datasets (10 to 10 million rows give or take).
# 
# ### What is [Numpy](https://numpy.org/doc/stable/user/whatisnumpy.html)?
# - Numpy is Pythons basic scientific computing package that provides several essential capabilities such as: 
#   - Multidimensional array object, 
#   - Derived objects (such as masked arrays and matrices), 
#   - Routines for fast array operations, including: 
#     - mathematical, 
#     - logical, 
#     - shape manipulation, 
#     - sorting, 
#     - selecting, 
#     - I/O (i.e. input/output), 
#     - discrete Fourier transforms, 
#     - basic linear algebra, 
#     - basic statistical operations, 
#     - random simulation, 
#     - and more.
# 
# ### What is Matplotlib
# - In Python, Matplotlib is the "grandfather" of data visualization. 
# - It was created to try and replicate MATLAB's plotting capabilities with Python. 
# - It is an excellent 2D and 3D graphics library for creating reproducible publication ready scientific figures.
#  
# - Some of the major Pros of Matplotlib are:
#   * Simple plots are generally easy to create
#   * Each element in the figure is nicely controlled
#   * A variety of output formats with high quality
# 
# ### What this module will cover
# - Today's main objective is to familiarize you with the core scientific packages in the Python eco-system.
# - We will start by looking over the different Numpy and Pandas data structures
#   - How to create them 
#   - How to use them 
#   - And how to save them 
# - Then focus on Numpy and go over some advanced functionalities 
# - Return to Pandas to explore some basic and advanced data capabilities   
# 
#   
# ### Links to expand your understanding 
# 
# For those interested in learning more...
# 
# - [Getting started with Pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
# - [NumPy quick start](https://numpy.org/doc/stable/user/quickstart.html)
# - [NumPy for MATLAB users](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html) 
# 
# 
# 

# ## Schedule 
# 
# |Time    | Session    | Description   | 
# |-----------:|----------:|---------:|
# |09:00-09:10| Day 04 overview | Intro to core scientific tools in Python |
# |09:10-09:50| [Numpy 101](01_Numpy_data_structures.ipynb)| Basic of Numpy |
# |09:50-09:55| Break | Coffee or Tea |
# |10:00-10:40| [Pandas 101](02_Pandas_data_structures.ipynb)| Basics of pandas |
# |10:40-10:45| Break | Coffee or Tea |
# |10:45-11:10| [From raw to tidy](03_raw_to_tidy_with_pandas.ipynb)| Practical pandas demonstration on real data  |
# |11:10-11:15| Break | Coffee or Tea |
# |11:15-11:45| [Plotting in Pandas](04_plotting_with_pandas.ipynb) | Plotting in Pandas |
# |11:45-11:50| Break | Coffee or Tea |
# |11:50-12:00| [homework assignment](05_home_work.ipynb) | Going over the homework assignment |
# 
# ## Home work
# 
# After finishing all the modules please complete day three [homework assignment](05_home_work.ipynb)
