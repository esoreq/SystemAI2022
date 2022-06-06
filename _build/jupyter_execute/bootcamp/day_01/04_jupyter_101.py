#!/usr/bin/env python
# coding: utf-8

# ## Jupyter notebooks 101
# 
# ### Jupyter basics
# #### What is a Jupyter notebook?
# 
# - Jupyter notebook is a modern web-based open-source tool specifically designed to support data science projects. 
# - You can use Jupyter Notebooks to document workflows and to share code for data processing, analysis and visualization.
#   
# 

# #### Jupyter Notebook Overview
# 
# The Data science field makes extensive use of notebooks, which allow you to document code and thoughts while being able to follow your work. This section explains how to use Jupyter Notebook to facilitate open reproducible science workflows and introduces you to the interface that you will use for running and editing code and Markdown cells. 
# 
# 

# #### Jupyter Notebook for Open Reproducible Science
# 
# - The Jupyter Notebook file format (.ipynb ) is constructed from linearly stacked cells allowing you to construct a single project-oriented file that combines descriptive text, code blocks and code output in a single file. 
# - The code cells have output cells associated with them, allowing you to include plots, tables, and textual outputs to communicate your findings, within the notebook file. 
# - You can then export the notebook to a .pdf or .html that can then be shared with anyone.
# 

# #### Key benefits of the Jupyter Notebook
# 1. **Human readable**: Using Jupyter, you can bridge ideas and concepts with methodology and results, creating a notebook that can be understood by different types of researchers. By adding Markdown text around your code, your project becomes more user-friendly and easier to understand. 
# 1. **Simple syntax:**  Markdown is simple to learn and use reducing the learning curve needed to produce well-documented Jupyter reports.
# 1. **Documenting your ideas:** Research is all about creating logical steps based on assumptions followed by tests. However, actual Research is messy, and many things will be left on your digital workbench. Forming the habit of documenting your workflow, making inline references when needed, and explaining the logical workflow, will be priceless to the future you. Just imagine changing or adapting specific parts of a study two years after it was created, without some comments.
# 1. **Easy to Modify:** analyses contained within a Jupyter Notebook can be easily extended, improved or refined by adding or editing the workflow and rerunning the notebook.
# 1. **Simple to share:** Sharing your workflow with colleague or supervisor is in the core of the Jupyter DNA. A notebook can be shared using file-sharing services like Dropbox or Google Drive or more sophisticated approaches such as Github. This simplifies the process of validating, replicating, extending, refining and communicating your workflow.
# 1. **Flexible export formats:** Notebooks can be exported into various formats including HTML, PDF and slideshows.

# #### Jupyter Notebook types
# 
# There are four kinds of notebooks you would want to create:  
# 
# - **The lab** - a historical (and dated) record of your analysis
# - **The report** - a polished version of some study, intended for collaboration and review 
# - **The presentation** - a slideshow designed to communicate ideas with collaborators  
# - **The book** - Multi-notebook scientific project presented in book format

# ####  What are Jupyter kernels 
# A kernel is a computer program that runs and inspects the user's code. IPython includes a kernel for Python code. Others have written kernels for various other languages. We will begin by using the bash built-in kernel today. Tomorrow, we will cover how to set up a project-specific environment and start our journy into python.

# ### Opening a notebook on your local computer 
# #### Jupyter notebook server
# There are many ways to create a [Jupyter notebook](https://jupyter-notebook.readthedocs.io/en/latest/) instance,
# The simplest way is to open a terminal and run the the following command: 
#    
# ```bash
# jupyter notebook
# ```
# 
# If you followed the previous sessions a notebook server will initialize a local server and open a jupyter notebook inside your default browser.
# 

# #### Using a notebook for the first time  
# Jupyter Notebook is a web-based platform that lets developers write, display, share, and integrate multimedia in a single document. You can view both the code and the results in the same file, making it a popular tool for demonstrating work.
# Executing each line of code individually improves data scientists' knowledge. Jupyter Notebook users may download the notebook in PDF, HTML, Python, Markdown, or .ipynb format.
# 

# #### Markdown and Code Cells are essential to a Jupyter Notebook.
# 
# ##### Markdown Cell
# When you use a Markdown Cell, you're giving your readers enough information about the code block underneath to understand what you're trying to convey. Every data scientist has to know how to write in Markdown. The markup language is used to format the text, which is then displayed. Code Cells Will Be the Default for All Cells By Default Hit ESC to enter command mode and then press m to convert it to markdown.

# #### Code Cell
# You are able to Create, Update, Read, Edit, and Delete Code inside a Code Cell while also benefiting from comprehensive syntax highlighting and tab completion.  
# Ipython, which is short for interactive Python, is the kernel that Jupyter Notebook uses by default (but you can use alternative kernels).  
# The flow of the code is sent to the kernel, whenever a Code Cell executes the code that is contained inside it is run.  
# You can use two Keyboard combination to run a code cell 
# 1. <kbd>Ctrl+Enter</kbd>  runs current cell 
# 2. <kbd>Shift+Enter</kbd> runs current cell + select/create the cell below
# 
# A key difference between the two shortcuts is that the first moves to the next cell and creates it if it does not exist, while the other simply runs the cell.
# This shortcut <kbd>Ctrl+Shift+-</kbd> makes it easy to create a new cell, as well as a convenient way to divide a cell that contains multiple commands into independent cells so you can add comments explaining what they do.
# 
# Mastering the shortcuts will improve the way you interact with the notebook and will speed your work significantly 

# ### Jupyter lab 
# 
# Alternatively, one can use a slightly more modern approach using a web-based user interface called [jupyter lab](https://jupyterlab.readthedocs.io/en/stable/) that allows you to work with a more unified framework.   
# 
# ```bash
# jupyter lab
# ```
# 
# This will spawn a local server as well, however, it will generate a more efficient UI that contains the ability to explore local files, manage extensions and more. 
# 

# ```{warning} 
# In both cases if you close the terminal you will terminate your server and your notebooks will stop functioning 
# ```
# 

# ### Integrated development environment (IDE) 
# 
# A solution that requires more initial effort, that will eventually pay off is using a proper IDE. 
# There are many options to choose from TBH, a free open-source solution that I use is called [VScode](https://code.visualstudio.com/). 
# This gives you the capability to create notebooks within the IDE and comes with multiple perks that I urge to you to explore on your own.  

# ## Cloud based solutions 
# 
# Jupyter has many side projects that enable spawning a notebook with access to cluster capabilities. This can be a lab owned small cluster or a large one owned by a University or one owned by some commerical company. In the context of our own center some of us have access to [Research Computing Service (RCS)](https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/) notebook lab hub that gives you a portal to the Imperial College Cluster.  
# 
# The main differences from your local version to the cloud based lies in the access to joint storage, computing resources and standardised underlying software and hardware setups. 
# 
# Notably, there are other notebook solutions that resemble the Jupyter solution, the most famous is [Colab](https://colab.research.google.com/?utm_source=scs-index) owned and developed by Google. 

# ## Practicalities 
# 
# ### Opening a notebook 
# 
# In a cloud lab environment press <kbd>Shift + CMD + L</kbd> to open a new launcher (or open the file menu and select new Launcher). If you select the default notebook, a new notebook tab named `Untitled.ipynb` will appear.

# ### Jupyter Notebook modes 
# 
# - There are two modes of action in Jupyter: *Command* and *Edit*.  
# - Command mode allows you to edit your notebook, but you cannot type in cells
# - to enter command mode you press the  <kbd>Esc</kbd>  button. 
# - Pressing <kbd>Enter</kbd> will transfer you to EDIT mode where you can interact with each cell in your notebook. 

# ### EDIT mode useful shortcuts
# When in EDIT mode, there are several key commands it is good to know.  
# You should practice using these commands until they become second nature. 
# 
# 
# | Mac  |  Function | 
# | :--  |  :--      |
# |<kbd>Tab</kbd>|  code completion/indent |
# |<kbd>Shift+Tab</kbd>|  function help |
# |<kbd>Cmd + /</kbd>|  comment/uncomment |
# |<kbd>Ctrl+Enter</kbd>| run current cell |
# |<kbd>Shift+Enter</kbd>|  run current cell + select below|
# |<kbd>Alt+Enter</kbd>|  run current cell + insert below|
# |<kbd>Ctrl+Shift+-</kbd>|  Split cell at cursor |
# |<kbd>Cmd+s</kbd>|   Save notebook |
# |<kbd>D+D</kbd>|   Delete selected cells |

# ### COMMAND mode useful shortcuts
# 
# The same goes to COMMAND shortcuts.  
#   
# | Key | Function | 
# | :-- | :-- |
# | <kbd>Esc + Y</kbd> | Change cell to code type |
# | <kbd>Esc +  M</kbd> | Change cell to markdown type |
# | <kbd>Esc + SHIFT + up</kbd> | select cells above |
# | <kbd>Esc + SHIFT + down</kbd> | select cells above |
# | <kbd>Esc + SHIFT + M</kbd> | merge selected cells |
# | <kbd>c</kbd> | copy selected cells |
# | <kbd>x</kbd> | cut selected cells |
# | <kbd>v</kbd> | paste selected cells |

# ### Document this code using markdown
# 
# One useful suggestion is to start the habit of documenting your learning experiences using markdown and coding when relevant  
# This will accelerate your work in the long run...
