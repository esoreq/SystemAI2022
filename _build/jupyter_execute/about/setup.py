#!/usr/bin/env python
# coding: utf-8

# # ⚙️ Course Setup
# 
# ##  Requirements
# 
# - For the online sessions you must have a laptop with a Mac, Linux,or Windows operating system. 
# - Make sure you have admin privileges on the laptop so you can install the packages needed.
# 
# 

# 
# ## What do I need to have installed in advance? 
# - To participate in the online sessions, you will need access to the following tools and software:
#   - Bash terminal 
#   - Anaconda
#     - [Windows](https://docs.anaconda.com/anaconda/install/windows/)
#     - [Apple](https://docs.anaconda.com/anaconda/install/mac-os/)
#     - [Linux](https://docs.anaconda.com/anaconda/install/linux/)
# 
# 
# ### On your local computer I recommend also 
# - [VScode](https://code.visualstudio.com/)
# 
# 
# #### Recommended VScode extensions
# - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
# - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
# - [Path Intellisense](https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense)
# - [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
# 
# 

# 
# ### You can also participate using the GWDG jupyter hub
# - To setup the GWDG terminal to play nice with the anaconda setup you need to add a setup file called `.profile` 
# - This isn't hard just follow the steps below 
#   - Log on to the [GWDG Jupyter hub](https://jupyter-cloud.gwdg.de/jhub/hub/user/0610061/lab)
#   - Open a terminal using the Launcher 
#   - In the terminal run the command `nano` (the simplest text editor out there)
#   - copy the following lines 
#   ~~~bash
#   echo "running my .profile"
#   source /opt/conda/etc/profile.d/conda.sh
#   export PATH=/opt/conda/bin:/opt/conda/condabin:/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/bin
#   ~~~
#   - Now press <kbd>ctrl</kbd>+<kbd>x</kbd>
#   - And when prompted to supply a file name write `.profile`
#   - To test if this works run the following lines 
#   ~~~bash
#   source ~/.profile
#   conda activate base
#   ~~~ 
#   - If your terminal now includes a `(base)` prefix to the standard input line in the terminal you are all setup for the next step
#   

# ### Setup the course environment 
# - This step assumes you have either have an anaconda local setup with Jupyter lab installed or you are working with the gwdg cluster 
# - Open a new notebook in a folder that will contain your course material 
# - Copy the following code into a cell and run it 
# - This code block creates a folder structure for the course 
# 
# ~~~python
# from pathlib import Path
# root = Path().cwd()
# project_root = f'{root}/SYS_2022/course'
# sub_folders = ['data','notebooks','code','report','background']
# _ = [Path(project_root + f'/{folder}').mkdir(parents=True, exist_ok=True) for folder in sub_folders]
# ~~~

# - The next code block creates a yaml file that includes all the different tools we will be using in the next five weeks 

# ~~~python
# project_root = Path(f'{root}/SYS_2022')
# SYS_2022 = project_root / 'SYS_2022.yml'
# SYS_2022.write_text("""
# name: SYS_2022
# channels:
#   - conda-forge
# dependencies:
#   - numpy
#   - pandas
#   - jupyterlab
#   - scipy
#   - statsmodels
#   - pingouin
#   - scikit-learn
#   - matplotlib
#   - seaborn
#   - plotly
#   - pip
#   - ipykernel
#   - watermark
# """)
# ~~~

# - The next code block creates the conda environment
# 
# ~~~python
# %conda env create --file  ~/SYS_2022/SYS_2022.yml
# ~~~

# - Final step is to register this environment to the jupyter lab hub
# ~~~python
# %%bash
# python -m ipykernel install --user --name SYS_2022 --display-name "Python (SYS_2022)"
# ~~~

# In[ ]:





# ### Check if this worked 
# - If everything worked as planned when you run the following line you will get the new SYS_2022 environment as one of the conda environments
# 
# ~~python 
# %conda env list
# ~~~
# 
# - Refresh your terminal and you can now work on the lab material 

# ```{note}
# To create notebooks inside the notebook folder you should navigate to the notebooks folder using the jupyter lab explorer and launch a notebook when you are in the right folder
# ```
