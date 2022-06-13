## What is Open and Reproducible Research?

- Scientific results and evidence are strengthened if those results can be replicated and confirmed by several independent researchers. 
- When researchers employ transparency in their research - in other words, when they properly document and share the data and processes associated with their analyses - the broader research community is able to save valuable time when reproducing or building upon published results. 
- Often, data or code from prior projects will be re-used by new researchers to verify old findings or develop new analyses.


![](https://the-turing-way.netlify.app/_images/research-cycle.jpg)

#### What does the word reproducibility mean?

- Reproducible research required authors to supply all of the relevant data and computer programmes to re-run the analysis and recreate the results.

##### Degrees of reproducibility ([Stodden 2014](https://www.edge.org/response-detail/25340))

- **Computational reproducibility**: When detailed information is provided about code, software, hardware and implementation details.

- **Empirical reproducibility**: When detailed information is provided about non-computational empirical scientific experiments and observations. In practice, this is enabled by making the data and details of how it was collected freely available.

- **Statistical reproducibility**: When detailed information is provided, for example, about the choice of statistical tests, model parameters, and threshold values. This mostly relates to pre-registration of study design to prevent p-value hacking and other manipulations.


### Levels of reproducible research

![the-turing-way](https://the-turing-way.netlify.app/_images/reproducible-matrix.jpg)


- **Reproducible**: A result is reproducible when the same analysis steps performed on the same dataset consistently produces the same answer.

- **Replicable**: A result is replicable when the same analysis performed on different datasets produces qualitatively similar answers.

- **Robust**: A result is robust when the same dataset is subjected to different analysis workflows to answer the same research question (for example one pipeline written in R and another written in Python) and a qualitatively similar or identical answer is produced. Robust results show that the work is not dependent on the specificities of the programming language chosen to perform the analysis.

- **Generalisable**: Combining replicable and robust findings allow us to form generalisable results. Note that running an analysis on a different software implementation and with a different dataset does not provide generalised results. There will be many more steps to know how well the work applies to all the different aspects of the research question. Generalisation is an important step towards understanding that the result is not dependent on a particular dataset nor a particular version of the analysis pipeline


#### Why Should We Bother?

- Reproducibility is crucial for complex projects. Where a team of experts is formed, and each is in charge of a facet of the problem
- It is also simpler to enforce in teams, as it is crucial in effective Collaboration.
- Furthermore, while neuroscience is a collaborative endeavor, most PhD students will work on specific projects sometimes alone.

#### Why Should You Bother?

- In this context, it is essential to understand that your collaborator is first and foremost your future self.
- In other words, data projects tend to be revisited, and your future self will be grateful if you create a clear and straightforward analysis project.

## The Costs of Reproducibility
###  The Futility of Underpowered Science
- We know that subtle behavioural neuronal markers require large numbers of samples to varify
- **Collaborate**: Try to join or form consortia to collect data that will answer your question
- **Use shared data**: Instead of proposing yet another little pilot in your PhD, try changing some of your questions in a manner that can be answered using datasets that are currently available.
- **Embrace theory**: Try to attack your question using either limitation in the current technology, or by using synthetic data that is simulated in some form. Generated data may be a way to answer multiple questions that might lead to unexpected solutions. 

### The Incentives Are Not Yet Aligned
- Reproducible research is harder to do 
- If you preregister your paper you are limited by your ability to manipulate the dat to increase the attractiveness of your paper 
- Hopefully if you do adapt to some of these guidelines your ability to produce better science and as a result knowledge will improve 

### Making Your Efforts Known
- Join hackathons 
- Join consortiums 
- Collaborate on large projects 
- Getting involved in social media
- Identify the key players in your field and interact with them 

### We Have a Problem
- We should focus less on the results and more on the questions and methods.
- We can try to include not only positive results but also negative ones. 
- Even when you present to your peers emphasising the negative as well will make the change in small bites  



### How to share your data 

- [best practices for sharing data on the Web summary](https://www.w3.org/TR/dwbp/#bp-summary)
- [git annex](https://git-annex.branchable.com/)
- [Datalad](http://datalad.org/)
- [FigShare](https://figshare.com/)


### Search for datasets

- [Google dataset](https://datasetsearch.research.google.com/)
- [Physionet](https://physionet.org/)
- [openneuro](https://openneuro.org/)
- [ukbiobank](https://www.ukbiobank.ac.uk/)
- [The Adolescent Brain Cognitive Development](https://abcdstudy.org/about/)

--- 

# Source material and websites on the topic

- [Guide for Reproducible Research](https://the-turing-way.netlify.app/reproducible-research/reproducible-research.html)
- [The Costs of Reproducibility](https://www.sciencedirect.com/science/article/pii/S0896627318310390)
- [The Good Research Code Handbook](https://goodresearch.dev/index.html)
