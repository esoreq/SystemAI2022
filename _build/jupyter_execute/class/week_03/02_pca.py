#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits
from IPython.display import display, Markdown 
digits = load_digits()
df_digits = pd.DataFrame(digits['data'],columns=digits['feature_names'])
df_digits = df_digits.assign(y = digits['target'])


# ## Principal Component Analysis (PCA)
# 
# Using PCA, we find directions of maximum variance in high-dimensional data,
# We project these directions into a new subspace with the same or fewer dimensions than the original one.
# 
# ## Maximal Variance and Information Loss
# Data points will be projected in the direction of maximal variance to form a new axis. 
# The further the points are to the axis, the biggest the information loss.

# ## Before we dive to the digit example let's review some basic properties of PCA
# - Loosely based on the following [scaling importance](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html) 

# In[3]:


from sklearn.datasets import load_wine
wine = load_wine()
wine_df = pd.DataFrame(wine['data'],columns=wine['feature_names'])
wine_df = wine_df.assign(y = wine['target'])


# In[4]:


display(Markdown(wine['DESCR']))


# In[5]:


fig,ax = plt.subplots(figsize=(10,10))
sns.heatmap(wine_df.corr(),vmin=-1,vmax=1,ax=ax,center=0, annot=True, fmt="0.2f")


# In[6]:


selected_features = ['proline','color_intensity','alcohol','flavanoids']
sns.pairplot(pd.DataFrame(wine_df[selected_features]))


# ## Reduce dimensionality to 2 features

# In[7]:


from sklearn.decomposition import PCA
pca = PCA(n_components=2) # 1. Define the PCA model with a hyper parameter
features = wine_df.drop(columns='y')
pca.fit(features) # 2. fit to data
wine_reduced = pd.DataFrame(pca.transform(features),columns =['pc1','pc2']).assign(y = wine_df.y) 
sns.scatterplot('pc1','pc2',data=wine_reduced,hue='y',palette='tab10')


# In[ ]:


display(Markdown(f'''### Model components : \n
$PC1 = {" + ".join([f"{b:0.3f}x_{{{i+1}}}" for i,b in enumerate(pca.components_[0,:])])}$\n
$PC2 = {" + ".join([f"{b:0.3f}x_{{{i+1}}}" for i,b in enumerate(pca.components_[1,:])])}$\n
'''))


# In[ ]:


display(Markdown(f'''### Model components explain variance ratio: \n
${", ".join([f"PC{i+1} = {100*r:0.1f}" for i,r in enumerate(pca.explained_variance_ratio_)])}$
'''))


# In[ ]:


display(Markdown(f'''### Model components explain variance: \n
${", ".join([f"PC{i+1} = {r:0.1f}" for i,r in enumerate(pca.explained_variance_)])}$
'''))


# # Is this as good as it gets? 
# 
# - Feature scaling through standardization (or Z-score normalization) can be an essential preprocessing step for many machine learning algorithms. Standardization involves rescaling the features with the properties of a standard normal distribution with a mean of zero and a standard deviation of one.
# - In PCA, we are interested in the components that maximize the variance. For example, suppose one component (e.g. flavonoids) varies less than another (e.g. proline) because of their respective scales. In that case, PCA might determine that the maximal variance more closely corresponds with the proline axis if those features are not scaled.
# - PCA is solved via the Singular Value Decomposition, which finds linear subspaces which best represent your data in the squared sense.
# - Linear Subspaces are an essential topic of study in Linear Algebra, and the most critical consequence of a linear subspace for PCA is that it has to go through the origin, the point [0, 0, ..., 0].
# - By centring our data, we guarantee that they exist near the origin, and it may be possible to approximate them with a low-dimensional linear subspace.
# - Scaling is essential because SVD approximates in the sum of squares sense, so if one variable is on a different scale than another, it will dominate the PCA procedure. So the low D plot will just be visualizing that dimension.
# - Let's add scaling to the mixture and plot again

# In[ ]:


from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
pca = PCA(n_components=2) # 1. Define the PCA model with a hyper parameter
scaler = StandardScaler()
features_s = scaler.fit_transform(features)
pca.fit(features_s) # 2. fit to data
wine_s_reduced = pd.DataFrame(pca.transform(features_s),columns =['pc1','pc2']).assign(y = wine_df.y)  
sns.scatterplot('pc1','pc2',data=wine_s_reduced,hue='y',palette='tab10')


# In[ ]:


display(Markdown(f'''### Model components : \n
$PC1 = {" + ".join([f"{b:0.3f}x_{{{i+1}}}" for i,b in enumerate(pca.components_[0,:])])}$\n
$PC2 = {" + ".join([f"{b:0.3f}x_{{{i+1}}}" for i,b in enumerate(pca.components_[1,:])])}$\n
'''))


# In[ ]:


display(Markdown(f'''### Model components explain variance ratio: \n
${", ".join([f"PC{i+1} = {100*r:0.1f}" for i,r in enumerate(pca.explained_variance_ratio_)])}$
'''))


# In[ ]:


display(Markdown(f'''### Model components explain variance: \n
${", ".join([f"PC{i+1} = {r:0.1f}" for i,r in enumerate(pca.explained_variance_)])}$
'''))


# In[ ]:


from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
pca = PCA(n_components=3) # 1. Define the PCA model with a hyper parameter
scaler = StandardScaler()
features_s = scaler.fit_transform(features)
pca.fit(features_s) # 2. fit to data
wine_s_reduced = pd.DataFrame(pca.transform(features_s),columns =['pc1','pc2','pc3']).assign(y = wine_df.y)  
sns.pairplot(data=wine_s_reduced,hue='y',palette='tab10')


# In[ ]:


display(Markdown(f'''### Model components explain variance ratio: \n
${", ".join([f"PC{i+1} = {100*r:0.1f}" for i,r in enumerate(pca.explained_variance_ratio_)])}$
'''))


# ### How many components is enough? 
# #### Rule of thumb 1 
# - The eigenvalues (variance explained by each PC) for PCs can help to retain the number of PCs. 
# - Generally, PCs with eigenvalues > 1 contributes greater variance and should be retained for further analysis.

# In[ ]:


pca = PCA() # 1. Define the PCA model with default
scaler = StandardScaler()  # 2. scale the data
features_s = scaler.fit_transform(features) # 3. transform the data
pca.fit(features_s) # 4. fit to data
exp_var = pca.explained_variance_
ax = pd.Series(exp_var).plot.bar()
ax.set_ylabel('Explained variance')
ax.hlines(1,-0.5,12.5,color='r',linestyles=':')


# #### Rule of thumb 2 
# - Scree plot (for elbow test) is another graphical technique useful in PCs retention. 
# - We should keep the PCs where there is a sharp change in the slope of the line connecting adjacent PCs.
# 

# In[ ]:


exp_ratio = pca.explained_variance_ratio_
def scree_plot(y,plot=True):
    
    ys, n = y/np.sum(y), y.shape[0]
    yl = np.linspace(ys[0],ys[-1],n)
    dtl = ((ys - yl)**2)**0.5
    data = pd.DataFrame(dict(y=y, ys=ys, yl=yl, dtl=dtl))
    elbow,value = data.agg(pc = ('dtl','argmax'), value = ('dtl','max')).to_numpy()
    if plot: 
        ax = data.y.cumsum().plot.bar(alpha=0.5,figsize=(12,4))
        ax.bar_label(ax.containers[0],padding=2,fontsize=10,color='k',fmt='%.2f')     
        data.y.plot.bar(ax=ax)
        data.yl.plot(ax=ax,linestyle=':')
        data.ys.plot(ax=ax,linestyle=':')
        data.dtl.plot(ax=ax,linestyle=':')
        ax.set_ylabel('Explained ratio %')
        ax.set_xlabel('PC')
        ax.plot(elbow,value,'r*')
        xlim = [-0.5,15] if n > 15 and elbow < 15 else [-0.5,n] if n < 15 else [-0.5,elbow+2]
        ax.set_xlim(*xlim)
        
    return int(elbow)
    
elbow = scree_plot(exp_ratio)


# #### Rule of thumb 3
# - Identify the number of components that maximise the utility 
# - This depends on the problem you are trying to solve and we will touch on this next week
# 
