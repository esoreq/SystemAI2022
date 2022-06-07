import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator
tasks =  set(df.columns.get_level_values(0))
completeness = {}
for task in tasks:
    completeness[task] = df.xs(task,1).notna().sum(axis=1)>0
    
completeness = pd.concat(completeness,axis=1)   
obs_order = completeness.sum(axis=1).sort_values(ascending=False).index
col_order = completeness.sum().sort_values().index
completeness = completeness.loc[obs_order,col_order].reset_index(drop=True)

fig,ax = plt.subplots(figsize=(15,5))
ax.pcolor(completeness.T.to_numpy(),cmap='Greys')

ax.xaxis.set_major_locator(MultipleLocator(2000))
ax.xaxis.set_minor_locator(AutoMinorLocator(4))
ax.set_xlim(0,df.shape[0])
ax.set_yticks(np.arange(0.5,len(tasks),1))
labels = completeness.columns.str.replace('_', ' ').str.title()
ax.set_yticklabels(labels,fontsize=20)
ax.spines[['top', 'right', 'left', 'bottom']].set_visible(True)
ax.spines[['top', 'right', 'left', 'bottom']].set_color('k')
ax.set_title('Data completeness across tasks (white == NaN)',fontsize=22)
ax.set_xticklabels(ax.get_xticks().astype(int),fontsize=20)
ax.set_xlabel('OBS',fontsize=22)
fig.savefig('completeness.png', bbox_inches = 'tight')



### seaborn 
plt.figure(figsize=(15,5))
sns.set(font_scale = 2)
ax = sns.heatmap(completeness.T,cbar=False,cmap='Greys',yticklabels=True); 
ax.spines[['top', 'right', 'left', 'bottom']].set_visible(True)
ax.spines[['top', 'right', 'left', 'bottom']].set_color('k')
ax.set_title('Data completeness across tasks (white == NaN)',fontsize=22)