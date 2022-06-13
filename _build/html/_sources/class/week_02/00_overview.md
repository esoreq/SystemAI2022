# WEEK 02

## Let's cover some basics 

### Types of learning or the ML cake

- Learning from examples: Supervised learning  
- Learning from data: UnSupervised learning  
- Learning from experience: Reinforcement learning (which we will not cover here)

In all cases we have some form of input and some expected output 

### Supervised learning 
- In supervised learning we commonly have a dataset formed from input-output pairs 
where the input (aka the feature space) is some n-dimensional dataset and the output (aka the response vector) is mostly a vector of variables that we wish to predict.
- Our objective is to find a way to learn a way to map input information in a way that predicts output 
- Given a dataset where samples are drawn from some unknown joint distribution $p(X, y)$. 
- And variables are independent and identically distributed ($\text{ i.i.d.}$) which means that variable distributions won't change over time or space and sample wont be dependent on each other in anyway.
- Where for each observation $i$ we have some feature input vector $X_i$ and it's paired output $y_i$.
- Our job is learn a function $f(X) \approx y$ that approximates the output $y_i$ for each known input $X_i$, however, the implicit assumption is that the same function will be able to perform equally good approximations for new inputs $x$ , and unobserved $y$.

#### Two types of problems 
- Regression: predict a number 
- Classification: predict a label 

### Unsupervised learning

- Unsupervised learning analyses unlabelled datasets using machine learning methods. These algorithms find hidden or natural data patterns without human interaction (i.e. without a teacher that provides labels). 
- Its capacity to find similarities and differences makes it perfect for exploratory data analysis, and feature engineering.
- Here we are also have a dataset where samples are drawn from some unknown distribution $p(X)$ 
- The assumption is that there exist some hidden associations that can be derived just by looking at the properties of the data using different tools  
- If we can uncover this association we can use them to :
  - Compress the data by removing redundant (i.e. overlapping) information. 
  - Find rules that allow us to identify similar and different observations 
  - Identify sub feature rules where specific sequences are common 
  - Separate independent information sources

#### Unsupervised learning problems

- Dimensionality reduction: compress dataset with minimal information loss 
- Clustering: Separate a dataset to k different groups  
- Association rules: Identify rules of association hidden within a dataset  


## How does this relate to feature creation? 
- A dataset is normaly created to answer a specific question 
- If the problem you want to solve is one of prediction you will require an annotated dataset 
- If on the other hand you wish to explore the hidden properties of a dataset you will need some in-depth understanding of the underlying dataset potential distributions and what features it makes sense to extract
- Regardless, your central aim is to transform a raw data into a quality/tidy datasets ready for analysis 


## What are quality datasets

Quality datasets have the following properties:

1. **Data-Type Constraints**: all column values assigned the correct datatype, i.e., binary, categorical, ordinal, numeric, date
1. **Mandatory Columns**: some columns cannot be empty.
1. **Range Constraints**: numeric or dates columns should fall within a certain domain range.
1. **Categorical Consistency**: Categorical columns have a set of unique values For example, a person’s sex may be male or female.
1. **Cross-Column Consistency**: There are some interactions that need to make sense (e.g. age in years should be assoicated to birth date)
1. **Uniformity Constraints**: The degree to which the data is specified using the same unit of measure.


## What is Data Preprocessing ?

The process of data preprocessing involves converting raw data into a format that can be analysed and used. Data from the real world tends to be incomplete, inconsistent, and/or lacking in certain behaviors and trends, as well as containing a lot of errors. This can be resolved through data cleaning.
Furthermore, when you have access to a large dataset with several potential interactions, you may wish to isolate a question of interest, doing so from the beginning will help you focus on what is most important at that time with the flexibility to always go back and incorporate the features or domains you excluded earlier.

## Why use Data Preprocessing?

In the real world, data often contain inaccuracies, noise, and inconsistencies.

- When an observation is incomplete, we mean that it lacks attribute values, lacks desired attributes, or is only aggregated.
- When there are errors or outliers in the data, they are considered noisy.
- Data that is inconsistent contains names or codes that aren't consistent with the structure of interest.

## What can I do when an observations are incomplete?

- If the dataset is large enough..., exclude all observations with missing values
- You might consider imputed values in rare datasets (even if they are large)
- Decide in advance (before you examine the dataset) some exclusion criteria

## What can I do when there are errors or outliers in the data?

- First task is to identify errors or outliers cases
  - Errors are values that were logged incorrectly
  - Outliers are values that can't be justified conceptually (i.e. using a domain expert)
- Once you find them, you need to come up with a strategy
  - In order to eliminate errors and outliers, we can filter data
  - Outliers and errors can be transformed or imputed
  - They can be investigated independently

## What can I do when my dataset is inconsistent?

It depends on the level of inconsistency?

- Sometimes it's all about simple hacks
- Sometimes you need some manual procedures
  - In manuals, it is crucial to identify problems
    - Understand them
    - Handle them

## Schedule

|Time    | Session    | Description   |
|-----------:|----------:|---------:|
|09:30-09:50| [Week 02 overview[(index.html)] | Basics of ML |
|09:50-10:30| [Data Cleaning lab](02_data_cleaning_lab.ipynb)| Basic data cleaning over simulated data|
|10:30-10:35| Break | Coffee or Tea |
|10:35-11:30| [Feature engineering 101](05_feature_engineering_lab.ipynb)| What is Feature_engineering |
|11:30-11:35| Break | Coffee or Tea |
|10:35-12:00| [outlier detection lab](03_outlier_detection_lab.ipynb) | Detecting outliers in the wild |

<!-- #### Reinforcement learning
- Reinforcement learning is all about continuous learning, that is creating output that adapts to a changing world.
- Reinforcement learning teaches a computer a task through trial-and-error encounters with a dynamic environment. This learning technique allows the computer to optimise a reward measure without human interaction or explicit programming.

#### Reinforcement learning problems -->
