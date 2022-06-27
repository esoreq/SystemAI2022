# %% 

import json

def read_ipynb(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_ipynb(notebook, notebook_path):
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f)    
# %%
from pathlib import Path


#  %%


# %% 
clean_kernel = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3"
    },
    "language_info": {
        "name": "python",
        "version": "3.8.12"
    }
}
# nb = read_ipynb(notebooks[43])
# nb['metadata'] = clean_kernel
# write_ipynb(nb, notebooks[43])

# %% 
notebooks = sorted(Path('/Users/eyalsoreq/github/SystemAI2022/class/week_01').rglob('*.ipynb'))
for i,notebook in enumerate(notebooks):
    nb = read_ipynb(notebook)
    nb['metadata'] = clean_kernel
    write_ipynb(nb, notebook)

# %% 
notebook
# %%
