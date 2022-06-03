#!/usr/bin/env python
# coding: utf-8

# # describing_data

# In[1]:


completed = pd.DataFrame()
for task in tasks:
    completed[task] = df[task].notna().sum(axis=1)>0


# In[ ]:


completed.sum()


# In[ ]:


completed.corr().round(2)


# In[ ]:


task_series = [completed[col] for col in completed]
venn = pd.crosstab(task_series,task_series)


# In[ ]:


venn.sum().to_frame().sort_values(0).tail(50)

