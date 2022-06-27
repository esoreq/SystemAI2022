#!/usr/bin/env python
# coding: utf-8

# ## Ten simple rules for reproducible research
# 
# ### RULE #1 - DATA CURATION
# 
# ![](https://i2.pickpik.com/photos/110/568/870/files-ddr-archive-preview.jpg)
# 
# - FOR EVERY RESULT, KEEP TRACK OF HOW IT WAS PRODUCED
# - Knowing how you went from the raw data to the conclusion allows you to:
#   - defend the results
#   - update the results if errors are found
#   - reproduce the results when data is updated
# 
# ### RULE #2 - AUTOMATE
# 
# ![](https://i1.pickpik.com/photos/373/813/306/heavy-hard-work-hard-work-preview.jpg)
# 
# - AVOID MANUAL DATA MANIPULATION STEPS
# - Sometimes it is far easier to open data files in an editor (did anyone say excel?) and manually clean up a couple of formatting errors or remove an outlier.
# - It is also easy to cut and paste between applications.
# - This temptation to use manual work instead of scripting should be resisted.
# - Manual data manipulation is hidden manipulation (violates rule 1).
# 
# ### RULE #3 - TRACK EXTERNAL VERSIONS
# 
# ![](https://p0.piqsels.com/preview/60/688/850/business-office-graphic-designer-planning-thumbnail.jpg)
# 
# - ARCHIVE THE EXACT VERSIONS OF ALL EXTERNAL PROGRAMS USED
# - Document the edition and version of all the software used
# - Operating system used
# - Hardware in special cases
# 
# ### RULE #4 - TRACK INTERNAL EVOLUTION
# ![](https://blog.k.io/attachment/f1224b44-d27f-4e45-8a49-47fb68f9c862/thumb1400.jpg)
# 
# - VERSION CONTROL ALL CUSTOM SCRIPTS
# - A version control system, (e.g. Git), should be used to track the evolution of your code.
# 
# ### RULE #5 - STORE DATA STEPS
# 
# ![](https://miro.medium.com/max/3200/1*SwXkSz05zb7_kCPQ4dhPug.jpeg)
# 
# - RECORD ALL INTERMEDIATE RESULTS, WHEN POSSIBLE IN STANDARDIZED FORMATS
# - In principle, as long as you kept raw data, all intermediate steps can also be recreated
# - In practice, some intermediate results are useful at least at the exploratory stage of the analysis.
# 
# ### RULE #6 - STORE DATA SEEDS
# 
# ![](https://miro.medium.com/max/3840/1*M70VAAHkWsq23ifZLIVpLw.jpeg)
# 
# - FOR ANALYSES THAT INCLUDE RANDOMNESS, NOTE UNDERLYING RANDOM SEEDS
# - Almost all machine learning algorithms have some stochastic element
# - This is also central for non parametric analysis
# - Even if your robust results are statistically reproducible, being able to reproduce the exact numbers produced by someone else - is key.
# 
# ### RULE #7 - STORE SUMMARY TABLES
# 
# ![](https://iotcdn.oss-ap-southeast-1.aliyuncs.com/2020-11/14.jpg)
# 
# - ALWAYS STORE RAW DATA BEHIND PLOTS
# - Automatically generate plots using code!!!
# - Figures will constantly change up until you present results.
# - If raw data is accessible, you can just change how you communicate it instead of what you communicate.
# - This is also a good habit to have when working with someone else
# 
# ### RULE #8 - RECREATE THE RABBIT HOLE
# 
# ![](https://c1.wallpaperflare.com/preview/331/516/975/water-plant-green-fine-layers.jpg)
# 
# - GENERATE HIERARCHICAL ANALYSIS OUTPUT, ALLOWING LAYERS OF INCREASING DETAIL TO BE INSPECTED
# - As scientists, our goal is to summarize results in some form.
# - That is a key step in communicating results.
# - However, summarizing data involves losing information
# - It is also an easy way to misuse data
# - For each summary result, have a link to the data used to calculate the summary.
# 
# ### RULE #9 - LINK EVERYTHING
# 
# ![](https://i.pinimg.com/originals/a0/f3/81/a0f381ead8a60dfe88bbf1ddc414708b.png)
# 
# - CONNECT TEXTUAL STATEMENTS TO UNDERLYING RESULTS
# 
# - Data analysis results are commonly presented as a report containing words and images.
# - The link between analysis and interpretations is not always straight forward.
# - Therefore it’s essential that the report of a study be linked back to the results.
# - And because of Rule #1, all the way back to the raw data.
# - This can be achieved, by using a computational notebook
# 
# ### RULE #10 - BE TRANSPARENT
# ![](https://p1.piqsels.com/preview/915/529/243/keyboard-button-key-entering-input-internet.jpg)
# 
# - PROVIDE PUBLIC ACCESS TO SCRIPTS, RUNS, AND RESULTS
# - Open version control systems, such as GitLab and GitHub, allow the creation of both private and public repositories
# - Private repositories can be accessed by authorized colleagues.
# - public repositories can be accessed by anyone with a computer.
# - More eyes on your analysis leads to less mistakes
# - So the more you share, the better your analyses are likely to be.
