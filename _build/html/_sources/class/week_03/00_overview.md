# WEEK 03

## Let's cover some more basics 

### What are models?

- Modelling is a way of representing some phenomenon in a simple, useful way  
- It is useful because it makes it easier to understand, define, quantify, visualize, or simulate that phenomenon.  
- Models can be simple equations that represent the relationship between two variables or complex systems with intricate laws.  
- And most importantly models  allow us to convert complex datasets to stories.  

#### Use models to describe a dataset

- We have already discussed some of the different data models that can be used for describing data properties.
- In this section we will cover models that try to discover some natural relationships in datasets at lower dimension.

#### We covered the most famous model out there - The mean

- We defined it as the sum of the sample divided by the number of observed elements

$$ \bar{x} = \frac{1}{n} \sum_{i=1}^n x_i $$

- With $x_i$ representing the value of one random observation, and $\bar{x}$ as the mean value of all observations
and $n$ is the number of observations. And in our course observation is exactly the same as an event.

#### We also covered the variance

- As the expectation of the squared deviation of a random variable from its mean.
- In other words, it measures how far a set of numbers is spread out from their average value.  
$$ \sigma^2 =  \frac{\sum_{i=1}^n(x_i-\bar{x})^2} {n} $$

#### And its normalised version the standard deviation

- By determining each data point's deviation from the mean, the standard deviation is calculated as the square root of variance.
- Within the data set, there will be a higher deviation if the data points are further away from the mean;
- Therefore, the higher the standard deviation, the more spread out the data is.

$$ \sigma =  \frac{\sum_{i=1}^n(x_i-\bar{x})^2} {n} $$


#### We also mentioned probability

- Probability = The expected **relative** frequency of some outcome.  
- e.g. for a fair coin $P(heads)=P(tails)=0.5$

#### Which leads to the idea of a random variable and conditional probability

- Variable determined by a random experiment or sampling

##### For example:

According to a [Nature article](http://www.nature.com/articles/s41598-019-55432-z#data-availability) almost all females have a foot size smaller than 280mm[1].  

In men, the probability of having a foot size larger than 280 is around 0.3, as you can see from this recent study that analysed 1.2 million foot scans.

![](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-019-55432-z/MediaObjects/41598_2019_55432_Fig2_HTML.png?as=webp)

This allows us to confidently state the following from these plots of the probability distribution function (pdf) of different conditional distributions:

$$ P(FL>fl|M) \neq P(FL>fl|F) $$  

The conditional probability of foot size for males being larger than some limit fl is most of the time different than females

We can be more specific in our comparison and state the directionality of the relationship

$$ P(FL>fl|M) > P(FL>fl|F) $$  


#### The expected value is equal to the sample mean, i.e. the random variable in some experiment

- So $$ E[X] = \bar{x} = \frac{1}{n} \sum_{i=1}^n x_i $$
- And the variance would be describing the dispersion or the spread of the sampled observations around the mean  
- And Covariance would be the paired variance of two random variables
$$ Cov[X,Y] = E[[(X-E[X])(Y-E[Y])] $$


### What is an estimator and how do we assess it?

- An "estimator" or "point estimate" is a statistic used to infer the value of an unknown parameter in a statistical model.

#### We have some error in every prediction, which is a function of the **accuracy** of your estimator and the **quality** of the observed sample

$$ \epsilon(x) = \widehat\Theta(x) - \Theta $$


#### We have also the sampling deviation

The difference is accepting that each sampling has its own error, which is different from the actual error

$$ d(x) = \widehat\Theta(x) - E(\widehat\Theta(X)) $$

#### Which brings us back to Variance

The variance of $\widehat\Theta$ is simply the expected value of the squared sampling deviations

$$ VAR(\widehat\theta)=E[(\widehat\theta-E[\widehat\theta])^2] $$

#### And Bias

$$ B(\widehat\theta) = E(\widehat\theta)-\theta = E(\widehat\theta-\theta) $$

Which is the expected value of the error, i.e. the mean error of the sample
Or the difference between the Predicted Value and the Expected Value.

## But why do we need all of this?

A possible reason would be to measure the level of association between two or more variables

### One simple estimator of the association between two variables would be the Covariance

Remember that covariance indicates how closely two random variables change together.  
It's the unscaled measure that indicates the direction of the linear relationship between variables.    
As such it is hard to compare between two variables of different scales.  

### The scaled version of the covariance is (you guessed it) correlation

It is a measure used to measure the strength of the linear association between two random variables  
And is just the covariance divided by the product of both variables standard deviation.  
It's values range from -1 to 1 in contrast to the covariance matrix that ranges from $-\infty$ to $\infty$


### Why would we want that? 

- One simple reason would be to see if there is redundancy in your dataset 
- If your dataset has high degree of association it is useful to reduce it's Dimensionality 


### Curse of dimensionality

- Dimensionality is the number of variables, characteristics or features present in the dataset.
- These dimensions are represented in a tidy dataset as columns, and they are often expected to have some redundancy.
- The ratio between the number of observations and features is key, with a rule of thumb that to interpret a model you need 10 observations per feature  

### Dealing with Dimensionality

- There are two approaches for dimensionality reduction: 
  - **Feature Selection** : the process of selecting features using either data-driven approaches or domain expertise. 
  - **Feature Extraction** : the process of transforming the existing features into few features. 
  


### Today we will cover the concept of feature extraction

- Feature extraction is a process of reducing the dimensionality of a dataset.
- Feature extraction involves combining the existing features into new ones, thereby reducing the number of features in the dataset.
- This process reduces the amount of data into manageable sizes for algorithms to process with minimal distorting the original relationships or relevant information.

## The advantages of feature extraction

- Reduce computational complexity
- Reduce noise effects
- Improve our understanding of the big picture
- Merge together collinear features

## Limitations of feature extraction

- The new features generated are not easily interpretable.
- Scalability, some of these approaches require large computational resources that mean they are limited by number of observations and features

## We will also touch on the process of clustering 

- which can be viewed as a way to create a response vector when you don't have one


## Schedule

|Time    | Session    | Description   |
|-----------:|----------:|---------:|
|09:30-10:00| Week 03 overview | Basic terminology and overview |
|10:00-10:50| [Sklearn 101 A](01_sklearn_101.ipynb)| hands on to basic design patterns in sci kit-learn module with simple examples of feature extraction |
|10:50-10:55| Break | Coffee or Tea |
|10:55-11:40| [PCA](02_pca.ipynb) | hands on to the basic idea behind PCA | 
|11:40-12:00| [home work](03_home_assignment.ipynb)|  Apply PCA and tSNE to the 12tasks data|



